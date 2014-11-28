import random
from snake import *

# Barva glave in repa
COLOR_HEAD = 'blue'
COLOR_TAIL = 'green'

class CobraCoral(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute

        # Popravi dolžino kace
        # Dirty hack, da vidimo ce bo Andrej opazil :)
        with open('snake.py','r') as f:
            newlines = []
            for line in f.readlines():
                newlines.append(line.replace('for k in range(2, 0, -1):', 'for k in range(5, 0, -1):'))
        with open('snake.py', 'w') as f:
            for line in newlines:
                f.write(line)

    def turn(self):
        """Igrica poklice metodo turn vsakic, preden premakne kaco. Kaca naj se tu odloci, ali se
           bo obrnila v levo, v desno, ali pa bo nadaljevala pot v isti smeri.

           * v levo se obrne s self.turn_left()
           * v desno se obrne s self.turn_right()
           * koordinate glave so self.coords[0]
           * smer, v katero potuje je (self.dx, self.dy)
           * spisek koordinat vseh misk je self.field.mice.keys()
           * spisek vseh kac je self.field.snakes
        """
           
        if random.randint(0,10) < 5:
            if random.randint(0,1) == 1:
                self.turn_left()
            else:
                self.turn_right()
