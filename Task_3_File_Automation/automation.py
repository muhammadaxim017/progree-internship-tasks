
import re
from pathlib import Path
import shutil
import csv


data_folder = Path("data")
organized_folder = Path("organized")

images_folder = organized_folder / "images"
documents_folder = organized_folder / "documents"
text_folder = organized_folder / "text"

# Create destination folders
images_folder.mkdir(parents=True, exist_ok=True)
documents_folder.mkdir(parents=True, exist_ok=True)
text_folder.mkdir(parents=True, exist_ok=True)

# Check each item in the data folder
for file in data_folder.iterdir():

    if file.is_file():

        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            destination = images_folder / file.name

        elif file.suffix.lower() in [".pdf", ".docx", ".doc"]:
            destination = documents_folder / file.name

        elif file.suffix.lower() in [".txt", ".log"]:
            destination = text_folder / file.name

        else:
            print("Unrecognized file type:", file.name)
            continue

        # Move the file to its destination
        shutil.move(str(file), str(destination))
        print("Moved:", file.name, "->", destination)


log_file = Path("organized/text/transaction.log")

if log_file.exists():
    text = log_file.read_text(encoding="utf-8")
    print(text)
    pattern = re.compile(
        r"Customer email:\s*(?P<email>[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\s*"
        r"Transaction ID:\s*(?P<transaction_id>TXN-\d{4}-\d+)",
        re.IGNORECASE
    )

    records = []

    for match in pattern.finditer(text):
        records.append({
            "email": match.group("email"),
            "transaction_id": match.group("transaction_id")
        })

    print("Records found:", records)
    csv_file = Path("master.csv")

    with csv_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["email", "transaction_id"]
        )

        writer.writeheader()
        writer.writerows(records)
        print("Records written to CSV:", len(records))

    print("CSV file created:", csv_file.resolve())
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text)

    print("Emails found:", emails)
    transaction_ids = re.findall(
        r"\bTXN-\d{4}-\d+\b",
        text
    )

    print("Transaction IDs found:", transaction_ids)
else:
    print("Log file not found.")
