from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
DADOS_CLIMA = {
    "lisboa": {"temp": "22C", "condição": "Sol"},
    "porto": {"temp": "19C", "condição": "Nublado"},
    "coimbra": {"temp": "21C", "condição": "Parcialmente Nublado"},
    "faro": {"temp": "25C", "condição": "Céu limpo"}
}

class TelaClima(BoxLayout):
    resultado = StringProperty("Insira uma cidade e carregue em Pesquisar")


    def buscar_clima(self):
        cidade = self.ids.entrada.text.lower().strip()
        if cidade in DADOS_CLIMA:
            clima = DADOS_CLIMA[cidade]
            self.resultado = f"{cidade.title()}: {clima['temp']} - {clima['condição']}"
        else:
            self.resultado = f"Clima para '{cidade.title}' não encontrado."


class ClimaApp(App):
    def build(self):
        return TelaClima()

ClimaApp().run()

#Fazer varias listas diferentes tipos de condições meteorologicas dependo de onde está a estação meteorologica
#Deteção de Alertas automáticos de meteorologicas
#Verde:Limpo
#Amarelo:médio
#laranja:médio grave
#vermelho: grave