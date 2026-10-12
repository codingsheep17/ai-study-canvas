"""StudyCanvas AI - Home page (Reflex)."""

import os
import asyncio
from pathlib import Path
from pydantic import BaseModel
import reflex as rx

# --- Import your backend pipeline ---
from models_scripts.datavalidator import build_llm_payload
from models_scripts.llm import process_study_material
from models_scripts.gen_ai import generate_image

# ---------- Theme ----------
BG = "#0A0C13"
SURFACE = "#131726"
PRIMARY = "#6366F1"
PRIMARY_2 = "#8B5CF6"
ACCENT = "#22D3EE"
SUCCESS = "#34D399"
ERROR = "#FB7185"
TEXT = "#E8EAF6"
MUTED = "#8B90A8"
BORDER = "rgba(255,255,255,0.08)"
GRADIENT = f"linear-gradient(135deg, {PRIMARY}, {PRIMARY_2})"
TEXT_GRADIENT = f"linear-gradient(90deg, {PRIMARY_2}, {ACCENT})"

FONT_URL = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
PAD_X = ["1.25rem", "2rem", "4rem"]
MAX_W = "1120px"

LEVELS = [
    ("School student", "Simple words and everyday examples"),
    ("College student", "Clear concepts with key terms"),
    ("University student", "Detailed and technical"),
]

class QuizItem(BaseModel):
    q: str
    options: list[str]
    answer: str

# ---------- State ----------
class State(rx.State):
    
    # Processing state
    is_processing: bool = False
    loading_text: str = ""
    error_message: str = ""
    
    # Inputs
    query: str = ""
    topic: str = "Your Uploaded Topic"
    level: str = "University student"
    uploaded_name: str = ""
    rendered_img: str = ""

    # AI Outputs
    ai_notes: list[str] = []
    ai_quiz: list[QuizItem] = []
    
    # UI Control Variables
    show_notes: bool = False
    show_quiz: bool = False
    submitted: bool = False
    answers: list[str] = ["", "", "", "", ""]

    # --- Setters ---
    @rx.event
    def set_level(self, value: str):
        self.level = value
        self.reset_quiz()

    @rx.var
    def notes(self) -> list[str]:
        return self.ai_notes

    # --- The Core AI Pipeline ---
    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        # Strict backend lock: Ignore all new requests if already running
        if self.is_processing:
            return
            
        if not files:
            return
            
        self.error_message = ""
        self.is_processing = True
        self.loading_text = "Reading uploaded files... (Please wait a moment)"
        yield
        await asyncio.sleep(0.1)
        
        try:
            saved_files = []
            for file in files:
                name = Path(getattr(file, "filename", None) or getattr(file, "name", None) or "upload.png").name
                data = await file.read()
                outfile = os.path.join(rx.get_upload_dir(), name)
                with open(outfile, "wb") as f:
                    f.write(data)
                saved_files.append((outfile, name))

            # STEP 2: Vision OCR Extraction
            self.loading_text = "Extracting text.. (Please wait, large images take 15-30 seconds)"
            yield
            await asyncio.sleep(0.1)
            
            # Offload the heavy blocking OCR task to a background thread
            # so it doesn't kill the Reflex WebSocket heartbeat!
            extracted_text = await asyncio.to_thread(build_llm_payload, saved_files)
            
            # Loop through the generator to catch real-time UI updates
            report = None
            for step in process_study_material(extracted_text, self.level):
                if "status" in step:
                    self.loading_text = step["status"]
                    yield
                    await asyncio.sleep(0.1)
                elif "result" in step:
                    report = step["result"]
            
            self.ai_notes = report.concise_notes
            self.ai_quiz = [QuizItem(q=q.question_text, options=q.options, answer=q.answer) for q in report.quiz_questions]
            
            self.show_notes = True
            self.show_quiz = True

            # STEP 5: Diagram Generation
            self.loading_text = "Rendering flowchart diagram... (Almost done!)"
            yield
            await asyncio.sleep(0.1)
            
            # Generate the flowchart in assets/ and update the state path
            new_filename = generate_image(report.image_prompt)
            self.rendered_img = f"/{new_filename}"

        except Exception as e:
            print(f"Pipeline Error: {e}")
            self.error_message = f"Error: {str(e)}"
            yield
        finally:
            self.is_processing = False
            self.loading_text = ""
            yield

    # --- UI Interactions ---
    @rx.event
    def toggle_notes(self):
        self.show_notes = not self.show_notes

    @rx.event
    def generate_quiz(self):
        self.submitted = False
        self.show_quiz = True

    @rx.event
    def check_quiz(self):
        self.submitted = True

    @rx.event
    def reset_quiz(self):
        self.submitted = False
        self.show_quiz = False

    @rx.event
    def reset_on_load(self):
        """Wipes the state clean when the page is refreshed."""
        self.is_processing = False
        self.loading_text = ""
        self.topic = "Your Uploaded Topic"
        self.uploaded_name = ""
        self.rendered_img = ""
        self.ai_notes = []
        self.ai_quiz = []
        self.show_notes = False
        self.show_quiz = False
        self.submitted = False
        self.answers = ["", "", "", "", ""]

