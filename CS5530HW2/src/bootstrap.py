# This file loads the sample data, bootstraps the data to create a 500 sets of 150 data points. It then calculates based on "c)", generates,
# and saves the charts and data readouts.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def run():
    # Set paths
    sample_path = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_preprocess\\sample_data.csv"
    save_results_folder = r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\results"
    os.makedirs(save_results_folder, exist_ok=True)

    # Load sample data
    sample_df = pd.read_csv(sample_path)
    df = pd.read_csv(r"C:\\Users\\Manny B\\Documents\\CS5530HW2\\data_raw\\diabetes.csv")

    # Bootstrap sampling
    num_samples = 500
    sample_size = 150

    # Arrays to store the statistics from each bootstrap sample
    bootstrap_means = []
    bootstrap_stds = []
    bootstrap_98th_percentiles = []

    # Perform bootstrap sampling
    for _ in range(num_samples):
        sample = df['BloodPressure'].sample(n=sample_size, replace=True)
        bootstrap_means.append(sample.mean())
        bootstrap_stds.append(sample.std())
        bootstrap_98th_percentiles.append(sample.quantile(0.98))

    # Compute statistics for the population
    population_mean_bp = df['BloodPressure'].mean()
    population_std_bp = df['BloodPressure'].std()
    population_98th_percentile_bp = df['BloodPressure'].quantile(0.98)

    # Compute average statistics from bootstrap samples
    average_mean_bp = np.mean(bootstrap_means)
    average_std_bp = np.mean(bootstrap_stds)
    average_98th_percentile_bp = np.mean(bootstrap_98th_percentiles)

    # Save statistics to a CSV file
    bp_stats = pd.DataFrame({
        "Statistic": ["Population Mean", "Bootstrap Average Mean", "Population Std Dev", "Bootstrap Average Std Dev",
                      "Population 98th Percentile", "Bootstrap Average 98th Percentile"],
        "BloodPressure": [population_mean_bp, average_mean_bp, population_std_bp, average_std_bp, 
                          population_98th_percentile_bp, average_98th_percentile_bp]
    })
    bp_stats.to_csv(os.path.join(save_results_folder, "bp_stats.csv"), index=False)
    print("Blood Pressure statistics saved.")

    # Plot KDEs for Bootstrap vs Population
    plt.figure(figsize=(18, 12))

    # KDE Plot for Bootstrap Sample Means vs Population Mean
    plt.subplot(3, 2, 1)
    sns.kdeplot(bootstrap_means, label='Bootstrap Sample Means', color='lightblue', fill=True)
    plt.axvline(population_mean_bp, color='red', linestyle='--', label='Population Mean')
    plt.xlabel('BloodPressure Mean')
    plt.ylabel('Density')
    plt.title('KDE Plot of Bootstrap Sample Means vs Population Mean')
    plt.legend()
    plt.savefig(os.path.join(save_results_folder, "bootstrap_means_kde_plot.png"))

    # KDE Plot for Bootstrap Sample Standard Deviations vs Population Std Dev
    plt.subplot(3, 2, 2)
    sns.kdeplot(bootstrap_stds, label='Bootstrap Sample Std Devs', color='lightgreen', fill=True)
    plt.axvline(population_std_bp, color='red', linestyle='--', label='Population Std Dev')
    plt.xlabel('BloodPressure Std Dev')
    plt.ylabel('Density')
    plt.title('KDE Plot of Bootstrap Sample Std Devs vs Population Std Dev')
    plt.legend()
    plt.savefig(os.path.join(save_results_folder, "bootstrap_std_kde_plot.png"))

    # KDE Plot for Bootstrap Sample 98th Percentiles vs Population 98th Percentile
    plt.subplot(3, 2, 3)
    sns.kdeplot(bootstrap_98th_percentiles, label='Bootstrap Sample 98th Percentiles', color='lightcoral', fill=True)
    plt.axvline(population_98th_percentile_bp, color='red', linestyle='--', label='Population 98th Percentile')
    plt.xlabel('BloodPressure 98th Percentile')
    plt.ylabel('Density')
    plt.title('KDE Plot of Bootstrap Sample 98th Percentiles vs Population 98th Percentile')
    plt.legend()
    plt.savefig(os.path.join(save_results_folder, "bootstrap_98th_percentile_kde_plot.png"))

    # Horizontal Bar Chart for Comparison of Means
    plt.subplot(3, 2, 4)
    labels = ['Population Mean', 'Bootstrap Average Mean']
    values = [population_mean_bp, average_mean_bp]
    plt.barh(labels, values, color=['blue', 'red'])
    plt.xlabel('Mean BloodPressure')
    plt.title('Comparison of Mean BloodPressure')
    plt.savefig(os.path.join(save_results_folder, "bp_mean_comparison_bar_chart.png"))

    # Horizontal Bar Chart for Comparison of Standard Deviations
    plt.subplot(3, 2, 5)
    labels = ['Population Std Dev', 'Bootstrap Average Std Dev']
    values = [population_std_bp, average_std_bp]
    plt.barh(labels, values, color=['blue', 'red'])
    plt.xlabel('Standard Deviation BloodPressure')
    plt.title('Comparison of Standard Deviation of BloodPressure')
    plt.savefig(os.path.join(save_results_folder, "bp_std_comparison_bar_chart.png"))

    # Horizontal Bar Chart for Comparison of 98th Percentiles
    plt.subplot(3, 2, 6)
    labels = ['Population 98th Percentile', 'Bootstrap Average 98th Percentile']
    values = [population_98th_percentile_bp, average_98th_percentile_bp]
    plt.barh(labels, values, color=['blue', 'red'])
    plt.xlabel('98th Percentile BloodPressure')
    plt.title('Comparison of 98th Percentile of BloodPressure')
    plt.savefig(os.path.join(save_results_folder, "bp_98th_percentile_comparison_bar_chart.png"))

    plt.tight_layout()
    plt.show()
    print("Bootstrap charts saved.")

if __name__ == "__main__":
    run()
