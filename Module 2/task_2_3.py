string = input()

rubles = len(string) * 60 // 100
pennies = len(string) * 60 - rubles * 100

print(f'{rubles} р. {pennies} коп.')