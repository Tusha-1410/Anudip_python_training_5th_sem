fill_rate = 10

if fill_rate > 0:
    water_level = 0

    while water_level < 100:
        water_level += fill_rate
        print("Water Level:", water_level, "liters")

    print("Tank is full.")
else:
    print("Invalid fill rate! Fill rate must be greater than 0.")