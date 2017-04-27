# 4주차 과제 1

class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
    def get(self):
        tup =  (self.x, self.y)
        print (tup)
    def move(self, dx,dy):
        self.x += dx
        self.y += dy
