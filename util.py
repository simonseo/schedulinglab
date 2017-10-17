#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: util.py
# @Created:   2017-10-16 11:31:40  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 13:22:23  Simon Seo (simon.seo@nyu.edu)
import glb
import os

class Timekeeper():
	"""Tracks time for all processes"""
	def __init__(self):
		self.now = 0
	def tick(self):
		self.now += 1
	def getNow(self):
		return self.now

class Random():
	"""Random variable generator"""
	def __init__(self, filename):
		if not os.path.isfile(filename):
			raise Exception('The input file does not exist. The input filename should be the last argument.')
		self.file = open(filename,'r')
	def randInt(self):
		return int(self.file.readline().strip())
	def randomOS(self, U):
		randInt = self.randInt()
		if glb.sr:
			print('Find burst when choosing ready process to run', randInt)
		return 1 + randInt % U

def parseInput(filename):
	"""returns list of process specs"""
	result = []
	if not os.path.isfile(filename):
		raise Exception('The input file does not exist. The input filename should be the last argument.')
	with open(filename, 'r') as f:
		nums = []
		for l in f:
			nums += [int(el) for el in l.strip().split() if el.isnumeric()]
	psl = nums.pop(0) #processes (list) length
	for i in range(psl):
		result.append(nums[4*i:4*i+4])
	return result

		