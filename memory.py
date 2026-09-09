import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "student_name": "",
            "topics": [],
            "progress": []
        }

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def add_topic(topic):
    memory = load_memory()

    if topic not in memory["topics"]:
        memory["topics"].append(topic)

    save_memory(memory)


def add_progress(progress):
    memory = load_memory()
    memory["progress"].append(progress)

    save_memory(memory)