with open('files/population.txt', encoding='utf-8') as inf:
    for line in inf:
        country, population = line.split('\t')
        if country.startswith('G') and int(population) > 5e5:
            print(country)
