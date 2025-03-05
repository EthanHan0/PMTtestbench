import os
import numpy as np
import matplotlib.pyplot as plt

# Directory path
dir = "C:/Users/User/OneDrive - University of Adelaide/Physics/DM_SabraPMT/DarkRate/txtfiles/MultiEvents"

# Get all file names in the directory
FileNameArray = os.listdir(dir)

# Get all possible voltages
Voltages = []
for i in FileNameArray: 
    Voltage = i[:5]
    Voltages.append(Voltage)
# Extract unique voltages only
unique_voltages = list(set(Voltages))

# All Trigger levels to be plotted
trig = [-3.5, -3.75, -4, -4.25, -4.5, -4.75, -5]

# Initialize the dark_rate dictionary
dark_rates = {}
dark_rate_errors = {}

for v in unique_voltages:
    rates = []
    errors = []
    for t in trig:
        # Construct the expected file name pattern
        file_name = f"{v}DR_{t}mV.txt"
        
        # Check if the file exists in the directory
        if file_name in FileNameArray:
            file_path = os.path.join(dir, file_name)
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()
                second_line = file.readline().strip()
                # Extract dark rate and error
                dark_rate = first_line.split(';')[0]
                dark_rate = dark_rate[9:]
                dark_rate = dark_rate[:-2]
                print(f'dark_rate is {dark_rate}')
                DRerror = second_line.split(';')[0][14:-2]
                print(f'DRerror is {DRerror}')
                # Convert to float then append
                rates.append(float(dark_rate))
                errors.append(float(DRerror))
        else:
            # If the file does not exist, append NaN
            rates.append(np.nan)
            errors.append(np.nan)

    dark_rates[v] = rates
    dark_rate_errors[v] = errors

    print(dark_rate)
    print(dark_rate_errors)

    #print(dark_rates)
# Sort the dark_rates dictionary by the voltage keys (from 1300V to 1800V)
for voltage, rates in sorted(dark_rates.items(), key=lambda v: v[0][:4]):
    errors = dark_rate_errors[voltage]
    plt.errorbar(trig, rates, yerr=errors, marker='.', linestyle='-', label=voltage)

plt.xlabel("Trigger Voltage (mV)")
plt.ylabel("Trigger Rate")
plt.title("Dark Rate vs Trigger Threshold")
plt.legend(title="PMT_Voltage")
# plt.yscale('log')
plt.grid()
plt.show()