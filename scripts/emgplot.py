#!/usr/bin/env python

import rospy
from ros_myo.msg import EmgArray
import numpy as np
import matplotlib.pyplot as plt

time_series = [[], [], [], [], [], [], [], []]

def onMsg(data):
	global time_series

	plt.cla()
	plt.axis([0, 100, 0, 1500])
	print(data.data)
	
	for i in range(len(data.data)):
		time_series[i].append(data.data[i])
		
		if len(time_series[i]) > 100:
			time_series[i].pop(0)
			
		plt.plot(time_series[i], label=str(i))

	plt.legend(loc='upper left')
	plt.pause(0.001)


def listener():
	rospy.init_node('emgplot', anonymous = True)
	rospy.Subscriber('myo_emg', EmgArray, onMsg)
	rospy.spin()

if __name__ == '__main__':
	plt.ion()
	listener()
	
