import flet
from time import sleep
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
    ElevatedButton,
    ProgressRing,
)


# Write main app code here
# def mainApp(UserControl):
def main(page: Page):
    page.title = "Transportaser"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.bgcolor = "#253439"
    page.update()

    title = Container(
        content=Text(
            "Transportaser",
            size=70,
            color=colors.WHITE,
            weight="normal"),
        margin=margin.only(top=50)
    )

    img = Image(
        src=f"images/lightning_icon1.png",
        width=200,
        height=200,
        fit="contain",
    )

    body_connect = Container(
        content=Text(
            "Connect Device",
            size=40,
            color=colors.WHITE,
            weight="normal")
    )

    body_connecting = Container(
        content=Text(
            "Connecting...",
            size=40,
            color=colors.WHITE,
            weight="normal")
    )

    pair_button = Container(
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
        on_click=lambda e: (page.remove(body_connect, pair_button), page.add(body_connecting, pr)),
        margin=margin.only(top=30),
        )

    page.add(title, img, body_connect, pair_button)

    pr = ProgressRing(width=35, height=35, stroke_width=10)
    for i in range(0, 101):
        pr.value = i * 0.01
        sleep(0.05)
        page.update()


flet.app(target=main, assets_dir=f"assets")
