/*
 * body.cpp
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


#include "body.h"

using namespace std;

void body::init ( HTML_CONFIG _config, string file_in, string file_out, string _title="file.html" )
{
	config = _config;
	title = _title;
	body_in = File ( file_in ).readlines ( );
	
	sig.load ( config, file_in );
	sig_parser.parse ( sig );
	sig_parser.write_out ( );
	system ( "ls" );
	body_out = sig_parser.output_file;
	buff_file = file_in;
}

void body::write_file ( string new_file )
{
	ofstream file;
	file.open ( new_file.c_str ( ) );
	for ( vector < string >::iterator it = body_out.begin ( ); it != body_out.end ( ); it++ )
	{
		file << *it;
	}
	
	file.close ( );
}
