

HOST=192.168.8.61
HOST_LIBDIR="/lib/"
HOST_APPDIR="/"

APP_FILES += main.py 
APP_FILES += m5stickc.py 
APP_FILES += axp192.py	

LIB_FILES += ./WiFiManager/wifimgr.py
LIB_FILES += ./ftp_server/uftpd.py

install: .app_installed_${HOST} .lib_installed_${HOST}

help:
	@echo "Makefile targets:"
	@echo "  help"
	@echo "  install:    copies required files to ${HOST}."
	@echo "              (maybe you want to call \"make install HOST=ip-address\""
	@echo "  clean:      removes local marker files"
	@echo "  realclean:  removes local marker files as well as submodule folders"


realclean: clean
	rm -fr ./WiFiManager
	rm -fr ./ftp_server

clean:
	rm -f .app_installed_* .lib_installed_*

$(LIB_FILES):
	git submodule update --init

.app_installed_${HOST}: $(APP_FILES)
	@for i in $?; do \
		echo "copy $$i"; \
		curl -s --ftp-pasv -T $$i ftp://$(HOST)$(HOST_APPDIR) || exit 1; \
	done
	touch $@

.lib_installed_${HOST}: $(LIB_FILES)
	@for i in $?; do \
		echo "copy $$i"; \
		curl -s --ftp-pasv -T $$i ftp://$(HOST)$(HOST_LIBDIR) || exit 1; \
	done
	touch $@

