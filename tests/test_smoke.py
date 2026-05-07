def test_environment_ready():
    """Базовая проверка импортов криптографических зависимостей."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from argon2 import PasswordHasher, Type

    assert AESGCM is not None
    assert PasswordHasher is not None
    assert Type.ID is not None
