import pandas as pd


def clean_student_data(raw_data):
    df = pd.DataFrame(raw_data)

    # normalize columns
    df.columns = df.columns.str.lower().str.strip()

    # rename from backend fields -> standard fields
    rename_map = {
        "math": "math_score",
        "english": "english_score",
        "literature": "literature_score",
    }
    df = df.rename(columns=rename_map)

    # ensure required columns exist
    required_cols = [
        "student_id", "first_name", "last_name",
        "email", "date_of_birth", "hometown",
        "math_score", "english_score", "literature_score"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None

    # convert scores to numeric (null nếu không hợp lệ)
    score_cols = ["math_score", "english_score", "literature_score"]
    for col in score_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # clean hometown (KHÔNG drop sinh viên)
    df["hometown"] = df["hometown"].astype(str).str.strip()
    df.loc[df["hometown"].isin(["None", "nan", ""]), "hometown"] = None

    # ✅ HANDLE DUPLICATE: unique by student_id
    if "student_id" in df.columns:
        df = df.drop_duplicates(subset=["student_id"], keep="last")

    return df
