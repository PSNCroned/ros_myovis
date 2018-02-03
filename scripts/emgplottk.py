#!/usr/bin/env python

import rospy
from ros_myo.msg import EmgArray
import numpy as np
import time
import matplotlib
import Tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

matplotlib.use('TkAgg')

time_series = [[], [], [], [], [], [], [], []]
root = Tk.Tk()
root.wm_title('Myo EMG')
fig = Figure(figsize = (5, 4), dpi = 100)
plt = fig.add_subplot(111)
hz = 0.00
last = 0.00

def onMsg(data):
	global time_series
	global hz
	global last

	print(data.data)

	plt.cla()
	
	if not hz:
		if last:
			hz = round(1 / (time.time() - last), 2)
		else:
			last = time.time()
	
	plt.set_title(str(hz) + " hz")
	plt.axis([0, 100, 0, 1500])
		
	
	for i in range(len(data.data)):
		time_series[i].append(data.data[i])
		
		if len(time_series[i]) > 100:
			time_series[i].pop(0)
			
		plt.plot(time_series[i], label=str(i))

	plt.legend(loc='upper left')
	fig.canvas.draw()

def listener():
	rospy.init_node('emgplot', anonymous = True)
	rospy.Subscriber('myo_emg', EmgArray, onMsg)

def quit():
	root.quit()
	root.destroy()

if __name__ == '__main__':
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.show()
	canvas.get_tk_widget().pack(side = Tk.TOP, fill = Tk.BOTH, expand = 1)

	toolbar = NavigationToolbar2TkAgg(canvas, root)
	toolbar.update()
	canvas._tkcanvas.pack(side = Tk.TOP, fill = Tk.BOTH, expand = 1)

	button = Tk.Button(master = root, text = 'Quit', command = quit)
	button.pack(side = Tk.BOTTOM)

	listener()

	root.protocol('WM_DELETE_WINDOW', quit)
	Tk.mainloop()
	
