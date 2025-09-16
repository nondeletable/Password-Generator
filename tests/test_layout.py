import flet as ft

from password_gen.ui import layout


class FakePage:
    def __init__(self):
        self.updated = False
        self.fonts = {}
        self.overlay = []
        self.window = type(
            "Window", (), {"close": lambda self: None, "minimized": False}
        )()

    def update(self):
        self.updated = True


def test_build_ui_returns_container():
    page = FakePage()
    container = layout.build_ui(page)

    assert isinstance(container, ft.Column)
    # в контейнере должны быть элементы, например title_bar и footer
    assert any(isinstance(ctrl, ft.Row) for ctrl in container.controls)
    assert any(
        isinstance(ctrl, ft.Text) and "DEVELOPED BY CODEBIRD" in ctrl.value
        for ctrl in container.controls
    )


def _find_control(root, cls, label=None):
    """Рекурсивный поиск контрола по типу (и по label если нужно)."""
    stack = [root]
    while stack:
        ctrl = stack.pop()
        if isinstance(ctrl, cls) and (
            label is None or getattr(ctrl, "label", None) == label
        ):
            return ctrl
        if hasattr(ctrl, "controls"):
            stack.extend(ctrl.controls)
    return None


def test_set_custom_mode_triggers_update():
    page = FakePage()
    container = layout.build_ui(page)

    policy_selector = _find_control(container, ft.Dropdown, label="Mode:")
    length_selector = _find_control(container, ft.Dropdown, label="Password length:")

    # убедимся, что нашли
    assert policy_selector is not None
    assert length_selector is not None

    # имитируем смену политики
    policy_selector.value = "Admin"
    page.updated = False

    # дергаем on_change у length_selector → должен сбросить на Custom
    length_selector.on_change(None)

    assert policy_selector.value == "Custom"
    assert page.updated
