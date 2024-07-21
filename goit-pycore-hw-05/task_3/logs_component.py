class LogsParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load_logs(self) -> list:
        """
        Load a Log File and return list of parsed records.
        """
        logs = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    logs.append(self.parse_log_line(line.strip()))
        except FileNotFoundError:
            print(f"File {self.file_path} not found!")
        except Exception as e:
            print(f"An error occurred while loading logs: {e}")
        return logs

    @staticmethod
    def parse_log_line(line: str) -> dict:
        """
        Parse log line and return dict with components:
        date, time, level, message.
        """
        try:
            parts = line.split(" ", 3)
            if len(parts) < 4:
                raise ValueError(f"Invalid log line format: {line}")
            return {
                "date": parts[0],
                "time": parts[1],
                "level": parts[2],
                "message": parts[3],
            }
        except ValueError as e:
            print(e)
            return {}

    @staticmethod
    def filter_logs_by_level(logs: list, level: str) -> list:
        """
        Filter log records by level.
        """
        try:
            return [log for log in logs if log["level"] == level]
        except KeyError as e:
            print(f"Error while filtering logs: {e}")
            return []

    @staticmethod
    def count_logs_by_level(logs: list) -> dict:
        """
        Count logs records for each log level.
        """
        counts = {}
        try:
            for log in logs:
                level = log.get("level")
                if level:
                    counts[level] = counts.get(level, 0) + 1
                else:
                    raise KeyError(f"Missing 'level' in log record: {log}")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred while counting logs: {e}")
        return counts

    @staticmethod
    def display_log_counts(counts: dict):
        """
        Format and return results of records count by log level.
        """
        try:
            print(f"{'Log Level':<20} | {'Count':<10}")
            print("-" * 32)
            for level, count in counts.items():
                print(f"{level:<20} | {count:<10}")
        except Exception as e:
            print(f"An error occurred while displaying log counts: {e}")

    @staticmethod
    def display_filtered_logs(logs: list, level: str):
        """
        Display detailed information regarding records by level.
        """
        try:
            print(f"\nLogs Details for Level '{level}':")
            for log in logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        except KeyError as e:
            print(f"Error while displaying logs: {e}")
        except Exception as e:
            print(f"An error occurred while displaying logs: {e}")
