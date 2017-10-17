#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: algorithms.py
# @Created:   2017-10-16 13:50:51  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 12:59:14  Simon Seo (simon.seo@nyu.edu)
import sys
import glb
from util import Timekeeper, Random

def FCFS(ps):
	"""First Come First Serve"""
	tk = glb.tk = Timekeeper() # Reset time
	glb.r = Random(glb.rf) # Reset Random numbers
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll() # advance/deduct all time variables
		ps.updateStateAll() # update state accordingly
		if not len(ps.getByState('running')): # if there is no running process
			readyps = ps.getByState('ready').sortByInput().sortByArrival().sortByReady()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick() # advance 1 cycle
	print('The scheduling algorithm used was First Come First Served\n')
	ps.printSummaryAll()

def RR(ps, quantum=2):
	"""Round Robin"""
	glb.q = quantum
	tk = glb.tk = Timekeeper()
	glb.r = Random(glb.rf)
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if not len(ps.getByState('running')):
			readyps = ps.getByState('ready').sortByInput().sortByArrival().sortByReady()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was Round Robbin\n')
	ps.printSummaryAll()
	glb.q = False

def SJF(ps):
	"""Shortest Job First: total time remaining (i.e., the
	input value C minus the number of cycles this process has run)"""
	tk = glb.tk = Timekeeper()
	glb.r = Random(glb.rf)
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if not len(ps.getByState('running')):
			readyps = ps.getByState('ready').sortByInput().sortByArrival().sortByJob()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was Shortest Job First\n')
	ps.printSummaryAll()

def HPRN(ps):
	"""Highest Priority Ratio Next"""
	tk = glb.tk = Timekeeper()
	glb.r = Random(glb.rf)
	while not ps.finished():
		if glb.v:
			print('Before cycle{}: {}.'.format((' '*5+str(tk.getNow()))[-5:],ps))
		ps.tickAll()
		ps.updateStateAll()
		if not len(ps.getByState('running')):
			readyps = ps.getByState('ready').sortByInput().sortByArrival().sortByRatio()
			if len(readyps) > 0:
				readyps.pop(0).run()
		tk.tick()
	print('The scheduling algorithm used was Highest Priority Ratio Next\n')
	ps.printSummaryAll()
		