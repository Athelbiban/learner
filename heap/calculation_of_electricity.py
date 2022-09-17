meter_readings = {52: (23493, 23447, 1),
                  53: (72689, 72675, 0),
                  54: (29064, 28874, 3),
                  56: (32715, 32528, 1),
                  57: (46440, 46186, 3),
                  58: (31986, 31794, 3),
                  59: (25340, 25157, 2),
                  61: (37845, 37693, 2),
                  'g': (48742, 47562, 15)
                  }
kilowatt_per_month = {}
for key, val in meter_readings.items():
    kilowatt_per_month[key] = kilowatt_per_month.get(key, val[0] - val[1])

general_energy_consumption = 0
for key, val in kilowatt_per_month.items():
    if key != 'g':
        general_energy_consumption -= val
    else:
        general_energy_consumption += val


