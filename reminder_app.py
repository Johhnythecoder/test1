import json
import os
import time
import argparse
from datetime import datetime

DATA_FILE = "reminders.json"

def load_reminders():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_reminders(reminders):
    with open(DATA_FILE, "w") as f:
        json.dump(reminders, f, indent=2)


def add_reminder(args):
    reminders = load_reminders()
    due = datetime.fromisoformat(args.time)
    reminders.append({"time": due.isoformat(), "message": args.message})
    save_reminders(reminders)
    print(f"Added reminder for {due}")


def list_reminders(args):
    reminders = load_reminders()
    if not reminders:
        print("No reminders set.")
        return
    for r in reminders:
        print(f"{r['time']} - {r['message']}")


def run_reminders(args):
    print("Running reminder loop. Press Ctrl+C to exit.")
    while True:
        now = datetime.now()
        reminders = load_reminders()
        remaining = []
        for r in reminders:
            due = datetime.fromisoformat(r['time'])
            if due <= now:
                print(f"Reminder: {r['message']} (due {due})")
            else:
                remaining.append(r)
        if len(remaining) != len(reminders):
            save_reminders(remaining)
        time.sleep(30)


def main():
    parser = argparse.ArgumentParser(description="Simple reminder app")
    sub = parser.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Add a reminder")
    a.add_argument("time", help="Time in ISO format, e.g. 2024-05-01T14:30")
    a.add_argument("message", help="Reminder text")
    a.set_defaults(func=add_reminder)

    l = sub.add_parser("list", help="List reminders")
    l.set_defaults(func=list_reminders)

    r = sub.add_parser("run", help="Run reminder loop")
    r.set_defaults(func=run_reminders)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
