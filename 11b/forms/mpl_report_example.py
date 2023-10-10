import matplotlib.pyplot as plt

def generate_plot(filename):
    plt.plot([1, 2, 3, 4])
    plt.ylabel('Some report values')
    plt.savefig(filename)

generate_plot("example.png")
