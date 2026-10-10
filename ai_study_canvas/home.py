"""StudyCanvas AI - Home page (Reflex).

Place this file in your app folder and import it once in the main app file:
    from .home import home  # noqa: F401
The @rx.page decorator registers the route "/" automatically.

NOTE: AI is not connected yet. The explanation, notes and quiz below are sample
content (Photosynthesis). Replace the sample data / generate_clean_visual()
with your computer-vision + generative-AI + LLM calls.
"""

from pathlib import Path

import reflex as rx

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

# ---------- Sample data (replace with AI output) ----------
LEVELS = [
    ("School student", "Simple words and everyday examples"),
    ("College student", "Clear concepts with key terms"),
    ("University student", "Detailed and technical"),
]

TOPIC_CHIPS = ["Photosynthesis", "Newton's laws", "Cell division", "Binary trees"]

OVERVIEW = {
    "School student": "Plants use sunlight to make their own food.",
    "College student": "Chloroplasts turn light, water and CO₂ into glucose and oxygen.",
    "University student": "Light reactions and the Calvin cycle convert light energy into chemical energy.",
}

EXPLANATION = {
    "School student": (
        "Plants make their own food. They take in sunlight, water from the soil and carbon dioxide "
        "from the air. Inside the green parts of the leaf they turn these into sugar (glucose) for "
        "energy, and they release oxygen. Think of a leaf as a tiny kitchen powered by the sun."
    ),
    "College student": (
        "Photosynthesis happens in chloroplasts. Chlorophyll absorbs light, and the light reactions "
        "use that energy to split water and make ATP and NADPH. The Calvin cycle then uses ATP and "
        "NADPH to turn CO₂ into glucose. Oxygen is released as a by-product of splitting water."
    ),
    "University student": (
        "The light-dependent reactions on the thylakoid membrane use photosystems II and I and an "
        "electron transport chain to build a proton gradient, which drives ATP synthase, and to make "
        "NADPH. In the stroma, RuBisCO fixes CO₂ onto RuBP in the Calvin-Benson cycle, producing G3P "
        "that is used to build glucose. C4 and CAM pathways reduce photorespiration when RuBisCO binds O₂."
    ),
}

NOTES = {
    "School student": [
        "Photosynthesis is how plants make food.",
        "Plants need sunlight, water and carbon dioxide.",
        "The food they make is glucose, a type of sugar.",
        "Plants give out oxygen, which we breathe.",
        "It happens in the green parts of the plant.",
    ],
    "College student": [
        "Site: chloroplasts, using the green pigment chlorophyll.",
        "Light reactions make ATP and NADPH and release O₂.",
        "Calvin cycle uses ATP and NADPH to fix CO₂ into glucose.",
        "Overall: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂.",
        "Rate depends on light intensity, CO₂ level and temperature.",
    ],
    "University student": [
        "Thylakoid membrane: PSII, cytochrome b6f, PSI, ATP synthase.",
        "Non-cyclic flow gives ATP and NADPH; cyclic flow gives extra ATP.",
        "Calvin-Benson cycle: carboxylation, reduction, regeneration of RuBP.",
        "RuBisCO also binds O₂, causing photorespiration.",
        "C4 and CAM plants concentrate CO₂ to reduce this loss.",
    ],
}

