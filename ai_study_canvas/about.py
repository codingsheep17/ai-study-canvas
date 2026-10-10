"""StudyCanvas AI - About page (Reflex).

Place this file in your app folder and import it once in the main app file:
    from .about import about  # noqa: F401
The @rx.page decorator registers the route /about automatically.
"""

import reflex as rx

# ---------- Theme (same tokens as the Home page) ----------
BG = "#0A0C13"
SURFACE = "#131726"
PRIMARY = "#6366F1"
PRIMARY_2 = "#8B5CF6"
ACCENT = "#22D3EE"
SUCCESS = "#34D399"
TEXT = "#E8EAF6"
MUTED = "#8B90A8"
BORDER = "rgba(255,255,255,0.08)"
GRADIENT = f"linear-gradient(135deg, {PRIMARY}, {PRIMARY_2})"

FONT_URL = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
PAD_X = ["1.25rem", "2rem", "4rem"]
MAX_W = "960px"


# ---------- Content (edit freely) ----------
FLOW = ["Rough notes", "Clear visuals", "Understandable explanations", "Interactive learning"]

STEPS = [
    ("Upload your notes", "Add a photo of a handwritten page, a sketch or a textbook diagram."),
    ("We read the image", "Computer vision picks up the shapes, labels and arrows in your drawing."),
    ("We redraw it", "Generative AI creates a clean, labelled version of the same diagram."),
    ("You learn from it", "An LLM writes a simple explanation, the key concepts and a short quiz."),
]

LEVELS = [
    ("Beginner", "Plain words and everyday examples. No background needed.", SUCCESS),
    ("University", "Proper terminology with the reasoning behind each idea.", PRIMARY),
    ("Advanced", "More depth, edge cases and harder quiz questions.", PRIMARY_2),
]

FEATURES = [
    ("Clean visual", "A tidy, labelled version of your sketch that is easy to revise from."),
    ("Simple explanation", "A short write-up of the diagram, matched to your level."),
    ("Key concepts", "The important terms pulled out so you know what to remember."),
    ("Quick quiz", "A few questions to check what you understood."),
]

AUDIENCE = [
    "Students who revise from handwritten notes",
    "Self-learners who sketch ideas to understand them",
    "Anyone who wants a fast recap of their own material",
]




# ---------- Building blocks ----------
def block(*children, id: str | None = None, border_top: bool = True) -> rx.Component:
    return rx.box(
        rx.box(*children, width="100%", max_width=MAX_W, margin_x="auto"),
        id=id,
        width="100%",
        padding_x=PAD_X,
        padding_y=["2.5rem", "3rem", "3.5rem"],
        border_top=f"1px solid {BORDER}" if border_top else "none",
    )


def heading(text: str) -> rx.Component:
    return rx.heading(text, size="6", color=TEXT, weight="bold", letter_spacing="-0.02em")


def body(text: str, **props) -> rx.Component:
    return rx.text(text, color=MUTED, size="3", line_height="1.75", **props)


def nav_link(label: str, href: str, active: bool = False) -> rx.Component:
    return rx.link(
        label,
        href=href,
        color=TEXT if active else MUTED,
        font_size="0.9rem",
        font_weight="500",
        text_decoration="none",
        _hover={"color": TEXT},
    )


# ---------- Sections ----------
def navbar() -> rx.Component:
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
                nav_link("Home", "/"),
                nav_link("About", "/about", active=True),
                spacing="5",
                align="center",
            ),
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


def page_title() -> rx.Component:
    return block(
        rx.vstack(
            rx.hstack(
                rx.link("Home", href="/", color=MUTED, font_size="0.85rem", text_decoration="none"),
                rx.text("/", color=MUTED, font_size="0.85rem"),
                rx.text("About", color=TEXT, font_size="0.85rem"),
                spacing="2",
            ),
            rx.heading(
                "About StudyCanvas AI",
                size={"initial": "8", "md": "9"},
                color=TEXT,
                weight="bold",
                letter_spacing="-0.03em",
            ),
            rx.text(
                "StudyCanvas AI is an AI-powered learning platform that transforms students' messy "
                "handwritten notes, sketches and educational diagrams into clean, understandable "
                "study material.",
                color=MUTED,
                size="4",
                line_height="1.75",
                max_width="720px",
            ),
            spacing="5",
            align="start",
        ),
        border_top=False,
    )


def mission() -> rx.Component:
    def flow_row(i: int, label: str) -> rx.Component:
        last = i == len(FLOW) - 1
        return rx.vstack(
            rx.text(label, color=ACCENT if last else TEXT, font_weight="600"),
            *([] if last else [rx.icon(tag="arrow-down", size=16, color=MUTED)]),
            spacing="1",
            align="start",
        )

    return block(
        rx.grid(
            rx.vstack(
                heading("Why we built it"),
                body(
                    "Students take notes fast, and those notes are rarely tidy. A half-drawn diagram "
                    "or a crossed-out arrow is easy to misread a week later, right when revision starts."
                ),
                body(
                    "StudyCanvas AI closes that gap. You upload an image, and the platform works out "
                    "what you meant, redraws it cleanly and teaches it back to you."
                ),
                body("Our goal is simple: make revision faster and more engaging."),
                spacing="4",
                align="start",
            ),
            rx.box(
                rx.vstack(
                    *[flow_row(i, label) for i, label in enumerate(FLOW)],
                    spacing="2",
                    align="start",
                ),
                border_left=f"2px solid {ACCENT}",
                padding_left="1.5rem",
                padding_y="0.25rem",
            ),
            columns={"initial": "1", "md": "2"},
            spacing="8",
            width="100%",
        ),
    )


