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

import filetab, filemanager, builderset

def on_key_function ( widget, event ):
	
	if event.keyval == 65307: # ESC
		widget.hide ( )

class Project:
	file_names = []
	file_types = []
	
	def __init__ ( self, start_doc, _dir, _type, signals ):
		GObject.type_register ( GtkSource.View )
		
		self.builders = builderset.BuilderSet ( _dir )
		
		self.builders.new ( "main.ui" )
		self.builders [ "main.ui" ].connect_signals ( signals )
		
		self.MainWindow = self.builders [ "main.ui" ].get_object ( "main" )
		self.file_chooser = self.builders [ "main.ui" ].get_object ( "filechooser" )
		
		self.MainWindow.set_icon_from_file ( "icon.png" )
		
		self.file_chooser.connect ( "key-press-event", on_key_function )
		
		self.file_chooser.set_transient_for ( self.MainWindow )
		
		self.files = filemanager.FileManager ( self.builders [ "main.ui" ].get_object ( "main_box" ) )
		
		self.open ( start_doc, _type )
		
		self.accel_group = Gtk.AccelGroup ( )
		self.builders [ "main.ui" ].get_object ( "open" ).add_accelerator("activate", self.accel_group, ord('o'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "save" ).add_accelerator("activate", self.accel_group, ord('s'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "quit" ).add_accelerator("activate", self.accel_group, ord('q'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "reload" ).add_accelerator("activate", self.accel_group, ord('r'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "redo" ).add_accelerator("activate", self.accel_group, ord('y'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "undo" ).add_accelerator("activate", self.accel_group, ord('z'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "cut" ).add_accelerator("activate", self.accel_group, ord('x'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "copy" ).add_accelerator("activate", self.accel_group, ord('c'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.builders [ "main.ui" ].get_object ( "paste" ).add_accelerator("activate", self.accel_group, ord('v'), Gdk.ModifierType.CONTROL_MASK, Gtk.AccelFlags.VISIBLE)
		self.MainWindow.add_accel_group ( self.accel_group )
		
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
