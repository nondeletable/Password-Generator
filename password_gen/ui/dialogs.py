import webbrowser

import flet as ft

from password_gen.utils import resources


def close_dialog(page: ft.Page, dialog: ft.AlertDialog):
    """Закрытие диалога."""
    dialog.open = False
    page.update()


def open_nfo_window(page: ft.Page):
    """Окно с контактной информацией."""

    def open_link(url):
        webbrowser.open(url)

    discord_path = resources.get_image_path("discord.svg")
    email_path = resources.get_image_path("email.svg")
    github_path = resources.get_image_path("github.svg")

    dialog = ft.AlertDialog(
        title=ft.Text("ABOUT", text_align=ft.TextAlign.CENTER, font_family="Rubik"),
        shape=ft.RoundedRectangleBorder(radius=8),
        content=ft.Column(
            height=300,
            width=270,
            controls=[
                ft.Text(
                    "Hi! My name is Alexandra.\n"
                    "I'm a Python developer.\n"
                    "Thank you for using my app!",
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    font_family="Rubik2",
                    width=300,
                ),
                ft.Text(
                    "If you’d like to say thanks, leave feedback, report a bug, "
                    "or discuss collaboration, "
                    "feel free to contact me via Discord, email, or GitHub.",
                    size=15,
                    text_align=ft.TextAlign.CENTER,
                    font_family="Rubik2",
                ),
                ft.Container(height=10),  # Небольшой отступ
                # Ряд с круглыми кнопками
                ft.Row(
                    controls=[
                        # Discord
                        ft.ElevatedButton(
                            content=ft.Image(
                                src=str(discord_path), width=80, height=80
                            ),
                            width=60,
                            height=60,
                            style=ft.ButtonStyle(
                                padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: open_link("https://discord.gg/QUC4mnBF"),
                        ),
                        # Email
                        ft.ElevatedButton(
                            content=ft.Image(src=str(email_path), width=80, height=80),
                            width=60,
                            height=60,
                            style=ft.ButtonStyle(
                                padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: open_link(
                                "mailto:nondeletable@gmail.com"
                            ),
                        ),
                        # GitHub
                        ft.ElevatedButton(
                            content=ft.Image(src=str(github_path), width=80, height=80),
                            width=60,
                            height=60,
                            style=ft.ButtonStyle(
                                padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                            ),
                            on_click=lambda e: open_link(
                                "https://github.com/nondeletable/Password-Generator"
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40,
                ),
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(page, dialog))],
    )

    page.overlay.append(dialog)
    dialog.open = True
    page.update()
