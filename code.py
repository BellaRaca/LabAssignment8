import pandas as pd
import matplotlib.pyplot as plt

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