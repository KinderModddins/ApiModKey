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
     #   print(f'Ключ создан: {msg["key"]}')
        return msg["key"]  # Возвращаем ключ для дальнейшего использования
    else:
        return {msg}


def edit_key_status(api_key, key, new_status):
    status, msg = api_request(
        api_key=api_key,
        method='edit-key-status',
        key=key,
        type=new_status
    )
    
    if status:
        return {msg["old_status"]} # Просто выводим строку
        return {msg["new_status"]}
    else:
        return {msg}


def edit_key_max_devices(api_key, key, new_max_devices):
    status, msg = api_request(
        api_key=api_key,
        method='edit-key-max-devices',
        key=key,
        new_max_devices=new_max_devices
    )
    
    if status:
        return {msg["old_max_devices"]}
        return {msg["new_max_devices"]}
    else:
        return {msg}


def edit_user_key(api_key, key, new_user_key):
    status, msg = api_request(
        api_key=api_key,
        method='edit-user-key',
        key=key,
        new_user_key=new_user_key
    )

    if status:
        return new_user_key
    else:
        return {msg}
