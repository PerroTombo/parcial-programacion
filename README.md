Este trabajo permite identificar las peliculas clasificándolas por un código ya predefinido, utilizando conceptos para programación orientada a objetos (POO)

La clase Pelicula permite:

- Registrar una película con:
  - Código
  - Título
  - Duración
  - Director
  - Estado de préstamo (sí o no)
- Prestar o devolver una película.
- Calcular el costo de reproducción (según tarifa/minuto).
- Comparar dos películas por su código único.

1. Asegúrate de tener Python 3 instalado.
2. Descarga los archivos.
3. Ejecutar 

Código main.py

pelicula1 = Pelicula(
    codigo=1602,
    titulo="Interstellar",
    duracion=169,
    director="Christopher Nolan",
    prestada=False
)
print(pelicula1)

Salida esperada

La película 1602 titulada Interstellar dirigida por Christopher Nolan dura 169 minutos y no está prestado

Autor
- Felipe Marin Zuluaga
- Uniminuto
- Programación Orientada a Objetos  Segundo Corte  Parcial
- 2025  


