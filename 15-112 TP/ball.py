from vectors import Vec
class Ball:
    def __init__(self, x, y, z, color, angle, stripes, number):
        self.x = x
        self.y = y
        self.z = z
        self.pos = Vec(x, y, z)
        self.vel = Vec(0, 0, 0)
        self.accel = Vec(0, 0, 0)
        self.color = color
        self.angle = angle
        self.stripes = stripes
        self.number = number

        


    
    
    