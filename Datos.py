import sqlite3
#Abrir conexion
conexion = sqlite3.connect("Mi_base.db")
cursor = conexion.cursor()
#Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT, 
        edad INTEGER, 
        carrera TEXT
    )
""")
conexion.commit()
print("Base de datos creada.") 
# Insertar 3 alumnos
cursor.execute("INSERT INTO alumnos (nombre, edad, carrera) VALUES (?, ?, ?)",
                ("Emmanuel", 20, "Ingeniero de Software"))
cursor.execute("INSERT INTO alumnos (nombre, edad, carrera) VALUES (?, ?, ?)",
                ("Fatima", 23, "Medicina"))
cursor.execute("INSERT INTO alumnos (nombre, edad, carrera) VALUES (?, ?, ?)",
                ("Uriel", 21, "Derecho"))
#Guardar cambios
conexion.commit()
#Leer todos los alumnos
cursor.execute(" SELECT * FROM alumnos")
resultados = cursor.fetchall()
for alumno in resultados:
    print(alumno)
print("Alumno agregado.")
#cerrar conexion
conexion.close()
