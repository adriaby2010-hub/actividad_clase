import math

for y in range(-15, 16):
    linea = ""
    for x in range(-45, 46):
        c = complex(x / 30.0, y / 15.0)
        z = 0
        for i in range(1, 30):
            z = z * z + c
            if abs(z) > 2: break
        linea += " .:-=+*#%@"[i % 10] if abs(z) > 2 else " "
    print(linea)