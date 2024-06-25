import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        numero = self._view.txt_durata.value
        if numero is None:
            self._view.create_alert("Non hai inserito nessun numero")
            return
        try:
            durata = int(numero)
        except ValueError:
            self._view.create_alert("Valore inserito non corretto!")
            return
        self._model.buildGraph(durata)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))
        self._view.update_page()

    def handle_adiacenze(self, e):
        pass