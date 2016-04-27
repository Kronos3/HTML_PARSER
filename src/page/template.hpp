/*
 * template.hpp
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

#ifndef __HTML_TEMPLATE___
#define __HTML_TEMPLATE___

#include <iostream>
#include "../config/html_config.hpp"
#include "../tools/_misc_tools.hpp"
#include "template_set.hpp"

using namespace std;

class Template
{
	public:
	
	vector < string > template_content;
	vector < string > template_out;
	string template_name;
	
	HTML_CONFIG config;
	
	template_set template_vars;
	
	void init ( HTML_CONFIG _config, string _template_name )
	{
		template_name = _template_name;
		template_content = File ( template_name ).readlines ( );
		
		template_out = template_content;
		
		for ( vector < string >::iterator i = template_out.end ( ); i != template_out.begin ( ); i-- )
		{
			int indent = 0;
			for ( string::iterator j = i->begin ( ); j != i->end ( ); j++ )
			{
				if ( *j != ' ' or *j != '	' )
				{
					break;
				}
				else
				{
					indent += 1;
				}
			}
			
			if ( i->at ( indent + 1 ) == '[' )
			{
				template_variable buff;
				buff.init_name ( template_out, i - template_content.begin ( ), indent );
				
				if ( config.variables [ buff.name ] == "$" )
				{
					string buff_str;
					if ( buff.name == "BODY" )
					{
						template_vars.add ( buff );
						continue;
					}
					else if ( buff.name == "TITLE" )
					{
						template_vars.add ( buff );
						continue;
					}
					else if ( buff.name == "CSS" )
					{
						buff_str = config.variables [ "css" ];
					}
					else if ( buff.name == "JS" )
					{
						buff_str = config.variables [ "js" ];
					}
					
					buff.init ( config.variables [ buff.name ], true, buff_str );
				}
				
				buff.init ( config.variables [ buff.name ] );
				template_out = buff.format_file ( );
				template_vars.add ( buff );
			}
		}
	}
	
	vector < string > new_file ( string body_file, string title )
	{
		vector < string > BUFF = template_content;
		for ( vector < string >::iterator i = BUFF.end ( ); i != BUFF.begin ( ); i-- )
		{
			int indent = 0;
			for ( string::iterator j = i->begin ( ); j != i->end ( ); j++ )
			{
				if ( *j != ' ' or *j != '	' )
				{
					break;
				}
				else
				{
					indent += 1;
				}
			}
			
			if ( i->substr ( indent + 1, 5 ) == "[BODY" )
			{
				template_variable buff;
				buff.init_name ( template_out, i - template_content.begin ( ), indent );
				buff.init ( body_file );
				BUFF = buff.format_file ( );
			}
			else if ( i->substr ( indent + 1, 6 ) == "[TITLE" )
			{
				template_variable buff;
				buff.init_name ( template_out, i - template_content.begin ( ), indent );
				
				string title_cmd = "echo \"<title>" + title + "</title>\" >> title.temp";
				system ( title_cmd.c_str ( ) );
				
				buff.init ( "title.temp" );
				BUFF = buff.format_file ( );
				
				system ( "rm -rf title.temp" );
			}
		}
		
		return BUFF;
	}
};

#endif
