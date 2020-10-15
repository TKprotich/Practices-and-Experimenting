import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols =  1

        self.inside =GridLayout()
        self.inside.cols = 2

        
        
        self.inside.add_widget(Label(text="File Name: "))
        self.fname = TextInput(multiline = False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="File Path: "))
        self.fpath = TextInput(multiline = False)
        self.inside.add_widget(self.fpath)



        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 50)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        fname = self.fname.text
        fpath = self.fpath.text
        file = (fpath + "/" + fname)
        print(file)
        path = "C:/Users/user/Documents"
        images = convert_from_path(file, output_folder=path, fmt='jpeg')
        self.fname.text = ""
        self.fpath.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    MyApp().run()
