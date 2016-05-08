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

import filetab, project, builderset, configitem, configfile

class FileManager:
	
	tabs = []
	
	clipboard = None
	
	def __init__ ( self, _main_box, log ):
		self.main_box = _main_box
		self.log = log
		self.notebook = Gtk.Notebook ( )
		self.main_box.add ( self.notebook )
		self.clipboard = Gtk.Clipboard.get_default ( Gdk.DisplayManager.get ( ).get_default_display ( ) )
		self.notebook.connect ( "page-reordered", self.reordered )
	
	def get_bare_name ( self, string ):
		i = string.rfind ( "/" )
		return string [ i + 1: ]
	
	def close_file ( self, button, sig=True ):
		__file = button.get_parent ( ).get_label ( )
		if ( sig == True ):
			self.log.set_text ( "Closed %s" % button.get_parent ( ).file_name )
		tab = self.tabs.index ( button.get_parent ( ) )
		self.tabs.remove ( self.tabs [ tab ] )
		self.notebook.remove_page ( tab )
		self.notebook.show_all ( )
		self.set_reorder ( )
	
	def set_reorder ( self ):
		for t in range ( len ( self.tabs ) ):
			curr_child = self.notebook.get_nth_page ( t )
			self.notebook.set_tab_reorderable ( curr_child, True )
	
	def reordered ( self, notebook, tab, num ):
		tab_buff = self.tabs
		self.tabs = []
		for t in range ( len ( tab_buff ) ):
			curr_child = self.notebook.get_nth_page ( t )
			self.tabs.append ( self.notebook.get_tab_label ( curr_child ) )
	
	def changed ( self, buff ):
		src = self.get_src_from_buff ( buff )
		index = self.get_index_from_buff ( buff )
		
		try:
			file_buff = open ( src.file_name, "r" ).read ( )
		except FileNotFoundError:
			self.tabs [ index ].changed ( )
			return
		else:
			file_buff = open ( src.file_name, "r" ).read ( )
		text = buff.get_text ( buff.get_start_iter ( ), buff.get_end_iter ( ), True )
		if ( text != file_buff ):
			self.tabs [ index ].changed ( )
		else:
			self.tabs [ index ].save ( Gtk.Button ( ) )
	
	def new_file ( self ):
		buffer = GtkSource.Buffer ( )
		buffer.can_redo ( )
		buffer.can_undo ( )
		buffer.place_cursor ( buffer.get_start_iter ( ) )
		SOURCE = GtkSource.View.new_with_buffer ( buffer )
		SOURCE.set_auto_indent ( True )
		SOURCE.set_indent_on_tab ( True )
		SOURCE.set_show_line_numbers ( True )
		SOURCE.set_highlight_current_line ( True )
		SOURCE.set_draw_spaces ( GtkSource.DrawSpacesFlags.SPACE )
		SOURCE.set_draw_spaces ( GtkSource.DrawSpacesFlags.TAB )
		
		fontdesc = Pango.FontDescription ( "Monospace 10" )
		SOURCE.override_font ( fontdesc )
		
		SOURCE.set_tab_width ( 4 )
		
		curr_scrolled = Gtk.ScrolledWindow ( )
		curr_scrolled.add ( SOURCE )
		curr_scrolled.set_hexpand ( True )
		curr_scrolled.set_vexpand ( True )
		
		tab = filetab.FileTab ( "untitled", SOURCE, True )
		
		tab.set_tooltip_text ( "untitled" )
		
		tab.button_gtk.connect ( "clicked", self.close_file )
		buffer.connect ( "changed", self.changed )
		
		self.tabs.insert ( 0, tab )
		
		SOURCE.set_bottom_margin ( 20 )
		
		self.notebook.prepend_page ( curr_scrolled, tab )
		self.notebook.show_all ( )
		self.notebook.set_current_page ( 0 )
		self.log.set_text ( "Opened %s" % tab.file_name )
		self.set_reorder ( )
	
	def reload ( self ):
		index = self.notebook.get_current_page ( )
		__file = open ( self.file_n [ index ], "r" ).read ( )
		buff = self.buffers [ index ]
		buff.set_text ( __file )
	
	def redo ( self ):
		self.get_buff ( ).redo ( )
	
	def undo ( self ):
		self.get_buff ( ).undo ( )
	
	def cut ( self ):
		buff = self.get_buff ( )
		buff.cut_clipboard ( self.clipboard, buff.get_text ( buff.get_start_iter ( ), buff.get_end_iter ( ), True ) )
	
	def copy ( self ):
		self.get_buff ( ).copy_clipboard ( self.clipboard )
	
	def paste ( self ):
		buff = self.get_buff ( )
		if ( len ( buff.get_selection_bounds ( ) ) > 0 ):
			buff.paste_clipboard ( self.clipboard, buff.get_selection_bounds ( ) [ 0 ], True )
		else:
			buff.paste_clipboard ( self.clipboard, buff.get_iter_at_mark ( buff.get_insert ( ) ), True )
	
	def open ( self, __file ):
		lm = GtkSource.LanguageManager.new ( )
		language = lm.guess_language ( __file, None )
		buffer = GtkSource.Buffer ( )
		buffer.can_redo ( )
		buffer.can_undo ( )
		
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
		
		style = sm.get_scheme ( "oblivion_new" )
		buffer.set_style_scheme ( style )
		
		SOURCE = GtkSource.View.new_with_buffer ( buffer )
		SOURCE.set_auto_indent ( True )
		SOURCE.set_indent_on_tab ( True )
		SOURCE.set_show_line_numbers ( True )
		SOURCE.set_highlight_current_line ( True )
		SOURCE.set_draw_spaces ( GtkSource.DrawSpacesFlags.SPACE )
		SOURCE.set_draw_spaces ( GtkSource.DrawSpacesFlags.TAB )
		
		fontdesc = Pango.FontDescription ( "Monospace 10" )
		SOURCE.override_font ( fontdesc )
		
		SOURCE.set_tab_width ( 4 )
		
		curr_scrolled = Gtk.ScrolledWindow ( )
		curr_scrolled.add ( SOURCE )
		curr_scrolled.set_hexpand ( True )
		curr_scrolled.set_vexpand ( True )
		
		tab = filetab.FileTab ( __file, SOURCE )
		
		tab.set_tooltip_text ( __file )
		
		tab.button_gtk.connect ( "clicked", self.close_file )
		buffer.connect ( "changed", self.changed )
		
		self.tabs.insert ( 0, tab )
		
		SOURCE.set_bottom_margin ( 20 )
		
		self.notebook.prepend_page ( curr_scrolled, tab )
		self.notebook.show_all ( )
		self.notebook.set_current_page ( 0 )
		self.log.set_text ( "Opened %s" % tab.file_name )
		self.set_reorder ( )
	
	def get_index ( self ):
		return self.notebook.get_current_page ( )
	
	def get_page ( self ):
		return self.tabs [ self.get_index ( ) ]
	
	def get_buff ( self ):
		return self.tabs [ self.get_index ( ) ].get_buff ( )
	
	def get_src_from_buff ( self, buff ):
		for t in self.tabs:
			if ( t.get_buff ( ) == buff ):
				return t
	
	def get_index_from_buff ( self, buff ):
		for t in self.tabs:
			if ( t.get_buff ( ) == buff ):
				return self.tabs.index ( t )
