class Usuario:

    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def usuario(self, usuario):
        self._username = usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def informacion(self):
        return self.__str__()

    def __str__(self):
        return f'Persona: {self._username} - {self._password}'