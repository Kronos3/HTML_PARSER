/*
 * parser.hpp
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
 

#ifndef __HTML_CONFIG__
#define __HTML_CONFIG__

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "../tools/file.hpp"
#include "../tools/_misc_tools.hpp"

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
	
	
	void load ( string _file )
	{
		file = file;
		content = File ( file ).readlines ( );
		
		for ( size_t i = 0; i != content.size ( ); i++ )
		{
			string curr ( content [ i ] );
			if ( curr [ 0 ] == '#' )
			{
				continue;
			}
			
			vector < string > __temp__ ( misc::split ( curr, '=', true ) );
			
			variables [ __temp__ [ 0 ] ] = __temp__ [ 1 ];
			var_list.push_back ( __temp__ [ 0 ] );
			val_list.push_back ( __temp__ [ 1 ] );
			
			if ( __temp__ [ 1 ].find ( ',' ) != string::npos )
			{
				vector < string > buff_vec misc::split ( __temp__[1], ',', true );
				vector_vars [ __temp__ [ 0 ] ]  = buff_vec;
			}
<<<<<<< HEAD
			
			if ( __temp__.length ( ) <= 1 )
=======
			else if ( __temp__[ 1 ].length ( ) <= 1 )
>>>>>>> 6313af6b12b3a53fd6ff4130b5960186d5e23124
			{
				char BUFF = __temp__ [ 1 ] [ 0 ];
				char_variables [ __temp__ [ 0 ] ] = BUFF;
			}
		}
	}
};

#endif

#ifndef __HTML_ST_SIG__
#define __HTML_ST_SIG__

// Use struct to conserve memory.
typedef struct
{
	int line_number;
	string sig_type;
	int start;
	int end;
	
	void init ( int _line_number, string _sig_type, int _start = -1, int _end = -1 )
	{
		line_number = _line_number;
		sig_type = _sig_type;
		if ( _start != -1 )
		{
			start = _start;
		}
		if ( _end != -1 )
		{
			end = _end;
		}
	}
	
	void clear ( )
	{
		line_number = -1;
		sig_type = "";
		start = -1;
		end = -1;
	}
} SIGNAL;

#endif

#ifndef __HTML_SIG__
#define __HTML_SIG__


class HTML_SIG
{
	public:
	HTML_CONFIG CONFIG;
	vector < string > file;
	vector < SIGNAL > SIGNALS;
	vector < string > sig_types;
	vector < vector < int > > line_start_end;
	
	void load ( HTML_CONFIG _CONFIG, string _file )
	{
		CONFIG = _CONFIG;
		file = File ( _file ).readlines ( );
		for ( size_t i = 0; i != file.size ( ); i++ )
		{
			string curr_line ( file [ i ] );
			
			bool esc;
			SIGNAL TEMP_SIG_TOP;
			SIGNAL TEMP_SIG_BOTTOM;
			vector < int > TEMP_SIG_LINE;
			
			for ( size_t j = 0; j != curr_line.length ( ); j++ )
			{
				char curr_char = curr_line [ j ];
<<<<<<< HEAD
				if ( j != 0 )
				{
					if ( curr_line [ j - 1 ] == CONFIG.variables["esc"] )
					{
						continue;
					}
				}
				if ( curr_char == CONFIG.variables["start_esc"] )
=======
				if ( curr_char == CONFIG.char_variables["start_esc"] )
>>>>>>> 6313af6b12b3a53fd6ff4130b5960186d5e23124
				{
					esc = true;
					TEMP_SIG_TOP.init ( i, "esc", j );
					sig_types.push_back ( "esc" );
					continue;
				}
				
				if ( curr_char == CONFIG.char_variables["end_esc"] )
				{
					esc = false;
					
					TEMP_SIG_TOP.end=j;
					SIGNALS.push_back ( TEMP_SIG_TOP );
					
					TEMP_SIG_LINE.push_back ( i );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_TOP.start );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_TOP.end );
					
					line_start_end.push_back ( TEMP_SIG_LINE );
					
					TEMP_SIG_LINE.clear ( );
					
					continue;
				}
				
				if ( esc )
				{
					if ( curr_char == CONFIG.char_variables["start_class"] )
					{
						TEMP_SIG_BOTTOM.clear ( );
						TEMP_SIG_BOTTOM.init ( i, "class", j );
						sig_types.push_back ( "class" );
						continue;
					}
					
					if ( curr_char == CONFIG.char_variables["end_class"] )
					{
						TEMP_SIG_BOTTOM.end=j;
						SIGNALS.push_back ( TEMP_SIG_BOTTOM );
						
						TEMP_SIG_LINE.push_back ( i );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
						
						line_start_end.push_back ( TEMP_SIG_LINE );
						
						TEMP_SIG_LINE.clear ( );
					}
					
					if ( curr_char == CONFIG.char_variables["start_id"] )
					{
						TEMP_SIG_BOTTOM.clear ( );
						TEMP_SIG_BOTTOM.init ( i, "id", j );
						sig_types.push_back ( "id" );
						continue;
					}
					
					if ( curr_char == CONFIG.char_variables["end_id"] )
					{
						TEMP_SIG_BOTTOM.end=j;
						SIGNALS.push_back ( TEMP_SIG_BOTTOM );
						
						TEMP_SIG_LINE.push_back ( i );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
						
						line_start_end.push_back ( TEMP_SIG_LINE );
						
						TEMP_SIG_LINE.clear ( );
					}
					
					if ( curr_char == CONFIG.char_variables["end_style"] )
					{
						TEMP_SIG_BOTTOM.clear ( );
						TEMP_SIG_BOTTOM.init ( i, "style", j );
						sig_types.push_back ( "style" );
						continue;
					}
					
					if ( curr_char == CONFIG.char_variables["end_style"] )
					{
						TEMP_SIG_BOTTOM.end=j;
						SIGNALS.push_back ( TEMP_SIG_BOTTOM );
						
						TEMP_SIG_LINE.push_back ( i );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
						TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
						
						line_start_end.push_back ( TEMP_SIG_LINE );
						
						TEMP_SIG_LINE.clear ( );
					}
				}
			}
		}
	}
};

#endif
