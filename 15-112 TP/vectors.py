import math
#Vector initializer and all methods
class Vec:
   def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z
#Printing a vector
   def Vprint(self):
       print(self.x,self.y,self.z)
#Adding 2 vectors to create a new vector
   def Vadd(v1, v2):
       return Vec(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)
#Adding 2 vectors and replacing the first vector
   def Vadd2(v1, v2):
       v1.x = v1.x+v2.x
       v1.y = v1.y+v2.y
       v1.z = v1.z+v2.z
#Subtracting 2 vectors to create a new vector
   def Vsub(v1, v2):
       return Vec(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z)
#Subtracting 2 vectors and replacing the first vector
   def Vsub2(v1, v2):
       v1.x = v1.x-v2.x
       v1.y = v1.y-v2.y
       v1.z = v1.z-v2.z
#Multiplication create a new vector
   def Vmul(v, c):
       return Vec(v.x*c, v.y*c, v.z*c)
#Multiplication 2 vectors and replacing the first vector
   def Vmul2(v, c):
       v.x = v.x*c
       v.y = v.y*c
       v.z = v.z*c
#Division 2 vectors to create a new vector
   def Vdiv(v, c):
       return Vec(v.x/c, v.y/c, v.z/c)
#Division 2 vectors and replacing the first vector
   def Vdiv2(v, c):
       v.x = v.x/c
       v.y, = v.y/c
       v.z = v.z/c
#Magnitude
   def Vmag(v):
       return math.sqrt((v.x**2+v.y**2+v.z**2))
#Normalization to create a new vector
   def Vnorm(v):
       if Vec.Vmag(v)==0:
           return Vec(0,0,0)
       else:
           return Vec(v.x/Vec.Vmag(v), v.y/Vec.Vmag(v), v.z/Vec.Vmag(v))
#Normalization to replace the first vector
   def Vnorm2(v):
       v.x = v.x/Vec.Vmag(v)
       v.y = v.y/Vec.Vmag(v)
       v.z = v.z/Vec.Vmag(v)
#Dot product
   def Vdot(v1, v2):
       return (v1.x*v2.x)+(v1.y*v2.y)+(v1.z*v2.z)
#Cross product to create a new vector
   def Vcross(v1, v2):
       return Vec(v1.y*v2.z-v1.z*v2.y, v1.z*v2.x-v1.x*v2.z, v1.x*v2.y-v1.y*v2.x)
#Cross product to replace the first vector
   def Vcross2(v1, v2):
       v1.x = v1.y*v2.z-v1.z*v2.y
       v1.y = v1.z*v2.x-v1.x*v2.z
       v1.z = v1.x*v2.y-v1.y*v2.x
       v1.z = v1.x*v2.y-v1.y*v2.x

#Addition of more than 2 vectors
   def Vaddmore(*args):
       sum = Vec(0,0,0)
       for a in args:
           sum = Vec.Vadd(sum, a)
       return sum
#Subtraction of more than 2 vectors
   def Vsubmore(*args):
       i = 0
       for a in args:
           if i < 1:
               diff = a
               i += 1
           else:
               diff = Vec.Vsub(diff, a)
               i += 1
       return diff