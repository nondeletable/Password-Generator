import flet as ft

from password_gen.ui import handlers
from password_gen.utils import timers


# --- фейки ---
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
        self.visible = False  # для strength_color


class FakePasswordInput:
    def __init__(self, value=""):
        self.value = value
        self.password = False
        self.suffix = type("Sfx", (), {"icon": None})()


def _setup_controls():
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


def test_generate_password_weak_branch(monkeypatch):
    """Покрываем строки 51–54: ветка weak."""
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
    ) = _setup_controls()

    # заглушки: отключаем blacklist, форсим weak
    monkeypatch.setattr(
        "password_gen.ui.handlers.generate_password", lambda *a, **k: "abc123"
    )
    monkeypatch.setattr(
        "password_gen.ui.handlers.check_blacklist", lambda _pw: None
    )  # <— важно
    monkeypatch.setattr("password_gen.ui.handlers.check_strength", lambda _pw: "weak")

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

    assert "Weak" in strength_label.value
    assert strength_label.color == ft.Colors.RED
    assert strength_color.bgcolor == ft.Colors.RED
    assert strength_color.visible is True


def test_generate_password_fair_branch(monkeypatch):
    """Покрываем строки 56–59: ветка fair."""
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
    ) = _setup_controls()

    monkeypatch.setattr(
        "password_gen.ui.handlers.generate_password", lambda *a, **k: "Abcdef12"
    )
    monkeypatch.setattr("password_gen.ui.handlers.check_blacklist", lambda _pw: None)
    monkeypatch.setattr("password_gen.ui.handlers.check_strength", lambda _pw: "fair")

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

    assert "Fair" in strength_label.value
    assert strength_label.color == ft.Colors.ORANGE
    assert strength_color.bgcolor == ft.Colors.ORANGE
    assert strength_color.visible is True


def test_auto_hide_password_direct_call():
    """Покрываем строки 83–85: _auto_hide_password."""
    page = FakePage()
    pwd = FakePasswordInput(value="x")
    pwd.password = False
    pwd.suffix.icon = ft.Icons.VISIBILITY  # до вызова

    timers.auto_hide_password(page, pwd)

    assert pwd.password is True
    assert pwd.suffix.icon == ft.Icons.VISIBILITY_OFF
    assert page.updated
