import flet as ft

from password_gen.utils import timers


class FakePage:
    def __init__(self):
        self.updated = False

    def update(self):
        self.updated = True


class FakePasswordInput:
    def __init__(self):
        self.password = False
        self.suffix = type("Sfx", (), {"icon": ft.Icons.VISIBILITY})()


def test_run_delayed_invokes_func(monkeypatch):
    called = {}

    def fake_timer(seconds, func):
        called["seconds"] = seconds
        called["func"] = func
        return type("T", (), {"start": lambda self: func()})()

    monkeypatch.setattr("password_gen.utils.timers.threading.Timer", fake_timer)

    timers.run_delayed(2, lambda: called.setdefault("ran", True))

    assert called["seconds"] == 2
    assert called["ran"] is True


def test_auto_hide_password_changes_state():
    page = FakePage()
    pwd = FakePasswordInput()

    timers.auto_hide_password(page, pwd)

    assert pwd.password is True
    assert pwd.suffix.icon == ft.Icons.VISIBILITY_OFF
    assert page.updated
