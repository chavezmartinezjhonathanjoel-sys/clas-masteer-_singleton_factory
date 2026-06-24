class ConexionBaseDatos:
    _instancia = None

    def __new__(cls, nombre_bd):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre_bd = nombre_bd
            print(f"Conectando a {nombre_bd}...")
        else:
            print(f"Reutilizando conexión existente a {cls._instancia.nombre_bd}")
        return cls._instancia

    def consultar(self, sql):
        print(f"Ejecutando: {sql}")
        return f"Resultado de {self.nombre_bd}"


if __name__ == "__main__":
    conexion1 = ConexionBaseDatos("usuarios.db")
    resultado1 = conexion1.consultar("SELECT * FROM usuarios")

    conexion2 = ConexionBaseDatos("productos.db")
    resultado2 = conexion2.consultar("SELECT * FROM productos")
    print(f"Conexion 2: {id(conexion2)}")

