import json

def save_to_text_file(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def load_from_text_file(file_path):
    """
    Load ALL data from JSON Lines file
    (used for pandas cleaning only)
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def load_page_from_text_file(file_path, page=1, page_size=10):
    start = (page - 1) * page_size
    end = start + page_size

    records = []
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i < start:
                continue
            if i >= end:
                break
            records.append(json.loads(line))
    return records


def count_records(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
