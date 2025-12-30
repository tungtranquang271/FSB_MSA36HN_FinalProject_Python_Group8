import pandas as pd


def average_math_english_by_hometown(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"hometown", "math_score", "english_score"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    out = (
        df.groupby("hometown")[["math_score", "english_score"]]
        .mean()
        .reset_index()
        .sort_values("hometown")
    )
    return out


def average_all_subjects_by_hometown(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"hometown", "math_score", "english_score", "literature_score"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    out = (
        df.groupby("hometown")[["math_score", "english_score", "literature_score"]]
        .mean()
        .reset_index()
        .sort_values("hometown")
    )
    return out


def subject_difficulty(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"math_score", "english_score", "literature_score"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    avg_math = df["math_score"].mean()
    avg_eng = df["english_score"].mean()
    avg_lit = df["literature_score"].mean()

    out = pd.DataFrame(
        {
            "subject": ["Math", "English", "Literature"],
            "average_score": [avg_math, avg_eng, avg_lit],
        }
    ).sort_values("average_score")  # thấp nhất = khó nhất
    return out


def correlation_math_english(df: pd.DataFrame) -> float:
    needed = {"math_score", "english_score"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    clean = df[["math_score", "english_score"]].dropna()
    if len(clean) < 2:
        raise ValueError("Not enough data to compute correlation.")
    return float(clean["math_score"].corr(clean["english_score"]))


def top_students_by_subject(df: pd.DataFrame, subject: str, limit: int = 5) -> pd.DataFrame:
    subject_map = {
        "math": "math_score",
        "english": "english_score",
        "literature": "literature_score",
    }
    if subject not in subject_map:
        raise ValueError("subject must be one of: math, english, literature")

    col = subject_map[subject]
    needed = {col, "student_id", "first_name", "last_name"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    temp = df[[ "student_id", "first_name", "last_name", col ]].dropna().copy()
    temp["full_name"] = temp["first_name"].astype(str).str.strip() + " " + temp["last_name"].astype(str).str.strip()
    temp = temp.rename(columns={col: "score"})
    out = temp.sort_values("score", ascending=False).head(limit)[["student_id", "full_name", "score"]]
    return out

def performance_level_distribution(df: pd.DataFrame, subject: str = "english") -> pd.DataFrame:
    subject_map = {
        "math": "math_score",
        "english": "english_score",
        "literature": "literature_score",
    }

    if subject not in subject_map:
        raise ValueError("subject must be one of: math, english, literature")

    col = subject_map[subject]

    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

    scores = df[col].dropna()

    def classify(score):
        if score < 5:
            return "Weak"
        elif score < 7:
            return "Average"
        elif score < 8:
            return "Good"
        else:
            return "Excellent"

    levels = scores.apply(classify)

    result = (
        levels.value_counts()
        .reindex(["Weak", "Average", "Good", "Excellent"], fill_value=0)
        .reset_index()
    )

    result.columns = ["performance_level", "count"]
    return result