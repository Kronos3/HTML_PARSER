/*
 * template_variable.h
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


#ifndef TEMPLATE_VARIABLE_H
#define TEMPLATE_VARIABLE_H

#include "include.h"
#include "file.h"
#include "_misc_tools.h"
#include "body.h"

using namespace std;

class template_variable
{
	public:
		int indent;
		int line_number;
		
		string file_name;
		string name;
		
		vector < string > template_file;
		vector < string > in_file;
		vector < string > out_file;
		body processed;
		HTML_CONFIG config;
		
		void init_name ( vector < string > __template, int _line_number, int _indent );
		void init ( string _file_name, HTML_CONFIG _config, bool __auto__, string auto_filenames );
		void format_special ( string auto_filenames );
		vector < string > format_file ( );
};

#endif /* TEMPLATE_VARIABLE_H */ 
