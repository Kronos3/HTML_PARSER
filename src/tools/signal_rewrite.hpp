/*
 * signal_rewrite.hpp
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
 

#ifndef __HTML_MULT_REPLACE__
#define __HTML_MULT_REPLACE__

#include <iostream>
#include "../page/signal_parser.hpp"

using namespace std;

string mult_replace ( string in, vector < string > toReplace, vector < SIGNAL > sig_in )
{
	string out = in;
	int minus;
	int plus;
	for ( size_t i = 0; i != toReplace.size ( ); i++ )
	{
		if ( sig_in [ i ].sig_type == "esc" )
		{
			continue;
		}
		
		minus = 1;
		plus = 2;
		
		out.replace ( sig_in [ i ].start - minus, sig_in [ i ].length + plus, toReplace [ i ] );
	}
	return out;
}

#endif
