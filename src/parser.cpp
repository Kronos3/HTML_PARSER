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
#include <fstream>
#include <unistd.h>
#include <vector>
#include <string>
#include "file.h"
#include "_misc_tools.h"
#include "html_config.h"
#include "signal_parser.h"
#include "body.h"
#include "template_variable.h"
#include "template_set.h"
#include "template.h"
#include "optionset.h"

using namespace std;

int main(int argc, char *argv [])
{
	string input;
	
	for ( int i = 0; i != argc; i++ )
	{
		input += argv [ i ];
		input += " ";
	}
	
	HTML_CONFIG MAIN_CONFIG;
	Template MAIN_TEMPLATE;
	vector < body > body_files;
	OptionSet opts;
	
	opts.init ( "parser", "Parse the input files for HTML_PARSER", 15 );
	
	opts.add_arg ( "OPTIONS" );
	opts.add_arg ( "CONFIG" );
	
	opts.add_option ( "config", "parser.cfg", "c", "string", "Specify the config file for parser" );
	opts.add_option ( "write", "true", "w", "bool", "Specify whether to write the output file" );
	
	opts.create_help ( );
	opts.feed ( input );
	
	chdir ( misc::get_dir ( opts ( "config" ) ).c_str ( ) );
	MAIN_CONFIG.load ( opts ( "config" ) );
	for ( size_t i = 0; i != MAIN_CONFIG.vector_vars [ "input_files" ].size ( ); i++ )
	{
		body curr_body;
		curr_body.init ( MAIN_CONFIG, MAIN_CONFIG.vector_vars [ "input_files" ] [ i ], MAIN_CONFIG.vector_vars [ "output_files" ] [ i ], MAIN_CONFIG.vector_vars [ "title" ] [ i ] );
		body_files.push_back ( curr_body );
	}
	
	MAIN_TEMPLATE.init ( MAIN_CONFIG, MAIN_CONFIG.variables [ "template" ] );
	
	if ( opts [ "write" ] )
	{
		for ( size_t i = 0; i != MAIN_CONFIG.vector_vars [ "output_files" ].size ( ); i++ )
		{
			vector < string > buff = MAIN_TEMPLATE.new_file ( body_files [ i ] );
			ofstream curr_file;
			string curr_file_name = MAIN_CONFIG.vector_vars [ "output_files" ] [ i ];
			curr_file.open ( curr_file_name.c_str ( ), ios::out | ios::trunc );
			for ( vector < string >::iterator line = buff.begin ( ); line != buff.end ( ); line++ )
			{
				curr_file << line->c_str ( );
			}
			
			curr_file.close ( );
		}
	}
	
	return 0;
}
