import eel

eel.init('resources')

@eel.expose
def demo(x):
    return x**2

eel.start('index.html', size=(1600, 1300))