#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filemanager.py
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

import filetab, project, builderset

class FileManager:
	
	buffers = []
	labels = []
	
	def __init__ ( self, _main_box ):
		self.main_box = _main_box
		self.notebook = Gtk.Notebook ( )
		self.main_box.add ( self.notebook )
	
	def get_bare_name ( self, string ):
		i = string.rfind ( "/" )
		return string [ i + 1: ]
	
	def close_file ( self, button ):
		if button.__changed__:
			__file = button.get_label ( ) [ :-1 ]
		else:
			__file = button.get_label ( )
		self.notebook.remove_page ( self.labels.index ( __file ) )
		self.tabs.remove ( self.tabs [ self.labels.index ( __file ) ] );
		self.buffers.remove ( self.buffers [ self.labels.index ( __file ) ] );
		self.labels.remove ( __file );
		self.notebook.show_all ( )
	
	def open ( self, __file ):
		lm = GtkSource.LanguageManager.new ( )
		language = lm.guess_language ( __file, None )
		buffer = GtkSource.Buffer ( )
		
		if language:
			buffer.set_highlight_syntax ( True )
			buffer.set_language ( language )
		else:
			print ( "No language found for file '%s'" % __file )
			print ( "Using first line program" )
			
			buff = open ( __file, "r" ).readlines ( ) [ 0 ]
			try:
				buff.split ( " " ) [ 1 ]
			except IndexError:
				slash = buff.rfind ( "/" )
				if ( slash == -1 ):
					print ( "Language not found!" )
					buffer.set_highlight_syntax ( False )
				else:
					lan_name = buff [ slash + 1: ]
					language = lm.guess_language ( "a.%s" % lan_name, None )
					buffer.set_highlight_syntax ( True )
					buffer.set_language ( language )
			else:
				lan_name = buff.split ( " " ) [ 1 ]
				lan_name = lan_name.replace ( "\n", "" )
				if ( lan_name == "perl" ):
					lan_name = "pl"
				elif ( lan_name == "python3" or lan_name == "python" ):
					lan_name = "py"
				
				file_name = "a.%s" % lan_name
				
				language = lm.guess_language ( file_name, None )
				buffer.set_highlight_syntax ( True )
				buffer.set_language ( language )
		
		buff_txt = open ( __file ).read ( )
		buffer.set_text ( buff_txt )
		buffer.place_cursor ( buffer.get_start_iter ( ) )
		sm = GtkSource.StyleSchemeManager.new ( )
		sm.append_search_path ( os.path.dirname ( os.path.realpath ( __file__ ) ) )
		
		style = sm.get_scheme ( "solarizeddark" )
		buffer.set_style_scheme ( style )
		
		SOURCE = GtkSource.View.new_with_buffer ( buffer )
		SOURCE.set_auto_indent ( True )
		SOURCE.set_indent_on_tab ( True )
		SOURCE.set_show_line_numbers ( True )
		SOURCE.set_highlight_current_line ( True )
		
		fontdesc = Pango.FontDescription ( "Monospace 10.5" )
		SOURCE.override_font ( fontdesc )
		
		SOURCE.set_tab_width ( 4 )
		
		curr_scrolled = Gtk.ScrolledWindow ( )
		curr_scrolled.add ( SOURCE )
		curr_scrolled.set_hexpand ( True )
		curr_scrolled.set_vexpand ( True )
		
		tab = filetab.FileTab ( __file )
		
		tab.connect ( "clicked", self.close_file )
		buffer.connect ( "changed", tab.changed )
		
		self.tabs = []
		self.tabs.insert ( 0, tab )
		
		self.labels.insert ( 0, self.get_bare_name ( __file ) )
		self.buffers.insert ( 0, buffer )
		
		self.notebook.prepend_page ( curr_scrolled, tab )
		self.notebook.show_all ( )
		self.notebook.set_current_page ( 0 )