# ---------- Building blocks ----------
def primary_button_link(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.box(
            label,
            padding_x="1.4rem",
            padding_y="0.7rem",
            border_radius="10px",
            background=GRADIENT,
            color="white",
            font_weight="600",
            font_size="0.95rem",
            box_shadow=f"0 8px 24px {PRIMARY}55",
            _hover={"filter": "brightness(1.1)"},
        ),
        href=href,
        text_decoration="none",
    )

def ghost_button_link(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.box(
            label,
            padding_x="1.4rem",
            padding_y="0.7rem",
            border_radius="10px",
            border=f"1px solid {BORDER}",
            color=TEXT,
            font_weight="500",
            font_size="0.95rem",
            _hover={"background": "rgba(255,255,255,0.05)"},
        ),
        href=href,
        text_decoration="none",
    )

def action_button(label: str, on_click, **props) -> rx.Component:
    base = dict(
        on_click=on_click,
        background=GRADIENT,
        color="white",
        cursor="pointer",
        size="3",
        radius="medium",
        box_shadow=f"0 8px 24px {PRIMARY}44",
    )
    base.update(props)
    return rx.button(label, **base)

def card(*children, **props) -> rx.Component:
    base = dict(
        background=SURFACE,
        border=f"1px solid {BORDER}",
        border_radius="16px",
        padding=["1.25rem", "1.5rem", "1.75rem"],
        width="100%",
    )
    base.update(props)
    return rx.box(*children, **base)

def tool_section(id: str, title: str, subtitle: str, *children) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading(title, size="6", color=TEXT, weight="bold", letter_spacing="-0.02em"),
                rx.text(subtitle, color=MUTED, size="3", line_height="1.6", max_width="620px"),
                spacing="1",
                align="start",
            ),
            *children,
            spacing="5",
            align="start",
            width="100%",
            max_width=MAX_W,
            margin_x="auto",
        ),
        id=id,
        width="100%",
        padding_x=PAD_X,
        padding_y=["1.5rem", "2rem", "2rem"],
        scroll_margin_top="80px",
    )

