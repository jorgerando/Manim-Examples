from manim import *
import numpy as np

class TextoBasico(Scene):

   def construct(self):

        # crear text normal con Manim
        saludo = Text("Hola mundo",
        color=RED,
        font_size=40)
        # añadir a la escena sin animacion
        self.add(saludo)
        # eliminar de la escena tras 2 segundos
        self.wait(1)
        self.remove(saludo)

        #crear texto latex
        saludo2 = Tex(r'$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$')
        self.add(saludo2)
        self.wait(1)
        self.remove(saludo2)

class TextoAnimaciones(Scene):

    def construct(self):

        msg = Text("Hola")
        # Animacion creacion escritura
        self.play(Write(msg),runtime=2)
        # Animacion texto elminiacion desvanecer
        self.play(FadeOut(msg))
        self.wait(1)

        msg1 = Tex("Formula matematica")
        msg2 = Tex(r'$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$')
        #Transformacion de un texto en otro
        self.play(Transform(msg1,msg2),runtime=5)
        self.wait(1)
        self.remove(msg1,msg2)

        #concatenar textos uno debajo de otro
        texto1 = Tex(r'$\frac{1}{2}(2x^2 + 4x + 6)$')
        self.play(Write(texto1))
        self.wait(0.3)

        # Paso 2: Simplificar dentro del paréntesis dividiendo cada término por 2
        texto2 = Tex(r'$\frac{1}{2}(x^2 + 2x + 3)$')
        texto2.next_to(texto1, DOWN)  # Coloca el texto2 debajo del texto1
        self.play(Write(texto2))
        self.wait(0.3)

        # Paso 3: Expandir el factor común
        texto3 = Tex(r'$\frac{1}{2}x^2 + \frac{1}{2}(2x) + \frac{1}{2}(3)$')
        texto3.next_to(texto2, DOWN)
        self.play(Write(texto3))
        self.wait(0.3)

class TextoAgruparMover(Scene):

      def construct(self):

          tex1 = Text('Hola',color=BLUE,)
          circle = Circle(radius=1,color=BLUE)

          # la posicion del texto es relativa al circulo
          tex1.next_to(circle,UP)

          # agrupo los 2 elementos
          grup = VGroup(tex1,circle)
          self.play(Write(grup))
          self.wait(1)

          # movimientos absolutos

          # hay 8 unidades de largo y 6 de alto (x :[-8,8] , y :[-6,6])
          # move_to mueve un objeto de manera absoluta
          self.play(grup.animate.move_to(np.array([7,0,0])))
          self.wait(1)
          self.play(grup.animate.move_to(np.array([-7,0,0])))
          self.wait(1)
          self.play(grup.animate.move_to(np.array([0,5,0])))
          self.wait(1)
          self.play(grup.animate.move_to(np.array([0,-5,0])))
          self.wait(1)

          # shift suma a la posion un vector
          dir = [UP,DOWN,RIGHT,LEFT]
          self.play(grup.animate.to_edge(UP*2 + LEFT*2))
          self.wait(1)
          self.play(grup.animate.to_edge(DOWN*2 + RIGHT*2))
          self.wait(1)
