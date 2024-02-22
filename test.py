import math

import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    page.title = "Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

   
    page.theme_mode = ft.ThemeMode.LIGHT
    
    a = ft.Container(
        bgcolor=ft.colors.AMBER_100,
        content=ft.Row(
            tight=True,
            spacing=0,
            controls=[
                ft.Text('log', size=20), ft.Text('2', size=15, offset=(0, -0.5)), 
                ft.Container(
                    width=10, 
                    height=10, 
                    bgcolor=ft.colors.TRANSPARENT, 
                    border_radius=ft.border_radius.all(0), 
                    margin=ft.margin.only(0,0,0, 0), 
                    border=ft.border.all(2, ft.colors.BLUE_GREY_500,
                    offset=(0, -0.5))
                )
            ]
        )
    )

    page.add(a)

ft.app(main)