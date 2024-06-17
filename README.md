# Group 2: Permutation GUI

This README file provides an overview of the Python PyQt5 application for calculating various permutation and combination scenarios.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Features](#features)
6. [Known Issues](#known-issues)
7. [Future Improvements](#future-improvements)

## Project Description
This project is for the compliance of our discrete mathematics final Performance Innovative Task:
- Groupmates:
- MOSQUIDA EDIMAR
- PACAMO, RAMMEL 
- HARLAN, MIKE
- RUBIN, ASHLEE
- BUHISAN, MARHEAN
- OBSID, REGIE ANN   

The application is designed to perform calculations for combinations, combinations with repetition, permutations with replacement, and permutations. It provides a user-friendly interface using PyQt5 and allows users to input values for N and R, and then calculates the results.

## Installation
To run this application, you need to have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, follow these steps to install the required libraries:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the project files.
3. Install PyQt5 by running the following command:
   ```
   pip install PyQt5
   ```

## Usage
To run the application, execute the following command in the terminal or command prompt:

```
python main.py
```

This will open the PyQt5 window with the application interface.

## Code Structure
The code is organized into a single Python file named `main.py`. The file contains the main window class `mainWindow` that inherits from `QMainWindow`. The class initializes the GUI components, handles button clicks, and performs calculations based on the selected scenario.

## Features
- Calculates combinations, combinations with repetition, permutations with replacement, and permutations.
- Provides a user-friendly interface with buttons and input fields.
- Displays the results in real-time as the user enters values for N and R.

## Known Issues
- None reported at the moment.

## Future Improvements
- Add error handling for invalid input values.
- Implement unit tests to ensure the accuracy of calculations.
- Add more advanced features, such as calculating probabilities or generating random permutations.
