import datetime
import os
import random
import time
import json


def generate_accuracy_data():
    utc_now = datetime.datetime.utcnow()
    timestamp = utc_now - datetime.timedelta(hours=5)
    pid = str(random.randint(100000, 999999))  # PID
    accuracy = random_number = round(random.uniform(50, 100), 2)
    return {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"), "pid": pid, "accuracy": accuracy}


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    acc_data = []
    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time.total_seconds() > 10:
            break

        acc_data.append(generate_accuracy_data())
        time.sleep(1)

    # os.makedirs(os.path.dirname(f'/Users/neeleshkarthikeyan/Library/CloudStorage/OneDrive-IndianaUniversity/research_assistanship/cep_engine/logs/acc.json'), exist_ok=True)
    # os.makedirs(os.path.dirname(f'logs/acc.json'), exist_ok=True)
    with open(f'logs/acc.json', 'w') as file:
        json.dump(acc_data, file, indent=4)
