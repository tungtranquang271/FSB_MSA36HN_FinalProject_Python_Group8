import json

def save_to_text_file(data, file_path):
    """
    Save crawled data to text file (JSON Lines)
    """
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def load_from_text_file(file_path):
    """
    Load data from text file
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data
