import matplotlib.pyplot as plt
import numpy as np


def plot_grouped_math_english_by_hometown(df):
    """
    df columns: hometown, math_score, english_score
    """
    hometowns = df["hometown"].tolist()
    math_scores = df["math_score"].tolist()
    english_scores = df["english_score"].tolist()

    x = np.arange(len(hometowns))
    width = 0.38

    plt.figure(figsize=(11, 6))
    plt.bar(x - width / 2, math_scores, width, label="Math")
    plt.bar(x + width / 2, english_scores, width, label="English")

    plt.xlabel("Hometown")
    plt.ylabel("Average Score")
    plt.title("Average Math vs English by Hometown")
    plt.xticks(x, hometowns, rotation=25, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_grouped_all_subjects_by_hometown(df):
    """
    df columns: hometown, math_score, english_score, literature_score
    """
    hometowns = df["hometown"].tolist()
    math_scores = df["math_score"].tolist()
    english_scores = df["english_score"].tolist()
    literature_scores = df["literature_score"].tolist()

    x = np.arange(len(hometowns))
    width = 0.26

    plt.figure(figsize=(12, 6))
    plt.bar(x - width, math_scores, width, label="Math")
    plt.bar(x, english_scores, width, label="English")
    plt.bar(x + width, literature_scores, width, label="Literature")

    plt.xlabel("Hometown")
    plt.ylabel("Average Score")
    plt.title("Average Scores by Hometown (All Subjects)")
    plt.xticks(x, hometowns, rotation=25, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_subject_difficulty(df):
    """
    df columns: subject, average_score
    Lower average score = harder subject
    """

    subjects = df["subject"].tolist()
    scores = df["average_score"].tolist()

    colors = ["#4C72B0", "#DD8452", "#55A868"]  # blue, orange, green

    plt.figure(figsize=(7, 5))
    bars = plt.bar(subjects, scores, color=colors)

    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.title("Subject Difficulty (Lower = Harder)")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.ylim(0, 10)
    plt.tight_layout()
    plt.show()


def plot_top_students(df, subject_label: str):
    """
    df columns: student_id, full_name, score
    """
    labels = df["full_name"].tolist()
    scores = df["score"].tolist()

    plt.figure(figsize=(9, 5))
    plt.barh(labels, scores)
    plt.xlabel("Score")
    plt.title(f"Top Students - {subject_label}")
    plt.tight_layout()
    plt.show()

def plot_performance_level(df, subject_label: str):
    levels = df["performance_level"].tolist()
    counts = df["count"].tolist()

    colors = ["#C44E52", "#4C72B0", "#DD8452", "#55A868"]  # red, blue, orange, green

    plt.figure(figsize=(7, 5))
    bars = plt.bar(levels, counts, color=colors)

    plt.xlabel("Performance Level")
    plt.ylabel("Number of Students")
    plt.title(f"Student Performance Distribution ({subject_label})")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.2,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()
    plt.show()
