import string

import pytest

from password_gen.constants import AMBIGUOUS, SYMBOLS
from password_gen.generator.generator import generate_password


def test_password_length():
    """Пароль всегда должен быть указанной длины."""
    pw = generate_password(
        length=16, use_letters=True, use_digits=True, use_symbols=True
    )
    assert len(pw) == 16


def test_contains_all_selected_categories():
    """Пароль должен содержать хотя бы один символ из каждой выбранной категории."""
    pw = generate_password(
        length=12, use_letters=True, use_digits=True, use_symbols=True
    )

    assert any(c in string.ascii_letters for c in pw)  # буквы
    assert any(c in string.digits for c in pw)  # цифры
    assert any(c in SYMBOLS for c in pw)  # символы


def test_only_letters():
    """Если выбраны только буквы, пароль не должен содержать других символов."""
    pw = generate_password(
        length=10, use_letters=True, use_digits=False, use_symbols=False
    )
    assert all(c in string.ascii_letters for c in pw)


def test_only_digits():
    """Если выбраны только цифры, пароль не должен содержать других символов."""
    pw = generate_password(
        length=10, use_letters=False, use_digits=True, use_symbols=False
    )
    assert all(c in string.digits for c in pw)


def test_error_on_no_categories():
    """Если не выбрана ни одна категория — должна быть ошибка."""
    with pytest.raises(ValueError):
        generate_password(
            length=10, use_letters=False, use_digits=False, use_symbols=False
        )


def test_error_if_length_too_short():
    """Длина пароля меньше числа выбранных категорий → ошибка."""
    with pytest.raises(ValueError):
        generate_password(length=2, use_letters=True, use_digits=True, use_symbols=True)


def test_exclude_ambiguous():
    pw = generate_password(
        20, use_letters=True, use_digits=True, use_symbols=False, exclude_ambiguous=True
    )
    for ch in pw:
        assert ch not in AMBIGUOUS


def test_length_equals_categories():
    pw = generate_password(3, use_letters=True, use_digits=True, use_symbols=True)
    assert any(c in string.ascii_letters for c in pw)
    assert any(c in string.digits for c in pw)
    assert any(c in SYMBOLS for c in pw)


def test_only_symbols():
    pw = generate_password(10, use_letters=False, use_digits=False, use_symbols=True)
    assert all(c in SYMBOLS for c in pw)


def test_generate_password_no_chars(monkeypatch):
    # замокаем SYMBOLS = "O0l1I", чтобы после exclude_ambiguous ничего не осталось
    monkeypatch.setattr("password_gen.generator.generator.SYMBOLS", "O0l1I")

    with pytest.raises(ValueError, match="No characters available"):
        generate_password(
            length=8,
            use_letters=False,
            use_digits=False,
            use_symbols=True,
            exclude_ambiguous=True,
        )
