CWD := $(shell readlink -en $(dir $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))))


.PHONY: all
all: fetch_docker build_from_docker

.PHONY: build_from_docker
build_from_docker:
	docker run --rm -it -v $(CWD):/work jamrizzi/centos-dev:latest make build_centos
	docker run --rm -it -v $(CWD):/work jamrizzi/ubuntu-dev:latest make build_ubuntu
	$(info built from docker)
.PHONY: build_centos
build_centos: fetch_dependancies build beegfs-installer-centos.tar.gz sweep
	$(info built for centos)
.PHONY: build_ubuntu
build_ubuntu: fetch_dependancies build beegfs-installer-ubuntu.tar.gz sweep
	$(info built for ubuntu)

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

beegfs-installer-centos.tar.gz:
	@mkdir beegfs-installer
	@cp -r dist/* beegfs-installer
	@tar -zcvf beegfs-installer-centos.tar.gz beegfs-installer
	@rm -rf beegfs-installer
beegfs-installer-ubuntu.tar.gz:
	@mkdir beegfs-installer
	@cp -r dist/* beegfs-installer
	@tar -zcvf beegfs-installer-ubuntu.tar.gz beegfs-installer
	@rm -rf beegfs-installer

.PHONY: clean
clean: sweep bleach
	$(info cleaned)
.PHONY: sweep
sweep:
	@rm -rf build dist *.spec */*.spec *.pyc */*.pyc get-pip.py
	$(info swept)
.PHONY: bleach
bleach:
	@rm -rf beegfs-installer beegfs-installer*
	$(info bleached)

.PHONY: fetch_dependancies
fetch_dependancies: pip future pyinstaller
	$(info fetched dependancies)
.PHONY: pip
pip:
ifeq ($(shell whereis pip), $(shell echo pip:))
	curl -O https://bootstrap.pypa.io/get-pip.py
	python get-pip.py
endif
.PHONY: future
future:
	pip install future
.PHONY: pyinstaller
pyinstaller:
ifeq ($(shell whereis pyinstaller), $(shell echo pyinstaller:))
	pip install pyinstaller
endif
.PHONY: fetch_docker
fetch_docker:
ifeq ($(shell whereis docker), $(shell echo docker:))
	curl -L https://get.docker.com/ | bash
endif
	$(info fetched docker)
