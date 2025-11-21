
def _write_file(self, usuarios: dict[int, Usuario]):
    with open(self.filename, "w") as f:
        for usuario in usuarios.values():
            f.write(usuario.to_line() + "\n")

def _append_file(self, usuario: dict | int, Usuario):
    with open(self.filename, "a") as f:
        f.write(usuario.to_line() + "\n")

def insert(self, nombre: str, edad: int) -> Usuario:
    new_id = self._get_next_id()
    usuario = Usuario(new_id, nombre, edad)
    usuarios[new_id] = usuario
    self._append_file(usuarios)
    return usuario

def update(self, id: int, nombre: str, edad: int) -> bool:
    usuarios = self._read_file()
    if id in usuarios:
        usuarios[id].nombre = nombre
        usuarios[id].edad = edad
        self._write_file(usuarios)
        return True
    return False

def delete(self, id: int) -> Usuario | None:
    usuarios = self._read_file()

    if id in usuarios:
        del usuarios[id]
        self._write_file(usuarios)
        return True
    return False

def get(self, id: int) -> Usuario | None:
    usuarios = self._read_file()
    return usuarios.get(id)

def get_all(self) -> dict[int, Usuario]:
    return self._read_file()