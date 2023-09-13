import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .validators import validate_json
from .dynamic_imports import load_custom_modules

custom_modules = load_custom_modules()


@csrf_exempt
def json_sorting(request):
    if request.method == 'POST':
        try:
            data_json = json.loads(request.body.decode('utf-8'))

            # Если в body был json, то проводим валидацию его
            is_valid, error_message = validate_json(data_json)

            if not is_valid:
                return JsonResponse({'error': error_message}, status=400)

            module_name = data_json.get('module')
            function_name = data_json.get('function')
            data = data_json.get('data')

            # Проверка наличия модуля и функции в custom_modules
            full_function_name = f"{module_name}.{function_name}"
            module_exists = any(key.startswith(f"{module_name}.") for key in custom_modules.keys())
            function_exists = full_function_name in custom_modules

            if not module_exists:
                return JsonResponse({'error': f"Модуль '{module_name}' не найден"}, status=500)

            if not function_exists:
                return JsonResponse({'error': f"Функция '{function_name}' не найдена"}, status=500)

            function_to_call = custom_modules[full_function_name]
            response_data = function_to_call(data)

            return JsonResponse({'data': response_data})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Некорректный JSON'}, status=400)
    else:
        return HttpResponse("Метод не разрешен", status=405)
