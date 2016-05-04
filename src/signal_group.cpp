/*
 * signal_group.cpp
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


#include "signal_group.h"
#include "include.h"

using namespace std;

void signal_group::init ( vector < SIGNAL > _signals )
{
	signals = _signals;
	for ( size_t i = 0; i != signals.size ( ); i++ )
	{
		SIGNAL curr = signals [ i ];
		line_numbers.push_back ( curr.line_number );
	}
}

vector < SIGNAL > signal_group::operator[] ( int __line )
{
	vector < SIGNAL > BUFF;
	for ( vector < SIGNAL >::iterator i = signals.begin ( ); i != signals.end ( ); i++ )
	{
		if ( i->line_number == __line )
		{
			BUFF.insert ( BUFF.begin ( ), *i );
		}
	}
	return BUFF;
}

vector < int > signal_group::operator ( ) ( int __line )
{
	vector < int > BUFF;
	for ( unsigned int i = 0; i != signals.size ( ); i++ )
	{
		if ( signals [ i ].line_number == __line )
		{
			BUFF.push_back ( i );
		}
	}
	return BUFF;
}
