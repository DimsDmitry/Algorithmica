def f3():
    '''область всех закрывающих функций '''
    def f4():
        '''локальная'''
        global number
        number = 10
        print(number)
    global number
    number = 30
    f4()
    print(number)
number = 100
f3()
print(number)


'''
1) Локальная - local scope. Самая внутренняя область (в текущей функции)
2) Encloding - область всех закрывающих функций 
3) Global - глобальная область
'''