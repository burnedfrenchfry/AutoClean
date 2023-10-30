# AutoClean
**Overview**
This Python utility provides an automated solution for cleaning up old and unused files in a specified folder. It calculates a date threshold based on the current date and the user-defined number of months, moving files older than this threshold to the recycling bin. This approach allows safe file deletion without permanently removing them from the system. This utility is particularly useful for managing cache folders, temporary files, or any location prone to accumulating outdated data.

**Features**
Automated Cleanup: The utility automatically identifies and moves files older than the specified timeframe to the recycling bin.
Customizable Timeframe: Users can adjust the number of months to define what constitutes an "old" file.
Safe Deletion: Files are moved to the recycling bin, providing a safety net in case of accidental deletions.
Easy Integration: The script can be scheduled to run periodically, ensuring continuous maintenance of specified folders.

**Requirements**
Python 3
send2trash Python library

**Configure the Scrip**
Modify the cache_folder_path variable in the script to specify the target folder path.
Adjust the months_threshold variable to set the desired timeframe for considering files as old.
Run the Script:

**Copy code**
python cleanup.py
Ensure you have the necessary permissions to delete files in the specified folder.

**Schedule Regular Cleanup (Optional)**:

On Unix-based systems, use cron jobs to schedule the script to run at desired intervals.
On Windows, use Task Scheduler to create a task that runs the script periodically.

Warning
Caution: Exercise caution while using this utility, as it permanently deletes files by moving them to the recycling bin. Deleted files can only be restored from the recycling bin. Make sure to understand the implications before running the script
