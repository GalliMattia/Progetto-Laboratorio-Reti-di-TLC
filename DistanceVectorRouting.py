class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {name: 0}  # Distanza da sé stesso è 0
        self.neighbors = {}  # Vicini diretti e i loro costi

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor.name] = cost
        self.routing_table[neighbor.name] = cost

    def update_routing_table(self):
        updated = False
        for neighbor_name, cost_to_neighbor in self.neighbors.items():
            neighbor = nodes[neighbor_name]
            for destination, neighbor_cost in neighbor.routing_table.items():
                new_cost = cost_to_neighbor + neighbor_cost
                if destination not in self.routing_table or new_cost < self.routing_table[destination]:
                    self.routing_table[destination] = new_cost
                    updated = True
        return updated

    def __str__(self):
        table = f"Routing Table for {self.name}:\n"
        for dest, cost in self.routing_table.items():
            table += f"  To {dest}: Cost {cost}\n"
        return table

# Creazione dei nodi
nodes = {
    "A": Node("A"),
    "B": Node("B"),
    "C": Node("C"),
    "D": Node("D")
}

# Configurazione dei vicini
nodes["A"].add_neighbor(nodes["B"], 1)
nodes["A"].add_neighbor(nodes["C"], 4)
nodes["B"].add_neighbor(nodes["A"], 1)
nodes["B"].add_neighbor(nodes["C"], 2)
nodes["B"].add_neighbor(nodes["D"], 6)
nodes["C"].add_neighbor(nodes["A"], 4)
nodes["C"].add_neighbor(nodes["B"], 2)
nodes["C"].add_neighbor(nodes["D"], 3)
nodes["D"].add_neighbor(nodes["B"], 6)
nodes["D"].add_neighbor(nodes["C"], 3)

# Simulazione degli aggiornamenti di routing
def simulate_routing():
    print("Inizio della simulazione del protocollo di routing...\n")
    converged = False
    iteration = 0

    while not converged:
        print(f"Iterazione {iteration + 1}:\n")
        converged = True
        for node in nodes.values():
            if node.update_routing_table():
                converged = False
        for node in nodes.values():
            print(node)
        iteration += 1

    print("\nLa rete ha raggiunto la convergenza.")

if __name__ == "__main__":
    simulate_routing()
