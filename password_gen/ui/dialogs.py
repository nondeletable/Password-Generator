import webbrowser

import flet as ft


def close_dialog(page: ft.Page, dialog: ft.AlertDialog):
    """Закрытие диалога."""
    dialog.open = False
    page.update()


def open_nfo_window(page: ft.Page):
    """Окно с контактной информацией."""

    def open_link(url):
        webbrowser.open(url)

    dialog = ft.AlertDialog(
        title=ft.Text("My contacts", text_align=ft.TextAlign.CENTER),
        shape=ft.RoundedRectangleBorder(radius=8),
        content=ft.Column(
            controls=[
                ft.Text(
                    "Hi! My name is Alexandra. I'm a Python developer. "
                    "It's one of my apps. If you like my work, "
                    "there are contacts below where you can contact me!",
                    size=18,
                ),
                # Website
                ft.Row(
                    controls=[
                        ft.Text("My website:", expand=1, size=18),
                        ft.IconButton(
                            icon=ft.Icons.WEB,
                            tooltip="Website",
                            icon_size=30,
                            on_click=lambda e: open_link("https://mywebsite.com"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # Email
                ft.Row(
                    controls=[
                        ft.Text("My mail:", expand=1, size=18),
                        ft.IconButton(
                            icon=ft.Icons.EMAIL,
                            tooltip="Email",
                            icon_size=30,
                            on_click=lambda e: open_link(
                                "mailto:alexgicheva@gmail.com"
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # GitHub
                ft.Row(
                    controls=[
                        ft.Text("My github:", expand=1, size=18),
                        ft.IconButton(
                            icon=ft.Icons.HUB,
                            tooltip="GitHub",
                            icon_size=30,
                            on_click=lambda e: open_link(
                                "https://github.com/SkriptSparrow"
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            spacing=20,
        ),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(page, dialog))],
    )

    page.overlay.append(dialog)
    dialog.open = True
    page.update()
