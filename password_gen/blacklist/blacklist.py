COMMON_PASSWORDS = {"password", "123456", "qwerty"}


def is_blacklisted(pw: str) -> bool:
    return pw.lower() in COMMON_PASSWORDS


def has_repeated_chars(pw: str, min_repeats: int = 4) -> bool:
    return any(pw.count(ch) >= min_repeats for ch in set(pw))


def is_too_short(pw: str, min_length: int = 8) -> bool:
    return len(pw) < min_length


def check_blacklist(pw: str) -> str | None:
    if is_blacklisted(pw):
        return "This password is too common."
    if has_repeated_chars(pw):
        return "This password has too many repeated characters."
    if is_too_short(pw):
        return "This password is too short."
    return None
