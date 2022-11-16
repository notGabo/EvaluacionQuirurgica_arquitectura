from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():

    data = {
        'titulo':'Login Intranet - Servicio de Salud Metropolitano Sur Oriente',
        'actualOption':'login'
    }

    return render_template('prequirurgico/login.html', data=data)

@app.route('/pre-quirurgica/buscar-paciente')
def buscarPaciente():

    data = {
        'titulo':'Buscar Paciente - Servicio de Salud Metropolitano Sur Oriente',
        'actualOption':'pre-quirurgico'
    }

    return render_template('prequirurgico/buscarPaciente.html', data=data)

@app.route('/pre-quirurgica/evaluar-paciente')
def evaluarPaciente():
    data = {
        'titulo':'Evaluar Paciente - Servicio de Salud Metropolitano Sur Oriente',
        'actualOption':'pre-quirurgico'
    }
    return render_template('prequirurgico/evaluarPaciente.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=80)
