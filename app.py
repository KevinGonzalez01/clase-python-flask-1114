# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html")


@app.route("/dos")
def dos():
    titulo = "Panel de inicio"
    usuario = "Ana"
    mensaje = "Bienvenida a Flask"
 
    return render_template("dos.html",
    titulo=titulo,
    usuario=usuario,
    mensaje=mensaje
    )



@app.route("/tres")
def tres():
 
    return render_template("tres.html")


@app.route("/cuatro")
def cuatro():
 
    return render_template("cuatro.html")



@app.route("/cinco")
def cinco():
 
    return render_template("cinco.html")



if __name__ == "__main__":


    app.run(debug=True)
