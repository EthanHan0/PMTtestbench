import os
import numpy as np
import matplotlib.pyplot as plt

def OverLayingHistoFromtxt(dir,Volt,min_bin = None, max_bin = None):
    # Make sure we got different color for different plot here.
    colors = plt.cm.viridis(np.linspace(0, 2, 20))  # Adjust the color depends on how it comes out

    #Read everything in the directory
    for filename in os.listdir(dir):
        if filename.startswith(Volt):
            #print(filename)
            file_path = os.path.join(dir, filename)
            print(file_path)
            TriggerValue = filename[8:-4]  # Extract the trigger value
            #print(TriggerValue)

            # Initialize arrays to store bin edges and counts
            bin_edges = []
            counts = []
            
            # Open the file and read the data
            with open(file_path, 'r') as file:
                #skip the space
                next(file) 
                next(file)
                next(file)

                # Read the remaining lines
                for line in file:
                    parts = line.split()
                    if len(parts) == 2:
                        bin_edge = float(parts[0])  
                        count = int(parts[1])    
                        bin_edges.append(bin_edge)
                        counts.append(count)

            # Convert lists to numpy arrays
            bin_edges = np.array(bin_edges)
            counts = np.array(counts)

            
            # Filter the data based on the specified range
            if min_bin is not None:
                mask = bin_edges >= min_bin
                bin_edges = bin_edges[mask]
            counts = counts[mask]
            if max_bin is not None:
                mask = bin_edges <= max_bin
                bin_edges = bin_edges[mask]
                counts = counts[mask]

            # Define a dictionary to map trigger values to specific colors
            color_map = {
                '-4mV': 'red',
                '-4.25mV': 'blue',
                '-4.5mV': 'green',
                '-3.5mV': 'orange',
                '-3.75mV': 'purple',
                '-4.75mV': 'pink', 
                '-5mV':'black'
               
            }

            # Check if the trigger value is in the color map
            if TriggerValue in color_map:
                # Use the color map to get the color for the current trigger value
                color = color_map[TriggerValue]

                # Plot the data
                plt.plot(bin_edges, counts, label=f'{TriggerValue}', color=color)
            
    # Set plot labels and title
    plt.xlabel('Charge Accumulation(pC)')
    plt.ylabel('Count')
    plt.title(f'Histograms for {Volt} with Different Trigger Values')
    plt.yscale('log')
    plt.grid(True)
    plt.legend(title='Trigger Value')

    # Show the plot
    plt.show()

#One time use
dir = 'C:/Users/User/OneDrive - University of Adelaide/Physics/DM_SabraPMT/DarkRate/txtfiles/SingleEvent'
min_bin = -1
max_bin = 4.5
Volt = '1700V'
OverLayingHistoFromtxt(dir,Volt, min_bin, max_bin)