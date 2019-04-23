# Team the space Guys
# 3em2 students of the Gymnase Jean Sturm Strasbourg
# life in space
# Our programm takes humidity, temperature, lat and longitude
# we want to see if we can see a difference between the night and the day interface in the iss"


import ephem
import time
import datetime as dt
from sense_hat import SenseHat
import csv
from math import degrees
from ephem import readtle

sense = SenseHat()
sense.clear()

#--------------calculating the gps position --------------------------------------------------------#

time_format = "%d/%m/%Y %H:%M:%S"

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   19035.70914902  .00002470  00000-0  45950-4 0  9990"
line2 = "2 25544  51.6436 300.0564 0005072 352.8246  93.8019 15.53235656154673"

iss = ephem.readtle(name, line1, line2)

#---------------------------Introduction message------------------------------------------------------

# Color definition

x=[0,0,0]       #eteint
s=[0,255,225]   #bleu clair
t=[0,116,189]   #bleu foncé
j=[255,255,0]   #Jaune
c=[255,255,200] #Jaune claire
r=[255,0,0]     #red

# introduction message

sense.set_rotation(270)
sense.show_message("Hi expedition 58 crew ! we are the Space guys", text_colour=t, scroll_speed=0.08)

crew = [r, r, r, x, x, r, r, x,
        r, x, x, x, r, x, x, r,
        r, x, x, x, r, x, x, r,
        r, r, x, x, x, r, r, x,
        x, x, r, x, x, r, r, x,
        x, x, r, x, r, x, x, r,
        x, x, r, x, r, x, x, r,
        r, r, x, x, x, r, r, x,]

sense.set_pixels(crew)
time.sleep(3)

sense.set_rotation(270)
sense.show_message("This program will mesure the temperature and humidity", text_colour=t, scroll_speed=0.08)

water=[x, x, x, x, s, x, x, x,
       x, x, x, s, s, x, x, x,
       x, x, s, s, s, s, x, x,
       x, s, s, s, s, s, s, x,
       x, s, s, s, s, s, s, x,
       x, s, s, s, s, s, s, x,
       x, x, s, s, s, s, x, x,
       x, x, x, s, s, x, x, x]

water2=[x, x, x, x, c, x, x, x,
       x, x, x, c, c, x, x, x,
       x, x, c, c, c, c, x, x,
       x, c, c, c, c, c, c, x,
       x, c, c, c, c, c, c, x,
       x, c, c, c, c, c, c, x,
       x, x, c, c, c, c, x, x,
       x, x, x, c, c, x, x, x]
sense.set_pixels(water)

# ----------------------configuration of csv file-----------------------------------------------------

print("start recording data",time.strftime('%x, %X'))

fichier = open("/home/pi/Desktop/datas Space guys 3eme2 Jean STURM.csv", "a")
fichier.write("\nDebut mesures ")
fichier.write(",")
fichier.write(str(time.strftime('%x, %X')))
fichier.write("\n\n")
fichier.write("Date")
fichier.write(",")
fichier.write("Heure")
fichier.write(",")
fichier.write("Lat")
fichier.write(",")
fichier.write("Long")
fichier.write(",")
fichier.write("Temperature")
fichier.write(",")
fichier.write("humidity")
fichier.write(",")
fichier.close()


#--------------------Calculating the distance and mesure humidity and temperature --------------------------------------

for n in range(9500):

    hum = sense.get_humidity()
    hum = round(sense.get_humidity(),2)
    temp = sense.get_temperature()
    temp = round(sense.get_temperature(),2)
    iss.compute()
    iss_lat = degrees(iss.sublat)
    iss_long = degrees(iss.sublong)

    print("Lat: %s - Long: %s - Humidity: %s - Temperature: %s" % (iss_lat, iss_long, hum, temp))

#--------------------------writing data into the csv file-------------------------------------------

    fichier = open("/home/pi/Desktop/datas Space guys 3eme2 Jean STURM.csv", "a")

    fichier.write("\n")
    fichier.write(time.strftime('%x'))
    fichier.write(',')
    fichier.write(time.strftime('%X'))
    fichier.write(',')
    fichier.write(str(iss_lat))
    fichier.write(",")
    fichier.write(str(iss_long))
    fichier.write(",")
    fichier.write(str(temp))
    fichier.write(",")
    fichier.write(str(hum))
    fichier.write(",")
    fichier.close()
    time.sleep(0.5)
    sense.set_pixels(water)
    time.sleep(0.5)
    sense.set_pixels(water2)
