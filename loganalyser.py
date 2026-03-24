def analyse_logs(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            logs = file.readlines()

        failed_attempts = 0
        for line in logs:
            # Check for "failed login" keyword in each log entry
            if "failed login" in line.lower():
                failed_attempts += 1

        print(f"Total Failed Login Attempts: {failed_attempts}")

    except FileNotFoundError:
        print("Error: The log file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    # Provide the log file path
log_file_path = "sample_log.txt"  # Replace with the actual path
analyse_logs(log_file_path)