/*
 * html_config.h
 * 
 * Copyright 2016 Andrei Tumbar <atuser@Kronos>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#ifndef HTML_CONFIG_H
#define HTML_CONFIG_H

#include <iostream>
#include <map>
#include "file.h"
#include "_misc_tools.h"

using namespace std;

class HTML_CONFIG
{
	public:
		string file;
		vector < string > content;
		
		vector < string > var_list;
		vector < string > val_list;
		map < string, string > variables;
		map < string, char > char_variables;
		
		map < string, vector < string > > vector_vars;
		
		vector < string > output_files;
		vector < string > css_files;
		vector < string > js_files;
		
		void load ( string _file );
};

#endif /* HTML_CONFIG_H */ 
