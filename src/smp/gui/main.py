from flet import *

def main(page:Page):
    page.title = "SMP --- STUDENT MANAGER PROJECT --- "
    # page.window.width = page.width
    # page.window.height = 730
    page.bgcolor = Colors.CYAN_900
    page.theme_mode = ThemeMode.DARK

    page.auto_scroll = True

    page.add(
        Text("Hello",bgcolor=Colors.WHITE,color=Colors.BLACK,text_align=TextAlign.CENTER,width=page.width,weight=FontWeight.BOLD)
    )

    page.update()

app(main)