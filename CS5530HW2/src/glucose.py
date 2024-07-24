# This file imports the data sample and performs the first calculations, "a)", then generates the first graphs
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

    # Compute population statistics
    pop_mean_glucose = df['Glucose'].mean()
    pop_max_glucose = df['Glucose'].max()

    # Compute sample statistics
    sample_mean_glucose = sample_df['Glucose'].mean()
    sample_max_glucose = sample_df['Glucose'].max()

    # Save statistics to a CSV file
    glucose_stats = pd.DataFrame({
        "Statistic": ["Population Mean", "Sample Mean", "Population Max", "Sample Max"],
        "Glucose": [pop_mean_glucose, sample_mean_glucose, pop_max_glucose, sample_max_glucose]
    })
    glucose_stats.to_csv(os.path.join(save_results_folder, "glucose_stats.csv"), index=False)
    print("Glucose statistics saved.")

    # Create charts for comparison
    labels = ['Population Mean', 'Sample Mean', 'Population Max', 'Sample Max']
    values = [pop_mean_glucose, sample_mean_glucose, pop_max_glucose, sample_max_glucose]

    plt.figure(figsize=(14, 8))

    # Bar chart
    plt.subplot(2, 2, 1)
    plt.bar(labels, values, color=['blue', 'red', 'blue', 'red'])
    plt.ylabel('Glucose Value')
    plt.title('Comparison of Glucose Statistics')
    plt.savefig(os.path.join(save_results_folder, "glucose_bar_chart.png"))

    # KDE Plot
    plt.subplot(2, 2, 2)
    sns.kdeplot(df['Glucose'], label='Population', color='blue', fill=True)
    sns.kdeplot(sample_df['Glucose'], label='Sample', color='red', fill=True)
    plt.xlabel('Glucose')
    plt.ylabel('Density')
    plt.title('KDE Plot of Glucose Values')
    plt.legend()
    plt.savefig(os.path.join(save_results_folder, "glucose_kde_plot.png"))
    plt.show()
    print("Glucose charts saved.")

if __name__ == "__main__":
    run()
