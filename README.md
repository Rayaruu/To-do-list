# To-Do List App -Intern ID-CITS1647

A simple, cute desktop to-do list app built with **Python** and **Tkinter**. Add, complete, and delete tasks through a clean GUI with a gingham-pattern background — and your tasks stick around between sessions thanks to JSON-based persistence.

## Features

- Add new tasks via text entry or the Enter key
- Mark tasks as complete/incomplete with a checkbox
- Delete tasks individually
- Tasks automatically save to a local file and reload on startup
- Custom background image for a more personal, aesthetic look

## Built With

- **Python 3**
- **Tkinter** — GUI framework (built into Python)
- **Pillow (PIL)** — for loading and displaying the background image
- **JSON** — for saving/loading tasks between sessions

## Project Structure

```
Todolist/
├── Todo.py          # Main application file
├── gingham.png       # Background image
├── tasks.json         # Auto-generated; stores your tasks (ignored by Git)
└── .gitignore
```

## Getting Started

### Prerequisites

Make sure you have Python 3 installed. Then install Pillow:

```bash
pip install Pillow
```

### Running the app

1. Clone this repository:
   ```bash
   git clone https://github.com/Rayaruu/Todolist.git
   cd Todolist
   ```
2. Run the app:
   ```bash
   python Todo.py
   ```

That's it — the app opens with an empty list ready to go.

## How It Works

- Tasks are stored as a list of dictionaries (`{"text": ..., "done": ...}`) in memory while the app runs.
- Every time a task is added, completed, or deleted, the list is re-saved to `tasks.json`.
- On startup, the app reads `tasks.json` (if it exists) to restore your previous tasks — handled gracefully with a `try`/`except` so the app still works fine on a fresh install with no saved tasks yet.

## Notes

This was built as a learning project to practice:
- Tkinter GUI basics (widgets, layout, event handling)
- Python closures (the lambda + default-argument trick for loop-generated buttons)
- File I/O and JSON serialization
- Basic exception handling

## License

This project is open source and available for personal/educational use.
