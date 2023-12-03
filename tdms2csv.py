from nptdms import TdmsFile
import pandas as pd
import os

# Directory containing the .tdms files
directory = "."

# Iterate over all .tdms files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".tdms"):
        tdms_path = os.path.join(directory, filename)

        # Load the TDMS file
        tdms_file = TdmsFile.read(tdms_path)

        # Iterate over all groups in the file
        for group in tdms_file.groups():
            groupname = group.name

            # Create a list to store DataFrames for each channel
            dataframes = []

            # Iterate over each channel in the group
            for channel in group.channels():

                # Accessing the data
                data = channel[:]
                time = channel.time_track(absolute_time=True)

                # Retrieve metadata for the channel
                wf_increment = channel.properties.get('wf_increment', None)
                wf_samples = channel.properties.get('wf_samples', None)

                # Create a DataFrame for the current channel
                df = pd.DataFrame({
                    'timestamp': time, 
                    'group': groupname,
                    'channel': channel.name,
                    'data': data, 
                    'wf_increment': wf_increment,
                    'wf_samples': wf_samples
                })

                # Add the DataFrame to the list
                dataframes.append(df)

            # Concatenate all DataFrames in the list into one DataFrame
            all_data = pd.concat(dataframes, ignore_index=True)

            # Generate the CSV filename
            csv_filename = f"{os.path.splitext(filename)[0]}_{groupname}.csv"

            # Save the combined data to a CSV file
            all_data.to_csv(os.path.join(directory, csv_filename), index=False)

            print(f"Processed and saved: {csv_filename}")
