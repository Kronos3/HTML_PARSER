/*
 * parser.cxx
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


#include <iostream>
#include "tools/Option.hpp"
#include "page/body.hpp"

int main(int argc, char *argv [])
{
	string input;
	
	for ( int i = 0; i != argc; i++ )
	{
		input += argv [ i ];
		input += " ";
	}
	
	OptionSet parser_opts;
	parser_opts.init ( "emerge", "Use the AutoGentoo portage API to install specified packages" );
	
	parser_opts.add_arg ( "OPTIONS" );
	parser_opts.add_arg ( "CONFIG" );
	
	parser_opts.add_option ( "config", "config/config", "c", "string", "Specify the config file for parser" );
	
	parser_opts.create_help ( );
	parser_opts.feed ( input );
	
	cout << parser_opts ( "config" ) << " << CONF_FILE" << endl;
	
	//HTML_CONFIG MAIN_CONFIG;
	//MAIN_CONFIG.load ( parser_opts ( "config" ) );
	
	//cout << MAIN_CONFIG.variables [ "header" ] << " << IN_FILE" << endl;
	//body BODY;
	//BODY.init ( MAIN_CONFIG, MAIN_CONFIG.variables [ "header" ] );
	//misc::print_vec < string > ( BODY.body_out );
	
	return 0;
}

