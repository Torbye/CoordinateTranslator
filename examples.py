import coordinate_translator as coor


# Find hypotenuse and angle in 2 dimensions
adjacent = 10 # "x"
opposite = 10 # "y"

translated = coor.car2pol([adjacent,opposite])
r = translated[0] # Radius
a = translated[1] # Angle

print("Find hypotenuse and angle in 2 dimensions:")
print("Hypotenuse =", str(r))
print("Angle =", str(a))



# Find radius, inclination and azimuth in 3 dimensions
x = 10
y = 10
z = 10

translated = coor.car2sph([x,y,z])
r = translated[0] # Radius
i = translated[0] # Inclination
a = translated[0] # Azimuth

print("\nFind hypotenuse, inclination and azimuth in 3 dimensions:")
print("Hypotenuse =", str(r))
print("Inclination =", str(i))
print("Azimuth =", str(a))
