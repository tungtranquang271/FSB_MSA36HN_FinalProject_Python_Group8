import pandas as pd

# =========================
# FIELD MAPPING (CLEAN DATA)
# =========================
MATH = "math"
ENGLISH = "english"
LITERATURE = "literature"


def average_math_english_by_hometown(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"hometown", MATH, ENGLISH}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return (
        df.groupby("hometown")[[MATH, ENGLISH]]
        .mean()
        .reset_index()
        .sort_values("hometown")
    )


def average_all_subjects_by_hometown(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"hometown", MATH, ENGLISH, LITERATURE}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return (
        df.groupby("hometown")[[MATH, ENGLISH, LITERATURE]]
        .mean()
        .reset_index()
        .sort_values("hometown")
    )


def subject_difficulty(df: pd.DataFrame) -> pd.DataFrame:
    needed = {MATH, ENGLISH, LITERATURE}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return pd.DataFrame({
        "subject": ["Math", "English", "Literature"],
        "average_score": [
            df[MATH].mean(),
            df[ENGLISH].mean(),
            df[LITERATURE].mean()
        ]
    }).sort_values("average_score")


def correlation_math_english(df: pd.DataFrame) -> float:
    needed = {MATH, ENGLISH}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    clean = df[[MATH, ENGLISH]].dropna()
    if len(clean) < 2:
        raise ValueError("Not enough data to compute correlation")

    return float(clean[MATH].corr(clean[ENGLISH]))


def top_students_by_subject(df: pd.DataFrame, subject: str, limit: int = 5):
    subject_map = {
        "math": MATH,
        "english": ENGLISH,
        "literature": LITERATURE,
    }

    if subject not in subject_map:
        raise ValueError("subject must be math | english | literature")

    col = subject_map[subject]

    needed = {"student_id", "first_name", "last_name", col}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    temp = df[["student_id", "first_name", "last_name", col]].dropna()
    temp["full_name"] = temp["first_name"] + " " + temp["last_name"]
    temp = temp.rename(columns={col: "score"})

    return temp.sort_values("score", ascending=False).head(limit)[
        ["student_id", "full_name", "score"]
    ]


def performance_level_distribution(df: pd.DataFrame, subject: str = "english"):
    subject_map = {
        "math": MATH,
        "english": ENGLISH,
        "literature": LITERATURE,
    }

    if subject not in subject_map:
        raise ValueError("subject must be math | english | literature")

    col = subject_map[subject]
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

    scores = df[col].dropna()

    def classify(x):
        if x < 5:
            return "Weak"
        elif x < 7:
            return "Average"
        elif x < 8:
            return "Good"
        return "Excellent"

    result = (
        scores.apply(classify)
        .value_counts()
        .reindex(["Weak", "Average", "Good", "Excellent"], fill_value=0)
        .reset_index()
    )

    result.columns = ["performance_level", "count"]
    return result
