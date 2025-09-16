from pathlib import Path

from password_gen.utils import resources


def test_get_font_path_returns_path():
    p = resources.get_font_path("Rubik-Medium.ttf")
    assert isinstance(p, Path)
    assert str(p).replace("\\", "/").endswith("assets/fonts/rubik/Rubik-Medium.ttf")


def test_get_image_path_returns_path():
    p = resources.get_image_path("logo.png")
    assert isinstance(p, Path)
    assert str(p).replace("\\", "/").endswith("assets/images/logo.png")
