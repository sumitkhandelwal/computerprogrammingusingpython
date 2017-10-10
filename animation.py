import turtle as t
t.shape("turtle")
color1 = ['Orange','Blue','Green','Red','Yellow','Blue','Black']
for i in range(40):
    t.speed(20)
    #t.bgcolor(color1[i%4])
    t.color(color1[i%7])
    t.width(5)
    t.fd(200)
    
    t.left(170)

