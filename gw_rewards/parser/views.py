import bcrypt
# https://api.sorare.com/api/v1/users/kotleta88@mail.ru

salt = "$2a$11$jsRjiy0o5s5frl2.wGyXNe"
password = "Raida88"
salt = bytes(salt)
password = bytes(password)

hashed_password = bcrypt.hashpw(password, salt)

