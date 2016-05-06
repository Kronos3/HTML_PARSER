/*
 * html_config.cpp
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


#include "html_config.h"

using namespace std;

void HTML_CONFIG::load ( string _file )
{
	file = _file;
	content = File ( file ).readlines ( );
	misc::print_vec ( content );
	for ( size_t i = 0; i != content.size ( ); i++ )
	{
		string curr ( content [ i ] );
		if ( curr [ 0 ] == '#' or curr.empty ( ) )
		{
			continue;
		}
		
		vector < string > __temp__ ( misc::split ( curr, '=', true ) );
		variables [ __temp__ [ 0 ] ] = __temp__ [ 1 ];
		var_list.push_back ( __temp__[0] );
		val_list.push_back ( __temp__[1] );
		
		if ( __temp__ [ 1 ].find ( ',' ) != string::npos )
		{
			vector < string > buff_vec ( misc::split ( __temp__[1], ',', true ) );
			vector_vars [ __temp__ [ 0 ] ] = buff_vec;
		}
		
		if ( __temp__ [ 1 ].length ( ) <= 1 )
		{
			char BUFF = __temp__ [ 1 ] [ 0 ];
			char_variables [ __temp__[0] ] = BUFF;
		}
	}
}
