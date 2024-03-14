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
        
        
        return f"{round(interval.interval_start, 5)} {chr_amount} {round(interval_end, 5)}"



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
                            f"= {round(self.iteration.average, 5)}"
                        ),
                        ft.Text(
                            width=10
                        ),
                        ft.Text(
                            f"f({round(self.iteration.average, 5)})  =  {round(self.iteration.calculation_average, 5)}"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                    
                ),
                padding=ft.padding.all(10),
            )
        )


class TextFancField(ft.UserControl):
    
    def __init__(self,):
        super().__init__()
        
        
        
    def build(self):
        
        # коффициент a
        
        cofifier = lambda name:(  
            ft.TextField(
                label=name, width=150, 
                keyboard_type=ft.KeyboardType.NUMBER, 
                text_align=ft.TextAlign.CENTER,  
                input_filter=ft.InputFilter(allow=True, regex_string=r"[-0-9]", replacement_string="")
            )
        )
        
        self.cofifier_a = cofifier('коэффициент a')
        self.cofifier_b = cofifier('коэффициент b')
        self.cofifier_d = cofifier('коэффициент d')
        self.cofifier_c = cofifier('коэффициент c')
        
        
        blok = ft.Row(
            controls=[
                ft.Image(src="f.png"),
                self.cofifier_a,
                self.cofifier_b,
                self.cofifier_d,
                self.cofifier_c
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        return blok
    
    def get_formula(self):
        return f"({self.cofifier_a.value} * (x ** 3)) + ({self.cofifier_b.value} * (x ** 2)) + ({self.cofifier_d.value} * (x ** 1)) + ({self.cofifier_c.value})"


def main(page: ft.Page):
    page.title = "Test"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    
    input_text = TextFancField()
    
    steps_decision: ft.Column
    answer: ft.Column
    
    text_field_a = ft.TextField(label="a", width=300)
    text_field_b = ft.TextField(label="b", width=300)
    text_field_accuracy = ft.TextField(label="точность", width=300)
    
    
    def on_click_calculate(e):
        print(input_text.get_formula())
        
        cal = Calculation(
            input_text.get_formula(), 
            [
                Interval(
                    int(text_field_a.value), 
                    int(text_field_b.value)
                )
            ], 
            len(text_field_accuracy.value.split('.')[1])
        )
        
        answer_solutions = cal.solutions_by_iterations()
        
        card = [
            CardIteration(i) for i in answer_solutions[0].iterations
        ]
                
        steps_decision.controls = card
        
        answer.controls = [
            ft.Card(
                content=ft.Container(
                    ft.Column(
                        controls=[
                            ft.Text(f"Ответ: {answer_solutions[0].root}", size=20)
                        ]
                    ),
                    padding=ft.padding.all(10),
                )
            )
        ]
        
        
        function_policy.update()
        page.update()
    
    
    button_calculate = ft.ElevatedButton(
        text="Calculate",
        on_click=on_click_calculate
    )
    
    
    steps_decision = ft.Column(
        [],
        scroll=ft.ScrollMode.AUTO
    )
    
    
    answer = ft.Column(
        [],
        width=400
    )
    
    
    steps_decision_and_answer = ft.Container(
        ft.Column(
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
                ft.Row(
                    controls=[
                        text_field_accuracy,
                        text_field_a,
                        text_field_b,
                        button_calculate,  
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                steps_decision_and_answer,
                
            ]
        ),
    )
    
    page.scroll = ft.ScrollMode.AUTO
    import math
    
    page.theme_mode = ft.ThemeMode.LIGHT
    

    page.update()
    page.add(function_policy)
    
    
ft.app(target=main)