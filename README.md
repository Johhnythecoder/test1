# Reminder App

This repository contains a simple command-line reminder application written in Python.

## Usage

Add a reminder with a due time in ISO format:

```
python3 reminder_app.py add 2024-05-01T14:30 "Take out the trash"
```

List all reminders:

```
python3 reminder_app.py list
```

Run the reminder loop which checks every 30 seconds and prints due reminders:

```
python3 reminder_app.py run
```

Reminders are stored in `reminders.json` in the current directory.
