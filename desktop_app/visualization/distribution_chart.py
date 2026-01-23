import matplotlib.pyplot as plt


def plot_histogram(df, col: str, title: str):
    """
    Plot histogram for a numeric column.
    Expected column examples: math, english, literature
    """
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in DataFrame")

    values = df[col].dropna()

    if values.empty:
        raise ValueError(f"No valid data to plot histogram for '{col}'")

    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=10, edgecolor="black")
    plt.xlabel(col.capitalize())
    plt.ylabel("Count")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x_col: str, y_col: str, title: str):
    """
    Plot scatter chart between two numeric columns.
    Example: math vs english
    """
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Missing columns: {x_col}, {y_col}")

    clean_df = df[[x_col, y_col]].dropna()

    if clean_df.empty:
        raise ValueError("Not enough valid data to plot scatter chart")

    plt.figure(figsize=(7, 5))
    plt.scatter(clean_df[x_col], clean_df[y_col], alpha=0.7)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.title(title)
    plt.tight_layout()
    plt.show()
