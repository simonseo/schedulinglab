#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: process.py
# @Created:   2017-10-16 11:31:12  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 05:44:15  Simon Seo (simon.seo@nyu.edu)
import glb

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
		self.q = 2               #quantum left for RR
		self.timeEnteredReady = None    #to find the earliest one

		self.finishTime = None          #time when process finishes
		self.turnaroundTime = 0      #finishing time - A
		self.ioTime = 0              #count time in blocked state
		self.waitingTime = 0         #count time in ready state
		self.runningTime = 0         #count time in running state

	def __lt__(self, p):
		'''priority: arrival time, input order'''
		return (self.A < p.A) if (self.A != p.A) else (self.i < p.i)

	def __repr__(self):
		return "({} {} {} {})".format(self.A, self.B, self.C, self.M)

	def __str__(self):
		stateStr = (' '*10 + self.state)[-10:]
		burstStr = (' '*3 + str(self.burst if not glb.q else self.q))[-3:]
		return stateStr + burstStr

	def printSummary(self):
		print('''	(A,B,C,M) = ({},{},{},{})
	Finishing time: {}
	Turnaround time: {}
	I/O time: {}
	Waiting time: {}\n''' \
			.format(self.A, self.B, self.C, self.M, 
				self.finishTime, self.turnaroundTime, 
				self.ioTime, self.waitingTime)
			)

	def tick(self):
		'''gateway function for updating state and time variables'''
		state = self.state
		if state not in ['unstarted', 'terminated']:
			self.turnaroundTime += 1
			if state == 'running':
				self.burst -= 1 if self.burst > 0 else 0
				self.Cleft -= 1
				self.q -= 1 if glb.q > 0 else 0
				self.runningTime += 1
			elif state == 'ready':
				self.waitingTime += 1
			elif state == 'blocked':
				self.burst -= 1 if self.burst > 0 else 0
				self.ioTime += 1
		return

	def updateState(self):
		now = glb.tk.getNow()
		if self.state == 'running':
			if self.Cleft == 0:
				self.state = 'terminated'
				self.finishTime = now
			elif self.burst == 0:
				self.block()
			elif self.q == 0:
				self.preempt()
		elif self.state == 'unstarted':
			if now == self.A:
				self.state = 'ready'
				self.timeEnteredReady = now
		elif self.state == 'blocked':
			if self.burst == 0:
				self.state = 'ready'
				self.timeEnteredReady = now
		elif self.state == 'ready':
			pass
		elif self.state == 'terminated':
			pass

		return self.state

	def ratio(self):
		T = self.turnaroundTime
		t = max(1, self.runningTime)
		return T/t

	def setRandomBurst(self):
		self.prevBurst = glb.r.randomOS(self.B)
		self.burst = self.prevBurst
		return

	def setIOBurst(self):
		self.burst = self.M * self.prevBurst #Assumes that prevBurst was CPUBurst
		return

	def run(self):
		self.state = 'running'
		if glb.q:
			self.q = glb.q
		if self.burst == 0:
			self.setRandomBurst()

	def block(self):
		self.state = 'blocked'
		self.setIOBurst()

	def preempt(self):
		self.state = 'ready'
		self.timeEnteredReady = glb.tk.getNow()
		# self.q_burst = self.burst
		# self.burst 

class ProcessTable(list):
	"""docstring for ProcessTable"""
	def __init__(self):
		super(ProcessTable, self).__init__()
		self.finishTime = 0
		self.IOutil = 0

	def __str__(self):
		#    unstarted  0   unstarted  0
		result = ''
		for el in self:
			result += ' {}'.format(el)
		return result
	
	def __repr__(self):
		# 2 (0 1 5 1) (0 1 5 1) 
		result = str(len(self))
		for el in self:
			result += ' {}'.format(el.__repr__())
		return result

	def sortByArrival(self):
		self.sort(key=lambda p: p.A)
		return self

	def sortByInput(self):
		self.sort(key=lambda p: p.i)
		return self

	def sortByReady(self):
		self.sort(key=lambda p: p.timeEnteredReady)
		return self

	def sortByRatio(self):
		self.sort(key=lambda p: -p.ratio())
		return self

	def sortByJob(self):
		self.sort(key=lambda p:p.C - p.runningTime)
		return self

	def finished(self):
		for p in self:
			if p.state != 'terminated':
				return False
		self.finishTime = glb.tk.getNow() - 1
		return True

	def getAll(self, f):
		result = ProcessTable()
		for p in self:
			if f(p):
				result.append(p)
		return result

	def tickAll(self):
		if len(self.getAll(lambda p: p.state == 'blocked')) > 0:
			self.IOutil += 1
		for p in self:
			p.tick()

	def updateStateAll(self):
		for p in self:
			p.updateState()

	def printSummaryAll(self):
		self.sortByArrival()
		psl = len(self)
		finishTime = self.finishTime
		CPUutil = sum(list([p.runningTime for p in self])) / finishTime
		IOutil = self.IOutil / finishTime
		Throughput = 100*psl/finishTime
		avgTurnaround = sum(list([p.turnaroundTime for p in self])) / psl
		avgWaiting = sum(list([p.waitingTime for p in self])) / psl
		for i, p in enumerate(self):
			print('Process {}:'.format(i))
			p.printSummary()
		print('''Summary Data:
	Finishing time: {}
	CPU Utilization: {:.6f}
	I/O Utilization: {:.6f}
	Throughput: {:.6f} processes per hundred cycles
	Average turnaround time: {:.6f}
	Average waiting time: {:.6f}\n''' \
				.format(finishTime, CPUutil, IOutil, Throughput, avgTurnaround, avgWaiting))


