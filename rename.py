import os
from datetime import datetime, timedelta

def rename_files(folder_path, start_date, years_forward, skip_weekdays=None):
    try:
        # Convert input date to datetime object
        start_date = datetime.strptime(start_date, '%Y-%m-%d')

        # Get a list of files in the folder, excluding .DS_Store files
        files = [file_name for file_name in os.listdir(folder_path) if not file_name.startswith('.DS_Store')]

        # Sort files based on names
        files = sorted(files)

        for file_name in files:
            # Check if skip_weekdays is provided and the current day is in the skip_weekdays list
            while skip_weekdays and start_date.weekday() in [weekday_index(skip_weekday) for skip_weekday in skip_weekdays]:
                # Skip renaming for this day but increment to the next day
                print(f"Skipping {start_date.strftime('%Y-%m-%d')} - {file_name}")
                start_date += timedelta(days=1)

            # Construct the new file name using the specified format
            comic_prefix = 'ZTSyd_'
            new_name = start_date.strftime(comic_prefix + '%Y%m%d')

            # Get the file extension
            _, file_extension = os.path.splitext(file_name)

            # Construct the full path of the old and new files
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name + file_extension)

            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renaming {file_name} to {new_name + file_extension}")

            # Increment the date for the next file only if the file is not skipped
            start_date += timedelta(days=1)

    except Exception as e:
        print(f"An error occurred: {e}")

def weekday_index(weekday):
    # Helper function to convert weekday name to index (0-6)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays.index(weekday.capitalize())

# Example usage:
folder_path = './files'  # Use the dot for the current directory
start_date = '2024-03-10'
years_forward = 2
skip_weekdays = ['Monday', 'Wednesday', 'Friday', 'Sunday']  # Specify weekdays to skip

rename_files(folder_path, start_date, years_forward, skip_weekdays)
