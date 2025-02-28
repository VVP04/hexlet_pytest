from pathlib import Path
from hexlet_pytest.reverse import reverse

# Функция для получения пути к тестовым данным
def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

# Функция для чтения файла
def read_file(filename):
    return get_test_data_path(filename).read_text()

# Тест для функции reverse
def test_reverse():
    # Чтение входных данных
    input_text = read_file('input.txt')
    
    # Чтение ожидаемого результата
    expected_output = read_file('expected_output.txt')
    
    # Вызов функции и получение результата
    actual_output = reverse(input_text)
    
    # Проверка результата
    assert actual_output == expected_output