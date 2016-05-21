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
	row_raw = []
	
	current_file = {}
	current = None
	
	def __init__ ( self, curr_dir, config, notebook, open_dialogue ):
		self.open_dialogue = open_dialogue
		self.dir = curr_dir
		self.notebook = notebook
		self.new_config ( config )
	
	def remove_config ( self ):
		self.input.destroy ( )
		self.output.destroy ( )
		self.treeview.destroy ( )
		self.var_store = None
		
		self.var_rend = None
		self.val_rend = None
		self.treeview.destroy ( )
		
		self.var_dict = {}
		self.var_list = []
		self.list_vars = [ "output_files", "input_files" ]
		self.conf_vars = [ "title", "css", "js" ]
		
		self.variables_box = Gtk.Box ( )
		self.configitems = []
		
		self.current_file = {}
		self.current = None
	
	def new_config ( self, config ):
		self.config_file_relative = config
		self.config_file_full = self.get_path ( config )
		
		self.__file_lines = open ( self.config_file_relative, "r" ).readlines ( )
		self.input = configitem.ConfigItem ( )
		self.output = configitem.ConfigItem ( )
		
		self.input.connect ( "new_config", self.get_new )
		self.output.connect ( "new_config", self.get_new )
		
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
	
	def get_new ( self, a, confitem ):
		if ( confitem == self.input ):
			self.current = "input"
		else:
			self.current = "output"
	
	def add ( self, __files ):
		if ( self.current == "input" ):
			self.input.add_items ( __files, remove=False )
		else:
			self.output.add_items ( __files, remove=False )
	
	def update_file ( self, var, val ):
		self.current_file [ var ] = val
	
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
		self.val_rend.connect ( "edited", self.vars_changes )
	
	def vars_changes ( self, renderer, path, new_text ):
		self.var_store.set ( self.var_store.get_iter ( path ), 1, new_text )
		self.var_dict [ self.var_store.get_value ( self.var_store.get_iter ( path ), 0 ) ] = new_text
		
	
	def add_var ( self, var, add_to_list=False ):
		if ( add_to_list ):
			self.var_list.append ( var )
			self.var_dict [ var ] = ""
		self.var_store.append ( [ var, self.var_dict [ var ] ] )
	
	def open_file ( self, path ):
		self.__file_lines = open ( path, "r" ).readlines ( )
		self.__file = open ( path, "w" ).readlines ( )
	
	def remove_var ( self ):
		model, treeiter = self.treeview.get_selection ( ).get_selected ( )
		
		self.var_dict.pop ( model [ treeiter ] [ 0 ], None )
		del self.var_list [ self.var_list.index ( model [ treeiter ] [ 0 ] ) ]
		self.var_store.remove ( treeiter )
	
	def get_conf_out ( self ):
		out_buff = []
		for x in self.var_list:
			buff = self.var_dict [ x ]
			if ( isinstance ( self.var_dict [ x ], list ) ):
				buff = ",".join ( self.var_dict [ x ] )
			out_buff.append ( x + " = " + buff )
		return out_buff
