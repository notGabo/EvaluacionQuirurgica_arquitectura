import sqlite3
import os
import time

def ingresarUsuario():
    rut = input('RUT (sin puntos ni guion): ')
    nombres = input('NOMBRES: ')
    apellidos = input('APELLIDOS: ')
    fecha_nac = input('FECHA DE NACIMIENTO: ')
    cargo = input('CARGO: ')
    seccion = input('SECCION: ')
    password = input('CONTRASEÑA: ')

    existe = existeUsuario(rut)

    if existe:
        print("\033[91m {}\033[00m".format('ERROR: USUARIO NO SE PUDO INGRESAR POR QUE YA EXISTE'))
        time.sleep(1.5)
    else:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(
            'INSERT INTO funcionario(rut, nombres, apellidos, fecha_nac, cargo, seccion, password) values (?,?,?,?,?,?,?)',
            (rut, nombres, apellidos, fecha_nac, cargo, seccion, password)
        )

        con.commit()
        cur.close()
        print("\033[92m {}\033[00m".format('USUARIO INGRESADO EXITOSAMENTE'))
        time.sleep(1.5)

def existeUsuario(rut):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT rut FROM funcionario WHERE rut=?', (rut,))

    result = cur.fetchone()
    cur.close()

    if result:
        return True
    else:
        return False

def mostrarUsuario():
    rut = input('\nRUT (sin puntos ni guion): ')

    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM funcionario WHERE rut=?', (rut,))

    result = cur.fetchone()
    cur.close()

    for i in result:
        print(i)
        
    input('\nPRESIONE INTRO PARA CONTINUAR')

def eliminarUsuario():
    rut = input('\nRUT (sin puntos ni guion): ')

    existe = existeUsuario(rut)

    if existe:
        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute('DELETE FROM funcionario WHERE rut=?', (rut,))
        con.commit()
        cur.close()
        print("\033[92m {}\033[00m".format('USUARIO ELIMINADO EXITOSAMENTE'))
        time.sleep(1.5)
    else:
        print("\033[91m {}\033[00m".format('ERROR: USUARIO NO SE PUDO ELIMINAR POR QUE NO EXISTE'))
        time.sleep(1.5)
    

while True:
    os.system('clear')
    print('APP ADMINISTRADOR\n')
    print('1. Ingresar Usuario 🖊 \n2. Mostrar Usuario 👁\n3. Eliminar Usuario 🗑\n0. Salir')

    try:
        opcion = int(input('SELECIONE UNA OPCION: '))
        if opcion == 1:
            print('\nELIJA UNA OPCION VALIDA')
            os.system('clear')
            ingresarUsuario()
        elif opcion == 2:
            os.system('clear')
            mostrarUsuario()
        elif opcion == 3:
            os.system('clear')
            eliminarUsuario()
        elif opcion == 0:
            break
    except:
        print('\nELIJA UNA OPCION VALIDA')
        time.sleep(1)