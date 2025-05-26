from collections import Counter
from pathlib import Path


def filter_ips(input_file_path: str, output_file_path: str, allowed_ips: list[str]) -> None:
    input_path = Path(input_file_path)
    output_path = Path(output_file_path)
    ip_counter = Counter()

    try:
        with input_path.open("r", encoding="utf-8") as infile:
            for line in infile:
                ip = line.strip().split()[0]
                if ip in allowed_ips:
                    ip_counter[ip] += 1
    except FileNotFoundError:
        print(f"Error: Input file not found - {input_file_path}")
        return
    except OSError:
        print(f"Error: Could not read from input file - {input_file_path}")
        return

    try:
        with output_path.open("w", encoding="utf-8") as outfile:
            for ip, count in ip_counter.items():
                outfile.write(f"{ip}: {count}\n")
    except OSError:
        print(f"Error: Could not write to output file - {output_file_path}")



if __name__ == "__main__":
    allowed = ["83.149.9.216", "121.107.188.202", "50.180.79.170", "208.115.111.72"]

    filter_ips("apache_logs.txt", "filtered_output.txt", allowed)

    print("Filtered IP counts:")
    print(Path("filtered_output.txt").read_text(encoding="utf-8"))
