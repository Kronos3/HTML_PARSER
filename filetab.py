#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filetab.py
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

class FileTab ( Gtk.Button ):
	
	__image = None
	__label = None
	file_name = ""
	__changed__ = False
	
	def __init__ ( self, label ):
		self.file_name = label
		self.__label = self.get_bare_name ( label )
		
		super( FileTab, self ).__init__ ( self.__label )
		
		self.__image = Gtk.Image.new_from_pixbuf ( Gtk.IconTheme.get_default ( ).load_icon ( "window-close", 64, 0 ) )
		self.set_label ( self.__label )
		
		self.set_image ( self.__image )
		self.set_image_position ( 2 )
	
	def get_bare_name ( self, __in ):
		i = __in.rfind ( "/" )
		if ( i == -1 ):
			return __in
		return __in [ i + 1: ]
	
	def changed ( self ):
		self.set_label ( "%s*" % self.__label )
		self.__changed__ = True
	
	def save ( self, button ):
		self.set_label ( self.__label )
		self.__changed__ = False
