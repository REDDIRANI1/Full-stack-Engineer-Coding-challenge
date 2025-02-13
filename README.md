Secret Santa Pairing Program

Overview

The Secret Santa Pairing Program is a Python script that assigns Secret Santa pairs to employees while ensuring that no one gets the same recipient as the previous year. The solution is modular, robust, and includes error handling for smooth execution.

Features

Reads employee details from a CSV file.

Ensures no one is assigned the same recipient as last year.

Randomly shuffles and assigns Secret Santa pairs.

Exports the assignments to a new CSV file.

Handles errors such as missing files and insufficient participants.

Requirements

Python 3.7+

Installation

Download or create the required script files manually.

Ensure you have Python installed on your system.

Install dependencies (if any are required in the future):

Usage

Input CSV Format

The input CSV (Secret_Santa.csv) should have the following columns:

Employee_Name,Employee_EmailID
Hamish Murray,hamish.murray@acme.com
Layla Graham
,layla.graham@acme.com
The previous year’s assignments CSV (previous_santa.csv) should be structured as:

Employee_EmailID,Secret_Child_EmailID
hamish.murray@acme.com,layla.graham@acme.com

Running the Script

To generate the Secret Santa assignments, run:

python secret_santa.py

Output

The output CSV (secret_santa_output.csv) will be structured as follows:

Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Hamish Murray,hamish.murray@acme.com
Layla Graham
,layla.graham@acme.com

Error Handling

If an input file is missing, an error message is displayed.

If there are fewer than two participants, the script terminates with an error.

If a valid assignment cannot be generated after multiple attempts, an error message is displayed.

Testing

To run tests (if implemented):

pytest tests/

Contribution

Create the repository.

Create a master branch (git checkout -b master-branch).

Commit changes (git commit -m 'Add feature').

Push to the branch (git push origin master-branch).

Open a Pull Request.

License

This project is publicly available under an open-source license.
