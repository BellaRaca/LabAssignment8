import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

baggage_complaints_data = pd.read_csv('baggagecomplaints.csv')
# Figure 1, Scatter plot of baggage complaints and enplaned passengers
plt.figure(figsize=(10, 6))
plt.scatter(baggage_complaints_data['Enplaned'], baggage_complaints_data['Baggage'])
plt.title('Baggage Complaints vs. Enplaned Passengers')
plt.xlabel('Enplaned Passengers')
plt.ylabel('Baggage Complaints')
plt.grid(True)
plt.show()

# Figure 2, Trend of Baggage Complaints Over Time
baggage_complaints_data['Date'] = pd.to_datetime(baggage_complaints_data['Date'], format='%m/%Y')
baggage_complaints_data_sorted = baggage_complaints_data.sort_values('Date')
plt.figure(figsize=(14, 7))
plt.plot(baggage_complaints_data_sorted['Date'], baggage_complaints_data_sorted['Baggage'])
plt.title('Trend of Baggage Complaints Over Time')
plt.xlabel('Date')
plt.ylabel('Baggage Complaints')
plt.grid(True)
plt.show()

# Figure 3, average baggage complaints per month
monthly_complaints = baggage_complaints_data.groupby('Month')['Baggage'].mean().reset_index()
plt.figure(figsize=(12, 7))
sns.barplot(x='Month', y='Baggage', data=monthly_complaints)
plt.title('Average Baggage Complaints Per Month')
plt.xlabel('Month')
plt.ylabel('Average Baggage Complaints')
plt.grid(True)
plt.show()


# Figure 4, plot for total baggage complaints per airline over time
baggage_complaints_data['Date'] = pd.to_datetime(baggage_complaints_data['Date'], format='%m/%Y')
complaints_over_time = baggage_complaints_data.pivot_table(index='Date', columns='Airline', values='Baggage', aggfunc='sum')
plt.figure(figsize=(14, 8))
sns.lineplot(data=complaints_over_time)
plt.title('Total Baggage Complaints Per Airline Over Time')
plt.xlabel('Date')
plt.ylabel('Total Baggage Complaints')
plt.legend(title='Airline', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()