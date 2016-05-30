#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  configfile.py
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

import filemanager, builderset, project

class ConfigFile ( Gtk.Box ):
	full_path = ""
	filename = ""
	
	notebook = None
	
	def __init__ ( self, file_path, notebook, __open=True ):
		self.notebook = notebook
		
		Gtk.Box.__init__ ( self, spacing=3 )
		self.open_button = Gtk.Button.new ()
		self.remove_button = Gtk.Button.new ()
		
		self.open_icon = Gtk.Image.new_from_stock ( "gtk-open", Gtk.IconSize.BUTTON )
		self.remove_icon = Gtk.Image.new_from_stock ( "gtk-remove", Gtk.IconSize.BUTTON )
		
		self.open_button.set_image (self.open_icon)
		self.remove_button.set_image (self.remove_icon)
		
		self.open_button.set_always_show_image ( True )
		self.remove_button.set_always_show_image ( True )
		
		self.file_label = Gtk.Label ( )
		self.full_path = file_path
		self.set_tooltip_text ( self.full_path )
		self.filename = self.get_bare_name ( self.full_path )
		self.file_label.set_text ( self.filename )
		
		self.add ( self.file_label )
		self.pack_end ( self.remove_button, False, False, 0 )
		
		if ( __open ):
			self.pack_end ( self.open_button, False, False, 0 )
		
		self.open_button.connect ( "clicked", self.open )
		self.remove_button.connect ( "clicked", self.__destroy )
		
	def get_bare_name ( self, __in ):
		i = __in.rfind ( "/" )
		if ( i == -1 ):
			return __in
		return __in [ i + 1: ]
	
	def open ( self, button ):
		self.notebook.open ( self.full_path )
	
	def __destroy ( self, button ):
		self.destroy ( )
