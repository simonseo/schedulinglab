#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: process.py
# @Created:   2017-10-16 11:31:12  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-16 14:03:27  Simon Seo (simon.seo@nyu.edu)


class Process():
	"""Class that simulates a process"""
	def __init__(self, A, B, C, M, i):
		self.A = A               #Arrival Time
		self.B = B               #CPU-burst time (block after)
		self.C = C               #total CPU time needed
		self.M = M               #ioburst = multiplier * cpuburst (block for)
		self.i = i               #order in list (id)

		self.state = 'unstarted' #unstarted, ready, running, blocked, terminated
		self.burst = 0           #time left for any state
		self.prevBurst = 0       #length of previous burst (used for calculating ioburst)
		self.Cleft = C           #CPU time left
		self.q = 0               #quantum left for RR
		self.timeEnteredReady = None    #to find the earliest one

		self.finishTime = None          #time when process finishes
		self.turnaroundTime = 0      #finishing time - A
		self.ioTime = 0              #count time in blocked state
		self.waitingTime = 0         #count time in ready state
		self.runningTime = 0        #count time in running state

	def __lt__(self, p):
		'''priority: arrival time, input order'''
		return (self.A < p.A) if (self.A != p.A) else (self.i < p.i)

	def __repr__(self):
		return "({} {} {} {})".format(self.A, self.B, self.C, self.M)

	def __str__(self):
		stateStr = (' '*11 + self.state)[-11:]
		burstStr = (' '*3 + str(self.burst))[-3:]
		return stateStr + burstStr

	def _updateState(self):
		if self.state == 'running':
			if self.Cleft == 0:
				self.state = 'terminated'
				self.finishTime = tk.getNow()
			elif self.burst == 0:
				self.state = 'blocked'
			elif self.q == 0:
				self.state = 'ready'
				self.timeEnteredReady = tk.getNow()
		# elif other states?
		return self.state

	def tick(self):
		'''gateway function for updating state and time variables'''
		state = self._updateState()
		self.turnaroundTime += 1
		if state not in ['unstarted', 'terminated']:
			self.burst -= 1 if self.burst > 0 else 0
			self.turnaroundTime += 1
			if state == 'running':
				self.Cleft -= 1
				self.runningTime += 1
			elif state == 'ready':
				self.waitingTime += 1
			elif state == 'blocked':
				self.ioTime += 1

	def ratio(self, now):
		T = self.turnaroundTime
		t = max(1, self.runningTime)
		return T/t

	def setRandomBurst(self):
		self.burst = r.randomOS(self.B)
		self.prevBurst = self.burst

	def setIOBurst(self):
		self.burst = self.M * self.prevBurst #Assumes that prevBurst was CPUBurst

class ProcessTable(list):
	"""docstring for ProcessTable"""
	def __init__(self):
		super(ProcessTable, self).__init__()

	def __str__(self):
		result = ''
		for el in self:
			result += ' {}'.format(el)
		return result
		#    unstarted  0   unstarted  0
	
	def __repr__(self):
		result = str(len(self))
		for el in self:
			result += ' {}'.format(el.__repr__())
		return result
		# 2 (0 1 5 1) (0 1 5 1) 

	def sortByArrival(self):
		self.sort(key=lambda p: p.A)

	def sortByInput(self, p):
		self.sort(key=lambda p: p.i)




