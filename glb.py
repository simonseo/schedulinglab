#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: glb.py
# @Created:   2017-10-17 00:44:56  seo (simon.seo@nyu.edu) 
# @Updated:   2017-10-17 12:48:02  Simon Seo (simon.seo@nyu.edu)

def init():
	global v, sr, f, r, rf, tk, q
	v = False    #option: verbose
	sr = False   #option: show random number used
	f = ''       #input file name
	rf = 'random-numbers.txt'  #random number file name
	r = None     #random number generator object
	tk = None    #timekeeper object
	q = False    #for round robin quantum: False or q