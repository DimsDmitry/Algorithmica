from sklearn.linear_model import LinearRegression
from sklearn import linear_model
# импортируем класс - линейная регрессия

lr = LinearRegression()
# создаём объект (экземпляр, instance) её класса
print(lr)

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
LinearRegression()


'''
Линейная регрессия - это алгоритм машинного обучения, основанный на контролируемом обучении. Он выполняет задачу
регрессии для вычисления коэффициентов регрессии. Регрессия моделирует целевой прогноз на основе независимых переменных.

Линейная регрессия выполняет задачу прогнозирования значения зависимой переменной (y) на основе заданной независимой
переменной (x). Таким образом, этот метод регрессии обнаруживает линейную зависимость между x (входной) и y (выходной).
Поэтому он получил имя Линейная регрессия.

Рассмотрим работу моделей для обучения с учителем и без учителя.
При обучении с учителем модель обучается на размеченном наборе данных и предсказывает ответы, которые используются
для оценки точности алгоритма на обучающих данных.
При обучении без учителя модель использует неразмеченные данные, из которых алгоритм самостоятельно пытается извлечь
признаки и зависимости.'''