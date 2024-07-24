# This file imports the sample data and performs the second calculation, "b)", then generates charts.
#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run():
    # Set paths
    sample_path = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_preprocess\\sample_data.csv"
    save_results_folder = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\results"
    os.makedirs(save_results_folder, exist_ok=True)

    # Load sample data
    sample_df = pd.read_csv(sample_path)
    df = pd.read_csv(r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_raw\\diabetes.csv")

    # Compute 98th percentile for BMI
    population_98th_percentile_bmi = df['BMI'].quantile(0.98)
    sample_98th_percentile_bmi = sample_df['BMI'].quantile(0.98)

    # Save statistics to a CSV file
    bmi_percentiles = pd.DataFrame({
        "Statistic": ["Population 98th Percentile", "Sample 98th Percentile"],
        "BMI": [population_98th_percentile_bmi, sample_98th_percentile_bmi]
    })
    bmi_percentiles.to_csv(os.path.join(save_results_folder, "bmi_percentiles.csv"), index=False)
    print("BMI percentiles saved.")

    # KDE Plot for BMI values with 98th Percentile
    plt.figure(figsize=(14, 8))
    sns.kdeplot(df['BMI'], label='Population', color='blue', fill=True)
    sns.kdeplot(sample_df['BMI'], label='Sample', color='red', fill=True)
    plt.axvline(population_98th_percentile_bmi, color='blue', linestyle='--', label='Population 98th Percentile')
    plt.axvline(sample_98th_percentile_bmi, color='red', linestyle='--', label='Sample 98th Percentile')
    plt.xlabel('BMI')
    plt.ylabel('Density')
    plt.title('KDE Plot of BMI Values with 98th Percentile')
    plt.legend()
    plt.savefig(os.path.join(save_results_folder, "bmi_kde_plot.png"))
    plt.show()
    print("BMI charts saved.")

if __name__ == "__main__":
    run()
