import numpy as np

def random_predict(number:int=99) -> int:
    """Игра угадай число.
Компьютер сам загадывает и угадывает число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # счётчик попыток
    a = 1 # нижняя граница диапазона 
    b = 101 # верхняя граница диапазона включительно 

    while True:
        count += 1
        predict_number = np.random.randint(a, b) # предполагаемое число        
        if number == predict_number:
            break # выход из цикла, если угадали
        elif predict_number > number:
            b = predict_number + 1 # если предполагаемое число больше загаданного, сдвигаем верхнюю границу
        elif predict_number < number:
            a = predict_number # если предполагаемое число меньше загаданного, сдвигаем нижнюю границу
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)