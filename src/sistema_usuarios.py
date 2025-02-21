
class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_usuario(self, usuario, contraseña):
        if usuario in self.usuarios:
            return False  # El usuario ya existe
        self.usuarios[usuario] = contraseña
        return True

    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            del self.usuarios[usuario]
            return True
        return False
