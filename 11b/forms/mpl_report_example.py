import matplotlib.pyplot as plt

def generate_plot(filename):
    plt.plot([1, 2, 3, 4])
    plt.ylabel('Некоторые значения')
    plt.savefig(filename)

generate_plot("example.png")
