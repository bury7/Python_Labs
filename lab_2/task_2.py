import hashlib
from pathlib import Path


def generate_file_hashes(*file_paths: str) -> dict[str, str]:
    file_hashes = {}

    for file_path in file_paths:
        path = Path(file_path)
        try:
            sha256_hash = hashlib.sha256()
            with path.open("rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    sha256_hash.update(chunk)
            file_hashes[file_path] = sha256_hash.hexdigest()
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except OSError:
            print(f"Error: Could not read file - {file_path}")

    return file_hashes


def main() -> None:
    hashes = generate_file_hashes("apache_logs.txt", "README.md")
    print("Generated hash for files:")
    for path, hash_value in hashes.items():
        print(f"{path}: {hash_value}")


if __name__ == "__main__":
    main()