SKETCH_SVG = """
<svg viewBox="0 0 260 190" width="100%" xmlns="http://www.w3.org/2000/svg" fill="none"
     stroke="#8B90A8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 58c-6-16 12-30 32-24 22 6 24 28 4 36-20 8-34 2-36-12z"/>
  <path d="M128 52c-4-18 18-30 40-22 20 8 20 30 0 38-22 8-38 0-40-16z"/>
  <path d="M60 52c20-8 40-8 62-2"/><path d="M112 46l10 4-8 8"/>
  <path d="M142 74c-4 20-6 36 0 50"/><path d="M136 116l6 10 8-10"/>
  <path d="M96 150c-4-12 22-20 52-16 30 4 46 16 26 26-22 10-72 8-78-10z"/>
  <text x="34" y="56" fill="#8B90A8" stroke="none" font-size="13" font-family="Georgia,serif" font-style="italic">sun</text>
  <text x="76" y="40" fill="#8B90A8" stroke="none" font-size="10" font-family="Georgia,serif" font-style="italic">energy?</text>
  <text x="140" y="54" fill="#8B90A8" stroke="none" font-size="13" font-family="Georgia,serif" font-style="italic">plant</text>
  <text x="120" y="152" fill="#8B90A8" stroke="none" font-size="13" font-family="Georgia,serif" font-style="italic">sugar</text>
</svg>
"""

# ---------- Sections ----------
def navbar() -> rx.Component:
    def nav_link(label: str, href: str) -> rx.Component:
        return rx.link(
            label,
            href=href,
            color=MUTED,
            font_size="0.9rem",
            font_weight="500",
            text_decoration="none",
            _hover={"color": TEXT},
        )

    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.box(width="28px", height="28px", border_radius="8px", background=GRADIENT),
                    rx.text("StudyCanvas AI", color=TEXT, font_weight="700", font_size="1.05rem"),
                    spacing="3",
                    align="center",
                ),
                href="/",
                text_decoration="none",
            ),
            rx.spacer(),
            rx.hstack(
                nav_link("Upload", "#upload"),
                nav_link("Quiz", "#quiz"),
                nav_link("About", "/about"),
                spacing="5",
                display=["none", "none", "flex"],
            ),
            rx.spacer(),
            align="center",
            width="100%",
            max_width=MAX_W,
            margin_x="auto",
        ),
        position="sticky",
        top="0",
        z_index="50",
        width="100%",
        padding_x=PAD_X,
        padding_y="1rem",
        background="rgba(10,12,19,0.85)",
        backdrop_filter="blur(12px)",
        border_bottom=f"1px solid {BORDER}",
    )

def hero() -> rx.Component:
    def mini_card(label: str, dot: str, content: rx.Component, glow: bool = False) -> rx.Component:
        return rx.box(
            rx.hstack(
                rx.box(width="6px", height="6px", border_radius="50%", background=dot),
                rx.text(label, color=MUTED, font_size="0.7rem", font_weight="600", letter_spacing="0.08em"),
                spacing="2",
                align="center",
            ),
            content,
            background=SURFACE,
            border=f"1px solid {PRIMARY}66" if glow else f"1px solid {BORDER}",
            box_shadow=f"0 0 40px {PRIMARY}26" if glow else "none",
            border_radius="16px",
            padding="1rem 1.25rem",
            width="100%",
            height="100%",
        )

    def node(label: str, color: str) -> rx.Component:
        return rx.center(
            rx.text(label, color=TEXT, font_weight="600", font_size="0.9rem"),
            padding="0.55rem 1rem",
            border_radius="10px",
            border=f"1.5px solid {color}",
            background=f"{color}1A",
        )

    clean = rx.vstack(
        rx.hstack(
            node("Sunlight", PRIMARY),
            rx.icon(tag="arrow-right", size=18, color=ACCENT),
            node("Plant", PRIMARY),
            spacing="2",
            align="center",
            margin_top="1rem",
        ),
        rx.icon(tag="arrow-down", size=18, color=ACCENT, margin_left="9rem"),
        rx.box(node("Glucose", ACCENT), margin_left="7rem"),
        spacing="2",
        align="start",
    )

    return rx.box(
        rx.grid(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.box(width="6px", height="6px", border_radius="50%", background=ACCENT),
                        rx.text("AI-POWERED REVISION", color=ACCENT, font_size="0.72rem", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding_x="0.9rem",
                    padding_y="0.35rem",
                    border_radius="999px",
                    border=f"1px solid {ACCENT}55",
                    background=f"{ACCENT}14",
                ),
                rx.heading(
                    "Upload your notes. Get ",
                    rx.text.span(
                        "study-ready diagrams",
                        style={
                            "background": TEXT_GRADIENT,
                            "WebkitBackgroundClip": "text",
                            "WebkitTextFillColor": "transparent",
                        },
                    ),
                    size={"initial": "8", "md": "9"},
                    color=TEXT,
                    weight="bold",
                    letter_spacing="-0.03em",
                    line_height="1.1",
                ),
                rx.text(
                    "Upload handwritten or printed notes. Get a clean visual flowchart, a simple explanation and a "
                    "quick quiz, matched perfectly to your level.",
                    color=MUTED,
                    size="4",
                    line_height="1.7",
                    max_width="520px",
                ),
                rx.hstack(
                    primary_button_link("Upload your notes →", "#upload"),
                    spacing="3",
                    flex_wrap="wrap",
                ),
                spacing="5",
                align="start",
            ),
            rx.flex(
                mini_card("YOUR NOTES", MUTED, rx.html(SKETCH_SVG)),
                rx.center(
                    rx.icon(tag="arrow-right", size=18, color=TEXT),
                    width="40px",
                    height="40px",
                    border_radius="50%",
                    border=f"1px solid {ACCENT}88",
                    background=SURFACE,
                    flex_shrink="0",
                    transform=["rotate(90deg)", "rotate(90deg)", "none"],
                ),
                mini_card("CLEAN VERSION", ACCENT, clean, glow=True),
                direction={"initial": "column", "md": "row"},
                align="center",
                gap="0.75rem",
                width="100%",
            ),
            columns={"initial": "1", "lg": "2"},
            spacing="8",
            align="center",
            width="100%",
            max_width=MAX_W,
            margin_x="auto",
        ),
        width="100%",
        padding_x=PAD_X,
        padding_y=["2.5rem", "3.5rem", "4.5rem"],
    )

