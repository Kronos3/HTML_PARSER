#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

os.chdir ( os.path.dirname ( os.path.realpath ( __file__ ) ) )
import filetab, filemanager, builderset, project

class main:
	
	template = ""
	config = ""
	pages = []
	other = []
	
	def __init__ ( self, start_file="src/parser.cpp", _dir="src/gui", start_type="input" ):
		self.project = project.Project ( start_file, _dir, start_type, main_handlers )
		
		if ( start_type == "input" ):
			self.pages.append ( start_file )
		elif ( start_type == "template" ):
			self.template = start_file
		elif ( start_type == "config" ):
			self.config = start_file
		elif ( start_type == "other" ):
			self.other.append ( start_file )
		else:
			raise ValueError ( "The following is not a valid file type: '%s'" % start_type )

def new_template ( button ):
	MAIN.project.builders [ "main.ui" ].get_object ( "temp_name" ).set_text ( "" )
	MAIN.project.TemplateWindow.show_all ( )

def new_page ( button ):
	pass
	
def temp_ok ( button ):
	template_name = MAIN.project.builders [ "main.ui" ].get_object ( "temp_name" ).get_text ( )
	
	# Create the empty file
	open(template_name, 'a').close()
	
	MAIN.project.files.open ( template_name )
	MAIN.project.TemplateWindow.hide ( )

def temp_cancel ( button, *args ):
	MAIN.project.TemplateWindow.hide ( )

def __open__ ( button ):
	MAIN.project.file_chooser.show_all ( )

def file_changed ( file_dialog ):
	__file = file_dialog.get_filename ( )
	open_file ( __file )

def close_file_dia ( button ):
	MAIN.project.file_chooser.hide ( )

def open_file ( __file ):
	type_chooser = MAIN.project.builders [ "main.ui" ].get_object ( "type_chooser" )
	
	type_id = type_chooser.get_model ( ) [ type_chooser.get_active ( ) ] [ 1 ]
	
	MAIN.project.open ( __file, type_id )
	MAIN.project.file_chooser.hide ( )

def open_file_sig ( button ):
	open_file ( MAIN.project.builders [ "main.ui" ].get_object ( "filechooser" ).get_filename ( ) )

def save_file ( button ):
	TAB = MAIN.project.files.tabs [ MAIN.project.files.notebook.get_current_page ( ) ]
	buff = MAIN.project.files.buffers [ MAIN.project.files.notebook.get_current_page ( ) ]
	text = buff.get_text ( buff.get_start_iter ( ), buff.get_end_iter ( ), True )
	curr_file = open ( TAB.file_name, "w+" )
	curr_file.truncate ( )
	curr_file.write ( text )
	TAB.save ( button )

main_handlers = {
"exit": Gtk.main_quit,
"template": new_template,
"page": new_page,
"temp_ok": temp_ok,
"temp_cancel": temp_cancel,
"open": __open__,
"file_changed": file_changed,
"close_file_dia": close_file_dia,
"open_file": open_file_sig,
"save_file": save_file,
}

global MAIN
MAIN = main ( )

Gtk.main ( )
