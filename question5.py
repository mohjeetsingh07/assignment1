import math

for angle in range(0, 346, 15):
    # Convert the angle to radians
    radians = math.radians(angle)

   
    sine = round(math.sin(radians), 4)
    cosine = round(math.cos(radians), 4)
# here radians ,sine,cosine,angle are comment
# rresults are rounded of to 4 digits

    
    print("Angle:", angle, "degrees")
    print("Sine:", sine)
    print("Cosine:", cosine)
    print()