def level_section() -> rx.Component:
    def option(name: str, desc: str) -> rx.Component:
        active = State.level == name
        return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text(name, color=TEXT, font_weight="600"),
                    rx.cond(active, rx.icon(tag="circle-check", size=16, color=SUCCESS), rx.fragment()),
                    align="center",
                    spacing="2",
                ),
                rx.text(desc, color=MUTED, size="2"),
                spacing="1",
                align="start",
            ),
            on_click=State.set_level(name),
            cursor="pointer",
            padding="1rem 1.25rem",
            border_radius="12px",
            border=rx.cond(active, f"1px solid {PRIMARY}", f"1px solid {BORDER}"),
            background=rx.cond(active, f"{PRIMARY}26", "transparent"),
            box_shadow=rx.cond(active, f"0 0 24px {PRIMARY}33", "none"),
            width="100%",
        )

    return tool_section(
        "levels",
        "Choose your level",
        "Explanations, notes and the quiz are matched to the level you pick.",
        rx.grid(
            *[option(n, d) for n, d in LEVELS],
            columns={"initial": "1", "md": "3"},
            spacing="3",
            width="100%",
        ),
    )

def upload_section() -> rx.Component:
    return tool_section(
        "upload",
        "Upload your notes",
        "PNG or JPG. Max 3 files at once.",
        card(
            rx.grid(
                rx.upload(
                    rx.vstack(
                        rx.center(
                            rx.icon(tag="upload", size=22, color=TEXT),
                            width="52px",
                            height="52px",
                            border_radius="14px",
                            background=f"{PRIMARY}26",
                            border=f"1px solid {PRIMARY}55",
                        ),
                        rx.text("Drop your notes here", color=TEXT, font_weight="600"),
                        rx.text("or click to select up to 3 files at once", color=MUTED, size="2"),
                        spacing="2",
                        align="center",
                    ),
                    id="notes_upload",
                    accept={
                        "image/png": [".png"], 
                        "image/jpeg": [".jpg", ".jpeg", ".jfif"],
                        "application/pdf": [".pdf"]
                    },
                    max_files=3,
                    multiple=True,
                    disabled=State.is_processing, # <-- Locks the dropzone
                    border=f"1.5px dashed {PRIMARY}66",
                    border_radius="14px",
                    padding="2.5rem 1rem",
                    width="100%",
                    background="transparent",
                    cursor="pointer",
                ),
                rx.vstack(
                    rx.text("Selected files", color=MUTED, size="2"),
                    rx.cond(
                        rx.selected_files("notes_upload").length() > 0,
                        rx.flex(
                            rx.foreach(
                                rx.selected_files("notes_upload"),
                                lambda f: rx.hstack(
                                    rx.icon(tag="image", size=16, color=ACCENT),
                                    rx.text(f, color=TEXT, size="2"),
                                    padding="0.3rem 0.6rem",
                                    border_radius="6px",
                                    background="rgba(255,255,255,0.05)",
                                    spacing="2",
                                    align="center",
                                )
                            ),
                            wrap="wrap",
                            gap="0.5rem",
                        ),
                        rx.text("No files selected yet.", color=MUTED, size="2"),
                    ),
                    rx.text("Level", color=MUTED, size="2", margin_top="0.5rem"),
                    rx.text(State.level, color=TEXT, size="2", font_weight="600"),
                    action_button(
                        "Generate study pack",
                        State.handle_upload(rx.upload_files(upload_id="notes_upload")),
                        margin_top="0.75rem",
                        loading=State.is_processing,
                        disabled=State.is_processing, # Locks the button during processing
                    ),
                    rx.cond(
                        State.is_processing,
                        rx.text(State.loading_text, color=ACCENT, size="2", font_weight="500", margin_top="0.5rem"),
                        rx.cond(
                            State.error_message != "",
                            rx.text(State.error_message, color=ERROR, size="2", font_weight="500", margin_top="0.5rem"),
                            rx.fragment()
                        )
                    ),
                    spacing="2",
                    align="start",
                    width="100%",
                ),
                columns={"initial": "1", "md": "2"},
                spacing="5",
                width="100%",
            )
        ),
    )

