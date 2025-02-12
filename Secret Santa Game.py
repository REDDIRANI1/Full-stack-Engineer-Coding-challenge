import csv
import random
import os
import sys
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """Reads a CSV file and returns a list of dictionaries."""
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        return []

def write_csv(file_path: str, data: List[Dict[str, str]], fieldnames: List[str]):
    """Writes data to a CSV file."""
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing file {file_path}: {e}", file=sys.stderr)

def generate_secret_santa(employees: List[Dict[str, str]], previous_pairs: Dict[str, str]) -> List[Dict[str, str]]:
    """Generates a Secret Santa pairing while avoiding previous year's assignments."""
    if len(employees) < 2:
        print("Error: Not enough employees for Secret Santa.", file=sys.stderr)
        return []
    
    names = [employee["Employee_EmailID"] for employee in employees]
    for _ in range(100):  # Try multiple times to find a valid pairing
        random.shuffle(names)
        pairs = {}
        valid = True
        
        for giver, receiver in zip(names, names[1:] + names[:1]):
            if giver == receiver or previous_pairs.get(giver) == receiver:
                valid = False
                break
            pairs[giver] = receiver
        
        if valid:
            return [{
                "Employee_Name": emp["Employee_Name"],
                "Employee_EmailID": emp["Employee_EmailID"],
                "Secret_Child_Name": next((e["Employee_Name"] for e in employees if e["Employee_EmailID"] == pairs[emp["Employee_EmailID"]]), ""),
                "Secret_Child_EmailID": pairs[emp["Employee_EmailID"]]
            } for emp in employees]
    
    print("Error: Unable to generate a valid Secret Santa assignment after multiple attempts.", file=sys.stderr)
    return []

def main():
    input_file = "santaprep.csv"  # Change as needed
    prev_year_file = "previous_santa.csv"  # Change as needed if provided
    output_file = "secret_santa_output.csv"
    
    employees = read_csv(input_file)
    prev_assignments = read_csv(prev_year_file) if os.path.exists(prev_year_file) else []
    
    previous_pairs = {row["Employee_EmailID"]: row["Secret_Child_EmailID"] for row in prev_assignments}
    
    assignments = generate_secret_santa(employees, previous_pairs)
    
    if assignments:
        write_csv(output_file, assignments, ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
        print(f"Secret Santa assignments saved to {output_file}")
    else:
        print("Failed to generate Secret Santa assignments.", file=sys.stderr)

if __name__ == "__main__":
    main()