def how_it_works() -> rx.Component:
    def step(i: int, title: str, desc: str) -> rx.Component:
        last = i == len(STEPS) - 1
        return rx.hstack(
            rx.vstack(
                rx.center(
                    rx.text(str(i + 1), color="white", font_weight="700", font_size="0.9rem"),
                    width="34px",
                    height="34px",
                    border_radius="50%",
                    background=GRADIENT,
                    flex_shrink="0",
                ),
                rx.box(
                    flex="1",
                    width="2px",
                    min_height="24px",
                    background="transparent" if last else BORDER,
                ),
                spacing="1",
                align="center",
            ),
            rx.vstack(
                rx.text(title, color=TEXT, font_weight="600", size="4"),
                body(desc),
                spacing="1",
                align="start",
                padding_bottom="1.5rem",
            ),
            spacing="4",
            align="stretch",
            width="100%",
        )

    return block(
        rx.grid(
            rx.vstack(
                heading("How it works"),
                body("From a photo of your notes to a full study pack, in four steps."),
                spacing="3",
                align="start",
            ),
            rx.vstack(
                *[step(i, t, d) for i, (t, d) in enumerate(STEPS)],
                spacing="0",
                align="start",
                width="100%",
            ),
            columns={"initial": "1", "md": "2"},
            spacing="8",
            width="100%",
        ),
        id="how-it-works",
    )


def levels() -> rx.Component:
    def level(title: str, desc: str, color: str) -> rx.Component:
        return rx.vstack(
            rx.hstack(
                rx.box(width="8px", height="8px", border_radius="50%", background=color),
                rx.text(title, color=TEXT, font_weight="600", size="4"),
                spacing="2",
                align="center",
            ),
            body(desc),
            spacing="2",
            align="start",
            background=SURFACE,
            padding="1.5rem",
            height="100%",
        )

    return block(
        rx.vstack(
            heading("Choose your learning level"),
            body("The same diagram can be explained in different ways. You pick the one that fits you."),
            rx.grid(
                *[level(t, d, c) for t, d, c in LEVELS],
                columns={"initial": "1", "md": "3"},
                gap="1px",
                width="100%",
                background=BORDER,
                border=f"1px solid {BORDER}",
                border_radius="14px",
                overflow="hidden",
            ),
            spacing="5",
            align="start",
            width="100%",
        ),
    )


def features() -> rx.Component:
    def row(title: str, desc: str) -> rx.Component:
        return rx.grid(
            rx.text(title, color=TEXT, font_weight="600"),
            body(desc),
            columns={"initial": "1", "md": "2"},
            spacing="2",
            width="100%",
            padding_y="1.1rem",
            border_bottom=f"1px solid {BORDER}",
        )

    return block(
        rx.vstack(
            heading("What you get from each upload"),
            rx.vstack(
                *[row(t, d) for t, d in FEATURES],
                spacing="0",
                width="100%",
                border_top=f"1px solid {BORDER}",
            ),
            spacing="5",
            align="start",
            width="100%",
        ),
    )


def audience_and_future() -> rx.Component:
    return block(
        rx.grid(
            rx.vstack(
                heading("Who it's for"),
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.icon(tag="check", size=16, color=SUCCESS, flex_shrink="0", margin_top="5px"),
                            body(item),
                            spacing="3",
                            align="start",
                        )
                        for item in AUDIENCE
                    ],
                    spacing="2",
                    align="start",
                ),
                spacing="4",
                align="start",
            ),
            rx.vstack(
                heading("Where we're headed"),
                body(
                    "We want StudyCanvas AI to be the place students go before an exam: upload your "
                    "own material, understand it, and test yourself in minutes. Next we plan to cover "
                    "more subjects, save study packs, and track progress over time."
                ),
                spacing="4",
                align="start",
            ),
            columns={"initial": "1", "md": "2"},
            spacing="8",
            width="100%",
        ),
    )




def closing() -> rx.Component:
    return block(
        rx.hstack(
            rx.text("Want to see it in action?", color=TEXT, font_weight="600", size="4"),
            rx.link(
                rx.hstack(
                    rx.text("Back to home", color=ACCENT, font_weight="600"),
                    rx.icon(tag="arrow-right", size=16, color=ACCENT),
                    spacing="1",
                    align="center",
                ),
                href="/",
                text_decoration="none",
            ),
            justify="between",
            align="center",
            width="100%",
            flex_wrap="wrap",
            gap="1rem",
        ),
    )


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("StudyCanvas AI", color=TEXT, font_weight="600", size="2"),
            rx.spacer(),
            rx.text("Made for the AI Study Canvas hackathon", color=MUTED, size="2"),
            width="100%",
            max_width=MAX_W,
            margin_x="auto",
            flex_wrap="wrap",
            gap="0.5rem",
        ),
        width="100%",
        padding_x=PAD_X,
        padding_y="1.5rem",
        border_top=f"1px solid {BORDER}",
    )


# ---------- Page ----------
@rx.page(
    route="/about",
    title="About | StudyCanvas AI",
    description="StudyCanvas AI turns handwritten notes and rough sketches into clean visuals, simple explanations and quizzes.",
)
def about() -> rx.Component:
    return rx.theme(
        rx.box(
            rx.el.link(rel="stylesheet", href=FONT_URL),
            navbar(),
            page_title(),
            mission(),
            how_it_works(),
            levels(),
            features(),
            audience_and_future(),
            closing(),
            footer(),
            background=BG,
            min_height="100vh",
            width="100%",
            font_family="'Inter', system-ui, sans-serif",
            style={"scrollBehavior": "smooth"},
        ),
        appearance="dark",
        has_background=False,
        accent_color="indigo",
    )