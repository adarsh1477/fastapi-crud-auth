from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()


class Hash():
    def encrypt(password: str):
        hashed_password = password_hasher.hash(password)
        return hashed_password
    def ver(plain_password,Hashed_password):
        return password_hasher.verify(plain_password,Hashed_password)