elements = []
for x in range(10):
  for y in range(10):
    #if x != y:
    elements.append((x, y))
print elements
print elements [5]

#r = ([] for iin range(10))

class Element: 
#  global ax0, ay0
  x = 0    #x position, m
  y = 0    #y position, m
  vx0 = 0  #Start speed along the x-axis, m/s
  vy0 = 0  #Start speed along the y-axis, m/s
  ax0 = 0  #Start acceleration along the x-axis, m/s**2
  ay0 = 9.8 #Start acceleration along the y-axis, m/s**2
  specific_mass = 0 #specific mass, kg/m**3 ???
  def set_acceleration(self, ax0_p, ay0_p):
      self.ax0=ax0_p
      self.ay0=ay0_p

e1 = Element()
e1.set_acceleration(0, 9.9)
print e1.ay0

class Element2: 
  def __init__(self):
    self.x = 0    #x position, m
    self.y = 0    #y position, m
    self.vx0 = 0  #Start speed along the x-axis, m/s
    self.vy0 = 0  #Start speed along the y-axis, m/s
    self.ax0 = 0  #Start acceleration along the x-axis, m/s**2
    self.ay0 = 9.8 #Start acceleration along the y-axis, m/s**2
    self.specific_mass = 0 #specific mass, kg/m**3 ???
  def set_initial_position(self, ax0, ay0):
      self.ax0=ax0
      self.ay0=ay0
  def set_initial_velocity(self, ax0, ay0):
      self.ax0=ax0
      self.ay0=ay0
  def set_initial_acceleration(self, ax0, ay0):
      self.ax0=ax0
      self.ay0=ay0

e2 = Element2()
e2.set_initial_acceleration(0, 9.999)
print e2.ay0

#Fra http://stackoverflow.com/questions/7745562/appending-to-2d-lists-in-python
listy = [[] for i in range(3)]

#Fra http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch20s05.html
table= [ [ 0 for i in range(6) ] for j in range(6) ]
print table
for d1 in range(6):
    for d2 in range(6):
        table[d1][d2]= d1+d2+2
print table


world = [ [ 0 for x in range(6) ] for y in range(6) ]
print table
for x in range(6):
    for y in range(6):
        world [x][y]= Element2()
#print world

for x in range(6):
    for y in range(6):
        world [x][y].y = 120 #.setinitial_position(0,9)

for x in range(6):
    for y in range(6):
      print x, y, world [x][y].ay0
