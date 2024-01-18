import matplotlib.pyplot as plt
import networkx as nx

def turtle_steps(N, m, n):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    intermediate_results = []

    for i in range(1, N + 1):
        intermediate_results.append(dp.copy())

        if i - m >= 0:
            dp[i] = min(dp[i], dp[i - m] + 1)
        if i - n >= 0:
            dp[i] = min(dp[i], dp[i - n] + 1)

    return dp, intermediate_results

def plot_turtle_steps(N, m, n):
    final_result, intermediate_results = turtle_steps(N, m, n)

    G = nx.DiGraph()

    for i in range(len(intermediate_results) + 1):
        for j in range(N + 1):
            G.add_node((i, j), label=f'Step {i}\nDepth {j}\nDays {intermediate_results[i-1][j]}')

    for i in range(len(intermediate_results)):
        for j in range(N + 1):
            G.add_edge((i, j), (i+1, j-m), label=f'Move -{m}\nDays 1')
            G.add_edge((i, j), (i+1, j-n), label=f'Move -{n}\nDays 1')

    pos = {(i, j): (i, -j) for i, j in G.nodes}
    labels = nx.get_edge_attributes(G, 'label')
    #edge_labels = {k: v for k, v in labels.items() if k[0] % 2 == 0}
    edge_labels = {k: v for k, v in labels.items() if isinstance(k[0], int) and k[0] % 2 == 0}


    print(final_result)

    plt.figure(figsize=(15, 10))
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

    plt.title('Dynamic Programming for Turtle Problem')
    plt.show()

# Приклад використання
N = 10  # глибина ями
m = 2   # висота, на яку можна підніматися
n = 3   # висота, на яку можна спускатися

plot_turtle_steps(N, m, n)
