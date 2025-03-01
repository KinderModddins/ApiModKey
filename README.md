
![Лого](https://i.ibb.co/zhP8MptB/IMG-20250301-153001-834.jpg)

### 📚 **Документация для библиотеки `apimodkey`**

Библиотека `apimodkey` предоставляет удобные методы для взаимодействия с API Modkey.space. С её помощью вы можете создавать ключи, изменять их статус и управлять ими, передавая API-ключ прямо в коде вашего проекта.

---

#### ⚙️ **Метод: `create_key`**

Этот метод позволяет создать новый ключ с заданными параметрами.

**Описание**:
- Метод создает ключ с указанным сроком действия, количеством устройств и типом ключа.
- Возвращает строку с результатом или ошибкой.

**Параметры**:
- `api_key` (str): Ваш API-ключ.
- `days` (int): Количество дней действия ключа.
- `devices` (int): Количество устройств, на которые можно активировать ключ.
- `key_type` (str): Тип ключа (например, 'APK').

**Возвращаемое значение**:
- Строка с результатом создания ключа или ошибкой.

---

**Пример использования**:

```python
from apimodkey import create_key

# Указываем API-ключ
api_key = "YOUR_API_KEY"

# Создаем ключ на 30 дней для 3 устройств с типом 'APK'
result = create_key(api_key, 30, 3, 'APK')

# Выводим результат
print(result)
```

**Пример вывода**:
```
Ключ успешно создан!
Ваш ключ: abc123xyz
```

---

#### 🔧 **Метод: `edit_key_status`(Временно не работает)**

Этот метод позволяет изменить статус уже существующего ключа.

**Описание**:
- Метод изменяет статус ключа на новый.
- Выводит старый и новый статус ключа, если операция прошла успешно.

**Параметры**:
- `api_key` (str): Ваш API-ключ.
- `key` (str): Ключ, для которого нужно изменить статус.
- `new_status` (str): Новый статус ключа (например, 'inactive').

**Возвращаемое значение**:
- None, но выводит в консоль старый и новый статус ключа.

---

**Пример использования**:

```python
from apimodkey import edit_key_status

# Указываем API-ключ
api_key = "YOUR_API_KEY"

# Изменяем статус ключа на 'inactive'
edit_key_status(api_key, 'your_key', 'inactive')
```

**Пример вывода**:
```
Статус ключа успешно изменен!
Старый статус: active
Новый статус: inactive
```

---

#### 💡 **Как использовать?**

Чтобы использовать методы из этой библиотеки, вам нужно:
1. Установить библиотеку через `pip`.
2. В вашем коде передать API-ключ в качестве аргумента для каждого метода.

---

### 🚀 **Установка библиотеки**

Для установки библиотеки используйте команду:

```bash
pip install apimodkey
```

---

#### 📝 **Пример с полной документацией**:

```python
from apimodkey import create_key, edit_key_status

# Указываем свой API-ключ
api_key = "YOUR_API_KEY"

# Пример создания ключа
result = create_key(api_key, 30, 3, 'APK')
print(result)  # Печатает результат создания ключа

# Пример изменения статуса ключа
edit_key_status(api_key, 'your_key', 'inactive')
```

---

#### 🎉 **Твой первый ключ уже создан!**

Используя эти простые методы, вы можете легко создавать и управлять ключами в Modkey.space. Наслаждайтесь работой с API! 🎉

---

### 📜 **Рекомендации по безопасности**:
- **Не раскрывайте свой API-ключ**! Он должен храниться в надежном месте и передаваться в коде в безопасных условиях.
- Используйте переменные окружения или конфигурационные файлы для дополнительной безопасности при передаче ключа.

#### Work
>Владельцем проекта(modkey.space) является  [CATPoN](https://t.me/EXPERT_CATPON)
>Разработчик проекта modkey.space  [Wardex](https://t.me/)
>**Над библиотекой и документанцией работал  [@MAKCNMOB](https://t.me/MAKCNMOB)**