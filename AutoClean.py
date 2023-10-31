import os
import datetime
import send2trash

def moving_old_files(folder_path, months_threshold):
    #Current Date & Time
    current_datetime = datetime.datetime.now()

    #Calculate Date Threshold
    threshold_date = current_datetime - datetime.timedelta(days=months_threshold * 30) #30 Days A Month

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        #Check if the file is old
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < threshold_date.timestamp():
            #Move the files to recycling bin
            send2trash.send2trash(file_path)
            print(f"Moved '{filename}' to recycling bin.")

#Path to cache folder
cache_folder_path = r'C:\path\to\your\cache\data'

#Timeframe
months_threshold = 1

#Call function to move to recycling bin
moving_old_files(cache_folder_path, months_threshold)
