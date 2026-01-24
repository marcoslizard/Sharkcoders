from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty , NumericProperty , ListProperty
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
perguntas = [
    {
        "pergunta": "Quem foi o Campeão de Formula 1 de 2025",
        "respostas": ["Lando Norris","Max Verstappen","Oscar Piastri"],
        "correta": "Lando Norris"
        },
    {
        "pergunta": "Oque significa o DRS",
        "respostas": ["Dynamic Racing Stabilizer","Dynamic Rear Spoiler","Drag Reduction System"],
        "correta": "Drag Reduction System"
        },
    {
        "pergunta": "Qual a principal função do safety car na F1?",
        "respostas": ["Aumentar a velocidade da corrida", "Controlar o ritmo e garantir segurança", "Fazer ultrapassagens"],
        "correta": "Controlar o ritmo e garantir segurança"
        },
    {
        "pergunta": "Quando podemos dizer que um carro está fora da pista",
        "respostas": ["quando nenhuma parte dos pneus está sobre a linha branca","Quando as duas rodas ultrapassam a linha branca","Quando o carro bate num muro"],
        "correta": "Quando nenhuma parte dos pneus está sobre a linha branca"
        }

]


class QuizLayout(BoxLayout):
    pergunta_texto = StringProperty("")
    opcoes = ListProperty([])
    pontuacao = NumericProperty(0)
    index = NumericProperty(0)

    def on_kv_post(self, base_widget):
        self.carregar_proxima()

    def carregar_proxima(self):
        if self.index < len(perguntas):
            pergunta_atual = perguntas[self.index]
            self.pergunta_texto = pergunta_atual["pergunta"]
            self.opcoes = pergunta_atual["respostas"]

        else:
            self.pergunta_texto = "Fim do Quiz"
            self.opcoes = []
            self.ids.resposta1.disabled = True
            self.ids.resposta2.disabled = True
            self.ids.resposta3.disabled = True

    def responder(self, resposta_escolhida):
        correta = perguntas[self.index]["correta"]
        if resposta_escolhida == correta:
            self.pontuacao += 1
            self.mostrar_popup("Certo!","Resposta correta!")
        else:
            self.mostrar_popup("Errado", f"A resposta correta era: {correta}")

        self.index += 1
        self.carregar_proxima()

    def mostrar_popup(self, titulo, mensagem):
        popup = Popup(title = titulo,
                  content=Label(text=mensagem),
                  size_hint=(None,None), size=(300,200))

        popup.open()
class QuizApp(App):
    def build(self):
        return QuizLayout()

QuizApp().run()