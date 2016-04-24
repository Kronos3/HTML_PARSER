/*
 * signal_parser.hpp
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
 

#ifndef __HTML_SIGNAL_PARSER__
#define __HTML_SIGNAL_PARSER__

#include <iostream>
#include "../config/html_config.hpp"
#include "signal_group.hpp"
#include "../tools/signal_rewrite.hpp"

using namespace std;

class signal_parser
{
	public:
	vector < string > input_file;
	vector < string > output_file;
	
	vector < SIGNAL > input_signals;
	vector < string > output_string;
	vector < int > str_len;
	vector < int > sig_line_numbers;
	
	signal_group sig_group;
	
	void parse ( __HTML_SIG__ __input__, bool create_out_file = true )
	{
		input_file = __input__.file;
		input_signals = __input__.SIGNALS;
		
		for ( size_t i = 0; i != input_signals; i++ )
		{
			SIGNAL curr = input_signals[ i ]; 
			sig_line_numbers.push_back ( curr.line_number )
			
			if ( curr.sig_type == "esc" )
			{
				output_string.push_back ( input_file [ curr.line_number ].substr ( curr.start, curr.length ) );
				continue;
			}
			
			curr_output_str = curr.sig_type;
			curr_output_str += "=\"";
			curr_output_str += input_file [ curr.line_number ].substr ( curr.start, curr.length );
			curr_output_str += "\"";
			
			output_string.push_back ( curr_output_str );
			str_len.push_back ( curr_output_str.length ( ) );
		}
		
		sig_group.init ( input_signals );
	}
	
	void write_out ( )
	{
		for ( size_t i = 0; i != output_string.size ( ); i++ )
		{
			string curr_str ( output_string [ i ] );
			int buff_i = static_cast < int > ( i );
			
			int find = misc::find < int > ( sig_line_numbers, buff_i )
			
			if ( find == -1 )
			{
				output_file.push_back ( curr_str );
				continue;
			}
			
			vector < SIGNAL > this_line = sig_group [ i ];
			vector < int > out_line_nums = sig_group ( i );
			vector < string > replacing;
			
			for ( vector < int >::iterator i = out_line_nums.begin ( ); i != out_line_nums.end ( ); i++ )
			{
				replacing.push_back ( output_string [ i ] );
			}
			
			curr_str = mult_replace ( curr_str, replacing, this_line );
			output_file.push_back ( curr_str );
		}
	}
};

#endif