# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    titulo = "Panel de inicio"
    usuario = "Kevin Gonzalez"
    mensaje = "Bienvenida a Flask"
    otro = "Tarea dos completada"
    edad= "17"
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html",
    titulo=titulo,
    usuario=usuario,
    mensaje=mensaje,
    otro=otro,
    edad=17)


@app.route("/acerca")
def acerca():
 
    return render_template("acerca.html")



@app.route("/contacto")
def contacto():
 
    return render_template("contacto.html")



@app.route("/recursos")
def recursos():
    recursos = [
    "Entorno virtual",
    "Rutas en Flask",
    "Plantillas HTML",
    "Variables con Jinja",
    "Verificación"
]
 
    return render_template("recursos.html",
    recursos=recursos)



if __name__ == "__main__":


    app.run(debug=True)
