# Log Analyzer - flags IPs with too many failed login attempts (possible brute force)
# by Sharon Sara George

LOG_FILE = "sample_auth.log"
FAILED_LOGIN_KEYWORD = "Failed password"
THRESHOLD = 5


def analyze_log(file_path):
    failed_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            if FAILED_LOGIN_KEYWORD not in line:
                continue

            words = line.split()
            if "from" not in words:
                continue

            ip = words[words.index("from") + 1]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    return failed_attempts


def report(failed_attempts, threshold):
    print("\n===== LOG ANALYSIS REPORT =====\n")

    if not failed_attempts:
        print("No failed login attempts found.")
        return

    for ip, count in failed_attempts.items():
        tag = "ALERT" if count >= threshold else "OK"
        print(f"[{tag}] {ip} -> {count} failed attempts")

    print("\n================================\n")


if __name__ == "__main__":
    results = analyze_log(LOG_FILE)
    report(results, THRESHOLD)
