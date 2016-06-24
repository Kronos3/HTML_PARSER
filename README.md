#Installation
##Windows
Decompress and run the setup.exe file
##Linux
The following are required on Linux:
 * gcc-4.9 or greater
 * gtk-3.18 or greater
 * gnome-3.18 or greater
 * python-3.4 or greater
 * Gobject-Introspection
 * pygobject
 * GtkSource

#Config File Documentation

##Parsing Variables
 * start_esc = any single character, leave this as “<” (default html syntax)
 * 		This will signal to the program when to look for class names or tags
 * end_esc = any single character, leave this as “>” (default html syntax)
 * 		This will signal when to stop looking for class names or tags
 * 
 * start_class = any character just don’t use quotes
 * 		Define tag class name for css
 * end_class = any character just don’t use quotes
 * 
 * And so on…

 * esc = leave as backslash, this will ignore the next special character such as < or >
 * output_files = list of output files (website files) always include a comma even if there is only one page
 * input_files = list of input files that will be parsed. List corresponds to output_files
 * title = list of title for output files
 * css = list of css files local or global that will be included in every output file
 * js = list of javascript files local or global that will be included in every output file
 * template = local file path for template

##LEAVE ALL THESE VARIABLES EQUAL to $
 * TITLE=$
 * CSS=$
 * JS=$
 * BODY=$

 * HEADER = a default user defined variable, will point to an input file path
(This is also known as a section)

##Defining custom sections
A section can be defined in the template.html page by surrounding the variable name with brackets ([])

#UI Documentation
Config UI

This section of the UI will parse a config file that can be opened from File → Open Config. The changes made in this section can be saved to a file by clicking on Build → Write config to file. If this software is ran then the current changes in the UI will be used but not saved to a file.

Markdown Documentation
HTML Parser has full support for markdown and will can convert it to html by going to Build → Convert Markdown to HTML. This will open a file save dialogue to ask where to save the html file.

Basic Markdown
>An h1 header
>============
>Paragraphs are separated by a blank line.
>2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
>look like:
>  * this one
>  * that one
>  * the other one
>
>Note that --- not considering the asterisk --- the actual text
>content starts at 4-columns in.
>> Block quotes are
>> written like so.
>>
>> They can span multiple paragraphs,
>> if you like.
>Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
>in chapters 12--14"). Three dots ... will be converted to an ellipsis.
>Unicode is supported.

If inline HTML is needed just surround the HTML with blank lines.

The full markdown syntax can be found at https://daringfireball.net/projects/markdown/syntax.

Build Menu Tool
Under the Build menu you will find a variety of different tools that HTML parser provides. First of which is Write config to file. When clicked the UI will ask where you would like to save your config and then will take your changed made in the Config UI and create a new config file. The next item is Write .desktop file. This option is not useful in Windows as it is a .desktop file is a Linux (GNOME) specific file type. The next option is Write. This is the main feature of this software and will run HTMLParser.py to parse your project. Finally is the Convert Markdown to HTML. This option will convert the file that is currently open (assuming its Markdown) and will convert it to an HTML document. This option will use the library that can be found at https://pypi.python.org/pypi/Markdown/2.6.6.

How to use this tool (Tutorial)
Step 1: Create an input file

The easiest way to create an input file in HTML Parser is to write one in Markdown. To do this just click File → New Page or just CTRL-N. This will create a new empty file. Next just write some simple text as shown to the right. Finally save the file as a .md file.





Step 2: Convert Markdown to HTML
To convert your Markdown file to an HTML file just click Build → Convert Markdown to HTML. Save the new html file to new.html

Step 3: Create a config file
The first step to creating a new config file is to remove the old default input and output files. To do this simply click the  button on each of the files to the left of the window. This will leave us will a blank config file. The next step is to add your HTML file you made previously. Do this by clicking the  button under Input Files and selecting your HTML file. Next just create a new file and save it to output.html and add that to the output files. Finally change the title of the HTML file by clicking Open Variables and clearing the title variable and adding new page, (don’t forget the comma). The title variable should look something like this . Finally just export the config file and save it to new.cfg by clicking Build → Write config to file.

Step 4: Write the template
The template file is the backbone of your project, the code here will carry one to every output file. For now just open the default template by clicking the icon under the Template section to the left. This will open template.html in the text editor. Since we want a simple HTML file with no CSS or Javascript, just remove the lines that say [CSS], [JS], and [HEADER]. Your file should look something like this now:

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
[TITLE]
</head>
<body>
  [BODY]
</body>

</html>

Save your file with CTRL-S.

Step 5: Run the software
Now you are ready to run the program, simply click Build → Write. 
