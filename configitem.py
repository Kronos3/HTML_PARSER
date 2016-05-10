#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  configitem.py
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

import filemanager, builderset, project, configfile

class ConfigItem ( Gtk.Box ):
	
	items = []
	
	def __init__ ( self ):
		Gtk.Box.__init__ ( self, orientation=Gtk.Orientation.VERTICAL, spacing=6 )
		self.new_button = Gtk.Button.new_from_icon_name ( "gtk-new", Gtk.IconSize.BUTTON )
		self.new_button.set_always_show_image ( True )
	
	def add_items ( self, paths ):
		paths = list ( paths )
		print ( paths )
		self.forall ( self.remove )
		for p in paths:
			self.add_item ( p )
		self.add ( self.new_button )
		self.show_all ( )
	
	def add_item ( self, file_path ):
		buff_item = configfile.ConfigFile ( file_path )
		self.items.append ( buff_item )
		self.add ( buff_item )
	
	def index_from_item ( self, item ):
		for i in items:
			if i == item:
				return items.index ( i )
		return None
