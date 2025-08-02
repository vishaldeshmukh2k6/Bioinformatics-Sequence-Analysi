import matplotlib.pyplot as plt

def plot_gc_content(gc_contents):
    plt.hist(gc_contents, bins=20, color='green', alpha=0.7)
    plt.xlabel('GC Content')
    plt.ylabel('Frequency')
    plt.title('GC Content Distribution')
    plt.show()
