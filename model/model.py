import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self.nodi = []

    def buildGraph(self, durata):
        self.nodi = DAO.getAllNodi(durata)
        self._grafo.add_nodes_from(self.nodi)

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)