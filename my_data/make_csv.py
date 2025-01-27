import os
import csv

# Define the paths to your train and test directories
train_dir = r'C:\Users\kauladit\Downloads\my_data\train'
test_dir = r'C:\Users\kauladit\Downloads\my_data\test'

# Define the output CSV file paths
train_csv = r'C:\Users\kauladit\Downloads\my_data\my_dataset_train.csv'
test_csv = r'C:\Users\kauladit\Downloads\my_data\my_dataset_test.csv'

# Function to create CSV file
def create_csv(directory, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['path', 'text'])  # Write the header

        for filename in os.listdir(directory):
            if filename.endswith('.wav'):
                audio_path = os.path.join(directory, filename)
                # Extract the command from the filename (assuming the filename format is command_index.wav)
                command = filename.split('_')[0]
                writer.writerow([audio_path, command])

# Create CSV files for train and test datasets
create_csv(train_dir, train_csv)
create_csv(test_dir, test_csv)

print(f"CSV files created: {train_csv}, {test_csv}")