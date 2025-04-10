from collections import namedtuple

point = namedtuple('Point','x,y')
pt = point(2.0,8.1)
print(pt)

student = namedtuple('student',['name', 'id', 'cgpa'])
s1 = student(name='Manabendu',id=64,cgpa=9.7)
print(s1)
