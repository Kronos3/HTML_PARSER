/*
 * template.h
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


#ifndef TEMPLATE_H
#define TEMPLATE_H

#include "include.h"
#include "html_config.hpp"
#include "template_set.h"
#include "body.h"

using namespace std;

class Template
{
	public:
		vector < string > template_content;
		vector < string > template_out;
		string template_name;
		
		HTML_CONFIG config;
		
		template_set template_vars;
		
		void init ( HTML_CONFIG _config, string _template_name );
		vector < string > new_file ( body IN );
};

#endif /* TEMPLATE_H */ 
