import re
from collections import defaultdict
from pathlib import Path


def analyze_log_file(log_file_path: str) -> dict:
    status_codes = defaultdict(int)
    path = Path(log_file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                match = re.search(r'"\s(\d{3})\s', line)
                if match:
                    code = match.group(1)
                    status_codes[code] += 1
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except OSError:
        print(f"Error: An error occurred while reading the file '{log_file_path}'.")

    return dict(status_codes)


if __name__ == "__main__":
    result = analyze_log_file("apache_logs.txt")
    print("HTTP response code counts:")
    for code, count in result.items():
        print(f"{code}: {count}")
