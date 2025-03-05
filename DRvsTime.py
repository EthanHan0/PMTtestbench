import numpy as np 
import matplotlib.pyplot as plt
import os


#This script is used to produce darkrate against the relaxation time. 
# Directory path
dir = "C:/Users/User/OneDrive - University of Adelaide/Physics/DM_SabraPMT/DarkRate/txtfiles/RelaxTime/1500VDR_-4mV"

os.chdir(dir)

time_array = []
DR_array = []

FileNameArray = os.listdir(dir)

for i in FileNameArray:
    time = int(i[:-7])
    time_array.append(time)

    with open(i, 'r') as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()
        # Extract dark rate and error
        dark_rate = first_line.split(';')[0]
        dark_rate = dark_rate[9:]
        dark_rate = dark_rate[:-2]
        dark_rate = float(dark_rate)
        DR_array.append(dark_rate)

# Sort both arrays based on time_array
sorted_indices = np.argsort(time_array)
print(sorted_indices)
time_array = [time_array[i] for i in sorted_indices]
print(time_array)
DR_array = [DR_array[i] for i in sorted_indices]
print(DR_array) 

plt.plot(time_array, DR_array)
plt.xlabel('Time(min)')
plt.ylabel('Dark Rate(Hz)')
plt.title('Dark rate vs Relaxation time')
plt.show()

