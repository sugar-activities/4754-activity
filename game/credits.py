# -*- coding: utf-8 -*-
import spyral


class Creditos(spyral.Scene):
    def __init__(self, size):
        spyral.Scene.__init__(self, size)
        self.background = spyral.Image(size=self.size).fill((255,255,255))

        self.velocidad = 20.0

        spyral.event.register("input.keyboard.down.*", self.leave)
        spyral.event.register("input.mouse.down.*", self.leave)
        hangman = LogoSprite(self, "images/Hangman-0.png")
        secuencia = [spyral.Image("images/Hangman-0.png"), 
                     spyral.Image("images/Hangman-1.png"),
                     spyral.Image("images/Hangman-2.png"),
                     spyral.Image("images/Hangman-3.png"),
                     spyral.Image("images/Hangman-4.png"),
                     spyral.Image("images/Hangman-5.png"),
                     spyral.Image("images/Hangman-6.png")]
        animacion = spyral.Animation("image", spyral.easing.Iterate(secuencia), duration=10, loop=True)

        arbol = LogoSprite(self, "images/Arbol.png")
        arbol.scale = 0.5

        sprites = [
                MultiTexto(self, "Taller del Artesano", style="title"),
                MultiTexto(self, u"Ambiente de creación de videojuegos para Sugar y Spyral."),
                Espacio(self),
                MultiTexto(self, u"Ahorcadito", style="title"),
                MultiTexto(self, u"Aprende sobre tus derechos. Frases basadas en el Código de la Infancia y Adolescencia (Ley 1098 de 2006) de la República de Colombia."),
                MultiTexto(self, u"Adaptación por Laura Vargas. Ícono por Sebastian Silva."),
                Espacio(self),
                MultiTexto(self, u"Fondo \"Árbol\" por Javier Mercado."),
                arbol,
                Espacio(self),
                MultiTexto(self, u"Las siguientes personas contribuyeron a este juego durante el \
                                    evento Sugar Camp Chía 2014 : \
                                    Stefany Alvarez Meneses, Javier Eduardo Mercado Moreno, \
                                    Zaida Yolibeth Beltrán Durán, Maria Emilia Bustamante Hernández, \
                                    Natali Montoya Zuluaga, Yeison Ardila Agudelo, \
                                    Rafael Antonio Polo Ceballos."),
                Espacio(self),
                hangman,
                MultiTexto(self, u"imagenes obtenidas de artículo de Wikipedia \"Hangman (game)\"."),
                MultiTexto(self, u"<http://en.wikipedia.org/wiki/File:Hangman-0.png>", style="small"),
                Espacio(self),
                MultiTexto(self, u"sonidos \"BonusCube\" y \"Hurt\", CC-0 Public Domain by RaoulWB"),
                MultiTexto(self, u"<http://opengameart.org/content/platform-small-sound-effect-pack>", style="small"),
                Espacio(self),
                MultiTexto(self, u"sonidos \"snare\" y \"chipquest\" CC-BY 3.0 by Bart Kelsey. Commissioned by Will Corwin for OpenGameArt.org (http://opengameart.org)"),
                MultiTexto(self, u"<http://opengameart.org/content/level-up-sound-effects>", style="small"),
                Espacio(self),
                MultiTexto(self, u"sonido \"Applause\" tomado de LibreOffice, MPLv2"),
                Espacio(self),
                MultiTexto(self, u"sonido \"Punch\" tomado de ejemplos de PyGame, LGPLv2.1"),
                Espacio(self),
                MultiTexto(self, u"motor de videojuegos \"Spyral\" bajo licencia GNU LGPLv2.1"),
                MultiTexto(self, u"© Copyright 2012, Robert Deaton, Austin Bart."),
                MultiTexto(self, u"documentación disponible en <http://platipy.org/>", style="small"),
                Espacio(self),
                MultiTexto(self, u"Gracias al equipo Spyral por la excelente herramienta y a todos \
                                   aquellos sobre cuyos hombros estamos parados."),
                Espacio(self),
                MultiTexto(self, u"obra facilitada y desarrollada por:"),
                LogoSprite(self, "images/logo_labs.png"),
                MultiTexto(self, u"en alianza con:"),
                LogoSprite(self, "images/transformando.png"),
                Espacio(self),
                MultiTexto(self, u"Este juego fue desarrollado en el contexto del Taller \
                                    de Artesanía en Programación de Videojuegos \
                                    desarrollado en Chía durante 2014."),
                MultiTexto(self, u"""Colaboradores: Johan Camilo Adames Sanchez,
                                    Cristian Camilo Aguirre Quiroga,
                                    Yojan Stiven Chamorro Rodriguez,
                                    Laura Catalina Medina Arriero,
                                    Duvan Alexis Pisco Adames,
                                    Jose Benjamin Quiroga Torres,
                                    Johan Smith Sanchez,
                                    Johan David Barrera Espeleta,
                                    Andres Felipe Rozo Garzón,
                                    Maurel Yurani Diaz Mendivieso"""),
                MultiTexto(self, u"Copyright © 2014 Sebastian Silva, Laura Vargas."),
                LogoSprite(self, "images/gplv3.png"),
                MultiTexto(self, u"""
                                Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General de GNU tal como está publicada por la Free Software Foundation, bien de la versión 3 de dicha Licencia o bien (según su elección) de cualquier versión posterior.\n
                                Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA, incluso sin la garantía MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN PROPÓSITO PARTICULAR. Véase la Licencia Pública General de GNU para más detalles.\n
                                Usted debería haber recibido una copia de la Licencia Pública General junto con este programa. Si no ha sido así, consulte <http://www.gnu.org/licenses>."""),
                Espacio(self, 200),
                MultiTexto(self, u"\"El derecho a la vida es inviolable; no habrá pena de muerte.\" - Constitución de Colombia, 1991", style="small"),
                ]

        self.leaving = None

        cur_place = self.height
        for sprite in sprites:
            sprite.y = cur_place
            cur_place = cur_place + sprite.height + 30
            self.scrollup(sprite)

        hangman.animate(animacion)

        spyral.event.register("system.quit", spyral.director.pop)

    def scrollup(self, sprite):
        distancia = sprite.pos.distance((sprite.x, 0))
        tiempo = distancia / self.velocidad
        anim = spyral.Animation( "y", spyral.easing.Linear( sprite.y, -500), tiempo )
        sprite.animate(anim)

    def leave(self):
        if not self.leaving:
            spyral.director.pop()
        self.leaving = True

