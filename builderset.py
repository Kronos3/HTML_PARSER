#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  builderset.py
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

class BuilderSet ( object ):
	
	builder_dict = {}
	
	def __init__ ( self, directory ):
		self.directory = directory
	
	def new ( self, __file ):
		builder_buff = Gtk.Builder ( )
		builder_buff.add_from_file ( "%s/%s" % ( self.directory, __file ) )
		self.builder_dict [ __file ] = builder_buff
	
	def __getitem__ ( self, __name ):
		try:
			self.builder_dict [ __name ]
		except KeyError:
			print ( "Builder not initialized: '%s'" % __name )
			return
		
		return self.builder_dict [ __name ]
