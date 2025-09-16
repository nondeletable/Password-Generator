from importlib import resources as res
from pathlib import Path


def get_font_path(filename: str) -> Path:
    """Вернуть путь к шрифту в assets/fonts/."""
    return res.files("password_gen").joinpath(f"assets/fonts/rubik/{filename}")


def get_image_path(filename: str) -> Path:
    """Вернуть путь к картинке в assets/images/."""
    return res.files("password_gen").joinpath(f"assets/images/{filename}")
