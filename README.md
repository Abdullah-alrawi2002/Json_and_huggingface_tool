# HF JSON Tool

**HF JSON Tool** is a command-line Python application that demonstrates how to:

1. **Load and Validate** a local JSON dataset (e.g., `emails (1).json`) using:
   - [Pydantic](https://docs.pydantic.dev/) for schema validation
   - [Hugging Face Datasets](https://github.com/huggingface/datasets) to parse JSON files
2. **Push** the validated dataset to the [Hugging Face Hub](https://huggingface.co/)
3. **Read** the dataset **back** from the Hub
4. **Write** the downloaded dataset **to a local JSON file**

All of these actions are presented via a simple **menu** so you can choose exactly which step to perform.

---

## Features

- **Menu-Driven Interface**  
  Interactively select your desired action (load/validate, push, read, save, or exit).

- **Pydantic Validation**  
  Automatically checks each record in your JSON file against a defined schema (`EmailRecord`). Identifies invalid records immediately.

- **Hugging Face Hub Integration**  
  Easily push validated data to your own repository on the Hugging Face Hub. Log in via CLI (no Jupyter environment needed).

- **JSON Input/Output**  
  - Read from a local file (`emails (1).json`)
  - Save any Hugging Face `Dataset` to a local JSON file (`downloaded_emails.json`).

---

--- MENU ---
1) Load and validate local JSON dataset
2) Push the validated dataset to the Hugging Face Hub
3) Read the dataset back from the Hub
4) Write the downloaded dataset to a local JSON file
5) Exit
Choose an action (1-5):
