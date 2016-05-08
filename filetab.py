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

class FileTab ( Gtk.Box ):
	
	__image = None
	__label = None
	file_name = ""
	__changed__ = False
	
	def __init__ ( self, label, src, new_file=False ):
		self.file_name = label
		self.__label = self.get_bare_name ( label )
		self.src = src
		
		super( FileTab, self ).__init__ ( )
		
		self.__image = Gtk.Image.new_from_file ( "window-close.png" )
		
		self.label_gtk = Gtk.Label ( self.__label )
		self.new_file = new_file
		
		self.add ( self.label_gtk )
		
		self.button_gtk = Gtk.Button ( )
		
		self.button_gtk.set_image ( self.__image )
		self.button_gtk.set_image_position ( 2 )
		self.add ( self.button_gtk )
		
		self.set_spacing ( 6 )
		
		self.set_can_focus ( False )
		self.set_can_default ( False )
		
		self.show_all ( )
		
	def get_bare_name ( self, __in ):
		i = __in.rfind ( "/" )
		if ( i == -1 ):
			return __in
		return __in [ i + 1: ]
	
	def get_label ( self ):
		return self.label_gtk.get_text ( )
	
	def get_file ( self ):
		return self.file_name
	
	def changed ( self ):
		self.label_gtk.set_markup ( "<span color=\"#FF0000\">%s</span>" % self.__label )
		self.__changed__ = True
	
	def save ( self, button ):
		self.label_gtk.set_text ( self.__label )
		self.__changed__ = False
	
	def rename ( self, new_name ):
		file_name = new_name
		self.new_file = False
		self.__label = self.get_bare_name ( new_name )
		self.label_gtk.set_text ( self.__label )
	
	def get_buff ( self ):
		return self.src.get_buffer ( )
	
	def get_src ( self ):
		return self.src
