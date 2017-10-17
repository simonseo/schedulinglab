#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: scheduler.py
# @Created:   2017-10-13 18:57:02  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 05:44:53  Simon Seo (simon.seo@nyu.edu)
import sys
from copy import deepcopy as copy
import glb
from process import Process, ProcessTable
from util import Random, parseInput
from algorithms import *

def main():
	ps = ProcessTable()
	pspecs = parseInput(glb.f)
	for i in range(len(pspecs)):
		ps.append(Process(*pspecs[i], i))
	print('The original input was: {} '.format(ps.__repr__()))
	ps.sortByArrival()
	print('The (sorted) input is:  {} \n'.format(ps.__repr__()))

	if glb.v:
		print('This detailed printout gives the state and remaining burst for each process\n')

	# FCFS(copy(ps))
	RR(copy(ps), quantum=2)
	# SJF(copy(ps))
	# HPRN(copy(ps))
	# print(ps) # same as ps.__str__()


if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.argv.append('--verbose')
		sys.argv.append('--show-random')
		sys.argv.append('input/input-4.txt')
	glb.init()
	glb.v = '--verbose' in sys.argv
	glb.sr = '--show-random' in sys.argv
	glb.f = sys.argv[-1]
	glb.r = Random('random-numbers.txt')
	main()