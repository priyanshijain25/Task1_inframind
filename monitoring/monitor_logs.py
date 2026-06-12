import requests
import json
import time

LOKI_URL = "http://localhost:3100/loki/api/v1/query_range"
QUERY = '{app="employee-api"}'

seen_logs = set()
OUTPUT_FILE = "error_warning_logs.txt"

def get_logs():
    response = requests.get(
        LOKI_URL,
        params={
            "query": QUERY,
            "limit": 5
        }
    )

    response.raise_for_status()

    return response.json()


def main():

    while True:

        data = get_logs()

        print("\n===== Latest Logs =====\n")

        for stream in data["data"]["result"]:
            for timestamp, log in stream["values"]:

                if timestamp in seen_logs:
                    continue
                seen_logs.add(timestamp)
                log_data = json.loads(log)
                print(log_data)

                message = log_data["log"].strip()
                log_time = log_data["time"]

                message_upper = message.upper()

                if (
                    message_upper.startswith("ERROR")
                    or message_upper.startswith("WARNING")
                ):

                    alert_message = f"[{log_time}] {message}"

                    print(f"ALERT: {alert_message}")

                    with open(OUTPUT_FILE, "a") as f:
                        f.write(alert_message + "\n")

        time.sleep(5)


if __name__ == "__main__":
    main()