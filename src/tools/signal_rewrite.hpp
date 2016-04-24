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
 

#ifndef __HTML_SIGNAL_GROUP__
#define __HTML_SIGNAL_GROUP__

#include <iostream>
#include "signal_parser.hpp"

using namespace std;

string mult_replace ( string in, vector < string > toReplace, vector < string > sig_in )
{
	string out = in;
	for ( size_t i = 0; i != toReplace.size ( ); i++ )
	{
		out.replace ( sig_in [ i ].start, sig_in [ i ].length, toReplace [ i ] );
		in_len = sig_in [ i ].length;
		out_len = toReplace [ i ].length ( );
		sig_in [ i + 1 ].length += out_len - in_len; 
	}
	
	return out;
}