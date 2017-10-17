#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: algorithms.py
# @Created:   2017-10-16 13:50:51  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 06:04:24  Simon Seo (simon.seo@nyu.edu)
import sys
import glb
from util import Timekeeper

def FCFS(ps):
	"""First Come First Serve"""
	tk = glb.tk = Timekeeper()
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if len(ps.getAll(lambda p: p.state == 'running')) == 0:
			readyps = ps.getAll(lambda p: p.state == 'ready').sortByInput().sortByArrival().sortByReady()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was First Come First Served\n')
	ps.printSummaryAll()

class RR():
	"""Round Robin"""
	def __init__(self, ps, quantum=2):
		self.ps = ps
		glb.q = quantum
		glb.tk = Timekeeper()
		self.main()
	def main(self):
		tk = glb.tk
		ps = self.ps
		while not ps.finished():
			if glb.v:
				print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
			ps.tickAll()
			ps.updateStateAll()
			if len(ps.getAll(lambda p: p.state == 'running')) == 0:
				readyps = ps.getAll(lambda p: p.state == 'ready').sortByInput().sortByArrival().sortByReady()
				if len(readyps) > 0:
					readyps.pop(0).run()
			tk.tick()
		print('The scheduling algorithm used was Round Robbin\n')
		ps.printSummaryAll()

def SJF(ps):
	"""Shortest Job First: total time remaining (i.e., the
	input value C minus the number of cycles this process has run)"""
	tk = glb.tk = Timekeeper()
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if len(ps.getAll(lambda p: p.state == 'running')) == 0:
			readyps = ps.getAll(lambda p: p.state == 'ready').sortByInput().sortByArrival().sortByJob()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was Shortest Job First\n')
	ps.printSummaryAll()

def HPRN(ps):
	"""Highest Priority Ratio Next"""
	tk = glb.tk = Timekeeper()
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if len(ps.getAll(lambda p: p.state == 'running')) == 0:
			readyps = ps.getAll(lambda p: p.state == 'ready').sortByInput().sortByArrival().sortByRatio()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was Highest Priority Ratio Next\n')
	ps.printSummaryAll()
		