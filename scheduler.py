#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: scheduler.py
# @Created:   2017-10-13 18:57:02  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-16 13:49:57  Simon Seo (simon.seo@nyu.edu)
import sys
from process import Process, ProcessTable
from util import Timekeeper, Random, parseInput

def main():
	tk = Timekeeper()
	r = Random('random-numbers.txt')
	ps = ProcessTable()
	infilename = sys.argv[-1]
	pspecs = parseInput(infilename)
	for i in range(len(pspecs)):
		ps.append(Process(*pspecs[i], i))
	print(ps) # same as ps.__str__()
	print('The original input was:', ps.__repr__())




if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.argv.append('--verbose')
		sys.argv.append('input/input-4.txt')
	debug = True if '--verbose' in sys.argv else False
	main()