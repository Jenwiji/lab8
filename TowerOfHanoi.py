import turtle

class Disk(object):
    def __init__(self, name = "", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        turtle.left(90)
        turtle.penup()
        turtle.goto(self.dxpos,self.dypos)
        turtle.pendown()
        turtle.right(90)
        for x in range(2):
            turtle.fd(self.dwidth/2)
            turtle.left(90)
            turtle.fd(self.dheight)
            turtle.left(90)
            turtle.fd(self.dwidth/2)

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        turtle.pencolor("WHITE")
        self.showdisk()
        turtle.pencolor("BLACK")



        

