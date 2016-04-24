/*
 * signal_group.hpp
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
#include "../config/html_config.hpp"

using namespace std;

class signal_group
{
	public:
	
	vector < SIGNAL > signals;
	vector < int > line_numbers;
	
	void init ( vector < SIGNAL > _signals )
	{
		signals = _signals;
		for ( size_t i = 0; i != signals.size ( ); i++ )
		{
			SIGNAL curr = signals [ i ];
			line_numbers.push_back ( curr.line_number );
		}
	}
	
	vector < SIGNAL > operator[] ( int __line )
	{
		vector < SIGNAL > BUFF;
		for ( unsigned int i = 0; i != signals.size ( ); i++ )
		{
			if ( signals [ i ].line_number == __line )
			{
				BUFF.push_back ( signals [ i ] );
			}
		}
		return BUFF;
	}
	
	vector < int > operator ( ) ( int __line )
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
};

#endif
