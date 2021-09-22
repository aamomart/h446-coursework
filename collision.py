def rectCollision(x1, y1, w1, h1, x2, y2, w2, h2):
    
    tWidth = (w1/2)+(w2/2)
    tHeight = (h1/2)+(h2/2)
    xDistance = abs(x2-x1)
    yDistance = abs(y2-y1)
    
    return xDistance < tWidth and yDistance < tHeight