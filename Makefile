DOCKER_IMAGE := debianimage2font
DOCKER_ID := $(shell docker images --quiet=true --filter=label=name=$(DOCKER_IMAGE))
DOCKER_PS := $(shell docker ps --all=true --quiet=true --filter=label=name=$(DOCKER_IMAGE))

.PHONY: default build run stop rm rmi get
.SILENT: get

default: build run

build:
	docker build -t $(DOCKER_IMAGE) . ;

ifneq "$(DOCKER_PS)" ""
run:
	docker run --detach=true -it $(DOCKER_ENVS) $(DOCKER_IMAGE) ;
else
run: build
	docker run --detach=true -it $(DOCKER_ENVS) $(DOCKER_IMAGE) ;
endif

stop:
	docker stop -f $(DOCKER_PS) ;

rm: stop
	docker rm -f $(DOCKER_PS) ;

ifeq "$(DOCKER_PS)" ""
rmi: stop
	docker rmi -f $(DOCKER_ID) ;
else
rmi: rm
	docker rmi -f $(DOCKER_ID) ;
endif

get:
	echo $(DOCKER_PS) ;
