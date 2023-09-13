# app_frontend/views.py
import inspect

from django.shortcuts import render
from app_sorting.dynamic_imports import load_custom_modules


def index(request):
    template = 'index.html'
    context = {
    }
    return render(request, template, context)


def functions(request):
    custom_modules = load_custom_modules()
    custom_modules_info = []
    for full_function_name, func in custom_modules.items():
        module_name, function_name = full_function_name.split('.')
        description = func.__doc__

        # Обрезаем до первой точки или до первой новой строки
        if description:
            stop_idx = min(description.find('. '), description.find('\n'))
            if stop_idx != -1:
                description = description[:stop_idx]

        custom_modules_info.append({
            'module_name': module_name,
            'function_name': function_name,
            'description': description,
            'code': inspect.getsource(func) if inspect.isfunction(func) else 'N/A'
        })
    context = {
        'custom_modules': custom_modules_info,
    }
    return render(request, 'functions.html', context)
