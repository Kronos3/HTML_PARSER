SOURCEDIR=src

.PHONY : subsystem
.DEFAULT_GOAL := subsystem
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

subsystem:
	$(MAKE) -C $(SOURCEDIR)

clean:
	$(MAKE) clean -C $(SOURCEDIR)

windows:
	$(MAKE) -C $(SOURCEDIR) -f MakefileWin


desktop:
	# Making .desktop file
	
	echo "#!/usr/bin/env xdg-open" > $(ROOT_DIR)/"HTML Parser.desktop"
	echo "[Desktop Entry]" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Type=Application" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Version=3.1" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Name=HTML Parser" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Comment=GUI for easier web creation" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Exec=bash -c 'cd $(ROOT_DIR)/ && ./src/html_parser.py >> html_parser.log 2>&1'" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Icon=$(ROOT_DIR)/src/icon.png" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Terminal=false" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Categories=Languages;C++;Python" >> $(ROOT_DIR)/"HTML Parser.desktop"
	echo "Name[en_US]=HTML\ Parser" >> $(ROOT_DIR)/"HTML Parser.desktop"
	
