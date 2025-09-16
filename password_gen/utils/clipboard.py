import threading

import pyperclip


def copy_to_clipboard(text: str):
    """Скопировать текст в буфер обмена."""
    pyperclip.copy(text)


def clear_clipboard_after(seconds: int):
    """Очистить буфер обмена через указанное количество секунд."""

    def _clear():
        pyperclip.copy("")

    threading.Timer(seconds, _clear).start()
