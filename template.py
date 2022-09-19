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

    page.add()
    Block = Text(
        "Size 50, Normal",
        size=50,
        color="#253439",
        bgcolor="#253439",
        weight="normal",
    )

    Title = Text(
        value="TRANPORTASER",
        size=60,
        color="white",
        bgcolor="",
        weight="bold",
        italic=True,

    )

    Img = Image(
        src=f"images/lightning_icon1.png",
        width=100,
        height=100,
        fit="contain",
    )

    Body = Text(
        value="Connect Device",
        size=45,
        color="white",
        bgcolor="",
        weight="bold",
        italic=True,
    )

    Pair_button = Container(
        content=Text("Pair"),
        margin=10,
        padding=10,
        alignment=alignment.center,
        bgcolor=colors.CYAN_200,
        width=150,
        height=150,
        border_radius=10,
        ink=True,
        on_click=lambda e: print("Pairing")
    )

    page.add(Block, Title, Img, Body, Pair_button)

    # create application instance here
    # app = mainApp()

    # add application's root control to the page here
    # page.add(app)



flet.app(target=main)

flet.app(
    target=main,
    assets_dir=f"assets"
)
