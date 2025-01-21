HF JSON Tool
HF JSON Tool is a command-line Python application that showcases how to:

Load and validate a local JSON dataset using:
Pydantic for schema validation
Hugging Face Datasets to parse JSON files into a Dataset object.
Push the validated dataset to the Hugging Face Hub.
Read the dataset back from the Hugging Face Hub.
Write the downloaded dataset to a local JSON file.
All of these actions are presented via a simple menu in the command line, allowing you to select which step you want to perform.

Features
Menu-Driven Interface:
The script presents a menu with options (1–5) for each specific action.

Validation with Pydantic:

Ensures your JSON records match a defined schema (EmailRecord model).
Prints how many records are valid (and can be used downstream).
Integration with Hugging Face Hub:

Easily push validated data to your repository on the Hugging Face Hub.
Optionally log in via terminal (no Jupyter or Colab environment required).
Local JSON Support:

Load from your local JSON file (e.g., emails (1).json).
Save any Hugging Face Dataset to JSON (e.g., downloaded_emails.json).


Typical Workflow
Option 1 - Load and Validate:

Reads emails (1).json into a Hugging Face Dataset.
Validates each record against EmailRecord.
Stores the resulting validated dataset in memory.
Option 2 - Push to Hub:

Prompts you to log in to Hugging Face (if not already).
Pushes your validated dataset to the repository specified in repo_id.
Option 3 - Read from Hub:

Loads the dataset from your Hugging Face Hub repo back into a local Dataset object.
Option 4 - Write to Local JSON:

Saves the currently downloaded dataset to a local JSON file, one record per line.
Option 5 - Exit.

