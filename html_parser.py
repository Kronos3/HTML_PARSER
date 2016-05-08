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
import filetab, filemanager, builderset, project, configitem, configfile

class main:
	
	template = ""
	config = ""
	pages = []
	other = []
	
	def __init__ ( self, start_file="src/parser.cpp", _dir="src/gui", start_type="input" ):
		start_file = os.path.dirname ( os.path.realpath ( __file__ ) ) + "/" + start_file
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

def new_page ( button ):
	MAIN.project.files.new_file ( )

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
	open_file ( MAIN.project.file_chooser.get_filename ( ) )

def save_file ( button ):
	TAB = MAIN.project.files.get_page ( )
	
	if ( TAB.new_file ):
		save_as_open ( button )
		return
	
	if ( TAB.__changed__ ):
		buff = MAIN.project.files.tabs [ MAIN.project.files.notebook.get_current_page ( ) ].get_buff ( )
		text = buff.get_text ( buff.get_start_iter ( ), buff.get_end_iter ( ), True )
		curr_file = open ( TAB.file_name, "w+" )
		curr_file.truncate ( )
		curr_file.write ( text )
		TAB.save ( button )
	MAIN.project.log.set_text ( "Saved %s" % TAB.file_name )

def reload_file ( button ):
	MAIN.project.files.reload ( )
	MAIN.project.log.set_text ( "Reloaded %s" % TAB.file_name )

def redo ( button ):
	MAIN.project.files.redo ( )

def undo ( button ):
	MAIN.project.files.undo ( )

def cut ( button ):
	MAIN.project.files.cut ( )

def copy ( button ):
	MAIN.project.files.copy ( )

def paste ( button ):
	MAIN.project.files.paste ( )

def close_doc ( button ):
	TAB = MAIN.project.files.get_page ( )
	MAIN.project.files.close_file ( TAB.button_gtk, False )
	MAIN.project.log.set_text ( "Closed %s" % TAB.file_name )

def close_other ( button ):
	TAB = MAIN.project.files.get_page ( )
	for t in MAIN.project.files.tabs[::-1]:
		if ( t != TAB ):
			MAIN.project.close_file ( t.button_gtk, False )
	MAIN.project.log.set_text ( "Closed all files except %s" % TAB.file_name )

def close_all ( button ):
	for t in MAIN.project.files.tabs[::-1]:
		MAIN.project.files.close_file ( t.button_gtk, False )
	MAIN.project.log.set_text ( "Closed All Files" )

def save_as_open ( button ):
	MAIN.project.save_as.show_all ( )

def save_as_close ( button ):
	MAIN.project.save_as.hide ( )

def save_as ( button ):
	new_file = MAIN.project.save_as.get_filename ( )
	file_buff = open ( new_file, "w+" )
	buff = MAIN.project.files.get_buff ( )
	file_buff.write ( buff.get_text ( buff.get_start_iter ( ), buff.get_end_iter ( ), True ) )
	tab = MAIN.project.files.get_page ( )
	tab.rename ( new_file )
	save_as_close ( button )

def open_file_recent ( dialogue ):
	recent = dialogue.get_current_uri ( ).replace ( "file://", "" )
	open_file ( recent )

main_handlers = {
"exit": Gtk.main_quit,
"new_page": new_page,
"temp_ok": temp_ok,
"temp_cancel": temp_cancel,
"open": __open__,
"file_changed": file_changed,
"close_file_dia": close_file_dia,
"open_file": open_file_sig,
"save_file": save_file,
"reload": reload_file,
"redo": redo,
"undo": undo,
"cut": cut,
"copy": copy,
"paste": paste,
"close_doc": close_doc,
"close_other": close_other,
"close_all": close_all,
"save_as": save_as,
"save_as_close": save_as_close,
"save_as_open": save_as_open,
"open_file_recent": open_file_recent
}

global MAIN
MAIN = main ( )

Gtk.main ( )
