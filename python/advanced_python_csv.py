import csv

with open('faculty.csv', 'rb') as faculty:
    with open("emails.csv", 'wb') as f:
        reader = csv.reader(faculty)
        writer = csv.writer(f)
        next(faculty)
        for name, degree, title, email in reader:
            writer.writerow([email])

