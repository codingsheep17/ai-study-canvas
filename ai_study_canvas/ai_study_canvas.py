import reflex as rx
 
from .home import home  # noqa: F401  (registers "/")
from .about import about  # noqa: F401  (registers "/about")
 
app = rx.App()
 

# """Welcome to Reflex! This file outlines the steps to create a basic app."""

# import reflex as rx
# from rxconfig import config


# class State(rx.State):
#     """The app state."""


# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#     )


# app = rx.App()
# app.add_page(index)
