import requests

def api_request(api_key, method, **kwargs):

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
    status, msg = api_request(
        api_key=api_key,
        method='create-key',
        days=days,
        devices=devices,
        type=key_type
    )
    if status:
        print(f'{msg["key"]}')

    else:
        print(f'Ошибка: {msg}')

def edit_key_status(api_key, key, new_status):

    status, msg = api_request(
        api_key=api_key,
        method='edit-key-status',
        key=key,
        type=new_status
    )
    
    if status:
        print(f'Старый статус: {msg["old_status"]}')  # Просто выводим строку
        print(f'Новый статус: {msg["new_status"]}')
    else:
        print(f'Ошибка: {msg}')

def edit_user_key(api_key, key, new_key):

    response = api_request(
        api_key=api_key,
        method='edit-user-key',
        key=key,
        new_user_key=new_key
    )

    print(response)  # Ответ от апи


    if response[0] and isinstance(response[1], dict) and response[1].get('status'):
        print(f'Ключ {key} успешно изменен на {new_key}.')
    else:
        print(f'Ошибка: {response[1].get("message", "Неизвестная ошибка")}')
