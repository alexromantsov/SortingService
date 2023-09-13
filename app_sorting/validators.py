def validate_json(data_json):
    required_fields = ['module', 'function', 'data']

    for field in required_fields:
        if field not in data_json:
            return False, f'Отсутствует необходимое поле: {field}'

    return True, 'Ок'
