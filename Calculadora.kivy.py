from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import math

class CalculadoraLayout(BoxLayout):

    def calcular(self):
        try:
            expressao = self.ids.display.text
            expressao_original = expressao

            # Substituições para avaliação
            expressao_eval = expressao.replace("^", "**")
            expressao_eval = expressao_eval.replace("√", "math.sqrt")
            expressao_eval = expressao_eval.replace("sin", "math.sin")
            expressao_eval = expressao_eval.replace("cos", "math.cos")
            expressao_eval = expressao_eval.replace("π", "3.1415927")
            expressao_eval = expressao_eval.replace("x", "*")
            expressao_eval = expressao_eval.replace("÷", "/")

            resultado = eval(expressao_eval)

            # Formata o resultado
            if "π" in expressao_original:
                resultado_formatado = str(resultado)
            else:
                resultado_formatado = self.format_result(resultado)

            # Adiciona espaços entre números e operadores no display
            expressao_com_espacos = expressao_original
            for op in ["+", "-", "X", "÷", "="]:
                expressao_com_espacos = expressao_com_espacos.replace(op, f" {op} ")

            self.ids.display.text = f"{expressao_com_espacos} = {resultado_formatado}"

        except:
            self.ids.display.text = "Erro"

    def add_to_display(self, value):
        self.ids.display.text += value

    def clear_display(self):
        self.ids.display.text = ""

    def add_pi(self):
        self.ids.display.text += "π"

    def format_result(self, resultado):
        # Arredonda a 2 casas decimais
        resultado_arredondado = round(resultado, 2)

        # Se for número inteiro, converte para int
        if resultado_arredondado.is_integer():
            return str(int(resultado_arredondado))
        else:
            return str(resultado_arredondado)


class CalculadoraApp(App):
    def build(self):
        return CalculadoraLayout()


CalculadoraApp().run()


















