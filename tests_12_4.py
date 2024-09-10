import logging
import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            some_runner = runner.Runner('Макс', -1)
            if some_runner.speed > 0:
                logging.info(f'{some_runner} создан и test_walk для {some_runner} выполнен успешно')
            else:
                raise ValueError(f'Скорость может быть только положительным значением, текущее значение = {some_runner.speed}')
        except ValueError as ex:
            logging.warning(f'Неверная скорость для {some_runner}', exc_info=True)

    def test_run(self):
        try:
            some_runner = runner.Runner(1337)
            if isinstance(some_runner.name, str):
                logging.info(f'test_run для {some_runner.name} выполнен успешно')
            else:
                raise TypeError(f'Имя может быть только строковым значением, передано  = {type(some_runner.name).__name__}')
        except TypeError as ex:
            logging.warning('Неверный тип данных для имени объекта Runner', exc_info=True)

    def test_challenge(self):
        first_runner = runner.Runner('Вова ')
        second_runner = runner.Runner('Гриша')
        for i in range(1, 4):
            first_runner.run()
        for i in range(1, 4):
            second_runner.walk()
        self.assertNotEqual(first_runner.distance, second_runner.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',encoding='utf8',
                    format='%(asctime)s | %(levelname)s | %(message)s')