QUIZ = [
    {
        "q": "What do plants make using sunlight, water and CO₂?",
        "options": ["Only oxygen", "Glucose and oxygen", "Protein", "Only starch"],
        "answer": "Glucose and oxygen",
    },
    
    {
        "q": "Where in the cell does photosynthesis happen?",
        "options": ["Mitochondria", "Nucleus", "Chloroplast", "Ribosome"],
        "answer": "Chloroplast",
    },
    {
        "q": "Which pigment absorbs light for photosynthesis?",
        "options": ["Haemoglobin", "Chlorophyll", "Melanin", "Keratin"],
        "answer": "Chlorophyll",
    },
    {
        "q": "Which gas do plants take in for photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Hydrogen", "Carbon dioxide"],
        "answer": "Carbon dioxide",
    },
    {
        "q": "Which gas is released as a by-product?",
        "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Methane"],
        "answer": "Oxygen",
    },
]
FLASHCARDS = [
    {"front": "Photosynthesis", "back": "How plants turn light, water and CO₂ into glucose and oxygen."},
    {"front": "Chlorophyll", "back": "The green pigment that absorbs light energy."},
    {"front": "Chloroplast", "back": "The part of the plant cell where photosynthesis happens."},
    {"front": "Glucose", "back": "The sugar plants make as food and energy."},
    {"front": "Light reactions", "back": "Use light to make ATP and NADPH, and release oxygen."},
    {"front": "Calvin cycle", "back": "Uses ATP and NADPH to turn CO₂ into glucose."},
]

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


def generate_clean_visual(saved_name: str) -> str:
    """Hook for the AI image pipeline.

    Receives the saved upload filename (inside the Reflex upload dir) and should
    return the filename of the generated 1024x1024 clean visual. For now it just
    returns the upload so the preview area works.
    """
    return saved_name


