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