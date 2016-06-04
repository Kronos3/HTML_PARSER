#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  template.py
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

import parser, parserconfig
import sys

class Template:
	
	config = None
	template_file = []
	
	# A pointer is a variable in the template that wil point to an input file
	# Format looks like this:
	# [(variable_name, file, line_number, indent)]
	pointers = []
	parsed = []
	
	# Vars
	_vars = {}
	
	def __init__ (self, config):
		if not isinstance (config, parserconfig.ParserConfig):
			raise TypeError ("Argument 'config' is not an instance of ParserConfig")
		
		self.config = config
		self.load_template()
	
	def load_template (self):
		self.template_file = []
		self.pointers = []
		self.parsed = []
		self._vars = {}
		
		self.template_file = open(self.config["template"], "r").readlines ()
		for num,line in enumerate (self.template_file):
			curr_indent = self.get_indent (line)
			if (line[curr_indent] == "["):
				name = line.strip()[1:-1]
				__file = self.config[name]
				buff_tup = (name, __file, num, curr_indent)
				self.pointers.append (buff_tup)
		
		for var in self.pointers:
			self._vars [var[0]] = var[2]
	
	def get_indent (self, string):
		for num, x in enumerate (string):
			if x != ' ':
				return num
	
	def insert (self, original, num, insert):
		original.pop (num)
		if (isinstance (insert, list)):
			original[num:num] = insert
			return original
		
		original.insert (num, insert)
		return original
	
	def create_js (self, files):
		out = []
		for f in files:
			out.append ("<script type=\"text/javascript\" src=\"%s\"></script>" % f)
		return out
	
	def create_css (self, files):
		out = []
		for f in files:
			out.append ("<link rel=\"stylesheet\" href=\"%s\" type=\"text/css\" />" % f)
		return out
	
	def indent (self, ls, indent):
		buff = []
		for ln in ls:
			buff.append (" "*indent + ln)
		if (len(buff) == 1):
			return buff[0]
		return buff
	
	def get_body (self, file_lines, title):
		self.load_template()
		buff = []
		buff = self.template_file
		
		for key in reversed (self.pointers):
			
			if (key[0] == "BODY"):
				buff = self.insert (buff, key[2], self.indent (file_lines, key[3]))
			elif (key[0] == "TITLE"):
				buff = self.insert (buff, key[2], "%s<title>%s</title>" % (" "*key[3], title))
			elif (key[0] == "JS"):
				js = self.indent (self.create_js (self.config["js"]), key[3])
				buff = self.insert (buff, key[2], js)
			elif (key[0] == "CSS"):
				css = self.create_css (self.config["css"])
				buff = self.insert (buff, key[2], self.indent (css, key[3]))
			else:
				buff = self.insert (buff, key[2], self.indent (parser.Parser (self.config, self.config[key[0]]).out_file, key[3]))
		return buff

if __name__ == '__main__':
	b_conf = parserconfig.ParserConfig (sys.argv[1])
	buff = Template (b_conf)
