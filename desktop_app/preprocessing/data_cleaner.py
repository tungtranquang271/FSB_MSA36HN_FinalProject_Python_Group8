import pandas as pd
from storage.file_storage import load_from_text_file, save_to_text_file

RAW_FILE = "students_raw.txt"
CLEAN_FILE = "students_clean.txt"


def clean_and_save_students():
    # =====================
    # 1. Load RAW data
    # =====================
    df = pd.DataFrame(load_from_text_file(RAW_FILE))

    # =====================
    # 2. Sort & remove duplicate
    # =====================
    if "student_id" in df.columns:
        df = df.sort_values("student_id")
        df = df.drop_duplicates("student_id", keep="last")

    # =====================
    # 3. Type casting (SAFE)
    # =====================
    if "date_of_birth" in df.columns:
        df["date_of_birth"] = pd.to_datetime(
            df["date_of_birth"], errors="coerce"
        )

    score_cols = [c for c in ["math", "literature", "english"] if c in df.columns]
    for c in score_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # =====================
    # 4. Handle missing values
    # =====================

    # ---- hometown ----
    if "hometown" in df.columns and df["hometown"].notna().any():
        df["hometown"] = df["hometown"].fillna(
            df["hometown"].mode()[0]
        )

    # ---- fill score by hometown mean ----
    if "hometown" in df.columns and score_cols:
        df[score_cols] = (
            df.groupby("hometown")[score_cols]
              .transform(lambda x: x.fillna(x.mean()))
        )

    # ---- fallback global mean ----
    if score_cols:
        df[score_cols] = df[score_cols].fillna(
            df[score_cols].mean()
        )

    # ---- round scores to 2 decimals ----
    if score_cols:
        df[score_cols] = df[score_cols].round(2)

    # =====================
    # 5. Drop invalid records
    # =====================
    required = [
        c for c in ["student_id", "first_name", "last_name"]
        if c in df.columns
    ]

    if required:
        df = df[df[required].notna().all(axis=1)]

    # =====================
    # 6. Datetime → string (JSON SAFE)
    # =====================
    if "date_of_birth" in df.columns:
        df["date_of_birth"] = df["date_of_birth"].dt.strftime("%Y-%m-%d")

    # =====================
    # 7. Save CLEAN data
    # =====================
    save_to_text_file(df.to_dict(orient="records"), CLEAN_FILE)

    return df


if __name__ == "__main__":
    clean_and_save_students()
