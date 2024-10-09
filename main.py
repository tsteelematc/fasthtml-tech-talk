from fasthtml.common import *
import random

app, rt = fast_app()


@rt("/")
def get():
    color_list = [
        "silver",
        "pink",
        # 1,
        # 2,
    ]

    coin_sides = [
        "heads",
        "tails",
    ]

    return Div(
        Div(
            P("Hello World!"),
            P(f"{random.choice(coin_sides)}"),
        ),
        hx_get="/change",
        style=f"background-color: {random.choice(color_list)}; padding: 20px",
        # cls="foo",
        _class="bar",
    )


@rt("/change")
def get():
    return Div(
        H1("Foo"),
        H3("Bar"),
        H5("Cat"),
        # Card(
        #     "Foo",
        #     header="Header",
        #     footer="Footer",
        # ),
        style="background-color: pink;",
    )


serve()
