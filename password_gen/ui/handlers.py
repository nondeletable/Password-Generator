import flet as ft

from password_gen.blacklist.blacklist import check_blacklist
from password_gen.generator.generator import generate_password
from password_gen.generator.strength import check_strength
from password_gen.policies.policies import POLICIES
from password_gen.utils import clipboard, timers


def on_generate_password_click(
    e,
    page: ft.Page,
    length_selector,
    letters_switch,
    digits_switch,
    symbols_switch,
    password_input,
    strength_label,
    strength_color,
    strength_container,
):
    """Генерация пароля и проверка blacklist/strength."""
    try:
        length = int(length_selector.value)
    except ValueError:
        length = 12

    try:
        password_input.value = generate_password(
            length, letters_switch.value, digits_switch.value, symbols_switch.value
        )
    except ValueError as err:
        password_input.value = ""
        strength_label.value = str(err)
        page.update()
        return

    warning = check_blacklist(password_input.value)
    strength_color.visible = True

    if warning:
        strength_label.value = f"⚠️ {warning}"
        strength_label.color = ft.Colors.RED
        strength_color.bgcolor = ft.Colors.RED
        strength_container.border = ft.border.all(1, ft.Colors.RED)
    else:
        strength = check_strength(password_input.value)
        if strength == "weak":
            strength_color.bgcolor = ft.Colors.RED
            strength_label.value = "Strength: Weak"
            strength_label.color = ft.Colors.RED
            strength_container.border = ft.border.all(1, ft.Colors.RED)
        elif strength == "fair":
            strength_color.bgcolor = ft.Colors.ORANGE
            strength_label.value = "Strength: Fair"
            strength_label.color = ft.Colors.ORANGE
            strength_container.border = ft.border.all(1, ft.Colors.ORANGE)
        else:
            strength_color.bgcolor = ft.Colors.GREEN
            strength_label.value = "Strength: Strong"
            strength_label.color = ft.Colors.GREEN
            strength_container.border = ft.border.all(1, ft.Colors.GREEN)

    page.update()


def on_toggle_visibility_click(e, page: ft.Page, password_input, auto_hide_seconds=10):
    """Переключение видимости пароля + автоскрытие."""
    password_input.password = not password_input.password
    e.control.icon = (
        ft.Icons.VISIBILITY if not password_input.password else ft.Icons.VISIBILITY_OFF
    )
    if not password_input.password:
        timers.run_delayed(
            auto_hide_seconds,
            lambda: timers.auto_hide_password(page, password_input),
        )
    page.update()


def on_copy_password_click(e, page: ft.Page, password_input, clear_seconds=30):
    """Копирование в буфер обмена + автоочистка."""
    if password_input.value:
        clipboard.copy_to_clipboard(password_input.value)
        snack_bar = ft.SnackBar(
            ft.Text("Copied to clipboard!"), bgcolor=ft.Colors.BLACK, duration=1000
        )
        clipboard.clear_clipboard_after(clear_seconds)
    else:
        snack_bar = ft.SnackBar(
            ft.Text("Nothing to copy!"),
            bgcolor=ft.Colors.BLACK,
            duration=1000,
        )

    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()


def on_policy_change(
    e,
    page: ft.Page,
    policy_selector,
    length_selector,
    letters_switch,
    digits_switch,
    symbols_switch,
):
    """Применение выбранной политики."""
    selected = policy_selector.value
    if selected != "Custom":
        policy = POLICIES[selected]
        length_selector.value = str(policy["length"])
        letters_switch.value = policy["letters"]
        digits_switch.value = policy["digits"]
        symbols_switch.value = policy["symbols"]
        page.session.set("exclude_ambiguous", policy["exclude_ambiguous"])
    page.update()
