# Written in Python3 by Torjus Bye, 2019. https://github.com/Torbye

import math

def car2pol(coordinate_list): #Converts cartesian coordinate_listdinates to polar [X, Y] -> [Radius, Angle].
    x=coordinate_list[0]
    y=coordinate_list[1]
    return [math.sqrt(math.pow(x,2)+math.pow(y,2)), math.degrees(math.atan2(y,x))]

def pol2car(coordinate_list): #Converts polar coordinate_listdinates to cartesian [Radius, Angle] -> [X, Y].
    r=coordinate_list[0]
    a=math.radians(coordinate_list[1])
    return [r*math.cos(a), r*math.sin(a)]

def sph2car(coordinate_list):  #Converts spherical coordinate_listdinates to cartesian [Radius, Inclination, Azimuth] -> [X, Y, Z].
    i = pol2car([coordinate_list[0], coordinate_list[1]])
    z = i[1]
    i = pol2car([i[0], coordinate_list[2]])
    return [i[0], i[1], z]

def car2sph(coordinate_list):  #Converts cartesian to spherical coordinate_listdinates [X, Y, Z] -> [Radius, Inclination, Azimuth].
    x = coordinate_list[0]
    y = coordinate_list[1]
    z = coordinate_list[2]
    radius = math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))
    inclination = math.degrees(math.acos(z/radius))
    azimuth = math.degrees(math.atan(y/x))
    return [radius, inclination, azimuth]
