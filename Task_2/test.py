from unittest import TestCase
import main

class TestYandex(TestCase):
    def test_yandex(self):
        TOKEN = 'y0_AgAAAABoU-VWAADLWwAAAADbLtr00tGudcjtSkO1fNVLDUZsWNoW9DA'
        result = main.Yandex(TOKEN).create_folder(folder_name='test')
        try:
            self.assertEqual(201, result)
            print('Folder was created succesfully')
        except AssertionError:
            match result:
                case 409:
                    print("Folder already exists")
                case _:
                    print('Unknown error')




