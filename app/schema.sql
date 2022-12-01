CREATE TABLE funcionario (
    rut TEXT NOT NULL PRIMARY KEY,
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nac TEXT NOT NULL,
    cargo TEXT NOT NULL,
    seccion TEXT NOT NULL,
    password TEXT NOT NULL
)

CREATE TABLE paciente (
    rut TEXT NOT NULL PRIMARY KEY,
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nac TEXT NOT NULL,
    peso_kg REAL NOT NULL,
    estatura_cm REAL NOT NULL,
    sexo TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL, --Este va a guardar las calles comunas y ciudad y los va a separar por comas ,
    numeros_tel TEXT NOT NULL --Este va a guardar muchos numeros y los va a separar por guiones -
);

CREATE TABLE interconsulta (
    id_interconsulta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    observacion  TEXT NOT NULL,
    rut_paciente TEXT NOT NULL,
    rut_funcionario TEXT NOT NULL,
    FOREIGN KEY(rut_paciente) REFERENCES paciente(rut),
    FOREIGN KEY(rut_funcionario) REFERENCES funcionario(rut)
);