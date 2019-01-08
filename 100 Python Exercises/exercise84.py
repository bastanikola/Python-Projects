#Question:
'''
Please use a pyglet library to create a Hello world application

Hint: The pyglet homepage on PyPi could lead you to the answer:
https://pypi.python.org/pypi/pyglet
'''
#Answer:
'''
import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello world',
                           font_name = 'Times New Roman',
                           font_size = 36,
                           x=window.width//2, y=window.height//2,
                           anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()

https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html#hello-world
'''
