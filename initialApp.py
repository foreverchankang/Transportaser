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
    ProgressBar,
    Dropdown,
    dropdown,
)


class StationObj(UserControl):  # The bubble which pushed to the page every single click on the ADD button
    def __init__(self, name, delete_station):
        super().__init__()
        self.name = name  # Name of the added station
        self.delete_station = delete_station  # Function to delete the station bubble
        self.btn_delete = IconButton(
            icons.DELETE_OUTLINE,
            tooltip="Delete this station",
            on_click=self.btn_delete_clicked,
            icon_color=colors.RED_700,
        )
        self.rtn_display = None

    def build(self):
        self.rtn_display = Container(
            content=Row(
                controls=[
                    Text(
                        value=self.name,
                        size=20,
                        weight='normal',
                        color=colors.BLACK45
                    ),
                    self.btn_delete,
                ],
                alignment='spaceEvenly',
                vertical_alignment='center',
            ),
            width=120,
            height=50,
            alignment=alignment.center,
            bgcolor=colors.ORANGE_800,
            border_radius=5,
        )

        return self.rtn_display

    def btn_delete_clicked(self, e):
        self.delete_station(self)

    def update(self):
        super().update()


class MainApp(UserControl):
    def __init__(self):
        super().__init__()
        # Adding status variable here #
        self.status = 'root'
        self.main_display = Column(
            horizontal_alignment='center',
            alignment='center',
        )

        self.title = Container(
            content=Text(
                "Transportaser",
                size=70,
                color=colors.WHITE,
                weight="bold"),
            margin=margin.only(top=50)
        )

        self.img = Image(
            src=f"images/lightning_icon1.png",
            width=200,
            height=200,
            fit="contain",
        )

        self.connection_status = Container(
            content=Text(
                "No connection",
                size=40,
                color=colors.RED_500,
                weight="normal"
            )
        )

        self.btn_pair = Container(
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
            on_click=self.btn_pair_clicked,
            margin=margin.only(top=30),
        )

        self.rStations = Row(wrap=True, scroll="always")

        self.title_2 = Container(
            content=Text(
                "Transportaser",
                size=70,
                color=colors.WHITE,
                weight="bold"),
            margin=margin.only(top=30)
        )

        self.txt_pick = Container(
            content=Text(
                "Pick 4",
                size=20,
                color=colors.WHITE,
                weight='normal'),
            margin=margin.only(top=10, bottom=10)
        )

        self.dropdownObj = Container(
            content=Row(
                controls=[
                    Dropdown(
                        hint_text="選擇車站",
                        height=70,
                        width=150,
                        options=[
                            dropdown.Option(key='台北車站'),
                            dropdown.Option(key='淡水'),
                            dropdown.Option(key='石牌'),
                            dropdown.Option(key='大安')
                        ],
                    ),
                    ElevatedButton(text="Add", on_click=self.btn_add_clicked)
                ],
                alignment='center',
                vertical_alignment='center',
            ),
            alignment=alignment.center,
        )

        self.btn_transmit = Container(
            content=ElevatedButton(
                expand=True,
                width=200,
                height=60,
                text="TRANSMIT",
                on_click=self.btn_transmit_clicked,
                icon="start",
                icon_color="green400",
            ),
            margin=margin.only(top=20)
        )

    def btn_add_clicked(self, e):
        name = self.dropdownObj.content.controls[0].value

        # Prevent to add empty StationObj to rStation list
        if name is None:
            return

        station = StationObj(name, self.delete_station)
        self.rStations.controls.append(station)

        # Remove the option from dropdown if it is added to the rStation list
        d = self.dropdownObj.content.controls[0]
        for opt in d.options:
            if opt.key == name:
                d.options.remove(opt)
                break

        self.update()

    def delete_station(self, station):
        self.rStations.controls.remove(station)

        # Add the station back when it is removed from rStations list
        d = self.dropdownObj.content.controls[0]
        d.options.append(dropdown.Option(key=station.name))

        self.update()

    def btn_transmit_clicked(self, e):
        self.btn_transmit.content.disabled = True

        # Loading animation
        self.main_display.controls.append(
            Container(
                content=ProgressRing(
                    width=35,
                    height=35,
                    stroke_width=10
                ),
                margin=margin.only(top=20)
            )
        )
        self.update()
        sleep(3)
        self.main_display.controls.pop()

        # Completion text
        self.main_display.controls.append(
            Container(
                content=Text(
                    "Transmission Completed",
                    size=40,
                    color=colors.GREEN_300,
                    weight="normal"
                )
            )
        )

        self.update()

    def btn_pair_clicked(self, e):
        self.connection_status.content.value = 'Connecting...'
        self.connection_status.content.color = colors.WHITE
        self.main_display.controls.pop()
        self.main_display.controls.append(
            Container(
                content=ProgressRing(
                    width=35,
                    height=35,
                    stroke_width=10
                ),
                margin=margin.only(top=30)
            )
        )
        self.update()
        sleep(3)
        self.main_display.controls.pop()
        self.connection_status.content.value = 'Connected'
        self.connection_status.content.color = colors.GREEN_300
        self.update()
        sleep(1)
        self.status = 'menu'
        self.clear()
        self.main_display.controls.append(self.title_2)
        self.main_display.controls.append(self.txt_pick)
        self.main_display.controls.append(self.dropdownObj)
        self.main_display.controls.append(self.rStations)
        self.main_display.controls.append(self.btn_transmit)
        self.update()

    def build(self):
        if self.status == 'root':
            self.clear()
            self.main_display = Column(
                controls=[
                    self.title,
                    self.img,
                    self.connection_status,
                    self.btn_pair
                ],
                alignment='center',
                horizontal_alignment='center'
            )
            return self.main_display
        elif self.status == 'menu':
            self.clear()
            self.main_display = Column(
                controls=[
                    self.title_2,
                    self.txt_pick,
                    self.dropdownObj,
                    self.rStations,
                    self.btn_transmit
                ],
                alignment='center',
                horizontal_alignment='center'
            )
            return self.main_display

    def clear(self):
        for c in self.main_display.controls:
            self.main_display.controls.remove(c)

    def update(self):
        super().update()


def main(page: Page):
    page.title = "Transportaser"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.bgcolor = "#253439"
    page.update()

    # create application instance here
    app = MainApp()

    # add application's root control to the page here
    page.add(app)


flet.app(target=main, assets_dir=f"assets")
