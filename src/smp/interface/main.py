from flet import *

def main(page:Page):
    page.title = "SMP --- STUDENT MANAGER PROJECT --- "
    # page.window.width = page.width
    # page.window.height = 730
    page.bgcolor = Colors.CYAN_900
    page.theme_mode = ThemeMode.SYSTEM
    page.auto_scroll = True

    page.appbar = AppBar(
        leading=Icon(icons.HOME),
        leading_width=40,
        title=Text("SMP"),
        center_title=True,
        bgcolor=Colors.CYAN_900,
        actions=[
            IconButton(icons.SEARCH, tooltip="Search"),
            IconButton(icons.PERSON,tooltip="Person"),
            IconButton(icons.NOTIFICATIONS, tooltip="Notfications"),
            IconButton(icons.SETTINGS, tooltip="Settings"),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Students Manager"),
                    PopupMenuItem(text="Teacher Manager"),
                    PopupMenuItem(text="Class Manager"),
                    PopupMenuItem(text="Subjects Manager"),
                    PopupMenuItem(),
                    PopupMenuItem(text="Crit"),
                    PopupMenuItem(text="Abuts"),
                ],
            )
        ]
    )
            

    page.add()

    page.update()

app(main)