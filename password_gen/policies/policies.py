# password_gen/policies/policies.py

POLICIES = {
    "Standard": {
        "length": 12,
        "letters": True,
        "digits": True,
        "symbols": True,
        "exclude_ambiguous": False,
    },
    "Admin": {
        "length": 20,
        "letters": True,
        "digits": True,
        "symbols": True,
        "exclude_ambiguous": True,
    },
    "NIST": {
        "length": 12,
        "letters": True,
        "digits": True,
        "symbols": True,
        "exclude_ambiguous": False,
    },
}
