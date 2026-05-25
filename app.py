# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template, request


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    nombre_profesor = "Prof. Henry - Kyrbot Innovations"
    email_profesor = "henry@kyrbot.com"
    horario = "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
    aula = "215"
    descripcion = "Aprenderemos Python, Flask y construiremos un portal web real"
   

    return render_template("index.html",
    profesor=nombre_profesor,
    email=email_profesor,
    horario=horario,
    aula=aula,
    descripcion=descripcion)



@app.route("/informacion")
def informacion():
        datos = {
        "aula": "215",
        "profesor": "Henry Ortegon",
        "horario": "Miercoles 16:45-18:10 | Jueves 12:30-14:20",
        "objetivos": [
            "Aprender Python basico",
            "Entender Flask y aplicaciones web",
            "Construir un portal web real"
        ]
    }

        return render_template("informacion.html", **datos,)




@app.route("/tareas")
def contacto():
    tareas = [
        {"numero": 1, "titulo": "Portal base", "fecha": "25/05/2026"},
        {"numero": 2, "titulo": "Datos dinamicos", "fecha": "30/05/2026"},
        {"numero": 3, "titulo": "Multiple paginas", "fecha": "05/06/2026"}
    ]

 
    return render_template("tareas.html", tareas=tareas)



@app.route("/recursos")
def recursos():
    enlaces = [
    {"nombre": "Documentacion Flask", "url": "https://flask.palletsprojects.com"},
    {"nombre": "Tutorial Python", "url": "https://docs.python.org"},
    {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"},
    {"nombre": "MDN - HTML y CSS", "url": "https://developer.mozilla.org"}
]
 
    return render_template("recursos.html",enlaces=enlaces)


@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None
    
    if request.method == "POST":
        # El usuario envio el formulario
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")
        
        # Validacion basica
        if nombre and email and programa:
            mensaje = f"Bienvenido {nombre}! Te hemos registrado."
        else:
            mensaje = "Por favor completa todos los campos."
    
    return render_template("inscripcion.html", mensaje=mensaje)



if __name__ == "__main__":


    app.run(debug=True)
