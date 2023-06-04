import pytest
from functions import task_1, task_2, task_3

class TestFunctions:

    @pytest.mark.parametrize(
        "geo_logs, expected",
        [
            (
                [
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
                ],
                6,
            )
        ],
    )
    def test_1(self, geo_logs, expected):
        result = task_1(geo_logs)
        assert result == expected

    @pytest.mark.parametrize(
        "ids, expected",
        [
            (
                {
                    'user1': [213, 213, 213, 15, 213],
                    'user2': [54, 54, 119, 119, 119],
                    'user3': [213, 98, 98, 35]
                },
                6,
            )
        ],
    )
    def test_2(self, ids, expected):
        result = task_2(ids)
        assert result == expected

    @pytest.mark.parametrize(
        "stats, expected",
        [
            (
                {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
                {'yandex': 120},
            )
        ],
    )
    def test_3(self, stats, expected):
        result = task_3(stats)
        assert result == expected
