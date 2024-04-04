import datetime
import os
import random
import time
import json  # Import json for easy data serialization


def generate_cpu_data():
    utc_now = datetime.datetime.utcnow()
    timestamp = utc_now - datetime.timedelta(hours=5)
    wattage = round(random.uniform(1.0, 10.0), 6)  # power in Watts
    pid = str(random.randint(100000, 999999))  # PID
    process = random.choice(["python_1", "python_2", "python_3", "python_4", "python_5"])  # process name
    return {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"), "watt": wattage, "pid": pid, "process": process}


def generate_gpu_data():
    utc_now = datetime.datetime.utcnow()
    timestamp = utc_now - datetime.timedelta(hours=5)
    wattage = round(random.uniform(1.0, 10.0), 6)
    return {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"), "watt": wattage}


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    cpu_data = []
    gpu_data = []
    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time.total_seconds() > 10:
            break

        cpu_data.append(generate_cpu_data())
        gpu_data.append(generate_gpu_data())
        time.sleep(1)

    cpu_file_name = f'logs/cpu.json'
    os.makedirs(os.path.dirname(cpu_file_name), exist_ok=True)
    with open(cpu_file_name, 'w') as file:
        json.dump(cpu_data, file, indent=4)

    gpu_file_name = f'logs/gpu.json'
    os.makedirs(os.path.dirname(gpu_file_name), exist_ok=True)
    with open(gpu_file_name, 'w') as file:
        json.dump(gpu_data, file, indent=4)
