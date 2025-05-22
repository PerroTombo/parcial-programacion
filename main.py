from pelicula import Pelicula

def main():
    pelicula1 = Pelicula(
        codigo=1602,
        titulo="Interstellar",
        duracion=169,
        director="Christopher Nolan",
        prestada=False
    )

    print(pelicula1)
    
if __name__ == "__main__":
    main()