import json
from typing import List, Optional, Any
from pydantic import BaseModel
from datasets import load_dataset, Dataset
from huggingface_hub import login


# -----------------------------
#   Pydantic Models
# -----------------------------
class Profile(BaseModel):
    firstName: str
    lastName: str
    gender: str
    email: str
    age: int
    phoneNumber: str
    streetAddress: str
    city: str
    state: str
    zipCode: str
    occupation: str
    company: str
    communityInvolvement: str

class Topic(BaseModel):
    topicName: str

class EmailRecord(BaseModel):
    id: int
    profile: Profile
    sentiment: str
    urgencyLevel: str
    grammarLevel: str
    subject: str
    body: str
    edgeCase: Optional[str] = None
    comment: Optional[str] = None
    length: int
    category: str
    topics: List[Topic]
    legislations: List[Any]


# -----------------------------
#   Helper Functions
# -----------------------------
def validate_dataset(dataset, model):
    """
    Validate each row in the dataset with the specified Pydantic model.
    Returns a list of valid records as Pydantic model instances.
    """
    valid_records = []
    for i, row in enumerate(dataset):
        record = model(**row)  # raises ValidationError if mismatch
        valid_records.append(record)
    return valid_records


# -----------------------------
#   Main Program with Menu
# -----------------------------
def main():
    # We'll store intermediate data in this dictionary
    state = {
        "validated_dataset": None,    # Will hold the dataset validated locally
        "downloaded_dataset": None    # Will hold the dataset read from the Hub
    }

    repo_id = "abd222002/civic-synthetic-constituent-emails-100K-2024"
    input_json = "emails (1).json"
    output_json = "downloaded_emails.json"

    while True:
        print("\n--- MENU ---")
        print("1) Load and validate local JSON dataset")
        print("2) Push the validated dataset to the Hugging Face Hub")
        print("3) Read the dataset back from the Hub")
        print("4) Write the downloaded dataset to a local JSON file")
        print("5) Exit")

        choice = input("Choose an action (1-5): ").strip()

        if choice == "1":
            # (1) LOAD & VALIDATE LOCAL JSON DATASET
            print(f"\nLoading dataset from '{input_json}' ...")
            dataset_dict = load_dataset("json", data_files={"train": input_json})
            hf_dataset = dataset_dict["train"]

            print("Validating dataset...")
            valid_records = validate_dataset(hf_dataset, EmailRecord)
            print(f"Validated {len(valid_records)} records from '{input_json}'.")

            # Convert validated Pydantic objects to Hugging Face Dataset
            valid_dicts = [r.model_dump() for r in valid_records]
            state["validated_dataset"] = Dataset.from_list(valid_dicts)

            if len(state["validated_dataset"]) > 0:
                print("Example validated record:", state["validated_dataset"][0])

        elif choice == "2":
            # (2) PUSH VALIDATED DATASET TO HUGGING FACE HUB
            if state["validated_dataset"] is None:
                print("\nNo validated dataset found. Please run option (1) first.")
                continue

            print("\nLogging in to Hugging Face Hub (if needed)...")
            login()

            print(f"Now pushing validated dataset to '{repo_id}'...")
            state["validated_dataset"].push_to_hub(repo_id)
            print(f"Dataset successfully pushed to: https://huggingface.co/{repo_id}")

        elif choice == "3":
            # (3) READ DATASET BACK FROM HUB
            print(f"\nReading the dataset from '{repo_id}'...")
            downloaded_dataset = load_dataset(repo_id, split="train")
            state["downloaded_dataset"] = downloaded_dataset

            print(f"Successfully read {len(downloaded_dataset)} records from the Hub.")
            if len(downloaded_dataset) > 0:
                print("First record:", downloaded_dataset[0])

        elif choice == "4":
            # (4) WRITE DOWNLOADED DATASET TO LOCAL JSON
            if state["downloaded_dataset"] is None:
                print("\nNo dataset downloaded from the Hub. Please run option (3) first.")
                continue

            print(f"\nWriting downloaded dataset to '{output_json}' (one JSON object per line)...")
            state["downloaded_dataset"].to_json(output_json)
            print(f"Dataset has been written to '{output_json}'.")

        elif choice == "5":
            # EXIT
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------
#   Entry Point
# -----------------------------
if __name__ == "__main__":
    main()
