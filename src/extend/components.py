import flet as ft
import extend.theme as theme

searchBox = ft.TextField(
    label="Search here",
    focused_border_color=theme.SECONDARY,
    autofocus=True,
    hover_color=theme.HIGHLIGHT,
    bgcolor=theme.BACKGROUND,
    border_color=theme.PRIMARY,
)

searchBtn = ft.FilledButton(
    text="Search",
    bgcolor=theme.PRIMARY,
    color=ft.Colors.WHITE,
    icon=ft.Icons.SEARCH,
    height=50,
)
