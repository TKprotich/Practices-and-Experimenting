import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols =  1

        self.inside =GridLayout()
        self.inside.cols = 2

        
        
        self.inside.add_widget(Label(text="FirstNsame: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="SecondName: "))
        self.last = TextInput(multiline = False)
        self.inside.add_widget(self.last)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="Tel: "))
        self.tel = TextInput(multiline = False)
        self.inside.add_widget(self.tel)

        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 50)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.last.text
        comment = self.email.text
        tel = self.tel.text
        print(name, last, tel, comment)
        self.name.text = ""
        self.last.text = ""
        self.email.text = ""
        self.tel.text = ""
        print(name, last, comment)
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    MyApp().run()
