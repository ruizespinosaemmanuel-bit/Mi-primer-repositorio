import sqlite3
#abrir conexion
conexion = sqlite3.connect("Agenda.db")
cursor = conexion.cursor()
#crear tabla    
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        telefono TEXT
    )
""")
conexion.commit()

#insertar contactos
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",   
                ("Emmanuel", "9613482476"))
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",   
                ("Fatima", "3317103413"))
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",   
                ("Uriel", "9614516564"))
conexion.commit()
#guardar cambios
conexion.commit()
#Mostrar contactos
cursor.execute("SELECT * FROM contactos")
resultados = cursor.fetchall()
for contacto in resultados:
    print(contacto)
    print("Contacto agregado.")
    # Eliminar un contacto
cursor.execute("DELETE FROM contactos WHERE nombre = ?", ("Uriel",))
conexion.commit()
print("Contacto eliminado.")

# Mostrar contactos restantes
cursor.execute("SELECT * FROM contactos")
resultados = cursor.fetchall()
for contacto in resultados:
    print(contacto)
#cerrar conexion    
conexion.close()
