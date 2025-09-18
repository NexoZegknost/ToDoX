import flet as ft
import extend.components as cpn
import extend.theme as theme  

def main(page):
    
    page.adaptive = True
    page.title = "QueztFormula"
    page.bgcolor = theme.BACKGROUND
    page.fonts = {
        "Header": theme.HEADER_FONT,
        "content": theme.CONTENT_FONT,
    }
    page.theme = ft.Theme(font_family="content")

    def search(e):
        searchInput = searchBox.value
        print(searchInput)

    page.appbar = ft.AppBar(
        title=ft.Text(value="QueztFormula", font_family="Header", size=35),
        center_title=True,
        bgcolor=theme.PRIMARY,
    )

    searchBox = cpn.searchBox
    cpn.searchBtn.on_click = search
    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[
                    searchBox,
                    cpn.searchBtn,
                ]
            ),
        ),
    )


ft.app(target=main, assets_dir="assets")
