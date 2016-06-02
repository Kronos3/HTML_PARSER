#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parserconfig.py
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


class ParserConfig:
	
	__file = ""
	cfg_path = ""
	lines = []
	var_dict = {}
	var_list = []
	
	def __init__ (self, cfg_file):
		self.cfg_path = cfg_file[:cfg_file.rfind ("/")]
		self.__file = cfg_file
		self.lines = open(self.__file, "r").readlines()
		
		for line in self.lines:
			if (line[0] == "#" or not line.strip()):
				continue
			var, val = line.replace("\n", "").split ("=")
			var = var.strip()
			val = val.strip()
			
			if ("," in val):
				val = val.split (",")
			
			self.var_list.append (var)
			self.var_dict[var] = val
	def __getitem__ (self, var):
		try:
			self.var_dict[var]
		except KeyError:
			return None
		return self.var_dict[var]
