# TDMS Data Processor

## Overview
This script is designed to process .tdms files (a format used by National Instruments) and convert them into CSV format. It is particularly useful for handling large datasets typically generated in scientific and engineering experiments. The script automatically iterates over all groups and channels within each .tdms file, extracting relevant data and metadata, and then saving them as CSV files.

## Features
- Processes multiple .tdms files in a given directory.
- Handles multiple groups and channels within each .tdms file.
- Extracts data along with metadata such as timestamp, waveform increment, and samples.
- Generates CSV files named according to the source .tdms file and group name.

## Requirements
To run this script, you'll need the following installed:
- Python (3.x recommended)
- pandas
- nptdms

You can install the required Python packages using pip:
