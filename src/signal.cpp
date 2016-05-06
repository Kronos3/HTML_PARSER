/*
 * signal.cpp
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


#include "signal.h"

using namespace std;

void SIGNAL::init_start ( int _line_number, string _sig_type, int _start )
{
	int _end = -1;
	line_number = _line_number;
	sig_type = _sig_type;
	if ( _start != -1 )
	{
		start = _start + 1;
	}
	if ( _end != -1 )
	{
		end = _end;
		length = end - start;
	}
}

void SIGNAL::init_end ( int _line_number, string _sig_type, int _end )
{
	int _start = -1;
	line_number = _line_number;
	sig_type = _sig_type;
	if ( _start != -1 )
	{
		start = _start;
	}
	if ( _end != -1 )
	{
		end = _end;
		length = end - start;
	}
}

void SIGNAL::feed_chars ( char _start_char, char _end_char )
{
	start_char = _start_char;
	end_char = _end_char;
}

void SIGNAL::clear ( )
{
	line_number = -1;
	sig_type = "";
	start = -1;
	end = -1;
}
