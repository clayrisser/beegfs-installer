.PHONY: all
all: fetch_dependancies build package sweep


## BUILD ##
.PHONY: build
build: dist/admon-install dist/client-install dist/management-install dist/metadata-install dist/storage-install
	$(info built)

dist/admon-install:
	pyinstaller --onefile --noupx src/admon-install.py

dist/client-install:
	pyinstaller --onefile --noupx src/client-install.py

dist/management-install:
	pyinstaller --onefile --noupx src/management-install.py

dist/metadata-install:
	pyinstaller --onefile --noupx src/metadata-install.py

dist/storage-install:
	pyinstaller --onefile --noupx src/storage-install.py


## PACKAGE ##
.PHONY: package
package: beegfs-installer.tar.gz
	$(info packaged)

beegfs-installer.tar.gz:
	@mkdir beegfs-installer
	@cp -r dist/* beegfs-installer
	@tar -zcvf beegfs-installer.tar.gz beegfs-installer
	@rm -rf beegfs-installer


## CLEAN ##
.PHONY: clean
clean: sweep bleach
	$(info cleaned)

.PHONY: sweep
sweep:
	@rm -rf build dist *.spec */*.spec *.pyc */*.pyc
	$(info swept)

.PHONY: bleach
bleach:
	@rm -rf beegfs-installer.tar.gz beegfs-installer
	$(info bleached)


## FETCH DEPENDANCIES ##
.PHONY: fetch_dependancies
fetch_dependancies: pip pyinstaller
	$(info fetched dependancies)

.PHONY: pip
pip:
ifeq ($(shell which pip), $(shell echo))
	curl -O https://bootstrap.pypa.io/get-pip.py
	python get-pip.py
endif

.PHONY: pyinstaller
pyinstaller:
ifeq ($(shell which pyinstaller), $(shell echo))
	pip install pyinstaller
endif
