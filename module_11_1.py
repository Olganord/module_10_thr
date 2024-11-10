import requests
import numpy as np
import matplotlib.pyplot as plt

print('\nПримеры использования matplotlib (из документации):\n'
      'методы ax.plot для рисования линии на координатной плоскости\n'
      'а также ax.scatter и np.random.seed()\nдля построения графика рассеяния случайных пар точек.\n')


fig, ax = plt.subplots()             # Создайте фигуру, содержащую одну ось.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Нарисуйте некоторые данные на оси.

np.random.seed()  # запустите генератор случайных чисел.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

figure, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
x = np.linspace(0, 2, 100)  # Выборочные данные.

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Нанесите некоторые данные на оси.
ax.plot(x, x**2, label='quadratic')  # Нанесите дополнительные данные на оси...
ax.plot(x, x**3, label='cubic')  # ... и еще кое-что.
ax.set_xlabel('x label')  # Добавьте x-метку к осям
ax.set_ylabel('y label')  # Добавьте y-образную метку к осям.
ax.set_title("Simple Plot")  # Добавьте заголовок к осям.
ax.legend()  # Добавьте легенду.
plt.show()                           # Покажите фигуру.


print('Пример кода с использованием numpy: создание массивов,\nвыполнение различных математических операций.\n')

# Создаем массив чисел от 1 до 10
arr = np.arange(1, 11)
print('Массив чисел:', arr)

# Среднее значение массива
mean_value = np.mean(arr)
print('Среднее значение:', mean_value)

# Сумма всех элементов
total_sum = np.sum(arr)
print('Сумма всех элементов:', total_sum)

# Создание двумерных массивов, некоторые действия
a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])

print(f'\nПроизведение элементов массивов:', a*b)
print(f'Матричное произведение массивов:', a.dot(b))
print(f'Разность двух массивов', a-b)

print(f'\nПример кода, который использует библиотеку requests\n'
      f'для выполнения GET-запроса к API и получения данных в формате JSON:')

# URL для выполнения запроса
url = 'https://jsonplaceholder.typicode.com/todos/1'

# Выполнение GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг JSON-данных
    data = response.json()
    print('Полученные данные:', data)
else:
    print('Ошибка:', response.status_code)

print('\nВыполнение POST-запроса.')  # HTTP-метод POST предназначен для отправки данных на сервер.
# URL, на который мы будем отправлять запрос
url = "https://example.com/api/endpoint"

# Данные, которые мы хотим отправить
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Выполнение POST-запроса.
response = requests.post(url, json=data)

# Проверка статуса ответа
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print("Ответ сервера:", response.json())
else:
    print(f'Произошла ошибка: {response.status_code}')

print('\nВыполнение PUT-запроса.')  # Если целевой ресурс содержит
# отправляемую сущность и сущность была успешно обновлена, в соответствии с прилагаемыми в теле запроса данными,
# то сервер должен отправить 200 для информирования об успешном завершении запроса.
url = "https://example.com/api/endpoint"
response = requests.put('https://httpbin.org/put', data={'key' 'value'})
if response.status_code == 200:
    print("Запрос выполнен успешно!")
else:
    print(f'Произошла ошибка: {response.status_code}')
