import flet as ft

from password_gen.ui import dialogs


class FakePage:
    def __init__(self):
        self.updated = False
        self.overlay = []

    def update(self):
        self.updated = True


def test_close_dialog_sets_open_false():
    page = FakePage()
    dialog = ft.AlertDialog()
    dialog.open = True

    dialogs.close_dialog(page, dialog)

    assert dialog.open is False
    assert page.updated


def test_open_nfo_window_adds_dialog(monkeypatch):
    page = FakePage()

    # замокаем webbrowser.open, чтобы не открывал реальный браузер
    called = {}
    monkeypatch.setattr("webbrowser.open", lambda url: called.setdefault("url", url))

    dialogs.open_nfo_window(page)

    # в overlay должен появиться AlertDialog
    assert any(isinstance(ctrl, ft.AlertDialog) for ctrl in page.overlay)
    dlg = page.overlay[-1]
    assert dlg.open is True
    assert page.updated

    # проверим, что есть кнопка с on_click, которая вызывает webbrowser.open
    icon_buttons = [
        c
        for row in dlg.content.controls
        if isinstance(row, ft.Row)
        for c in row.controls
        if isinstance(c, ft.IconButton)
    ]
    assert icon_buttons, "Ожидались IconButton в диалоге"

    # вручную вызываем клик по первой кнопке
    icon_buttons[0].on_click(None)
    assert "url" in called
