#!/usr/bin/python3
import turtle
import urllib.request
import json

eoss  = 'http://api.open-notify.org/iss-now.json'

trackiss = urllib.request.urlopen(eoss)

ztrack = trackiss.read()

result = json.loads(ztrack.decode('utf-8'))


print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')


location = result['iss_position']
lat = location['latitude']
lon = location['longtitude']

print('\nLatitude: ', lat)
print('\nLatitude: ', lon)
 
screen = turtle.Screen()
screen.setup(720,360)

screen.setworkdcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lan = round(float(lan))


iss.penup()
iss.goto(lon,lat)
turtle.mainloop()
