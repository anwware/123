numbers = []
for i in range(5):
    number = float(input(f"Введите {i+1}-е число: "))
    numbers.append(number)
average = sum(numbers) / len(numbers)
print(f"Среднее значение введенных чисел: {average}")