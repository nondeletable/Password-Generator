import flet as ft

from password_gen.ui import handlers


class FakePage:
    def __init__(self):
        self.updated = False
        self.overlay = []

    def update(self):
        self.updated = True


class FakePasswordInput:
    def __init__(self, value=""):
        self.value = value
        self.password = True
        self.suffix = type("Suffix", (), {"icon": ft.Icons.VISIBILITY_OFF})()


class FakeEvent:
    def __init__(self, control=None):
        self.control = (
            control or type("Control", (), {"icon": ft.Icons.VISIBILITY_OFF})()
        )


def test_on_generate_password_click_valueerror(monkeypatch):
    page = FakePage()
    length_selector = type("Obj", (), {"value": "not-a-number"})()
    letters_switch = type("Obj", (), {"value": True})()
    digits_switch = type("Obj", (), {"value": True})()
    symbols_switch = type("Obj", (), {"value": True})()
    password_input = type("Obj", (), {"value": ""})()
    strength_label = type("Obj", (), {"value": ""})()
    strength_color = type("Obj", (), {"visible": False})()
    strength_container = type("Obj", (), {"border": None})()

    # генератор кидает ValueError
    monkeypatch.setattr(
        "password_gen.ui.handlers.generate_password",
        lambda *a, **k: (_ for _ in ()).throw(ValueError("fail")),
    )

    handlers.on_generate_password_click(
        None,
        page,
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
        password_input,
        strength_label,
        strength_color,
        strength_container,
    )

    assert password_input.value == ""
    assert "fail" in strength_label.value
    assert page.updated


def test_on_toggle_visibility_click_changes_state():
    page = FakePage()
    password_input = FakePasswordInput("abc")
    e = FakeEvent()

    # изначально password=True
    assert password_input.password is True

    handlers.on_toggle_visibility_click(e, page, password_input, auto_hide_seconds=1)

    # после клика password=False
    assert password_input.password is False
    assert e.control.icon == ft.Icons.VISIBILITY
    assert page.updated


def test_on_copy_password_click_with_value(monkeypatch):
    page = FakePage()
    password_input = FakePasswordInput("secret")

    called = {}

    def fake_copy(text):
        called["text"] = text

    monkeypatch.setattr("pyperclip.copy", fake_copy)

    handlers.on_copy_password_click(None, page, password_input, clear_seconds=1)

    # буфер вызван с паролем
    assert called["text"] == "secret"
    # на страницу добавился snack_bar
    assert any(
        "Copied" in ctrl.content.value
        for ctrl in page.overlay
        if isinstance(ctrl, ft.SnackBar)
    )
    assert page.updated


def test_on_copy_password_click_without_value(monkeypatch):
    page = FakePage()
    password_input = FakePasswordInput("")

    called = {}
    monkeypatch.setattr("pyperclip.copy", lambda text: called.setdefault("text", text))

    handlers.on_copy_password_click(None, page, password_input)

    # буфер не должен копировать ничего
    assert "text" not in called or called["text"] == ""
    # появился snack_bar с "Nothing to copy!"
    assert any(
        "Nothing" in ctrl.content.value
        for ctrl in page.overlay
        if isinstance(ctrl, ft.SnackBar)
    )
    assert page.updated
