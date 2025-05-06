from fasthtml.common import *
import random
from monsterui.all import *

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

    coin_toss_result_display = f"Coin Toss Result: {random.choice(coin_sides)}"
    print(coin_toss_result_display)

    return Div(
        Div(
            P("Hello World!"),
            P(coin_toss_result_display),
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


@rt("/cards")
def ex_card3():
    def team_member(name, role, location="Remote"):
        return Card(
            DivLAligned(DiceBearAvatar(name, h=24, w=24), Div(H3(name), P(role))),
            footer=DivFullySpaced(
                DivHStacked(UkIcon("map-pin", height=16), P(location)),
                DivHStacked(
                    *(
                        UkIconLink(icon, height=16)
                        for icon in ("mail", "linkedin", "github")
                    )
                ),
            ),
        )

    team = [
        team_member("Sarah Chen", "Engineering Lead", "San Francisco"),
        team_member("James Wilson", "Senior Developer", "New York"),
        team_member("Maria Garcia", "UX Designer", "London"),
        team_member("Alex Kumar", "Product Manager", "Singapore"),
        team_member("Emma Brown", "DevOps Engineer", "Toronto"),
        team_member("Marcus Johnson", "Frontend Developer", "Berlin"),
    ]
    return Div(
        Grid(
            *team,
            cols_sm=1,
            cols_md=1,
            cols_lg=2,
            cols_xl=3,
        ),
        style="width: 200px; height: 400px",
    )


serve()
