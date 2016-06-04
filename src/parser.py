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

import sys
import parserconfig

class Parser:
	
	config    =  None
	in_file   =  ""
	out_file  =  []
	
	def __init__ (self, config, in_file):
		if not isinstance (config, parserconfig.ParserConfig):
			raise TypeError ("Argument 'config' is not an instance of ParserConfig")
		
		self.in_file = in_file
		self.config  = config
		self.out_file = []
		in_file = ""
		
		
		file_b = open(self.in_file, "r").readlines()
		
		for num, line in enumerate (file_b):
			if (line.strip() [0:2] == "<!"):
				self.out_file.append (line)
				continue
			
			buff_line = line.replace ("\n", "")
			
			get_esc_start =  self.get_iters (buff_line, self.config["start_esc"])
			get_esc_end   =  self.get_iters (buff_line, self.config["end_esc"])
			
			esc_strs      =  self.get_str (buff_line, get_esc_start, get_esc_end)
			
			for esc in esc_strs:
				indent = self.get_indent(buff_line)
				buff_line =  self.parse (buff_line)
			self.out_file.append (buff_line)
	
	def get_indent (self, string):
		for num, x in enumerate (string):
			if x != ' ':
				return num
	
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
	
	def get_esc_s (self):
		return [self.config["start_esc"], self.config["start_class"], self.config["start_id"], self.config["start_style"]]
	
	def get_esc_e (self):
		return [self.config["end_esc"], self.config["end_class"], self.config["end_id"], self.config["end_style"]]
	
	def get_start (self, c):
		if (c == self.config["start_esc"]):
			return "esc"
		if (c == self.config["start_class"]):
			return "class"
		if (c == self.config["start_id"]):
			return "id"
		if (c == self.config["start_style"]):
			return "style"
	
	def get_end (self, c):
		if (c == self.config["end_esc"]):
			return "esc"
		if (c == self.config["end_class"]):
			return "class"
		if (c == self.config["end_id"]):
			return "id"
		if (c == self.config["end_style"]):
			return "style"
	
	def get_t (self, c, _def="start"):
		exec ("b_b = self.get_esc_%s ()" % _def[0])
		if b_b:
			exec ("return \"%s_\" self.get_%s (c)" % _def)
		if _def == "start":
			exec ("return \"start_\" + self.get_start (c)")
		if _def == "end":
			exec ("return \"end_\" + self.get_end (c)")
	
	def get_sigs (self, string):
		# Return a list with following contents:
		# 0: class  =  [ (start, end), (start, end), (start, end)]
		# 1: id     =  [ (start, end), (start, end), (start, end)]
		# 2: style  =  [ (start, end), (start, end), (start, end)]
		# So it will look like this:
		#              [class, id, style]
		
		__in      = {"class": False, "id": False, "style": False}
		
		_class    = []
		_id       = []
		_style    = []
		_esc      = []
		
		esc = False
		
		b_start = 0
		b_end = 0
		
		for num, c in enumerate (string):
			t = self.get_start (c)
			if t == "esc":
				esc = True
				continue
			
			if not esc:
				continue
			
			try:
				list(__in.keys())[list(__in.values()).index(True)]
			except ValueError:
				pass
			else:
				_type = self.get_end (c)
				if _type:
					if _type == "esc":
						continue
					if _type == list(__in.keys())[list(__in.values()).index(True)] and esc:
						b_end = num + 1
						exec ("_%s.append ((b_start, b_end))" % _type)
						
						__in [_type]  = False
						b_list        = []
					continue
			
			# Not in esc
			if self.get_start (c):
				_type         =  self.get_start (c)
				__in [_type]  =  True
				b_start = num
		
		return [_class, _id, _style]
	
	def get_content (self, _type, string):
		return "%s=\"%s\"" % (_type, string[1:-1])
	
	def parse (self, __string):
		string = __string
		
		_class, _id, _style = self.get_sigs (string)
		
		add = 0
		
		for x in _class:
			string = string [:x[0]+add] + self.get_content ("class", string[x[0]+add:x[1]+add]) + string[x[1]+add:]
			add += 6
		
		for x in _id:
			string = string [:x[0]+add] + self.get_content ("id", string[x[0]+add:x[1]+add]) + string[x[1]+add:]
			add += 3
		
		for x in _style:
			string = string [:x[0]+add] + self.get_content ("style", string[x[0]+add:x[1]+add]) + string[x[1]+add:]
			add += 6
		
		return string
	
	def get_iters (self, string, char):
		b_out = []
		
		for num, c in enumerate (string):
			if (c == char):
				b_out.append (num)
		
		return b_out

if __name__ == '__main__':
	b_conf = parserconfig.ParserConfig (sys.argv[1])
	buff = Parser (b_conf, sys.argv[2])
