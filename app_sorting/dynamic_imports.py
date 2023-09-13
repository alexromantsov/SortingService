# app_sorting/dynamic_imports.py
import os
import importlib

# Список имен модулей или функций для исключения
excluded = ['LooseVersion']


def load_custom_modules(app_name='app_sorting'):
    custom_modules = {}
    module_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'custom_modules')

    # Загрузка всех Python-файлов из папки
    for filename in os.listdir(module_folder_path):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Удаление расширения ".py"
            module = importlib.import_module(f'.custom_modules.{module_name}', app_name)

            # Добавление всех функций из модуля в словарь
            for attr_name in dir(module):
                attr_value = getattr(module, attr_name)
                if callable(attr_value) and attr_name not in excluded:
                    custom_modules[f"{module_name}.{attr_name}"] = attr_value

    return custom_modules
