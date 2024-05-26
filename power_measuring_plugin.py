import datetime
import os
import random
import time
import json  # Import json for easy data serialization
import threading


# Function to load pname_map from metadata.json
def load_pname_map(file_path):
    with open(file_path, 'r') as file:
        metadata = json.load(file)

    pname_map = {}
    for plugin in metadata.get("plugins", []):
        pname_map[plugin["name"]] = plugin["pids"]

    return pname_map


# Load pname_map from metadata.json
pname_map = load_pname_map('metadata.json')


# Define the get_pname function
def get_pname(pid):
    pid_map = {pid: pname for pname, pids in pname_map.items() for pid in pids}
    return pid_map.get(pid)

# server_id, plugin_name, type (cpu, gpu), value, process_id, timestamp
def generate_power_data():
    pid = random.choice([2437322, 3423844, 4737228, 5434722, 5428144, 5732728])
    pname = get_pname(pid)
    ptype = random.choice(['cpu', 'gpu'])
    server_id = random.randint(0, 10)
    wattage = round(random.uniform(1.0, 10.0), 6)  # power in Watts
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    return {"server_id": server_id,
            "plugin_name": pname,
            "type": ptype,
            "value": wattage,
            "process_id": pid,
            "timestamp": timestamp}


# Function to run the event creation in a separate thread
def event_thread():
    while True:
        event = generate_power_data()
        print(event)
        # Add a delay to avoid rapid event creation
        threading.Event().wait(0.5)

if __name__ == '__main__':
    # Start the event creation in a separate thread
    thread = threading.Thread(target=event_thread)
    thread.start()

    start_time = datetime.datetime.now()
    cpu_data = []
    gpu_data = []
    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time.total_seconds() > 10:
            break

        cpu_data.append(generate_power_data())
        time.sleep(1)

    cpu_file_name = 'logs/power.json'
    os.makedirs(os.path.dirname(cpu_file_name), exist_ok=True)
    with open(cpu_file_name, 'w') as file:
        json.dump(cpu_data, file, indent=4)

