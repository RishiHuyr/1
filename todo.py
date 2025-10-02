import json
from pathlib import Path

DB = Path("tasks.json")

def load_tasks():
    if DB.exists():
        return json.loads(DB.read_text())
    return []

def save_tasks(tasks):
    DB.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['title']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index-1 < len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print("Marked done.")
    else:
        print("Invalid index.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python todo.py add|list|done <args>")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        mark_done(int(sys.argv[2]))
    else:
        print("Unknown command.")
