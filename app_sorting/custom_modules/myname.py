from distutils.version import LooseVersion

from distutils.version import LooseVersion


def mytest(data):
    """Сортирует и преобразует входные данные на основе поля 'ident'.

    Данная функция сортирует входной словарь на основе поля 'ident', используя
    LooseVersion для сравнения строк, представляющих версии. Также она токенизирует
    поле 'value', преобразуя его в массив слов после удаления пробелов.
    """

    # Сортируем входной словарь
    sorted_items = sorted(data.items(), key=lambda item: LooseVersion(item[1]['ident']))

    sorted_data = {}
    for k, v in sorted_items:
        sorted_data[k] = v

    # Токенизируем поле 'value'
    for key, value in sorted_data.items():
        tokenized_value = value['value'].strip().split()
        value['value'] = tokenized_value

    return sorted_data


def hello(data):
    """
    Просто здороваемся
    """
    return "Hello"
