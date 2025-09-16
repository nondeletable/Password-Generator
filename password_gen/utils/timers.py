import threading

import flet as ft


def run_delayed(seconds: int, func):
    """Запустить функцию через указанное количество секунд в отдельном потоке."""
    threading.Timer(seconds, func).start()


def auto_hide_password(page: ft.Page, password_input):
    """Скрыть пароль и вернуть иконку 'закрытый глаз'."""
    password_input.password = True
    if hasattr(password_input, "suffix"):
        password_input.suffix.icon = ft.Icons.VISIBILITY_OFF
    try:
        page.update()
    except RuntimeError:
        # Если приложение уже закрыто
        pass
