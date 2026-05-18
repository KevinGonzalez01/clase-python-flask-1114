# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica
1. ¿Que problema concreto resuelve el entorno virtual en un proyecto Python?
---
El entorno virtual (.venv) resuelve el problema de las dependencias y versiones entre proyectos.
Permite que cada proyecto tenga sus propias librerías instaladas sin afectar al resto del sistema.
---
2. ¿Que diferencia hay entre instalar Flask globalmente y hacerlo dentro de .venv?

Instalar Flask globalmente lo deja disponible para toda la máquina. Instalarlo en .venv lo limita solo al proyecto actual.
3. ¿Por que requirements.txt forma parte del proyecto y no de tu maquina personal?
Requirements.txt pertenece al proyecto porque guarda las dependencias necesarias para ejecutar ese proyecto en cualquier entorno.
4. ¿Cuando ejecutas python app.py, que archivo actua como punto de entrada y por que?
El archivo app.py actúa como punto de entrada porque es el archivo que Python ejecuta primero.
5. ¿Que relacion hay entre la ruta /, la funcion inicio() y el archivo templates/index.html?
La ruta / llama a la función inicio(), y esa función devuelve templates/index.html al navegador.
6. ¿Que evidencia te da la terminal de que el servidor arranco correctamente?
La terminal muestra mensajes como: Running on http://127.0.0.1:5000
7. ¿Si cambias el HTML y el navegador muestra otra cosa, que te demuestra eso sobre el flujo entre backend y frontend en este proyecto?
Demuestra que Flask envía el HTML al navegador y que el frontend depende de lo que el backend renderiza.

## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
2. Las dependencias se instalaron desde `requirements.txt`.
3. La aplicacion corre en tu maquina y responde en el navegador.
4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
