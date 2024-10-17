import turtle as tl

class ponto():
  def __init__(self,x,y):
    self.x = x
    self.y = y

coord = ponto(10,20)
tl.goto(coord.x,coord.y)
tl.done()
