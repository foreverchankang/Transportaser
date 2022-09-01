import flet
from flet import (
    Column,
    Page,
    Row,
    Text,
    TextField,
    UserControl,
    colors,
    WEB_BROWSER,
    Container,
    alignment,
    margin,
    padding,
    Tabs,
    Tab,
    OutlinedButton,
    IconButton,
    icons,
    Checkbox,
    Image,
    ElevatedButton
)


# Write main app code here
# def mainApp(UserControl):
def main(page: Page):
    page.title = "Transportaser"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.bgcolor = "#253439"
    page.update()

    Title = Container(
        content=Text(
            "Transportaser",
            size=70,
            color=colors.WHITE,
            weight="normal"),
        margin=margin.only(top=50)
    )

    Img = Image(
        src=f"images/lightning_icon1.png",
        width=200,
        height=200,
        fit="contain",
    )

    Body = Container(
        content=Text(
            "Connect Device",
            size=40,
            color=colors.WHITE,
            weight="normal")
    )

    Pair_button = Container(
        content=Text("Pair",
                     size=25,
                     color="#253439",
                     bgcolor=colors.WHITE,
                     weight="normal"),
        bgcolor=colors.WHITE,
        alignment=alignment.center,
        width=140,
        height=35,
        border_radius=20,
        on_click=lambda e: print("Pairing, please wait. "),
        margin=margin.only(top=30),
        )

    page.add(Title, Img, Body, Pair_button)

flet.app(
    target=main,
    assets_dir=f"assets"
)