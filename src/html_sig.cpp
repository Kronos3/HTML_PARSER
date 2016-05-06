/*
 * html_sig.cpp
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


#include "html_sig.h"

using namespace std;

void HTML_SIG::load ( HTML_CONFIG _CONFIG, string _file )
{
	CONFIG = _CONFIG;
	file = File ( _file ).readlines ( );
	for ( size_t i = 0; i != file.size ( ); i++ )
	{
		string curr_line ( file [ i ] );
		
		bool esc = false;
		bool quote = false;
		
		bool __class = false;
		bool __style = false;
		bool __id = false;
		
		SIGNAL TEMP_SIG_TOP;
		SIGNAL TEMP_SIG_BOTTOM;
		
		vector < int > TEMP_SIG_LINE;
		
		for ( size_t j = 0; j != curr_line.length ( ); j++ )
		{
			char curr_char = curr_line [ j ];
			
			if ( curr_char == '\"' )
			{
				quote = !quote;
			}
			
			if ( j != 0 )
			{
				if ( curr_line [ j - 1 ] == CONFIG.char_variables["esc"] )
				{
					continue;
				}
			}
			
			if ( quote )
			{
				continue;
			}
			
			if ( curr_char == CONFIG.char_variables["start_esc"] )
			{
				esc = true;
				TEMP_SIG_TOP.init_start ( i, "esc", j );
				TEMP_SIG_TOP.feed_chars ( CONFIG.char_variables["start_esc"], CONFIG.char_variables["end_esc"] );
				sig_types.push_back ( "esc" );
				continue;
			}
			
			if ( curr_char == CONFIG.char_variables["end_esc"] )
			{
				esc = false;
				
				TEMP_SIG_TOP.init_end ( i, "esc", j );
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
				if ( curr_char == CONFIG.char_variables["start_class"] and !__class )
				{
					TEMP_SIG_BOTTOM.clear ( );
					TEMP_SIG_BOTTOM.init_start ( i, "class", j );
					TEMP_SIG_TOP.feed_chars ( CONFIG.char_variables["start_class"], CONFIG.char_variables["end_class"] );
					sig_types.push_back ( "class" );
					__class = true;
					continue;
				}
				
				if ( curr_char == CONFIG.char_variables["end_class"] and __class )
				{
					TEMP_SIG_BOTTOM.init_end ( i, "class", j );
					SIGNALS.push_back ( TEMP_SIG_BOTTOM );
					
					TEMP_SIG_LINE.push_back ( i );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
					
					line_start_end.push_back ( TEMP_SIG_LINE );
					
					TEMP_SIG_LINE.clear ( );
					
					__class = false;
				}
				
				if ( curr_char == CONFIG.char_variables["start_id"] and !__id )
				{
					TEMP_SIG_BOTTOM.clear ( );
					TEMP_SIG_BOTTOM.init_start ( i, "id", j );
					TEMP_SIG_TOP.feed_chars ( CONFIG.char_variables["start_id"], CONFIG.char_variables["end_id"] );
					sig_types.push_back ( "id" );
					__id = true;
					continue;
				}
				
				if ( curr_char == CONFIG.char_variables["end_id"] and __id )
				{
					TEMP_SIG_BOTTOM.init_end ( i, "id", j );
					SIGNALS.push_back ( TEMP_SIG_BOTTOM );
					
					TEMP_SIG_LINE.push_back ( i );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
					
					line_start_end.push_back ( TEMP_SIG_LINE );
					__id = false;
					
					TEMP_SIG_LINE.clear ( );
				}
				
				if ( curr_char == CONFIG.char_variables["start_style"] and !__style )
				{
					TEMP_SIG_BOTTOM.clear ( );
					TEMP_SIG_BOTTOM.init_start ( i, "style", j );
					TEMP_SIG_TOP.feed_chars ( CONFIG.char_variables["start_style"], CONFIG.char_variables["end_style"] );
					sig_types.push_back ( "style" );
					__style = true;
					continue;
				}
				
				if ( curr_char == CONFIG.char_variables["end_style"] and __style )
				{
					TEMP_SIG_BOTTOM.init_end ( i, "style", j );
					SIGNALS.push_back ( TEMP_SIG_BOTTOM );
					
					TEMP_SIG_LINE.push_back ( i );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.start );
					TEMP_SIG_LINE.push_back ( TEMP_SIG_BOTTOM.end );
					
					line_start_end.push_back ( TEMP_SIG_LINE );
					
					__style = false;
					TEMP_SIG_LINE.clear ( );
				}
			}
		}
	}
}
