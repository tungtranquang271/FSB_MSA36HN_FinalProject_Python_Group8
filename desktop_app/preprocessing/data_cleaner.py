import pandas as pd


def clean_student_data(raw_data):
    df = pd.DataFrame(raw_data)

    # normalize columns
    df.columns = df.columns.str.lower().str.strip()

    # rename from backend fields -> frontend standard fields
    rename_map = {
        "math": "math_score",
        "english": "english_score",
        "literature": "literature_score",
    }
    df = df.rename(columns=rename_map)

    # ensure required columns exist (create if missing)
    for col in ["student_id", "first_name", "last_name", "email", "date_of_birth", "hometown",
                "math_score", "english_score", "literature_score"]:
        if col not in df.columns:
            df[col] = None

    # convert scores to numeric
    for col in ["math_score", "english_score", "literature_score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # clean hometown
    df["hometown"] = df["hometown"].astype(str).str.strip()
    df.loc[df["hometown"].isin(["None", "nan", ""]), "hometown"] = None
    df = df.dropna(subset=["hometown"])

    return df
