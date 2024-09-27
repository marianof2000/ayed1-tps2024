"""Librería de SO"""

import os
from typing import List


def leer(archivo: str) -> List[List[str]]:
    """Lee todos los datos dentro del CSV con los repos de los alumnos"""
    datos = []
    try:
        with open(archivo, "rt", encoding="utf-8") as f:
            datos = [linea.strip().split(",") for linea in f]
    except Exception as e:
        print(e)
    return datos


def clonar_repos(lista: List[List[str]]) -> None:
    """Clona a disco todos los repos de los alumnos"""
    for repo in lista:
        os.system(f"git clone {repo[2]} {''.join(repo[1].title().split())}")


def actualizar_repos(ruta: str) -> None:
    """Recorre todos los repos de los alumnos y busca actualizaciones"""
    repos = [
        os.path.join(ruta, d)
        for d in os.listdir(ruta)
        if (os.path.isdir(os.path.join(ruta, d)) and not d.startswith("."))
    ]

    for repo in sorted(repos):
        print(repo.split("/")[-1])
        os.chdir(repo)
        os.system("git pull -v")
        print()


def opciones() -> None:
    """Muestra el menú con las opciones"""
    ops = ("Clonar repositorios", "Actualizar repositorios", "Salir")
    print()
    print("Opciones")
    for i, op in enumerate(ops, start=1):
        print(f"{i} - {op}")


def menu() -> None:
    """Muestra el menú con las opciones"""
    ruta = os.path.dirname(os.path.abspath(__file__))
    while True:
        opciones()
        op = input("Ingrese una de las siguientes opciones: ")
        if op == "1":
            if not ruta:
                continue
            repos = leer(os.path.join(ruta, "repos.csv"))[1:]
            if repos:
                clonar_repos(repos)
                print("Repositorios clonados")
            else:
                print("No hay repositorios para clonar")
        elif op == "2":
            if ruta:
                actualizar_repos(ruta)
        elif op == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


def main() -> None:
    """Función principal"""
    menu()


if __name__ == "__main__":
    main()