# ---------- State ----------
class State(rx.State):
    query: str = ""
    topic: str = "Photosynthesis"
    level: str = "University student"
    
    uploaded_name: str = ""
    rendered_img: str = ""

    doubt: str = ""
    explained: bool = False

    show_notes: bool = False
    show_cards: bool = False
    card_index: int = 0
    flipped: bool = False

    show_quiz: bool = False
    answers: list[str] = ["", "", "", "", ""]
    submitted: bool = False
    score: int = 0

    # --- setters ---
    @rx.event
    def set_query(self, value: str):
        self.query = value

    @rx.event
    def set_doubt(self, value: str):
        self.doubt = value

    @rx.event
    def set_level(self, value: str):
        self.level = value
        self.show_quiz = False
        self.submitted = False
        self.show_cards = False
        self.score = 0
        self.answers = ["", "", "", "", ""]

    # --- search ---
    @rx.event
    def run_search(self, form_data: dict):
        text = self.query.strip()
        if text and text != self.topic:
            self.topic = text
            self.show_quiz = False
            self.submitted = False
            self.show_cards = False
            self.score = 0
            self.answers = ["", "", "", "", ""]

    @rx.event
    def pick_topic(self, value: str):
        self.query = value
        if value != self.topic:
            self.topic = value
            self.show_quiz = False
            self.submitted = False
            self.show_cards = False
            self.score = 0
            self.answers = ["", "", "", "", ""]

    # --- upload ---
    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
        file = files[0]
        raw_name = getattr(file, "filename", None) or getattr(file, "name", None) or "upload.png"
        name = Path(raw_name).name
        data = await file.read()
        out = rx.get_upload_dir() / name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        self.uploaded_name = name
        self.rendered_img = generate_clean_visual(name)

    # --- misconception ---
    @rx.event
    def explain(self):
        if self.doubt.strip():
            self.explained = True

    # --- notes ---
    @rx.event
    def toggle_notes(self):
        self.show_notes = not self.show_notes


        show_quiz: bool = False

    @rx.event
    def generate_quiz(self):
        self.answers = ["", "", "", "", ""]
        self.submitted = False
        self.score = 0
        self.show_quiz = True

    # --- quiz ---
    @rx.event
    def select_answer(self, index: int, option: str):
        if self.submitted:
            return
        updated = list(self.answers)
        updated[index] = option
        self.answers = updated

    @rx.event
    def check_quiz(self):
        self.score = sum(1 for i, q in enumerate(QUIZ) if self.answers[i] == q["answer"])
        self.submitted = True

    @rx.event
    def reset_quiz(self):
        self.answers = ["", "", "", "", ""]
        self.submitted = False
        self.score = 0

        # --- flashcards ---
    @rx.event
    def generate_cards(self):
        self.card_index = 0
        self.flipped = False
        self.show_cards = True

    @rx.event
    def flip_card(self):
        self.flipped = not self.flipped

    @rx.event
    def next_card(self):
        self.card_index = (self.card_index + 1) % len(FLASHCARDS)
        self.flipped = False

    @rx.event
    def prev_card(self):
        self.card_index = (self.card_index - 1) % len(FLASHCARDS)
        self.flipped = False

    @rx.var
    def card_front(self) -> str:
        return FLASHCARDS[self.card_index]["front"]

    @rx.var
    def card_back(self) -> str:
        return FLASHCARDS[self.card_index]["back"]

    @rx.var
    def card_counter(self) -> str:
        return f"{self.card_index + 1} / {len(FLASHCARDS)}"
    # --- computed ---
    @rx.var
    def overview(self) -> str:
        return OVERVIEW[self.level]

    @rx.var
    def explanation(self) -> str:
        return EXPLANATION[self.level]

    @rx.var
    def notes(self) -> list[str]:
        return NOTES[self.level]


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
                nav_link("Search", "#search"),
                nav_link("Upload", "#upload"),
                nav_link("Learn", "#misconception"),
                nav_link("Flashcards", "#flashcards"),
                nav_link("Quiz", "#quiz"),
                nav_link("About", "/about"),
                spacing="5",
                display=["none", "none", "flex"],
            ),
            rx.spacer(),
            primary_button_link("Get started", "#search"),
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
                    "Turn rough sketches into ",
                    rx.text.span(
                        "study-ready visuals",
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
                    "Upload a handwritten diagram. Get a clean version, a simple explanation and a "
                    "quick quiz, matched to your level.",
                    color=MUTED,
                    size="4",
                    line_height="1.7",
                    max_width="520px",
                ),
                rx.hstack(
                    primary_button_link("Upload your notes →", "#upload"),
                    ghost_button_link("See example", "#render"),
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


def search_section() -> rx.Component:
    return tool_section(
        "search",
        "Search a topic",
        "Type what you want to study. We will build your study pack around it.",
        card(
            rx.vstack(
                rx.form(
                    rx.hstack(
                        rx.input(
                            rx.input.slot(rx.icon(tag="search", size=16)),
                            placeholder="e.g. Photosynthesis, Newton's laws, Binary trees",
                            value=State.query,
                            on_change=State.set_query,
                            size="3",
                            width="100%",
                            flex="1",
                        ),
                        action_button("Search", None, type="submit"),
                        width="100%",
                        spacing="3",
                    ),
                    on_submit=State.run_search,
                    width="100%",
                ),
                rx.flex(
                    rx.text("Try:", color=MUTED, size="2"),
                    *[
                        rx.box(
                            t,
                            on_click=State.pick_topic(t),
                            cursor="pointer",
                            padding="0.25rem 0.8rem",
                            border_radius="999px",
                            border=f"1px solid {BORDER}",
                            color=TEXT,
                            font_size="0.85rem",
                            _hover={"background": "rgba(255,255,255,0.06)"},
                        )
                        for t in TOPIC_CHIPS
                    ],
                    gap="0.6rem",
                    wrap="wrap",
                    align="center",
                ),
                rx.box(
                    rx.text("Studying", color=MUTED, size="1"),
                    rx.heading(State.topic, size="5", color=TEXT),
                    rx.text(State.overview, color=MUTED, size="2", margin_top="0.25rem"),
                    padding="1rem 1.25rem",
                    border_radius="12px",
                    border=f"1px solid {PRIMARY}44",
                    background=f"{PRIMARY}14",
                    width="100%",
                ),
                spacing="4",
                align="start",
                width="100%",
            )
        ),
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
        "PNG or JPG. Handwritten or printed.",
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
                        rx.text("or click to choose a file", color=MUTED, size="2"),
                        spacing="2",
                        align="center",
                    ),
                    id="notes_upload",
                    accept={"image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"]},
                    max_files=1,
                    multiple=False,
                    border=f"1.5px dashed {PRIMARY}66",
                    border_radius="14px",
                    padding="2.5rem 1rem",
                    width="100%",
                    background="transparent",
                    cursor="pointer",
                ),
                rx.vstack(
                    rx.text("Selected file", color=MUTED, size="2"),
                    rx.cond(
                        rx.selected_files("notes_upload").length() > 0,
                        rx.foreach(
                            rx.selected_files("notes_upload"),
                            lambda f: rx.hstack(
                                rx.icon(tag="image", size=16, color=ACCENT),
                                rx.text(f, color=TEXT, size="2"),
                                spacing="2",
                                align="center",
                            ),
                        ),
                        rx.text("No file selected yet.", color=MUTED, size="2"),
                    ),
                    rx.text("Level", color=MUTED, size="2", margin_top="0.5rem"),
                    rx.text(State.level, color=TEXT, size="2", font_weight="600"),
                    action_button(
                        "Generate study pack",
                        State.handle_upload(rx.upload_files(upload_id="notes_upload")),
                        margin_top="0.75rem",
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
        rx.icon(tag="image", size=40, color=MUTED),
        rx.text("Your clean visual will appear here", color=TEXT, font_weight="600"),
        rx.text("1024 × 1024", color=MUTED, size="2"),
        spacing="2",
        align="center",
    )
    return tool_section(
        "render",
        "Clean visual",
        "The redrawn diagram shows in a 1024 × 1024 space.",
        card(
            rx.vstack(
                rx.center(
                    rx.cond(
                        State.rendered_img != "",
                        rx.image(
                            src=rx.get_upload_url(State.rendered_img),
                            width="100%",
                            height="100%",
                            object_fit="contain",
                        ),
                        placeholder,
                    ),
                    width="100%",
                    max_width="1024px",
                    aspect_ratio="1 / 1",
                    margin_x="auto",
                    border_radius="14px",
                    border=f"1px dashed {BORDER}",
                    background="rgba(255,255,255,0.02)",
                    overflow="hidden",
                ),
                rx.text(
                    "Preview shows your upload until the AI-generated version is connected.",
                    color=MUTED,
                    size="2",
                ),
                spacing="3",
                align="center",
                width="100%",
            )
        ),
    )


def misconception_section() -> rx.Component:
    return tool_section(
        "misconception",
        "Not getting something?",
        "Write what confuses you. You get a simple explanation at your level.",
        card(
            rx.vstack(
                rx.text_area(
                    placeholder="e.g. I don't understand why oxygen is released in photosynthesis",
                    value=State.doubt,
                    on_change=State.set_doubt,
                    rows="4",
                    size="3",
                    width="100%",
                ),
                action_button("Explain it to me", State.explain),
                rx.cond(
                    State.explained,
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="lightbulb", size=16, color=ACCENT),
                            rx.text("Explanation for ", State.level, color=ACCENT, size="2", font_weight="600"),
                            spacing="2",
                            align="center",
                        ),
                        rx.text("Your question: ", State.doubt, color=MUTED, size="2", margin_top="0.5rem"),
                        rx.text(State.explanation, color=TEXT, size="3", line_height="1.75", margin_top="0.5rem"),
                        padding="1.1rem 1.25rem",
                        border_radius="12px",
                        border=f"1px solid {ACCENT}44",
                        background=f"{ACCENT}0F",
                        width="100%",
                    ),
                    rx.fragment(),
                ),
                spacing="4",
                align="start",
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

def flashcards_section() -> rx.Component:
    flash = rx.box(
        rx.vstack(
            rx.text(
                rx.cond(State.flipped, "ANSWER", "TERM"),
                color=ACCENT,
                size="1",
                font_weight="600",
                letter_spacing="0.1em",
            ),
            rx.text(
                rx.cond(State.flipped, State.card_back, State.card_front),
                color=TEXT,
                size="6",
                font_weight="600",
                text_align="center",
            ),
            rx.text("Click the card to flip", color=MUTED, size="1"),
            spacing="3",
            align="center",
            justify="center",
        ),
        on_click=State.flip_card,
        cursor="pointer",
        width="100%",
        max_width="560px",
        min_height="220px",
        margin_x="auto",
        padding="2rem",
        border_radius="16px",
        border=rx.cond(State.flipped, f"1px solid {ACCENT}88", f"1px solid {PRIMARY}88"),
        background=rx.cond(State.flipped, f"{ACCENT}12", f"{PRIMARY}1A"),
        box_shadow=f"0 0 40px {PRIMARY}22",
        display="flex",
        align_items="center",
        justify_content="center",
    )

    return tool_section(
        "flashcards",
        "Flashcards",
        "Flip through the key terms to memorize them.",
        card(
            rx.vstack(
                rx.hstack(
                    action_button(
                        rx.cond(State.show_cards, "Regenerate flashcards", "Generate flashcards"),
                        State.generate_cards,
                    ),
                    rx.text("Topic: ", State.topic, color=MUTED, size="2"),
                    spacing="3",
                    align="center",
                    flex_wrap="wrap",
                ),
                rx.cond(
                    State.show_cards,
                    rx.vstack(
                        flash,
                        rx.hstack(
                            rx.button("Previous", on_click=State.prev_card, variant="outline", cursor="pointer", size="3"),
                            rx.text(State.card_counter, color=MUTED, size="3"),
                            rx.button("Next", on_click=State.next_card, variant="outline", cursor="pointer", size="3"),
                            spacing="4",
                            align="center",
                            justify="center",
                            width="100%",
                        ),
                        spacing="4",
                        align="center",
                        width="100%",
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
    def option_button(i: int, opt: str, correct: str) -> rx.Component:
        selected = State.answers[i] == opt
        if opt == correct:
            border = rx.cond(State.submitted, SUCCESS, rx.cond(selected, PRIMARY, BORDER))
            bg = rx.cond(State.submitted, f"{SUCCESS}1F", rx.cond(selected, f"{PRIMARY}26", "transparent"))
        else:
            border = rx.cond(
                State.submitted,
                rx.cond(selected, ERROR, BORDER),
                rx.cond(selected, PRIMARY, BORDER),
            )
            bg = rx.cond(
                State.submitted,
                rx.cond(selected, f"{ERROR}1F", "transparent"),
                rx.cond(selected, f"{PRIMARY}26", "transparent"),
            )
        return rx.box(
            rx.text(opt, color=TEXT, size="3"),
            on_click=State.select_answer(i, opt),
            cursor="pointer",
            padding="0.85rem 1.1rem",
            border_radius="10px",
            border="1px solid",
            border_color=border,
            background=bg,
            width="100%",
            _hover={"background": "rgba(255,255,255,0.04)"},
        )

    def question(i: int, item: dict) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.text(f"Q{i + 1}. {item['q']}", color=TEXT, font_weight="600", size="4"),
                rx.grid(
                    *[option_button(i, o, item["answer"]) for o in item["options"]],
                    columns={"initial": "1", "md": "2"},
                    spacing="2",
                    width="100%",
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
        *[question(i, q) for i, q in enumerate(QUIZ)],
        rx.hstack(
            action_button("Check answers", State.check_quiz, disabled=State.submitted),
            rx.cond(
                State.submitted,
                rx.hstack(
                    rx.text("Score: ", State.score, " / 5", color=TEXT, font_weight="700", size="4"),
                    rx.button(
                        "Try again",
                        on_click=State.reset_quiz,
                        variant="outline",
                        cursor="pointer",
                        size="3",
                    ),
                    spacing="4",
                    align="center",
                ),
                rx.fragment(),
            ),
            spacing="4",
            align="center",
            flex_wrap="wrap",
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
    description="Turn rough sketches into study-ready visuals, explanations and quizzes.",
)
def home() -> rx.Component:
    return rx.theme(
        rx.box(
            rx.el.link(rel="stylesheet", href=FONT_URL),
            navbar(),
            hero(),
            search_section(),
            level_section(),
            upload_section(),
            render_section(),
            misconception_section(),
            notes_section(),
            flashcards_section(),
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