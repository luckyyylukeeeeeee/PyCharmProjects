import timeit
from codecarbon import OfflineEmissionsTracker
from pympler import asizeof

# -------------------------- Kod från AI -------------------------------
# ================================
#   ADJACENCY LIST IMPLEMENTATION
# ================================
class GraphAdjList:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj = None

    def initialize_list(self):
        """Skapa n stycken noder utan kanter. Mäter O(n)."""
        self.adj = {i: [] for i in range(self.num_nodes)}

    def add_edge(self, u, v):
        """Lägg till kant utan att kontrollera om den redan finns. O(1) per kant."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def build_graph(self, edges):
        """Lägg till alla kanter. O(k) för k kanter."""
        for u, v in edges:
            self.add_edge(u, v)

    def has_edge(self, u, v):
        """Kontrollera om kanten finns. I värsta fall O(d), där d är graden för nod u."""
        return v in self.adj[u]

# ================================
#   ADJACENCY MATRIX IMPLEMENTATION
# ================================
class GraphAdjMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = None

    def initialize_matrix(self):
        """Skapa n x n matris med 0:or (O(n^2))"""
        self.matrix = [[0]*self.num_nodes for _ in range(self.num_nodes)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def has_edge(self, u, v):
        """Kontrollera om kanten finns (O(1))"""
        return self.matrix[u][v] == 1

    def build_graph(self, edges):
        """Lägg till kanter efter init"""
        for u, v in edges:
            self.add_edge(u, v)


# ===================================
#   GENERATE RANDOM GRAPH
# ===================================
def generate_random_graph(num_nodes, edge_probability):
    import random
    edges = []
    expected_edges = int(num_nodes*(num_nodes-1)/2 * edge_probability)
    for _ in range(expected_edges):
        u = random.randint(0, num_nodes-1)
        v = random.randint(0, num_nodes-1)
        if u != v:
            edges.append((u,v))
    return edges

# -------------------------- Kod från AI -------------------------------


# ----------------------------
# ----- Testkod --------------
# ----------------------------
if __name__ == "__main__":
    n = 1000
    k = 0
    rand_edges = generate_random_graph(n, k)
    n_1 = 320
    n_2 = 999

    # ----------------------------
    # ----- Energianvädning ------
    # ----------------------------
    tracker = OfflineEmissionsTracker(
        project_name="helloworld",
        country_iso_code="SWE",
        log_level="error",
        save_to_file=False
    )

    # --- GRANNLISTA ---
    tracker.start_task()
    adj_list = GraphAdjList(n)
    adj_list.initialize_list()
    adj_list.build_graph(rand_edges)
    co2_list = tracker.stop_task()

    # --- GRANNMATRIS ---
    tracker.start_task()
    adj_matrix = GraphAdjMatrix(n)
    adj_matrix.initialize_matrix()
    adj_matrix.build_graph(rand_edges)
    co2_matrix = tracker.stop_task()

    print(f"Grannlista: {co2_list.emissions * 1000} g")
    print(f"Grannmatris: {co2_matrix.emissions * 1000} g")

    # ----------------------------
    # ----- Tidskomplexitet ------
    # ----------------------------

    # --- GRANNLISTA ---
    time_list_init = timeit.timeit(lambda: adj_list.initialize_list(), number=50)
    time_list_build = timeit.timeit(lambda: adj_list.build_graph(rand_edges), number=50)
    time_list_add = timeit.timeit(lambda: adj_list.add_edge(n_1, n_2), number=50)
    time_list_has_edge = timeit.timeit(lambda: adj_list.has_edge(n_1, n_2), number=50)

    print("Grannlista:")
    print("Initiera rymdkartan (grafen) med ENDAST planeter (noder):", round(time_list_init / 50, 10), "sek")
    print("Initiera rymdkartan (grafen) med planeter (noder) + resevägar (kanter):", round(time_list_build / 50, 10), "sek")
    print("Lägg till kant:", round(time_list_add / 50, 10), "sek")
    print("Kolla om reseväg finns (kant):", round(time_list_has_edge / 50, 10), "sek")

    # --- GRANNMATRIS ---
    time_matrix_init = timeit.timeit(lambda: adj_matrix.initialize_matrix(), number=50)
    time_matrix_build = timeit.timeit(lambda: adj_matrix.build_graph(rand_edges), number=50)
    time_matrix_add = timeit.timeit(lambda: adj_matrix.add_edge(n_1, n_2), number=50)
    time_matrix_has_edge = timeit.timeit(lambda: adj_matrix.has_edge(n_1, n_2), number=50)

    print("\nGrannmatris:")
    print("Initiera rymdkartan (grafen) med ENDAST planeter (noder):", round(time_matrix_init / 50, 10), "sek")
    print("Initiera rymdkartan (grafen) med planeter (noder) + resevägar (kanter):", round(time_matrix_build / 50, 10), "sek")
    print("Lägg till reseväg (kant):", round(time_matrix_add / 50, 10), "sek")
    print("Kolla om reseväg finns (kant):", round(time_matrix_has_edge / 50, 10), "sek")

    # ----------------------------
    # ----- Minnesåtgång ---------
    # ----------------------------

    # --- GRANNLISTA ---
    list_memory = asizeof.asizeof(adj_list.adj)
    print(f"Adjacency list memory: {list_memory} bytes")

    # --- GRANNMATRIS ---
    matrix_memory = asizeof.asizeof(adj_matrix.matrix)
    print(f"Adjacency matrix memory: {matrix_memory} bytes")
    # Hittar objektets direkta storlek via sys.getsizeof().Går igenom alla refererade objekt och returnerar totalen i bytes!
