import sys
from pathlib import Path
from collections import Counter


def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0], 
        'time': parts[1], 
        'level': parts[2],
        'message': parts[3].strip()
        }


def load_logs(file_path: str) -> list:
    file_path = Path(file_path)
    logs = []
    try:
        with open(file_path, "r", encoding='utf-8') as fh:
            for line in fh:
                logs.append(parse_log_line(line))
        return logs
    except FileNotFoundError:
        print("Файл не знайдений")
        sys.exit()


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log['level'].lower() == level.lower()]
    if not filtered_logs:
        print(f"\nНемає файлу з рівнем: '{level.upper()}'")
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    return Counter([log['level'] for log in logs])


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")



def main():
    if len(sys.argv) < 2:
        print("Неправильно введені аргументи. Використання: python main.py /path/to/logfile.log [level]")
        sys.exit()


    log_file_path = sys.argv[1]
    log_file_extension = Path(log_file_path).suffix

    if log_file_extension != '.log':
        print("Має бути log файл (.log)")
        sys.exit()

    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)

    level = sys.argv[2] if len(sys.argv) > 2 else None

    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")



if __name__ == "__main__":
    main()
