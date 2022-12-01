import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from dateutil import parser

app = Flask(__name__)
app.secret_key = "FZi&[1<9YtL7InQ"

def isLogged():
    try:
        if session['logged'] == True:
            return True
        else:
            return False

    except:
        session['logged'] = False
        return False

@app.route('/')
def home():
    if isLogged() == False:
        return redirect(url_for('login'))
    
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT nombres, apellidos FROM funcionario WHERE rut=?', (session['user'],))
    query = cur.fetchone()
    cur.close()

    data = {
        'titulo':'Home - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'home',
        'nombre':query[0] + ' ' + query[1]
    }

    return render_template('home.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if isLogged() == True:
        return redirect(url_for('home'))

    data = {
        'titulo':'Login Intranet - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'login'
    }

    if (request.method == 'POST'):
        rut = request.form.get('user').replace(".", "").replace("-", "")
        password = request.form.get('pass')

        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM funcionario WHERE rut=? AND password=?', (rut, password))
        query = cur.fetchone()
        cur.close()

        if query:
            session['logged'] = True
            session['user'] = rut
            return redirect(url_for('home'))
        else:
            data['error'] = True

    return render_template('login.html', data=data)

@app.route('/logout')
def logout():
    session['logged'] = False
    session.pop('user')
    return redirect(url_for('login'))

#region PRE-QUIRURGICA

@app.route('/pre-quirurgica/evaluacion/buscar-interconsulta', methods=['GET', 'POST'])
def buscarInterconsulta():
    if isLogged() == False:
        return redirect(url_for('login'))

    data = {
        'titulo':'Evaluacion Pre-quirurgica - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'pre-quirurgico',
        'buscado': False
    }
    result = []

    if request.method == 'POST':
        documento = request.form.get('option-input')

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        query = cur.execute('SELECT * FROM interconsulta WHERE rut_paciente =?', (documento,)).fetchall()
        pac = cur.execute("SELECT nombres||' '||apellidos FROM paciente WHERE rut=?", (documento,)).fetchone()

        # esto es solo para el testing
        data['buscado'] = True
        if pac:
            for item in query:
                funcionario = cur.execute("SELECT nombres||' '||apellidos FROM funcionario WHERE rut=?", (item[4],)).fetchone()[0]

                an_item = dict(rut_pac=documento, paciente=pac[0], funcionario=funcionario, fecha=item[1], estado=item[5])
                result.append(an_item)

        cur.close()

    return render_template('prequirurgico/buscarInterconsulta.html', data=data, table=result)


@app.route('/pre-quirurgica/evaluacion/datos-paciente/<rut_paciente>', methods=['GET', 'POST'])
def datosPaciente(rut_paciente):
    if isLogged() == False:
        return redirect(url_for('login'))

    data = {
        'titulo':'Evaluacion Pre-quirurgica - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'pre-quirurgico',
        'step':'0',
        'barProgress':'0%'
    }

    paciente = rut_paciente

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    query = cur.execute('SELECT * FROM paciente WHERE rut=?', (paciente,)).fetchone()
    cur.close()

    query = dict(
                rut=query[0],
                nombres=query[1],
                apellidos=query[2],
                fecha= parser.parse(query[3]).date().isoformat(),
                peso=query[4],
                altura=query[5],
                correo=query[7],
                direccion=query[8],
                numeros=query[9]
                )

    if request.method == 'POST':
        print('listo')
        return redirect(url_for('evaluacionEnfermedades'))

    return render_template('prequirurgico/datosPaciente.html', data=data, paciente=query)


@app.route('/pre-quirurgica/evaluacion/evaluacion-enfermedades', methods=['GET', 'POST'])
def evaluacionEnfermedades():
    if isLogged() == False:
        return redirect(url_for('login'))

    data = {
        'titulo':'Evaluacion Pre-quirurgica - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'pre-quirurgico',
        'step':'1',
        'barProgress':'50%'

    }
    if request.method == 'POST':
        return redirect(url_for('evaluacionRiesgo'))

    return render_template('prequirurgico/evaluacionEnfermedades.html', data=data)


@app.route('/pre-quirurgica/evaluacion/evaluacion-riesgo', methods=['GET', 'POST'])
def evaluacionRiesgo():
    if isLogged() == False:
        return redirect(url_for('login'))

    data = {
        'titulo':'Evaluacion Pre-quirurgica - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'pre-quirurgico',
        'step':'1',
        'barProgress':'50%'

    }
    
    if request.method == 'POST':
        return redirect(url_for('derivacion'))

    return render_template('prequirurgico/evaluacionRiesgo.html', data=data)


@app.route('/pre-quirurgica/evaluacion/derivacion', methods=['GET', 'POST'])
def derivacion():
    if isLogged() == False:
        return redirect(url_for('login'))

    data = {
        'titulo':'Evaluacion Pre-quirurgica - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'pre-quirurgico',
        'step':'2',
        'barProgress':'100%'

    }

    if request.method == 'POST':
        return redirect(url_for('home'));

    return render_template('prequirurgico/derivacion.html', data=data)


#endregion

#region PACIENTE

@app.route('/pre-quirurgica/buscar-paciente')
def buscarPaciente():

    data = {
        'titulo':'Buscar Paciente - Servicio de Salud Metropolitano Sur Oriente',
        'actualFase':'paciente'
    }

    return render_template('prequirurgico/buscarPaciente.html', data=data)

#endregion



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=80)
