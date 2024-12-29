import json
import os

users_db = {}

user_dict_template = {
    'user_name': '',
    'is_admin': False
}


def load_json_data(filepath: str = 'db.json') -> dict | list | None:
    """
    Открывает JSON-файл и возвращает данные из него.
    Args:
        filepath: Путь к JSON-файлу.
    Returns:
        Словарь, список или None, если файл не найден или не является корректным JSON.
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_filepath = os.path.join(current_dir, filepath)
        with open(full_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{filepath}' не является корректным JSON.")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None


def save_json_data(data: dict | list, filepath: str = 'db.json') -> bool:
    """
    Сохраняет данные в JSON-файл.
    Args:
        filepath: Относительный путь к JSON-файлу.
        data: Данные для сохранения (словарь или список).
    Returns:
        True, если сохранение прошло успешно, False в противном случае.
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_filepath = os.path.join(current_dir, filepath)

        with open(full_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла '{filepath}': {e}")
        return False


def get_admin_ids() -> tuple[int]:
    db = load_json_data()
    result = (int(user_id) for user_id in db.keys() if db[user_id]['is_admin'])
    return tuple(result)
