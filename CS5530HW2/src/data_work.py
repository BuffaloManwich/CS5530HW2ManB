# This file bring in a sample of 25 entries from the population
# 
import pandas as pd
import os

def run():
    # Set dataset path
    data_path = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_raw\\diabetes.csv"
    save_sample_path = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_preprocess\\sample_data.csv"

    # Ensure the save folder exists
    os.makedirs(os.path.dirname(save_sample_path), exist_ok=True)

    # Read the dataset
    df = pd.read_csv(data_path)

    # Take a random sample of 25 observations
    sample_df = df.sample(n=25, random_state=42)  # Setting a random_state for reproducibility

    # Save the sample dataset
    sample_df.to_csv(save_sample_path, index=False)
    print("Sample dataset saved.")

if __name__ == "__main__":
    run()
