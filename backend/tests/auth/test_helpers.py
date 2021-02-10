from faker import Faker

from app.helpers.auth import generate_password_hash, check_password_hash

fake = Faker()


def test_generate_password_hash():
    password = fake.password()

    assert generate_password_hash(password) is not None
    assert isinstance(generate_password_hash(password), bytes)


def test_check_password_hash():
    password = fake.password()
    password_hash = generate_password_hash(password)

    assert check_password_hash(password, password_hash)
    assert not check_password_hash(fake.password(), password_hash)
