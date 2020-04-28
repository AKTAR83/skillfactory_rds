import numpy as np
number = np.random.randint(1,101)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50   
    max_value = 100 # начальное значения диапазона
    min_value = 1 #начальное значения диапазона

    while number != predict:
        count += 1          
        if number > predict and max_value - predict != 1:
            min_value = predict
            predict = int(predict + (max_value - predict)/2) # сужаем диапазон     
        elif max_value - predict == 1: # проверяем что predict не "крайнее значение"
             predict += 1        
        elif number < predict:
            max_value = predict
            predict = int(predict - (max_value - min_value)/2)  # сужаем диапазон           
    return(count) # выход из цикла, если угадали

def score_game(game_core):  
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v2)