#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: algorithms.py
# @Created:   2017-10-16 13:50:51  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 03:32:15  Simon Seo (simon.seo@nyu.edu)
import sys
import glb
from util import Timekeeper

class FCFS():
	"""First Come First Serve"""
	def __init__(self, ps):
		self.ps = ps
		glb.tk = Timekeeper()
		self.main()

	def main(self):
		tk = glb.tk
		ps = self.ps
		while not ps.finished():
			if glb.v:
				print('Before cycle{}:{}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
			ps.tickAll()
			# print('All:', ps)
			ps.updateStateAll()
			# print('All:', ps)
			if len(ps.getAll(lambda p: p.state == 'running')) == 0:
				# print('All:', ps)
				# print('running:', ps.getAll(lambda p: p.state == 'running'))
				readyps = ps.getAll(lambda p: p.state == 'ready').sortByArrival()
				if len(readyps) > 0:
					# print('ready:', readyps)
					readyps.pop(0).run()
			tk.tick()
		print('The scheduling algorithm used was First Come First Served\n')
		ps.printSummaryAll()

class RR():
	"""Round Robin"""
	def __init__(self, ps, quantum=2):
		self.ps = ps
		self.q = quantum
		glb.tk = Timekeeper()
		self.main()
	def main(self):
		tk = glb.tk
		ps = self.ps
		psl = len(ps)
		while not ps.finished():
			if glb.v:
				print('Before cycle{}:{}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
			
			break
		pass

class SJF():
	"""Shortest Job First: total time remaining (i.e., the
	input value C minus the number of cycles this process has run)"""
	def __init__(self, ps):
		self.ps = ps
		glb.tk = Timekeeper()
		self.main()
	def main(self):
		tk = glb.tk
		ps = self.ps
		psl = len(ps)
		while not ps.finished():
			if glb.v:
				print('Before cycle{}:{}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
			
			break
		pass

class HPRN():
	"""Highest Priority Ratio Next"""
	def __init__(self, ps):
		self.ps = ps
		glb.tk = Timekeeper()
		self.main()
	def main(self):
		tk = glb.tk
		ps = self.ps
		psl = len(ps)
		while not ps.finished():
			if glb.v:
				print('Before cycle{}:{}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
			
			break
		pass
						
			