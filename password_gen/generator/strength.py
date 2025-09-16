def check_strength(password: str) -> str:
    """
    Very simple password strength checker.
    Can be improved later with entropy or zxcvbn.

    Args:
        password (str): Password to check.

    Returns:
        str: "weak", "fair", or "strong".
    """
    length = len(password)
    categories = sum(
        [
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(not c.isalnum() for c in password),
        ]
    )

    if length < 8 or categories < 2:
        return "weak"
    elif length < 12 or categories < 3:
        return "fair"
    else:
        return "strong"
