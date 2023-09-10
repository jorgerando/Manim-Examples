from manim import *

class Transformaciones(Scene):

   def construct(self):

       cua = []
       r = 5.0
       while r > 0.1 :
         squ = Square(side_length=r)
         cua.append(squ)
         r = r - 0.5

       for c in cua :
           self.wait(0.1)
           self.play(Create(c),runtime=0.1)

       # creo un grupo con todos los elementos
       grupo = VGroup(*cua)

       # los roto 4 veces
       for _ in range(4):
         self.play(grupo.animate.rotate(PI/4))
         self.wait(0.5)

       #  escalo
       esc = [0.5,0.5,2,2]
       for s in esc:
         self.play(grupo.animate.scale(s))
         self.wait(0.5)

class FusionarFormas(Scene):
    
    def construct(self):
        # Crea dos círculos en posiciones diferentes
        circulo1 = Circle(color=BLUE).shift(2*LEFT+2*UP)
        circulo2 = Circle(color=RED).shift(2*RIGHT+2*UP)

        # Crea un cuadrado
        cuadrado = Square()

        # Agrega los círculos y el cuadrado a la escena
        self.play(Create(circulo1), Create(circulo2))

        # Transforma el primer círculo en el cuadrado (fusión)
        self.play(ReplacementTransform(circulo1, cuadrado), ReplacementTransform(circulo2, cuadrado))

        # Espera unos segundos
        self.wait(1)
