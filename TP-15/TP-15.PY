import py5
x = 0
def setup():
    py5.size(400, 400)
    py5.background(255)
def draw():
    global x
    py5.background(255)
    py5.fill(150, 0, 150)
    py5.circle(x, 200, 50)
    x += 2 # Mueve el círculo hacia la derecha

    if x > py5.width:
        x = 0 # Reinicia la posición si se sale de la ventana
py5.run_sketch()