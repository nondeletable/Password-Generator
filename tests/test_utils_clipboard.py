import pyperclip

from password_gen.utils import clipboard


def test_copy_to_clipboard(monkeypatch):
    called = {}

    monkeypatch.setattr(
        pyperclip, "copy", lambda text: called.setdefault("value", text)
    )
    clipboard.copy_to_clipboard("hello")

    assert called["value"] == "hello"


def test_clear_clipboard_after(monkeypatch):
    called = {}

    monkeypatch.setattr(
        pyperclip, "copy", lambda text="": called.setdefault("cleared", text)
    )
    # заменим threading.Timer на прямой вызов
    monkeypatch.setattr(
        "password_gen.utils.clipboard.threading.Timer",
        lambda s, f: type("T", (), {"start": f}),
    )

    clipboard.clear_clipboard_after(1)

    assert called["cleared"] == ""
