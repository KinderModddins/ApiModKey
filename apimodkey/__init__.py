import requests

def api_request(api_key, method, **kwargs):
    """
    Выполняет запрос к API Modkey.space для различных действий.
    
    :param api_key: Ваш API-ключ.
    :param method: Метод, который нужно вызвать (например, 'create-key').
    :param kwargs: Дополнительные параметры для API-запроса.
    :return: Кортеж (status, message), где status - успешность запроса, а message - данные ответа.
    """
    url = 'https://modkey.space/api/v1/action'
    data = {
        'method': method,
        'api_key': api_key,
    }
    data.update(kwargs)

    try:
        response = requests.post(url, data=data)
        if response.ok:
            result = response.json()
            print(result)  # Выводим полный ответ для отладки
            if result.get('status'):  # Используем get(), чтобы избежать KeyError
                return True, result['data']  # Возвращаем саму data, а не msg
            else:
                return False, result.get('message', 'Error without message')  # Учитываем сообщение
        else:
            print(response.text)
            return False, 'Server error'
    except requests.RequestException as e:
        print(e)
        return False, f'Request failed: {str(e)}'

def create_key(api_key, days, devices, key_type):
    """
    Создает новый ключ с заданными параметрами.

    :param api_key: Ваш API-ключ.
    :param days: Количество дней действия ключа.
    :param devices: Количество устройств для активации ключа.
    :param key_type: Тип ключа (например, 'APK').
    :return: Строка с результатом создания ключа или ошибкой.
    """
    status, msg = api_request(
        api_key=api_key,
        method='create-key',
        days=days,
        devices=devices,
        type=key_type
    )
    if status:
 #       print('Ключ успешно создан!')
        print(f'{msg["key"]}')
 #       return f"Ключ успешно создан!\nВаш ключ: {msg['key']}"  # Возвращаем строку с результатом
    else:
        print(f'Ошибка: {msg}')
 #       return f"Ошибка при создании ключа: {msg}"  # Возвращаем строку с ошибкой

def edit_key_status(api_key, key, new_status):
    """
    Изменяет статус существующего ключа.

    :param api_key: Ваш API-ключ.
    :param key: Ключ, для которого нужно изменить статус.
    :param new_status: Новый статус для ключа.
    :return: None
    """
    status, msg = api_request(
        api_key=api_key,
        method='edit-key-status',
        key=key,
        type=new_status
    )
    
    if status:
#        print('Статус ключа успешно изменен!')
        print(f'Старый статус: {msg["old_status"]}')  # Просто выводим строку
        print(f'Новый статус: {msg["new_status"]}')
    else:
        print(f'Ошибка: {msg}')

def edit_user_key(api_key, key, new_key):
    """
    Изменяет пользовательский ключ.

    :param api_key: Ваш API-ключ.
    :param key: Ключ, который нужно изменить.
    :param new_key: Новый ключ.
    :return: None
    """
    response = api_request(
        api_key=api_key,
        method='edit-user-key',
        key=key,
        new_user_key=new_key
    )

    print("Ответ от API:", response)  # Печатаем результат

    # Проверяем, что response[0] - это статус
    if response[0] and isinstance(response[1], dict) and response[1].get('status'):
        print(f'Ключ {key} успешно изменен на {new_key}.')
    else:
        print(f'Ошибка: {response[1].get("message", "Неизвестная ошибка")}')
