# CoordinateTranslator
Written by Torjus Bye, 2019. https://github.com/Torbye
Python 3, dependencies: math

Converts list of coordinates from one type to another.

--------------------------------------------------------------------------
# Functions:

	car2pol(coordinate_list): # Converts cartesian coordinates to polar [X, Y] -> [Radius, Angle].

	pol2car(coordinate_list): # Converts polar coordinates to cartesian [Radius, Angle] -> [X, Y].

	sph2car(coordinate_list):  # Converts spherical coordinates to cartesian [Radius, Inclination, Azimuth] -> [X, Y, Z].

	car2sph(coordinate_list):  # Converts cartesian to spherical coordinates [X, Y, Z] -> [Radius, Inclination, Azimuth].

--------------------------------------------------------------------------
# Usage:

	import coordinate_translator as coor

	x = 10
	y = 5
	z = 1

	print( coor.car2pol([x,y]) ) # Results in polar coordinates.
	print( coor.car2sph([x,y,z]) ) # Results in spherical coordinates.
