#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  project.py
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
import datetime
import platform

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import Gtk, GObject, GLib, GtkSource, Pango, Gdk
from gi.repository.GdkPixbuf import Pixbuf

import filetab, filemanager, builderset, configitem, configfile, config

def on_key_function ( widget, event ):
	
	if event.keyval == 65307: # ESC
		widget.hide ( )

class Project:
	file_names = []
	file_types = []
	
	config_file = ""
	template_file = ""
	
	def __init__ ( self, _dir, _type, signals, curr_dir ):
		self._dir = _dir
		
		GObject.type_register ( GtkSource.View )
		
		self.builders = builderset.BuilderSet ( self._dir )
		
		self.builders.new ( "main.ui" )
		self.builders [ "main.ui" ].connect_signals ( signals )
		
		self.MainWindow = self.builders [ "main.ui" ].get_object ( "main" )
		self.file_chooser = self.builders [ "main.ui" ].get_object ( "filechooser" )
		self.save_as = self.builders [ "main.ui" ].get_object ( "savedialogue" )
		self.recent = self.builders [ "main.ui" ].get_object ( "recent" )
		self.action_notebook = self.builders [ "main.ui" ].get_object ( "actions_notebook" )
		
		self.input_ex = self.builders [ "main.ui" ].get_object ( "input_ex" )
		self.output_ex = self.builders [ "main.ui" ].get_object ( "output_ex" )
		self.variables_scroll = self.builders [ "main.ui" ].get_object ( "var_scroll" )
		self.template_name = self.builders [ "main.ui" ].get_object ( "template_name" )
		
		self.MainWindow.set_icon_from_file ( "icon.png" )
		
		self.file_chooser.connect ( "key-press-event", on_key_function )
		self.builders [ "main.ui" ].get_object ( "filechooser_new" ).connect ( "key-press-event", on_key_function )
		self.builders [ "main.ui" ].get_object ( "filechooser_conf" ).connect ( "key-press-event", on_key_function )
		self.builders [ "main.ui" ].get_object ( "savedialogue" ).connect ( "key-press-event", on_key_function )
		
		self.file_chooser.set_transient_for ( self.MainWindow )
		
		self.add_messages ( )
		self.files = filemanager.FileManager ( self.builders [ "main.ui" ].get_object ( "main_box" ), self.log )
		
		self.builders [ "main.ui" ].get_object ( "new_tool" )
		
		self.accel_group = Gtk.AccelGroup ( )
		self.builders [ "main.ui" ].get_object ( "open" ).add_accelerator ( "activate", self.accel_group, ord ( 'o' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "new_page" ).add_accelerator ( "activate", self.accel_group, ord ( 'n' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "save" ).add_accelerator ( "activate", self.accel_group, ord ( 's' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "save_as" ).add_accelerator ( "activate", self.accel_group, ord ( 's' ), Gdk.ModifierType.SHIFT_MASK | Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "quit" ).add_accelerator ( "activate", self.accel_group, ord ( 'q' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "reload" ).add_accelerator ( "activate", self.accel_group, ord ( 'r' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "redo" ).add_accelerator ( "activate", self.accel_group, ord ( 'y' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "undo" ).add_accelerator ( "activate", self.accel_group, ord ( 'z' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "cut" ).add_accelerator ( "activate", self.accel_group, ord ( 'x' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "copy" ).add_accelerator ( "activate", self.accel_group, ord ( 'c' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "paste" ).add_accelerator ( "activate", self.accel_group, ord ( 'v' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "close_doc" ).add_accelerator ( "activate", self.accel_group, ord ( 'w' ), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "close_all" ).add_accelerator ( "activate", self.accel_group, ord ( 'w' ), Gdk.ModifierType.SHIFT_MASK | Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "open_conf" ).add_accelerator ( "activate", self.accel_group, ord ( 'o' ), Gdk.ModifierType.SHIFT_MASK | Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE )
		key, mods = Gtk.accelerator_parse ( "F9" )
		self.builders [ "main.ui" ].get_object ( "make_desk" ).add_accelerator ( "activate", self.accel_group, key, Gdk.ModifierType.SHIFT_MASK | mods, Gtk.AccelFlags.VISIBLE )
		self.builders [ "main.ui" ].get_object ( "write_conf" ).add_accelerator ( "activate", self.accel_group, key, Gdk.ModifierType.SHIFT_MASK | Gdk.ModifierType.CONTROL_MASK | mods, Gtk.AccelFlags.VISIBLE )
		f5_key, f5_mods = Gtk.accelerator_parse ( "F5" )
		self.builders [ "main.ui" ].get_object ( "write" ).add_accelerator ( "activate", self.accel_group, f5_key, f5_mods, Gtk.AccelFlags.VISIBLE )
		
		self.MainWindow.add_accel_group ( self.accel_group )
		
		self.init_switch ( )
		self.get_recent ( )
		
		self.MainWindow.show_all ( )
	
	# File types:
	#  template
	#  input
	#  config
	#  other
	def open ( self, __file, _type="input" ):
		self.files.open ( __file )
		
		self.file_names.append ( __file )
		self.file_types.append ( _type )
	
	def get_recent ( self ):
		recent_menu = self.builders [ "main.ui" ].get_object ( "recent_menu" )
		for num, uri in enumerate ( self.recent.get_uris ( ) [ :15 ] ):
			if (platform.system()[:4] == "MSYS"):
				name_buff = uri.replace ( "file://", "" )
				name_buff = name_buff[1:]
			else:
				name_buff = uri.replace ( "file://", "" )
			curr_item = Gtk.MenuItem.new_with_label ( name_buff )
			curr_item.connect ( "activate", self.open_recent )
			recent_menu.attach ( curr_item, 0, 1, num, num + 1 )
		self.builders [ "main.ui" ].get_object ( "open_recent" ).set_menu ( recent_menu )
		recent_menu.show_all ( )
	
	def open_recent ( self, item ):
		self.open ( item.get_label ( ), "other" )
	
	def get_upper ( self, __in ):
		first = __in [ 0 ].upper ( )
		return first + __in [ 1: ]
	
	def close ( self, button, sig=True ):
		self.files.close_doc ( button, sig )
	
	def init_switch ( self ):
		for x in range ( 0, 9 ):
			key, mod = Gtk.accelerator_parse("<Alt>%s" % x )
			self.accel_group.connect ( key, mod, Gtk.AccelFlags.VISIBLE, self.switch )
	
	def switch ( self, accel_group, acceleratable, keyval, modifier ):
		keyval -= 49
		if keyval == 8:
			keyval = -1
		self.files.notebook.set_current_page ( keyval )
	
	def add_messages ( self ):
		self.log = Gtk.ListStore ( str )
		
		self.treeview = Gtk.TreeView.new_with_model ( self.log )
		
		self.tree_renderer = Gtk.CellRendererText ( )
		self.scrollable_treelist = Gtk.ScrolledWindow ( )
		self.scrollable_treelist.set_vexpand ( True )
		
		self.tree_renderer.set_property('editable', True)
		column = Gtk.TreeViewColumn ( "Message", self.tree_renderer, text=0 )
		self.treeview.append_column ( column )
		
		self.scrollable_treelist.add ( self.treeview )
		
		self.action_notebook.append_page ( self.scrollable_treelist, Gtk.Label ( "Messages" ) )
	
	def add_log ( self, text ):
		__time = str ( datetime.datetime.now ( ).time ( ) ) [ :str ( datetime.datetime.now ( ).time ( ) ).find ( "." ) ]
		full_text = __time + ": " + text
		self.log.append ( [ full_text ] )
	
	def get_bare_name ( self, __in ):
		i = __in.rfind ( "/" )
		if ( i == -1 ):
			return __in
		return __in [ i + 1: ]
	
	def load_config ( self, notebook, __config=None ):
		if ( __config == None ):
			_config = ""
			for i, t in enumerate ( self.types ):
				if ( t == "config" ):
					_config = self.file_names [ i ]
			if config == "":
				raise FileNotFoundError ( "You havn't opened a config file so you must input one" )
			else:
				__config = _config
		self.__config__ = config.Config ( os.getcwd ( ), __config, notebook, self.builders [ "main.ui" ].get_object ( "filechooser_new" ) )
		self.do_config_box_reset ( )
	
	def do_config_box_reset ( self ):
		if self.builders [ "main.ui" ].get_object ( "var_scroll" ).get_child ( ):
			self.builders [ "main.ui" ].get_object ( "var_scroll" ).remove ( self.builders [ "main.ui" ].get_object ( "var_scroll" ).get_child ( ) )
		self.template_name.set_text ( self.get_bare_name ( self.__config__.var_dict [ "template" ] ) )
		self.template_name.set_tooltip_text ( self.__config__.get_path ( self.__config__.var_dict [ "template" ] ) )
		
		self.input_ex.add ( self.__config__.input )
		self.output_ex.add ( self.__config__.output )
		self.variables_scroll.add ( self.__config__.treeview )
		self.variables_scroll.show_all ( )
		
		top_box = self.builders [ "main.ui" ].get_object ( "config_box" )
		ac_note = self.builders [ "main.ui" ].get_object ( "actions_notebook" )
		self.builders [ "main.ui" ].get_object ( "curr_dir_box" ).remove ( top_box )
		self.builders [ "main.ui" ].get_object ( "curr_dir_box" ).remove ( ac_note )
		new_window = Gtk.ScrolledWindow ( )
		new_window.set_min_content_height ( 300 )
		self.builders [ "main.ui" ].get_object ( "curr_dir_box" ).pack_start ( new_window, True, True, 0 )
		self.builders [ "main.ui" ].get_object ( "curr_dir_box" ).pack_start ( ac_note, True, True, 0 )
		new_window.add ( top_box )
		self.builders [ "main.ui" ].get_object ( "curr_dir_box" ).show_all ( )
