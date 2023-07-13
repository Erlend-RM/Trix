import math
radius = float(input("Skriv inn radiusen til en sirkel: "))

diameter = 2*radius
areal = math.pi * radius**2
omkrets = math.pi * diameter

print(f"Diameter: {diameter:.2f}")
print(f"Areal:   {areal:.2f}")
print(f"Omkrets:  {omkrets:.2f}")
