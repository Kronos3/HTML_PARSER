#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  htmlparser.py
#  
#  Copyright 2016 Andrei Tumbar <atuser@Kronos>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


class HtmlParser:
	
	config = None
	in_file = ""
	out_file = []
	
	def __init__ (self, config, in_file):
		self.in_file = in_file
		self.config = config
		
		file_b = open(in_file, "r").readlines()
		
		for line in file_b:
			buff_line = line
			
			get_esc_start = [c.start() for c in re.finditer(self.config["start_esc"], line)]
			get_esc_end = [c.start() for c in re.finditer(self.config["end_esc"], line)]
			
			esc_strs = self.get_str (line, get_esc_start, get_esc_end)
			
			for esc in esc_strs:
				buff_line = self.parse (buff_line)
	
	def get_str (self, string, ls_one, ls_two):
		if len(ls_one) != len(ls_two):
			raise TypeError ("Length of first list is not equal to that of the second list!")
		
		out_buff = []
		x = 0
		while x != len(ls_one):
			curr_s = ls_one [x]
			curr_e = ls_two [x]
			
			out_buff.append (string[curr_s:curr_e])
			x += 1
		
		return out_buff
	
	def parse (self, string):
		in_esc = False
		curr_esc = None
		esc = False
		
