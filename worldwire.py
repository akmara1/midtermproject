from dataclasses import Field
from string import whitespace
from tkinter import *
from time import sleep
from random import randint, choice
from turtle import heading

class Field:
    def __init__(self, c, m, n, width, height, ):
        self.m = m
        self.n= n
        self.a = []
        self.c = c
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.m):
            self.a.append([])
            for j in range(self.n):
                self.a[i].append(0)
        for num in range(4,10):
            self.a[num][3] = 1
            self.a[num][11] = 1
            self.a[10][11] = 1
            self.a[11][11] = 1
            self.a[3][10] = 1
            self.a[4][9] = 2
            self.a[5][9] = 3
            self.a[6][9] = 1
            self.a[7][9] = 1
            self.a[8][9] = 1
            self.a[9][9] = 1
            self.a[10][9] = 2
            self.a[11][9] = 3
            self.a[10][3] = 2
            self.a[10+1][3] = 3
            self.a[10+2][3+1] = 1
            self.a[10+3][3+1] = 1
            self.a[10+4][3+1] = 1
            self.a[10+5][3+1] = 1
            self.a[10+6][3+1] = 2
            self.a[10+7][3+1] = 3
            self.a[3][3+1] = 1
            self.a[4][5] = 1
            self.a[5][5] = 1
            self.a[6][5] = 1
            self.a[7][5] = 3
            self.a[8][5] = 2
            self.a[9][5] = 1
            self.a[10][5] = 1
            self.a[11][5] = 1
            self.a[12][10] = 1
            self.a[13][10] = 1
            self.a[14][10] = 1
            self.a[15][10] = 1
            self.a[16][10] = 1
            self.a[17][10] = 1
            self.a[18][9] = 1
            self.a[17][8] = 1
            self.a[18][8] = 1
            self.a[19][8] = 1
            self.a[20][8] = 1
            self.a[17][7] = 1
            self.a[20][7] = 1
            self.a[21][7] = 1
            self.a[22][7] = 2
            self.a[23][7] = 3
            self.a[24][7] = 1
            self.a[17][6] = 1
            self.a[18][6] = 1
            self.a[19][6] = 1
            self.a[20][6] = 1
            self.a[18][5] = 1
            #self.x[11+7][5] = 1
            self.draw()
    def step(self):
        b = []
        for i in range(self.m):
            b.append([])
            for j in range(self.n):
                b[i].append(0)
        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if self.a[i][j]==3:
                    b[i][j]=2
                elif self.a[i][j]==2:
                    b[i][j]=1
                elif self.a[i][j]==1:
                    if self.a[i-1][j]==3 or self.a[i+1][j]==3 or self.a[i][j-1]==3 or self.a[i][j+1]:
                        b[i][j] = 3
                    elif self.a[i-1][j-1]==3 or self.a[i+1][j-1]==3 or self.a[i-1][j+1]==3 or self.a[i+1][j+1]==3:
                        b[i][j] = 3
                    else:
                        b[i][j]=1
                else:
                    b[i][j]=0 
        self.a = b
    def print_field(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "grey"
        sizem = self.width // (self.m - 2)
        sizen = self.height // (self.n - 2)
        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if (self.a[i][j])==1:
                    color = "yellow"
                elif (self.a[i][j]==2):
                    color = "red"
                elif (self.a[i][j]==3):
                    color = "blue"
                else:
                    color = "white"
                self.c.create_rectangle((i-1) * sizem, (j-1) * sizen, (i) * sizem, (j) * sizen, fill=color)
        self.step()
        self.c.after(500, self.draw)


class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(self.x - self.size / 2,
        self.y - self.size / 2,
        self.x + self.size / 2,
        self.y + self.size / 2,
        fill=self.color)
 
    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()
 
    def draw(self):
 
        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)
 
        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(500, self.draw)
 
 
    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5
 
root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
 
#f = Field(c, 40, 40, 800, 800)
f = Field(c, 40, 40, 800, 800)
f.print_field()
 
'''
p1 = Player(c, 25, 25, 20, "GREEN")
p2 = Player(c, 375, 25, 20, "RED")
 
p1.moveto(150, 200)
p2.moveto(200, 300)
'''
 
root.mainloop()


            
        
