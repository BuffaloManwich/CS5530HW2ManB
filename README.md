# CS5530HW2ManB
This is a data preparation and analysis project for CS5530
I again had to copy the entire folder containing my code.

# Data Loading and Sampling w/ Save
Here I load the population set and take a sample of 25.
This sample will be used throughout for all three calculations/charts.
![Screenshot 2024-07-23 130832](https://github.com/user-attachments/assets/fbdb72a6-10a2-439b-9efd-81c89becf801)

# Here I perform the calculation for Mean and Max Glucose in the sample and population
I save the results and plot a couple of graphs comparing the results.
The KDE plot clearly shows that the sample has a lower Max value.
The Mean is close, however. This sample will work well.
![Screenshot 2024-07-23 130925](https://github.com/user-attachments/assets/074635ba-65da-406f-b583-d90f0171aa17)

# Here I calculate the 98th percentile of BMI for the sample and population
These calculations are saved and compared in charts. The KDE plot shows that there is a bit more discrepancy than we'd like.
As a representative sample however, this should work.
![Screenshot 2024-07-23 131038](https://github.com/user-attachments/assets/c4f0500f-9faa-40fb-a713-8b5a94ae0dc7)

# Here I bootstrap the sample to create a "new population" to analyze
The bootstrap data is analyzed and compare to the original population.
All results are saved.
![Screenshot 2024-07-23 131154](https://github.com/user-attachments/assets/d2b71a25-cbe7-48d9-9fc1-edb2f5ff4779)

![Screenshot 2024-07-23 131128](https://github.com/user-attachments/assets/6ff906f0-2c98-4756-a8e6-c01537b0ea70)
The KDE graphs are showing the calculations performed on each of the bootstrap samples. 
The dash line being the population actual value. The sets are averaged and compared in the bar graph. 
We see the results are very close to the actual population. 

# Here is the workflow file with the confirmations showing execution of the other steps
![Screenshot 2024-07-23 131252](https://github.com/user-attachments/assets/b81935f7-a0d0-4321-bc07-41fb3a244134)

# This process clearly indicates that the bottstrapping method is valuable.
This is an effective method of performing population analsis with access to the full population data.