def render_section() -> rx.Component:
    placeholder = rx.vstack(
        rx.icon(tag="git-merge", size=40, color=MUTED),
        rx.text("Your flowchart will appear here", color=TEXT, font_weight="600"),
        rx.text("Generated via AI logic mapping", color=MUTED, size="2"),
        spacing="2",
        align="center",
    )
    return tool_section(
        "render",
        "Clean visual",
        "A logical flowchart mapping the core concepts of your notes.",
        card(
            rx.vstack(
                rx.center(
                    rx.cond(
                        State.rendered_img != "",
                        rx.image(
                            src=State.rendered_img,
                            width="100%",
                            height="100%",
                            object_fit="contain",
                        ),
                        placeholder,
                    ),
                    width="100%",
                    min_height="400px",
                    margin_x="auto",
                    border_radius="14px",
                    border=f"1px dashed {BORDER}",
                    background="rgba(255,255,255,0.02)",
                    overflow="hidden",
                ),
                spacing="3",
                align="center",
                width="100%",
            )
        ),
    )

def notes_section() -> rx.Component:
    return tool_section(
        "notes",
        "Study notes",
        "Want short notes on this topic to revise from?",
        card(
            rx.vstack(
                rx.hstack(
                    action_button(
                        rx.cond(State.show_notes, "Hide notes", "Yes, make notes"),
                        State.toggle_notes,
                    ),
                    rx.text("Topic: ", State.topic, color=MUTED, size="2"),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap",
                ),
                rx.cond(
                    State.show_notes,
                    rx.vstack(
                        rx.foreach(
                            State.notes,
                            lambda n: rx.hstack(
                                rx.icon(tag="check", size=16, color=SUCCESS, flex_shrink="0", margin_top="4px"),
                                rx.text(n, color=TEXT, size="3", line_height="1.6"),
                                spacing="3",
                                align="start",
                            ),
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                        padding="1.1rem 1.25rem",
                        border_radius="12px",
                        border=f"1px solid {BORDER}",
                        background="rgba(255,255,255,0.02)",
                    ),
                    rx.fragment(),
                ),
                spacing="4",
                align="start",
                width="100%",
            )
        ),
    )

def quiz_section() -> rx.Component:
    def question(item, i) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.text("Q", (i + 1), ". ", item.q, color=TEXT, font_weight="600", size="4"),
                rx.cond(
                    State.submitted,
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="check", size=18, color=SUCCESS),
                            rx.text(item.answer, color=SUCCESS, font_weight="600", size="3"),
                            align="center"
                        ),
                        rx.text("Other options:", color=MUTED, size="2", margin_top="0.5rem"),
                        rx.foreach(
                            item.options,
                            lambda opt: rx.cond(
                                opt != item.answer,
                                rx.hstack(
                                    rx.icon(tag="dot", size=16, color=MUTED),
                                    rx.text(opt, color=MUTED, size="2"),
                                    align="center"
                                ),
                                rx.fragment()
                            )
                        ),
                        spacing="1",
                        align="start",
                        padding_top="0.5rem",
                        padding_left="1rem",
                        border_left=f"2px solid {SUCCESS}44",
                    ),
                    rx.fragment(),
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            padding_y="1.25rem",
            border_bottom=f"1px solid {BORDER}",
            width="100%",
        )

    quiz_body = rx.vstack(
        rx.foreach(State.ai_quiz, lambda item, i: question(item, i)),
        rx.hstack(
            rx.cond(
                State.submitted,
                rx.button(
                    "Hide answers",
                    on_click=State.reset_quiz,
                    variant="outline",
                    cursor="pointer",
                    size="3",
                ),
                action_button("Reveal answers", State.check_quiz),
            ),
            spacing="4",
            align="center",
            padding_top="1.25rem",
        ),
        spacing="0",
        align="start",
        width="100%",
    )

    return tool_section(
        "quiz",
        "Test yourself",
        "Want a quick quiz on this topic?",
        card(
            rx.vstack(
                rx.hstack(
                    action_button(
                        rx.cond(State.show_quiz, "Regenerate quiz", "Generate quiz"),
                        State.generate_quiz,
                    ),
                    rx.text("Topic: ", State.topic, color=MUTED, size="2"),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap",
                ),
                rx.cond(State.show_quiz, quiz_body, rx.fragment()),
                spacing="4",
                align="start",
                width="100%",
            )
        ),
    )

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("StudyCanvas AI", color=TEXT, font_weight="600", size="2"),
            rx.spacer(),
            rx.link("About", href="/about", color=MUTED, size="2", text_decoration="none"),
            width="100%",
            max_width=MAX_W,
            margin_x="auto",
        ),
        width="100%",
        padding_x=PAD_X,
        padding_y="1.5rem",
        margin_top="2rem",
        border_top=f"1px solid {BORDER}",
    )


# ---------- Page ----------
@rx.page(
    route="/",
    title="StudyCanvas AI",
    description="Upload notes, explanations and quizzes.",
    on_load=State.reset_on_load
)
def home() -> rx.Component:
    return rx.theme(
        rx.box(
            rx.el.link(rel="stylesheet", href=FONT_URL),
            rx.el.link(rel="icon", href="/icon.png", type="image/png"),  # <-- Add this line
            navbar(),
            hero(),
            level_section(),
            upload_section(),
            render_section(),
            notes_section(),
            quiz_section(),
            footer(),
            background=f"radial-gradient(ellipse at 50% -10%, {PRIMARY}33, transparent 55%), {BG}",
            min_height="100vh",
            width="100%",
            font_family="'Inter', system-ui, sans-serif",
            style={"scrollBehavior": "smooth"},
        ),
        appearance="dark",
        has_background=False,
        accent_color="indigo",
    )