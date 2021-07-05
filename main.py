import numpy as np

number = np.random.randint(1, 101)  # загадали число


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, (1000))

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v2(number):
    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 5
        elif number < predict:
            predict -= 2
    return (count)  # выход из цикла, если угадали


score_game(game_core_v2)