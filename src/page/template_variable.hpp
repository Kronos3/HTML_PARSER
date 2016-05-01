/*
 * template_variable.hpp
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

#ifndef __HTML_TEMPLATE_VARIABLE__
#define __HTML_TEMPLATE_VARIABLE__

#include <iostream>
#include <string>
#include <vector>
#include "../tools/file.hpp"
#include "../tools/_misc_tools.hpp"

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
	
	void init_name ( vector < string > __template, int _line_number, int _indent )
	{
		line_number = _line_number;
		template_file = __template;
		
		indent = _indent;
		name = template_file [ line_number ].substr ( indent + 1, template_file [ line_number ].length ( ) - indent - 2 );
	}
	
	void init ( string _file_name, HTML_CONFIG _config, bool __auto__ = false, string auto_filenames = "" )
	{
		file_name = _file_name;
		config = _config;
		
		if ( __auto__ )
		{
			format_special ( auto_filenames );
			return;
		}
		
		processed.init ( config, file_name, "" );
		in_file = processed.body_out;
		
		for ( vector < string >::iterator i = in_file.begin ( ); i != in_file.end ( ); i++ )
		{
			string buff;
			for ( int j = 0; j != indent; j++ )
			{
				buff += ' ';
			}
			
			buff += *i;
			out_file.push_back ( buff );
		}
	}
	
	void format_special ( string auto_filenames )
	{
		vector < string > names = misc::split ( auto_filenames, ',',  true );
		for ( vector < string >::iterator it = names.begin ( ); it != names.end ( ); it++ )
		{
			string buff;
			if ( name == "CSS" )
			{
				buff = "<link rel=\"stylesheet\" href=\"" + *it + "\" type=\"text/css\" />";
			}
			else if ( name == "JS" )
			{
				buff = "<script type=\"text/javascript\" src=\"" + *it + "\"></script>";
			}
			
			out_file.push_back ( buff );
		}
		
	}
	vector < string > format_file ( )
	{
		vector < string > template_buff = template_file;
		template_buff.erase ( template_buff.begin ( ) + line_number );
		if ( out_file.size ( ) == 1 )
		{
			template_buff.insert ( template_buff.begin ( ) + line_number, out_file [ 0 ] );
			return template_buff;
		}
		else if ( out_file [ 1 ] == "\n" or out_file [ 1 ].empty ( ) )
		{
			template_buff.insert ( template_buff.begin ( ) + line_number, out_file [ 0 ] );
		}
		else
		{
			template_buff.insert ( template_buff.begin ( ) + line_number, out_file.begin ( ), out_file.end ( ) );
		}
		return template_buff;
	}
};

#endif
