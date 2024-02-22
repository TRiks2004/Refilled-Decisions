from typing import Any, List
import flet as ft
import math

import flet.canvas as cv

from Calculation import Calculation, Interval, Iteration


class CardIteration(ft.UserControl):
    def __init__(self, iteration: Iteration):
        super().__init__()
        
        self.iteration = iteration

    def get_amount(self, interval: Interval) -> str:
        
        chr_amount: str
        
        interval_end = interval.interval_end
        
        if interval.interval_end < 0:
            chr_amount = '-'
            interval_end = interval_end * -1
        else:
            chr_amount = f"+"
        
        
        return f"{interval.interval_start} {chr_amount} {interval_end}"



    def build(self) -> ft.Card:
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            f"x{self.iteration.number + 1} ="
                        ),
                        ft.Column(
                            controls=[
                                ft.Container(
                                    ft.Text(self.get_amount(self.iteration.interval),),
                                    padding=ft.padding.only(bottom=1, left=5, right=5),
                                    border=ft.border.only(bottom=ft.BorderSide(1.5, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))),
                                ),                               
                                ft.Text(
                                    '2'
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=1
                        ),
                        ft.Text(
                            f"= {self.iteration.average}"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                    
                ),
                padding=ft.padding.all(10),
            )
        )



def main(page: ft.Page):
    page.title = "Test"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    
    input_text = ft.TextField(value='math.fabs(x + math.pow(math.e, x)) - 2')
    
    steps_decision: ft.Column
    
    
    def on_click_calculate(e):
        
        
        cal = Calculation(input_text.value, [Interval(-3, -1)], 5)
        
        answer = cal.solutions_by_iterations()
        
        
        card = [
            CardIteration(i) for i in answer[0].iterations
        ]
                
        steps_decision.controls = card
        
        
        
        
        
        print(input_text.value)
        function_policy.update()
        page.update()
    
    
    button_calculate = ft.ElevatedButton(
        text="Calculate",
        on_click=on_click_calculate
    )
    
    
    steps_decision = ft.Column(
        [],
        scroll=ft.ScrollMode.AUTO,
        
    )
    
    
    answer = ft.Column(
            [
            ft.Text("Step 1"),
            ft.Text("Step 2"),
            ft.Text("Step 3"),
            ft.Text("Step 4"),
            ft.Text("Step 5"),
        ],
        width=400
    )
    
    
    steps_decision_and_answer = ft.Container(
        ft.Row(
            controls=[
                steps_decision,
                answer
            ], 
        )
    )
    
    
    function_policy = ft.Container(
        ft.Column(
            controls=[
                input_text,
                button_calculate,
                steps_decision_and_answer,
                
            ]
        ),
    )
    
    page.scroll = ft.ScrollMode.AUTO
    
    
    page.update()
    page.add(function_policy)
    
    
ft.app(target=main)