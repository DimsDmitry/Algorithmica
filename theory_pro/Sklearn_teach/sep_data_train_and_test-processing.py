from sklearn.datasets import *
import numpy as np


# датасеты испортируются через sklearn.datasets
x, y = load_diabetes(return_X_y=True)
# в x передаются данные, в y - метки, характеризующие каждую запись из набора данных

# первые 3 записи из x
print('X:')
print(x[:3])

# первые 3 записи из y
print('Y:')
print(y[:3])

print(100 * '*')


# Разделение данных на обучающую и тестовую выборку
'''Разделение данных на обучающую и тестовую выборку является важной частью проверки того, насколько хорошо
работает модель. Изначально она обучается на отдельных данных (обучающей выборке), а затем проверяем качество работы
модели на тестовой выборке. Таким образом, можно измерить способность модели обобщать новые данные:'''

from sklearn.model_selection import train_test_split

# train_test_split разбивает выборку случайным образом на 2 подвыборки: обучающую и тестовую
# запускаем разбиение с параметрами по умолчанию
x_train, x_test, y_train, y_test = train_test_split(x, y)


# Кроме того, мы можем явно задать некоторые специальные параметры
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

'''test_size, train_size - необязательные параметры, отвечающие за количество данных в %, которые пойдут в обучающую 
или тестовую выборки.
random_state - отвечает за перемешивание данных. Туда передают какое-либо целочисленное занчение, чтобы при каждом
запуске выборка мешалась одинаково. Это гарантирует воспроизводимость эксперимента.
Кроме этого у функции train_test_split есть ещё несколько параметров по умолчанию (см. документацию).'''


'''Перед тем, как скармливать данные на обучение, их необходимо некоторым образом приготовить.
"Рецепт готовки" зависит от особенности конкретной модели, однако чаще всего используют следующие методы
из пакета `sklearn.preprocessing`
'''


# Стандартизация
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(x_train)
standardized_X = scaler.transform(x_train)

print('До стандартизации:')
print(x_train[0])
print()
print('После стандартизации:')
print(standardized_X[0])

print('Среднее до стандартизации:')
print(x_train[0].mean())
print()
print('Среднее после стандартизации:')
print(standardized_X[0].mean())

# умножилось примерно в 20 раз
'''Стандартизация – техника преобразования значений признака (Feature), адаптирующая признаки с разными диапазонами
 значений. Подразумевает приравнивание среднего значения к нулю и/или приравнивание стандартного отклонения к единице.
 Данный вид шкалирования стремится привести данные к нормальному распределению. 

Другими словами. Стандартизированные данные содержат ту же информацию, но имеют среднее значение 0 и отклонение 1
(здесь среднее = -0.724...).
После масштабирования данных математическая природа алгоритмов позволяет лучше с ними работать
(например SVM и метод K-means).'''

# Нормализация (Normalization)
from sklearn.preprocessing import Normalizer

scaler = Normalizer().fit(x_test)
normalized_X = scaler.transform(x_test)

print('До нормализации:')
print(x_test[:3])
print()
print('После нормализации:')
print(normalized_X[:3])

data = [[178, 500000, 58], [130, 5000, 110], [190, 100000000, 90]] # запись о людях (рост, зарплата, вес)

scaler = Normalizer().fit(data)
normalized_data = scaler.transform(data)

print('До нормализации:')
print(data[:3])
print()
print('После нормализации:')
print(normalized_data[:3]) # теперь нет гигантской разницы в признаках, как 58 и 100000000

print(100 * '#')

# Приведение к бинарному виду (Binarization)
'''Бинаризуйте данные (установите значения функций равными 0 или 1) в соответствии с пороговым значением.

Например, если мы выберем пороговое значение = 0,5, то значение набора данных выше этого станет 1, а ниже - станет 0.
Поэтому мы можем назвать его бинаризацией данных или пороговым значением данных. Этот метод полезен, когда у нас есть
вероятности в нашем наборе данных и мы хотим преобразовать их в четкие значения.
'''

from sklearn.preprocessing import Binarizer

X = 10 * np.random.random((5, 5)) - 5
print('x', X)

binarizer = Binarizer(threshold=0.0).fit(X) # в данном случае порог 0.0
binary_X = binarizer.transform(X)

print('До бинаризации:')
print(X[:5])
print()
print('После бинаризации:')
print(binary_X[:5])

# Мы хотим определить прогульщиков (у кого больше N пропусков занятий)

absenteeism_number_student = np.array([[3, 1, 5, 0, 2, 5, 9, 888]])
# количество прогулов у студентов

binarizer = Binarizer(threshold=3.0).fit(absenteeism_number_student)
# порог прогулов threshold = 3

binary_absenteeism_number_student = binarizer.transform(absenteeism_number_student)
# трансформируем данный с помощью transform
print(10 * '@')

print(binary_absenteeism_number_student)

print('Вывод: 3-й, 6,7,8-й студенты - прогульщики')

print(100 * '=')

# Кодирование Категориальных Признаков (Encoding Categorical Features)


from sklearn.preprocessing import LabelEncoder


y = np.array(['rus', 'usa', 'uk', 'usa', 'rus'])
# наш признак - строковое сокращение страны

enc = LabelEncoder()
# создаём объект LabelEncoder-а
y = enc.fit_transform(y)

print(y)
# [0 2 1 2 0] - замена каждого признака какой-то меткой
# теперь для нашей модели все люди из России в качестве признака County будет иметь значение 0
