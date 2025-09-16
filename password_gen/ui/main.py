import flet as ft

from password_gen.ui.layout import build_ui


def main(page: ft.Page):
    # --- Window setup ---
    page.window.center()
    page.title = "Password generator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 445
    page.window.height = 773
    page.window.resizable = False
    page.window.title_bar_hidden = True
    page.window.frameless = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary="#00bcd4"))

    # --- Add UI ---
    container = build_ui(page)
    page.add(container)
    page.update()


if __name__ == "__main__":
    import multiprocessing as mp

    mp.freeze_support()
    ft.app(target=main)
