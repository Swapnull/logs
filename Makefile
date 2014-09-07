PREFIX ?= /usr/local/bin

.PHONY: install uninstall

install:
	chmod +x Release/logs.py
	ln -s $(PWD)/Release/logs.py $(PREFIX)/logs
	
uninstall:
	rm -rf /usr/local/bin/logs