import pyglet
from pyglet.window import mouse
from pyglet.window import key

window = pyglet.window.Window()
event_logger = pyglet.window.event.WindowEventLogger()
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("got an A")
    else:
        window.push_handlers(event_logger)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("success")
    elif button == mouse.RIGHT:
        print("Keep it up")

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
