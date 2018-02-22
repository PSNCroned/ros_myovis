# ros_myovis

A ROS node for visualizing EMG data from a Myo armband. Subscribes to the Topic 'myo_emg' that [ros_myo](https://github.com/roboTJ101/ros_myo) publishes EMG data to.

## Requirements

- matplotlib
- python 2.7
- Tkinter

## To run

For basic EMG graphing
`rosrun myo_emg emgplot.py`

For EMG with a GUI framework
`rosrun myo_emg emgplottk.py`
The GUI will be updated over time as the project progresses.
