#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: util.py
# @Created:   2017-10-16 11:31:40  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-16 13:40:50  Simon Seo (simon.seo@nyu.edu)


class Timekeeper():
	"""Tracks time for all processes"""
	def __init__(self):
		self.now = 0
	def tick(self, ps=None):
		self.now += 1
		if ps is not None:
			for p in ps:
				p.tick()
	def getNow(self):
		return self.now

class Random():
	"""Random variable generator"""
	def __init__(self, filename):
		self.file = open(filename,'r')
	def randInt(self):
		return int(self.file.readline().strip())
	def randomOS(self, U):
		return 1 + self.randInt() % U

def parseInput(filename):
	"""returns list of process specs"""
	result = []
	with open(filename, 'r') as f:
		nums = []
		for l in f:
			nums += [int(el) for el in l.strip().split() if el.isnumeric()]
	psl = nums.pop(0) #processes (list) length
	for i in range(psl):
		result.append(nums[4*i:4*i+4])
	return result

		