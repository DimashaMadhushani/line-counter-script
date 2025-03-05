import sys
import os
import datetime
import json

def count_lines(file_path):
    """Counts the number of non-empty lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            non_empty_lines = [line for line in file if line.strip()]  # Ignore empty lines
            return len(non_empty_lines)
    except Exception as e:
        return f"Error processing {file_path}: {str(e)}"

def log_result(file_path, line_count):
    """Logs the result in a structured JSON-like format."""
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "file": os.path.basename(file_path),
        "line_count": line_count
    }

    with open("file_processing.log", "a", encoding='utf-8') as log_file:
        log_file.write(json.dumps(log_entry) + "\n")  # Store logs in JSON format

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python line_counter.py <file1> <file2> ...")
        sys.exit(1)

    for file_path in sys.argv[1:]:  # Process multiple files
        if os.path.isfile(file_path):
            line_count = count_lines(file_path)
            log_result(file_path, line_count)
            print(f"Processed {file_path}: {line_count} lines")
        else:
            print(f"Skipping {file_path}: File not found")
