#!/usr/bin/env python
import matplotlib.pyplot as plt
import os

class Plotting:		
	def plot(x,y,*args, **kwargs):
		colr = kwargs.get('colr','b')
		xlab = kwargs.get('xlab','')
		ylab = kwargs.get('ylab','')
		filename = kwargs.get('filename','file')
		show = kwargs.get('show','yes')
		save = kwargs.get('save','no')

		fig, ax = plt.subplots(figsize=(6,4))
		ax.plot(x,y,colr,LineWidth=6)
		ax.set_xlabel(xlab,fontsize='24')
		ax.set_ylabel(ylab,fontsize='24')
		ax.grid()
		plt.tight_layout()
		plt.savefig(str(os.getcwd() + '/figs/' + filename))
		if show=='yes':
			plt.show()
		elif show=='no':
			pass
		else:
			print('you must enter either yes or no for showing the plots')

		if save=='yes':
			plt.show()
		elif save=='no':
			pass
		else:
			print('you must enter either yes or no for showing the plots')

	# def subplot(x,y,row,col,*args, **kwargs):
	# 	colr = kwargs.get('colr','b')
	# 	xlab = kwargs.get('xlab','')
	# 	ylab = kwargs.get('ylab','')
	# 	filename = kwargs.get('filename','file')
	# 	show = kwargs.get('show','yes')
	# 	save = kwargs.get('save','no')
	# 	no_plots = kwargs.get('no_plots',1)

	# 	fig, ax = plt.subplots(figsize=(6,4))
	# 	for i in range(1,row*col+1):
	# 		ax=plt.subplot(row,col,i)

	# 		self.holdplot(x[i-1],y[i-1],color=colr[i-1]no_plots,ax)

	# 		ax.plot(x[i-1],y[i-1],colr[i-1],LineWidth=6)
	# 		ax.set_xlabel(xlab,fontsize='24')
	# 		ax.set_ylabel(ylab,fontsize='24')
	# 		ax.grid()
	# 		ax.legend(fontsize=16)
	# 		plt.tight_layout()

	# 	if show=='yes':
	# 		plt.show()
	# 	elif show=='no':
	# 		pass
	# 	else:
	# 		print('you must enter either yes or no for showing the plots')

	# 	if save=='yes':
	# 		plt.show()
	# 	elif save=='no':
	# 		pass
	# 	else:
	# 		print('you must enter either yes or no for showing the plots')

	# def holdplot(x,y,no_plots,ax):
	# 	colr = kwargs.get('color','b')
	# 	xlab = kwargs.get('xlab','')
	# 	ylab = kwargs.get('ylab','')
	# 	filename = kwargs.get('filename','file')
	# 	show = kwargs.get('show','yes')
	# 	save = kwargs.get('save','no')
	# 	no_plots = kwargs.get('no_plots',1)

	# 	for i in range(1,no_plots)
	# 		ax.plot(x,y,colr,LineWidth=6)

