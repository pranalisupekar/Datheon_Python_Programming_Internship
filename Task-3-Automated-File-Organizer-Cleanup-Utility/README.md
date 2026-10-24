# Automated File Organizer & Cleanup Utility

## Project Overview

The Automated File Organizer & Cleanup Utility is a Python-based application that organizes files into separate folders according to their file extensions.

It helps users keep their directories clean and organized.

## Features

* Automatically identifies file types using extensions.
* Creates category folders for Documents, Images, Videos, Archives, Code, and Other.
* Moves files into the appropriate folders.
* Handles duplicate filenames by generating a different filename.
* Handles permission errors and reports files that cannot be moved.
* Displays a summary of files checked, moved, and skipped.

## Technologies Used

* Python 3
* os module
* shutil module

## How to Run

1. Install Python 3.

2. Open a terminal in the project folder.

3. Run the following command:

   ```bash
   python organizer.py
   ```

4. Enter the path of the folder you want to organize.

5. The program will organize the files and display a summary.

## Example

If a folder contains:

* notes.txt
* program.py
* photo.jpg

The program organizes them into:

* Documents/notes.txt
* Code/program.py
* Images/photo.jpg

## Safety Note

Test the program on a separate folder containing sample files before using it on important folders. The program moves files rather than copying them.

## Author

Python Programming Internship Project
