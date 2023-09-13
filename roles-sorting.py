import csv

# Define the input and output file paths
input_file = 'user-roles.csv'
output_file = 'sorted-user-roles.csv'

# Initialize a dictionary to store roles for each user
user_roles = {}

# Read the input CSV file
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        user, *roles = row  # Get user and roles from each row
        user_roles.setdefault(user, set()).update(roles)  # Add roles to the set

# Write the results to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for user, roles in user_roles.items():
        writer.writerow([user, ', '.join(roles)])

print(f"Result written to {output_file}.")
