import flet as ft

from password_gen.ui import dialogs, handlers
from password_gen.utils import resources


def build_ui(page: ft.Page):
    AUTOHIDE_SECONDS = 10
    CLEAR_CLIPBOARD_SECONDS = 30

    # --- Window controls ---
    close_button = ft.IconButton(ft.Icons.CLOSE, on_click=lambda e: page.window.close())
    maximize_button = ft.IconButton(
        ft.Icons.MENU, on_click=lambda e: dialogs.open_nfo_window(page)
    )
    minimize_button = ft.IconButton(
        ft.Icons.REMOVE, on_click=lambda e: setattr(page.window, "minimized", True)
    )

    drag_area = ft.WindowDragArea(
        ft.Container(height=50, width=1000), expand=True, maximizable=False
    )

    title_bar = ft.Row(
        controls=[maximize_button, drag_area, minimize_button, close_button],
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    # --- Assets ---
    font_path = resources.get_font_path("Rubik-Medium.ttf")
    page.fonts = {"Rubik": str(font_path)}
    img_path = resources.get_image_path("logo.png")
    image = ft.Image(src=str(img_path), width=150, height=150)

    title = ft.Text(
        value="PASSWORD GENERATOR",
        font_family="Rubik",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    header_column = ft.Column(
        controls=[image, ft.Container(height=65, width=400), title],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=400,
        spacing=0,
    )

    # --- Switches & selectors ---
    letters_switch = ft.Switch(label="Letters", value=True)
    digits_switch = ft.Switch(label="Digits", value=True)
    symbols_switch = ft.Switch(label="Symbols", value=True)

    length_selector = ft.Dropdown(
        label="Password length:",
        options=[ft.dropdown.Option(str(n)) for n in range(6, 21, 2)],
        width=170,
        value="8",
        border_color="#00bcd4",
    )

    policy_selector = ft.Dropdown(
        label="Mode:",
        options=[
            ft.dropdown.Option("Custom"),
            ft.dropdown.Option("Standard"),
            ft.dropdown.Option("Admin"),
            ft.dropdown.Option("NIST"),
        ],
        value="Custom",
        width=170,
        border_color="#00bcd4",
    )

    length_policy_row = ft.Row(
        controls=[length_selector, policy_selector],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        width=350,
    )

    # --- Password field ---
    password_input = ft.TextField(
        label="Generated password:",
        width=350,
        height=55,
        read_only=True,
        password=True,
        suffix=ft.IconButton(
            icon=ft.Icons.VISIBILITY_OFF,
            on_click=lambda e: handlers.on_toggle_visibility_click(
                e, page, password_input, AUTOHIDE_SECONDS
            ),
        ),
        border_color="#00bcd4",
    )

    # --- Strength indicator ---
    strength_color = ft.Container(
        width=12, height=12, border_radius=6, bgcolor=None, visible=False
    )
    strength_label = ft.Text(
        "Strength", color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER
    )
    strength_row = ft.Row(
        controls=[strength_color, strength_label],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,
    )

    strength_container = ft.Container(
        content=strength_row,
        padding=5,
        border_radius=8,
        border=ft.border.all(1, ft.Colors.BLACK),
        width=190,
        alignment=ft.alignment.center,
    )

    # --- Buttons ---
    generate_button = ft.ElevatedButton(
        text="GENERATE",
        color=ft.Colors.WHITE,
        bgcolor="#00bcd4",
        on_click=lambda e: handlers.on_generate_password_click(
            e,
            page,
            length_selector,
            letters_switch,
            digits_switch,
            symbols_switch,
            password_input,
            strength_label,
            strength_color,
            strength_container,
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    copy_button = ft.ElevatedButton(
        content=ft.Icon(ft.Icons.CONTENT_COPY),
        on_click=lambda e: handlers.on_copy_password_click(
            e, page, password_input, CLEAR_CLIPBOARD_SECONDS
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    footer = ft.Text(
        "DEVELOPED BY CODEBIRD",
        color=ft.Colors.GREY_500,
        width=350,
        text_align=ft.TextAlign.CENTER,
    )

    switch_row = ft.Row(
        controls=[
            ft.Row([letters_switch]),
            ft.Row([digits_switch]),
            ft.Row([symbols_switch]),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=22,
    )

    button_row = ft.Row(
        controls=[generate_button, strength_container, copy_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    container = ft.Column(
        controls=[
            title_bar,
            ft.Container(height=100, width=400),
            header_column,
            ft.Container(height=25, width=400),
            switch_row,
            length_policy_row,
            password_input,
            button_row,
            ft.Container(height=5, width=400),
            footer,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    def set_custom_mode():
        policy_selector.value = "Custom"
        page.update()

    policy_selector.on_change = lambda e: handlers.on_policy_change(
        e,
        page,
        policy_selector,
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
    )
    length_selector.on_change = lambda e: set_custom_mode()
    letters_switch.on_change = lambda e: set_custom_mode()
    digits_switch.on_change = lambda e: set_custom_mode()
    symbols_switch.on_change = lambda e: set_custom_mode()

    return container
