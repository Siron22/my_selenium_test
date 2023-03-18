class User:
    INVALID_EMAIL_DATA = [('abc@', '12345678'), ('abc@com', '12345678'), ('@com.ua', '12345678'),
                                             ('emailcom.ua', '12345678'), ('#$%^&*@com.ua', '12345678')]

    UNREGISTERED_EMAIL = 'abc@test.com'
    INCORRECT_PASSWORD = '12345678'

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

# TODO: Make user`s data generation from file .json
