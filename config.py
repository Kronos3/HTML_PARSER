#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
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

import os, sys

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import Gtk, GObject, GLib, GtkSource, Pango, Gdk

os.chdir ( os.path.dirname ( os.path.realpath ( __file__ ) ) )
import filetab, filemanager, builderset, project, configitem, configfile

class Config:
	
	config_file_relative = ""
	config_file_full = ""
	
	__file_lines = None
	__file = None
	
	var_dict = {}
	list_vars = [ "output_files", "input_files", "title", "css", "js" ]
	
	variables_box = Gtk.Box ( )
	configitems = []
	
	def __init__ ( self, curr_dir, config ):
		self.dir = curr_dir
		
		self.config_file_relative = config
		self.config_file_full = self.get_path ( config )
		
		self.__file_lines = open ( self.config_file_relative, "r" ).readlines ( )
		self.input = configitem.ConfigItem ( )
		self.output = configitem.ConfigItem ( )
		self.title = configitem.ConfigItem ( )
		self.css = configitem.ConfigItem ( )
		self.js = configitem.ConfigItem ( )
		
		for l in self.__file_lines:
			if l [ 0 ] == "#" or l == "" or l == "\n":
				continue
			var, val = l.split ( "=" )
			# Remove the whitespace
			var = var.strip ( )
			val = val.strip ( )
			
			self.var_dict [ var ] = val
			
			if var in self.list_vars:
				self.var_dict [ var ] = val.split ( "," )
		
		for var in self.list_vars:
			buff = self.var_dict [ var ]
			print ( buff )
			exec ( "self.%s.add_items ( buff )" % var.replace ( "_files", "" ) ) 
		
		self.variables_box.add ( self.title )
		self.variables_box.add ( self.css )
		self.variables_box.add ( self.js )
	
	def get_path ( self, _in ):
		if self.dir [ -1 ] == "/":
			return self.dir + _in
		return self.dir + "/" + _in
	
	def open_file ( self, path ):
		self.__file_lines = open ( path, "r" ).readlines ( )
		self.__file = open ( path, "w" ).readlines ( )