class Espacio(spyral.Sprite):
    def __init__(self, scene, pixeles=30):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(scene.width, pixeles))
        self.anchor = "midtop"
        self.x = scene.width/2

class LogoSprite(spyral.Sprite):
    def __init__(self, scene, filename):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(filename=filename)
        self.anchor = "midtop"
        self.x = scene.width/2

class MultiTexto(spyral.Sprite):
    def __init__(self, scene, text, style=None):
        spyral.Sprite.__init__(self, scene)

        font_path = "fonts/LiberationSans-Regular.ttf"
        if style=="title":
            self.font = spyral.Font(font_path, 48, (0,0,0))
        elif style=="small":
            self.font = spyral.Font(font_path, 16, (0,0,0))
        else:
            self.font = spyral.Font(font_path, 24, (0,0,0))
        self.line_height = self.font.linesize
        self.margen = 30

        text_width = self.font.get_size(text)[0]

        ancho_promedio = self.font.get_size("X")[0]
        caracteres = (scene.width - 2 * self.margen) / ancho_promedio
        self.lineas = self.wrap(text, caracteres).splitlines()
        self.altura = len(self.lineas) * self.line_height

        self.image = spyral.Image(size = (scene.width, self.altura)).fill((255,255,255))
        self.image = self.render_text(text)

    def render_text(self, text):

        bloque = spyral.Image(size=(self.width, self.altura))

        ln = 0
        for linea in self.lineas:
            bloque.draw_image(image=self.font.render(linea),
                                position=(0, ln * self.line_height),
                                anchor="midtop")
            ln = ln + 1
        return bloque


    def wrap(self, text, length):
        """ Sirve para cortar texto en varias lineas """
        words = text.split()
        lines = []
        line = ''
        for w in words:
            if len(w) + len(line) > length:
                lines.append(line)
                line = ''
            line = line + w + ' '
            if w is words[-1]: lines.append(line)
        return '\n'.join(lines)

if __name__ == "__main__":
    size = (800, 600)
    spyral.director.init( size )
    spyral.director.push( Creditos(size=size) )
    spyral.director.run()
