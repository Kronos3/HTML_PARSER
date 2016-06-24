#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  HTMLParser.py
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

import parser, parserconfig, template
import sys, os

class HtmlParser:
	
	template   = None
	config     = None
	parsed     = []
	
	def __init__ (self, config):
		if (isinstance (config, parserconfig.ParserConfig)):
			self.config = config
		elif (isinstance (config, str)):
			self.config = parserconfig.ParserConfig (config)
		else:
			raise TypeError ("Argument 'config' must be an instance of ParserConfig or str")
		
		for _file in self.config ["input_files"]:
			self.parsed.append (parser.Parser (self.config, _file).out_file)
		
		# Initialize the template
		self.template = template.Template (self.config)
		
		for num, _file in enumerate (self.parsed):
			title = self.config["title"][num]
			self.write (self.config ["output_files"][num], self.template.get_body (_file, title))
		
	
	def write (self, name, ls):
		os.system ("echo -e \"\n\" > %s" % name)
		b_file = open (name, "w+", encoding="utf-8")
		for line in ls:
			b_file.write (line.replace("\n", "") + "\n")
		
		b_file.close()

if __name__ == '__main__':
	MAIN = HtmlParser (sys.argv[1])
