import turtle

class Forma:
    def desenhar(self):
        pass
class Circulo(Forma):
    def desenhar(self):
        turtle.speed(10)
        turtle.circle(50)

class Quadrado(Forma):
    def desenhar(self):
        turtle.speed(5)
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)  #

if _name_ == "_main_":
    forma_circulo = Circulo()
    forma_quadrado = Quadrado()

    forma_circulo.desenhar()

    turtle.penup()
    turtle.setpos(200, 0)
    turtle.pendown()

    forma_quadrado.desenhar()

    turtle.done()
