import numpy as np
import matplotlib.pyplot as plt

route_1_capacity = 500  # vph
route_2_capacity = 250  # vph
initial_demand = 900  # vph
reduced_demand = 150  # vph
change_time = 60  # minutes
total_time = 180  # full dynamics
time = np.arange(0, total_time + 1)

demand = np.piecewise(time, [time < change_time, time >= change_time], [initial_demand, reduced_demand])

cumulative_arrivals = np.cumsum(demand / 60)

cumulative_departures_1 = np.minimum(cumulative_arrivals, route_1_capacity * time / 60)
cumulative_departures_2 = np.minimum(cumulative_arrivals, route_2_capacity * time / 60)

queue_1 = cumulative_arrivals - cumulative_departures_1
queue_2 = cumulative_arrivals - cumulative_departures_2

plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(time, queue_1, label="Route 1 Queue", color='blue')
plt.plot(time, cumulative_arrivals, label="Cumulative Arrivals", linestyle='--', color='grey')
plt.plot(time, cumulative_departures_1, label="Cumulative Departures (Route 1)", linestyle=':', color='blue')
plt.xlabel('Time (minutes)')
plt.ylabel('Queue Length (vehicles)')
plt.title('Queue Diagram for Route 1')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, queue_2, label="Route 2 Queue", color='red')
plt.plot(time, cumulative_arrivals, label="Cumulative Arrivals", linestyle='--', color='grey')
plt.plot(time, cumulative_departures_2, label="Cumulative Departures (Route 2)", linestyle=':', color='red')
plt.xlabel('Time (minutes)')
plt.ylabel('Queue Length (vehicles)')
plt.title('Queue Diagram for Route 2')
plt.legend()

plt.tight_layout()
plt.show()

delay_1 = np.trapz(queue_1, time) / 60
delay_2 = np.trapz(queue_2, time) / 60

print(f"Total delay for Route 1: {delay_1:.2f} vehicle-hours")
print(f"Total delay for Route 2: {delay_2:.2f} vehicle-hours")


shock_wave_speeds = [(initial_demand - route_1_capacity) / 25, (initial_demand - route_2_capacity) / 25]
upstream_velocity = 60

plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(time, upstream_velocity * time / 60, label="Upstream Flow", color='blue')
plt.axvline(change_time, color='grey', linestyle='--', label="Change in Demand")
plt.xlabel('Time (minutes)')
plt.ylabel('Distance (miles)')
plt.title('Space-Time Diagram for Route 1')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, upstream_velocity * time / 60, label="Upstream Flow", color='red')
plt.axvline(change_time, color='grey', linestyle='--', label="Change in Demand")
plt.xlabel('Time (minutes)')
plt.ylabel('Distance (miles)')
plt.title('Space-Time Diagram for Route 2')
plt.legend()

plt.tight_layout()
plt.show()
