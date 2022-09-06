def riders(stations):
    miles = 0
    rider = 1
    for distance in stations:
        miles += distance
        if miles >= 100:
            rider += 1
            miles = distance
    return rider

if __name__ == '__main__':
    print(riders([38, 10, 41, 39, 48, 18, 6, 8, 35, 47, 50, 46, 39, 12, 37]))


# print(16 // 3)