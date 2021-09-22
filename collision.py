import math
from tphysics import Game, Rectangle

x1 = 2
y1 = 3
w1 = 2
h1 = 2

x2 = 5
y2 = 2
w2 = 2
h2 = 2

loop = False
global ans

def rectCollision(x1, y1, w1, h1, x2, y2, w2, h2):
    
    print("check2")
    
    tWidth = (x1/2)+(x2/2)
    tHeight = (y1/2)+(y2/2)
    xDistance = (x2-x1)
    yDistance = (y2-y1)
    
    print(xDistance)
    
    if xDistance < tWidth and yDistance < tHeight:
        loop = True
        ans = "COLLISION"
        print("check3")
    
    else:
        loop = True
        ans = "NO COLLISION"
        print("check4")
    

if loop == False:
    print("check1")
    rectCollision(x1, y1, w1, h1, x2, y2, w2, h2)
    
print("check5")
print(ans)