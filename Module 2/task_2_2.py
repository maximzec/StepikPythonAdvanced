weight = float(input())
height = float(input())

BMI = weight / height ** 2

if BMI < 18.5:
    print('Недостаточная масса')
elif BMI > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')