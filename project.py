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

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import Gtk, GObject, GLib, GtkSource, Pango, Gdk
from gi.repository.GdkPixbuf import Pixbuf

import filetab, filemanager, builderset, configitem, configfile

def on_key_function ( widget, event ):
	
	if event.keyval == 65307: # ESC
		widget.hide ( )

class Project:
	file_names = []
	file_types = []
	
	config_file = ""
	template_file = ""
	
	def __init__ ( self, start_doc, _dir, _type, signals ):
		GObject.type_register ( GtkSource.View )
		
		self.builders = builderset.BuilderSet ( _dir )
		
		self.builders.new ( "main.ui" )
		self.builders [ "main.ui" ].connect_signals ( signals )
		
		self.MainWindow = self.builders [ "main.ui" ].get_object ( "main" )
		self.file_chooser = self.builders [ "main.ui" ].get_object ( "filechooser" )
		self.save_as = self.builders [ "main.ui" ].get_object ( "savedialogue" )
		self.log = self.builders [ "main.ui" ].get_object ( "log_info" )
		
		self.MainWindow.set_icon_from_file ( "icon.png" )
		
		self.file_chooser.connect ( "key-press-event", on_key_function )
		
		self.file_chooser.set_transient_for ( self.MainWindow )
		
		self.files = filemanager.FileManager ( self.builders [ "main.ui" ].get_object ( "main_box" ), self.log )
		
		self.builders [ "main.ui" ].get_object ( "new_tool" )
		
		#pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
		
		self.open ( start_doc, _type )
		
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
		
		self.MainWindow.add_accel_group ( self.accel_group )
		
		self.init_switch ( )
		
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
