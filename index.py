from turtle import *
import colorsys

speed(0)
hue=0.8
bgcolor('black')

for i in range (130):
    col = colorsys.hsv_to_rgb(hue,1,1)
    hue+= 0.004
    fillcolor(col)
    begin_fill()
    circle (150-i,90)
    lt(10)
    lt(20)
    lt(90)
    circle (150-i,90)
    rt(80)
    end_fill()
done()