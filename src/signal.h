/*
 * signal.h
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


#ifndef SIGNAL_H
#define SIGNAL_H

#include <iostream>
#include "html_config.h"

using namespace std;

class SIGNAL
{
	public:
		int line_number;
		string sig_type;
		int start;
		int end;
		int length;
		char start_char;
		char end_char;
		
		void init_start ( int _line_number, string _sig_type, int _start );
		void init_end ( int _line_number, string _sig_type, int _end );
		void feed_chars ( char _start_char, char _end_char );
		void clear ( );
};

#endif /* SIGNAL_H */ 
