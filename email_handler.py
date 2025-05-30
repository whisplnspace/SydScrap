import csv

def save_email(email: str):
    with open("emails.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email])
