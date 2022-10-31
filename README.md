# Real-Time Human-Posture-Detection

DTW (Dynamic Time Wrapping) Algorithm is used for matching the accelerometer data to 
recognize the posture. The code ```live_acc.py``` plots live acceleration data and performs DTW 
algorithm for ```data.csv``` (real-time data) with the recorded data: ```sitting.csv```, ```standing.csv``` and 
```sleeping.csv``` for all x, y, z directions. If the posture has minimum cost value for all 3 
directions, it is the recognized posture and is displayed on the title of the plot. Otherwise, 
nothing is displayed (indicating a random posture/not one of the three given postures).

Used the PhonePI+ app (https://play.google.com/store/apps/details?id=com.phonepiplus&hl=en_US&gl=US) for streaming sensor data to the computer. Reference for the same: https://github.com/priyankark/PhonePi_SampleServer

List of files with description:
* ```requirements.txt``` – Contains all the dependencies required
* ```PhonePi.py``` – Records as well as prints real-time accelerometer data using Flask and Socket
* ```data.csv``` – Data is recorded in this file in real-time
* ```sitting.csv``` – Contains recorded data for sitting (plot for the same is shown in the report)
* ```standing.csv``` – Contains recorded data for standing (plot for the same is in the report)
* ```sleeping.csv``` – Contains recorded data for sleeping (plot for the same is shown in the report)
* ```live_acc.py``` – It performs DTW algorithm for data.csv with sitting.csv, standing.csv and sleeping.csv for all x, y, z directions and computes the minimum cost among these. Also plots the accelerometer data in real-time

# How to run:
* Install all the dependencies: ```pip install -r requirements.txt```
* Clear the data.csv so that fresh data is recorded in the file
* Run: ```python3 PhonePi.py``` in one terminal
* Enter the IP address in the PhonePI+ mobile app
* Change the output format from JSON to CSV in the app
* Update the frequency to 100 ms for the accelerometer 
* Turn ON its toggle button. This will start printing real-time acceleration data on the terminal as well as in data.csv
* Simultaneously, run: ```python3 live_acc.py``` in a different terminal for real-time plotting and posture recognition
* As soon as the plotting starts, perform any action (posture)
* If the action is one out of sitting or standing or sleeping, then it is recognized and the corresponding action is displayed on the title of the plot
* Turn OFF the sensor once the posture is recognized
