import sys

from logs_component import LogsParser as Logs


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        return
    file_path = sys.argv[1]
    log_parser = Logs(file_path=file_path)
    logs = log_parser.load_logs()

    if not logs:
        raise Exception("The Logs file is empty!")

    log_counts = log_parser.count_logs_by_level(logs)
    log_parser.display_log_counts(log_counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = log_parser.filter_logs_by_level(logs, level)
        log_parser.display_filtered_logs(filtered_logs, level)


if __name__ == "__main__":
    main()
