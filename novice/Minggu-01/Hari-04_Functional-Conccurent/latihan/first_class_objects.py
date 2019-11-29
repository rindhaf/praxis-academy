def hello_world(h):
    def world(w):
        print(h, w)
    return world 

h = hello_world
x = h("Hello")
x("Rindha")