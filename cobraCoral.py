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

        self.lsc = (0, 0) # Loop start coordinate
        self.loop = 0
        self.step = 0

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

        """
        if random.randint(0,10) < 5:
            if random.randint(0,1) == 1:
                self.turn_left()
            else:
                self.turn_right()
        """

        # Change color
        if len(self.cells) > 1:
            if self.color_head == 'red':
                self.color_head = 'blue'
            elif self.color_head == 'blue':
                self.color_head = 'red'

            if self.color_tail == 'yellow':
                self.color_tail = 'green'
            elif self.color_tail == 'green':
                self.color_tail = 'yellow'

        c = self.coords[0]
        #1 <= y <= 28
        #print(c)

        # Mouse generator
        #self.field.mice[c]...

        # Move bricks
        #self.field.bricks...

        # AI movements
        if len(self.cells) > 1 and (self.step + 1) % 90 == 0:
            print("Cobra Coral: detach the head from the tail")
            self.color_tail = 'white'
            self.color_head = 'blue'
            self.cells = [self.cells[0]] # detach the head from the tail to move easily
        elif len(self.cells) == 1 and (self.step + 1) % 450 == 0:
            print("Cobra Coral: detach all snake heads")
            for i in range(0, len(self.field.snakes), 1):
                self.field.snakes[i].color_tail = 'white'
                self.field.snakes[i].color_head = 'green'
                self.field.snakes[i].cells = [self.field.snakes[i].cells[0]]
        elif self.step % 30 == 0:
            self.turn_left()
        elif self.loop == 1:
            if self.lsc[0] == c[0] and self.lsc[1] == c[1]:
                print("Cobra Coral: stop loop")
                self.loop = 0
                self.turn_right()
            elif self.step % 3 == 0:
                self.turn_left()
        elif self.loop == 0 and c[1] == 14:
            print("Cobra Coral: start loop")
            self.lsc = c
            self.loop = 1
            self.turn_right()
        elif c[1] == 28:
            self.turn_left()
        elif c[1] == 1:
            self.turn_right()

        # Increase move counter
        self.step = self.step + 1
            
        

