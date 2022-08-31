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

    # create application instance here
    # app = mainApp()

    # add application's root control to the page here
    # page.add(app)


flet.app(target=main)
