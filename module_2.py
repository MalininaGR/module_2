number = int(input('Введите число от 3 до 20:'))
if number > 3:
    print('Введенное число',number,'не подходит условиям')
elif number < 20:
    print('Введенное число',number,'не подходит условиям')
else:
    result= ''
    list = range(1,21)
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            pair_sum = list[i] + list[j]
            if number % pair_sum == 0:
                result = result + str(list[i]) + str(list[j])
    print(result)
