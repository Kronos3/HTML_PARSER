/*
 * signal_group.h
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


#ifndef SIGNAL_GROUP_H
#define SIGNAL_GROUP_H

#include <iostream>
#include "html_config.hpp"

using namespace std;

class signal_group
{
	public:
		
		vector < SIGNAL > signals;
		vector < int > line_numbers;
		
		void init ( vector < SIGNAL > _signals );
		vector < SIGNAL > operator[] ( int __line );
		vector < int > operator ( ) ( int __line );
};

#endif /* SIGNAL_GROUP_H */ 
