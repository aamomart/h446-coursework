from collision import rectCollision

x1 = 2
y1 = 3
w1 = 2
h1 = 2

x2 = 3
y2 = 2
w2 = 2
h2 = 2

if rectCollision(x2, y2, w2, h2, x1, y1, w1, h1):
    print("Collision")
else:
    print("No collision")