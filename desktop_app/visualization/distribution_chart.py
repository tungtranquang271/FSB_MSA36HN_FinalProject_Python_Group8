import matplotlib.pyplot as plt


def plot_histogram(df, col: str, title: str):
    values = df[col].dropna().tolist()

    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=10)
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x_col: str, y_col: str, title: str):
    x = df[x_col]
    y = df[y_col]

    plt.figure(figsize=(7, 5))
    plt.scatter(x, y)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.tight_layout()
    plt.show()
