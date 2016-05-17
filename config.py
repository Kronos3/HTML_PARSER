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
	
	notebook = None
	open_dialogue = None
	
	var_dict = {}
	var_list = []
	list_vars = [ "output_files", "input_files" ]
	conf_vars = [ "title", "css", "js" ]
	
	variables_box = Gtk.Box ( )
	configitems = []
	rows = []
	
	def __init__ ( self, curr_dir, config, notebook, open_dialogue ):
		self.open_dialogue = open_dialogue
		self.dir = curr_dir
		self.notebook = notebook
		
		self.config_file_relative = config
		self.config_file_full = self.get_path ( config )
		
		self.__file_lines = open ( self.config_file_relative, "r" ).readlines ( )
		self.input = configitem.ConfigItem ( )
		self.output = configitem.ConfigItem ( )
		
		for l in self.__file_lines:
			if l [ 0 ] == "#" or l == "" or l == "\n":
				continue
			var, val = l.split ( "=" )
			# Remove the whitespace
			var = var.strip ( )
			val = val.strip ( )
			
			self.var_dict [ var ] = val
			
			self.var_list.append ( var )
			
			if var in self.list_vars:
				self.var_dict [ var ] = val.split ( "," )
		
		for var in self.list_vars:
			buff = self.var_dict [ var ]
			exec ( "self.%s.set_notebook ( self.notebook )"  % var.replace ( "_files", "" ) )
			exec ( "self.%s.set_dialogue ( self.open_dialogue )"  % var.replace ( "_files", "" ) )
			exec ( "self.%s.add_items ( buff )" % var.replace ( "_files", "" ) ) 
		
		self.__init_vars__ ( )
		
		for var in self.var_list:
			if ( not isinstance ( self.var_dict [ var ], list ) ):
				self.add_var ( var )
	
	def get_path ( self, _in ):
		if self.dir [ -1 ] == "/":
			return self.dir + _in
		return self.dir + "/" + _in
	
	def __init_vars__ ( self ):
		self.var_store = Gtk.ListStore ( str, str )
		
		self.treeview = Gtk.TreeView.new_with_model ( self.var_store )
		
		self.var_rend = Gtk.CellRendererText ( )
		self.val_rend = Gtk.CellRendererText ( )
		
		self.val_rend.set_property('editable', True)
		
		column_1 = Gtk.TreeViewColumn ( "Variables", self.var_rend, text=0 )
		column_2 = Gtk.TreeViewColumn ( "Value", self.val_rend, text=1 )
		
		self.treeview.append_column ( column_1 )
		self.treeview.append_column ( column_2 )
	
	def add_var ( self, var ):
		self.rows.append ( self.var_store.append ( [ var, self.var_dict [ var ] ] ) )
	
	def open_file ( self, path ):
		self.__file_lines = open ( path, "r" ).readlines ( )
		self.__file = open ( path, "w" ).readlines ( )
