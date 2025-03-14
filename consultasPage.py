import flet as ft

import ddbb


def main(page: ft.Page):
    page.title = "Consultas"

    # Consultar y cargar todos los arboles
    def consultar_arboles():
        arboles = ddbb.consultar_arboles() # Estos son los datos
        cargar_tabla(arboles)
        page.update()

    # Datos de la lista de arboles
    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))), # ID
                ft.DataCell(ft.Text(fila[1])), # Nombre
                ft.DataCell(ft.Text(fila[2])), # Tipo
                ft.DataCell(ft.Text(str(fila[3]))), # Altura
                ft.DataCell(ft.Text(str(fila[4]))), # Fecha
            ]))

    def buscar_arboles(e):
        lista_arboles = ddbb.consultar_arboles_por_nombre(nombre_tf.value)
        cargar_tabla(lista_arboles)
        page.update()

    # OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", on_click=buscar_arboles, width=300)
    tabla = ft.DataTable(bgcolor="blue",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Altura")),
            ft.DataColumn(ft.Text("Fecha")),
        ]
    )

    columna_datos = ft.Column(
        controls=[
            ft.Text("CONSULTAS", size=40),
            nombre_tf,
            buscar_btn,
            tabla,
        ]
    )

    # page.add(columna_datos)
    consultar_arboles()

    return consultar_arboles