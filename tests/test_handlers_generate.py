import flet as ft

from password_gen.ui import handlers


class FakePage:
    def __init__(self):
        self.updated = False
        self.overlay = []

    def update(self):
        self.updated = True


class FakeControl:
    def __init__(self, value=None):
        self.value = value
        self.color = None
        self.bgcolor = None
        self.border = None


def setup_controls():
    """Подготавливаем набор контролов для вызова on_generate_password_click."""
    return (
        FakeControl("12"),  # length_selector
        FakeControl(True),  # letters_switch
        FakeControl(True),  # digits_switch
        FakeControl(True),  # symbols_switch
        FakeControl(""),  # password_input
        FakeControl(""),  # strength_label
        FakeControl(None),  # strength_color
        FakeControl(None),  # strength_container
    )


def test_generate_password_basic():
    page = FakePage()
    (
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
        password_input,
        strength_label,
        strength_color,
        strength_container,
    ) = setup_controls()

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

    assert password_input.value != ""  # пароль сгенерирован
    assert page.updated  # страница обновилась


def test_generate_password_blacklist(monkeypatch):
    page = FakePage()
    (
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
        password_input,
        strength_label,
        strength_color,
        strength_container,
    ) = setup_controls()

    # подменяем генератор, чтобы вернуть плохой пароль
    monkeypatch.setattr(
        "password_gen.ui.handlers.generate_password", lambda *a, **kw: "password"
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

    assert "Too common" in strength_label.value
    assert strength_color.bgcolor == ft.Colors.RED


def test_generate_password_strong(monkeypatch):
    page = FakePage()
    (
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
        password_input,
        strength_label,
        strength_color,
        strength_container,
    ) = setup_controls()

    # подменяем генератор, чтобы вернуть длинный сложный пароль
    monkeypatch.setattr(
        "password_gen.ui.handlers.generate_password", lambda *a, **kw: "Abc123!@#XYZ"
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

    assert "Strong" in strength_label.value
    assert strength_color.bgcolor == ft.Colors.GREEN
