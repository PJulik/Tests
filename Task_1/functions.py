#1
def task_1(data):
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    data = [visit for visit in geo_logs if 'Россия' in list(visit.values())[0]]
    return len(data)

#2
def task_2(data):

    ids = {
      'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]
    }
    new_ids = []
    data = [new_ids.extend(value) for value in ids.values()]
    return len(set(new_ids))

#3
def task_3(data):
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    data = {key:value for (key, value) in stats.items() if value == max(stats.values())}
    return data
