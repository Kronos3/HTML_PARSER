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

global DIR
DIR = os.getcwd ( )

os.chdir ( os.path.dirname ( os.path.realpath ( __file__ ) ) )
import filetab, filemanager, builderset, project, configitem, configfile

class main:
	
	template = ""
	config = ""
	pages = []
	other = []
	dir = None
	
	def __init__ ( self, start_file="src/parser.cpp", _dir="src/gui", start_type="input" ):
		self.dir = DIR
		
		start_file = get_dir ( self.dir + "/" + start_file )
		self.project = project.Project ( start_file, _dir, start_type, main_handlers, self.dir )
		self.project.load_config ( self.project.files, "parser.cfg" )
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

def get_dir ( in_dir ):
	in_buff = in_dir.split ( "/" )
	out_buff = []
	for i, x in enumerate ( in_buff ):
		if ( x != ".." ):
			try:
				in_buff [ i + 1 ]
			except IndexError:
				out_buff.append ( x )
			else:
				if ( in_buff [ i + 1 ] != ".." ):
					out_buff.append ( x )
	return "/".join ( out_buff )

def new_page ( button ):
	MAIN.project.files.new_file ( )
	MAIN.project.add_log ( "File untitled opened" )

def __open__ ( button ):
	if len ( MAIN.project.files.tabs ) > 0 and MAIN.project.files.get_page ( ).get_label ( ) != "untitled":
		file_dir = get_dir ( MAIN.project.files.get_page ( ).get_file ( ) )
		MAIN.project.file_chooser.set_current_folder ( file_dir [ :file_dir.rfind ( "/" ) ] )
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
	MAIN.project.add_log ( "File %s opened" % __file )
	MAIN.project.file_chooser.hide ( )

def open_file_sig ( button ):
	for __FILE__ in MAIN.project.file_chooser.get_uris ( ):
		open_file ( __FILE__.replace ( "file://", "" ) )

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
	MAIN.project.add_log ( "File %s saved" % TAB.file_name )

def reload_file ( button ):
	MAIN.project.files.reload ( )
	MAIN.project.add_log ( "File %s reloaded" % MAIN.project.files.get_page ( ).get_file ( ) )

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
	MAIN.project.add_log ( "File %s closed" % TAB.file_name )

def close_other ( button ):
	TAB = MAIN.project.files.get_page ( )
	for t in MAIN.project.files.tabs[::-1]:
		if ( t != TAB ):
			MAIN.project.close_file ( t.button_gtk, False )
	MAIN.project.add_log ( "Closed all files except %s" % TAB.file_name )

def close_all ( button ):
	for t in MAIN.project.files.tabs[::-1]:
		MAIN.project.files.close_file ( t.button_gtk, False )
	MAIN.project.add_log ( "Closed All Files" )

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

def write ( button ):
	pass

def make_desk ( button ):
	os.system ( "cd %s && make desktop" % MAIN.dir )
	MAIN.project.add_log ( "Wrote .desktop file" )

def make ( button ):
	os.system ( "cd %s && make" % MAIN.dir )
	MAIN.project.add_log ( "Compiled and build HTML_PARSER C++ Source Code" )

def write_conf ( button ):
	pass

def close_file_new ( button ):
	MAIN.project.builders [ "main.ui" ].get_object ( "filechooser_new" ).hide ( )

def open_file_new ( button ):
	pass

def open_var ( button ):
	MAIN.project.builders [ "main.ui" ].get_object ( "variables_window" ).show_all ( )

def close_var ( button ):
	MAIN.project.builders [ "main.ui" ].get_object ( "variables_window" ).hide ( )

def apply_var ( button ):
	pass

main_handlers = {
"exit": Gtk.main_quit,
"new_page": new_page,
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
"open_file_recent": open_file_recent,
"write": write,
"make_desk": make_desk,
"make": make,
"write_conf": write_conf,
"close_file_new": close_file_new,
"open_file_new": open_file_new,
"open_var": open_var,
"close_var": close_var,
"apply_var": apply_var,
}

global MAIN
args = sys.argv
if ( len ( args ) == 1 ):
	 MAIN = main ( )
else:
	MAIN = main ( args [ 1 ] )

Gtk.main ( )
