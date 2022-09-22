import turtle as tur
def clock(rad,init):
    tur.penup()
    tur.goto(init[0],init[1]-rad*5/2)
    tur.pendown() 
    tur.pencolor('black')
    tur.begin_fill()
    tur.circle(rad*5/2)
    tur.end_fill()
    tur.penup()
    tur.goto(init[0],init[1]-rad*3/2)
    tur.pencolor('white')
    tur.circle(rad*3/2,180)
    for i in range(1,13):
        tur.penup()
        tur.circle(rad*3/2,-30)
        tur.pendown()
        tur.pencolor('white')
        tur.write(i)
    tur.penup()
    tur.circle(rad*3/2,180)
    tur.pendown()
    tur.penup()
    tur.goto(init[0],init[1])
    tur.pendown()

    
def time_angle(settime):
    hr=settime[0]/12*360 + settime[1]/12*360/60 + settime[2]/12*360/60/60 + 270
    mins=settime[1]/60*360 + settime[2]*360/60/60 + 270
    sec=settime[2]/60*360 +270
    return [hr,mins,sec]

def scene(angles,rad):
    col=('red','blue','green')
    for i,c in enumerate(col):
        tur.pencolor(c)
        tur.rt(angles[i])
        tur.fd(rad)
        tur.back(rad)
        tur.lt(angles[i])

def clearscene(angles,rad):
     tur.pencolor('black')
     for i in angles:
          tur.rt(i)
          tur.fd(rad)
          tur.back(rad)
          tur.lt(i)
     tur.pencolor('white')
