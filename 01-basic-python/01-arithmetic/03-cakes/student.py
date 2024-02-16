def cakes(eggs, butter, flour):
    eggz = eggs // 5
    butterz = butter // 250
    flourz = flour // 250
    return min(eggz, butterz, flourz)