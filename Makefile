DOCKER_IMAGE := debianimage2font
DOCKER_ID := $(shell docker images --quiet="true" --filter="label=name=$(DOCKER_IMAGE)")
DOCKER_PS := $(shell docker ps -a --quiet="true" --filter="label=name=$(DOCKER_IMAGE)")

ifneq "$(shell command -v boot2docker)" ""
DOCKER_ENVS := -v /home:/opt/home
else
DOCKER_ENVS := -v $(HOME):/opt/home
endif

default: build run

build:
	docker build -t "$(DOCKER_IMAGE)" . ;

ifneq "$(DOCKER_PS)" ""
run:
	docker run -it $(DOCKER_ENVS) "$(DOCKER_IMAGE)" ;
else
run: build
	docker run -it $(DOCKER_ENVS) "$(DOCKER_IMAGE)" ;
endif

ifneq "$(shell command -v boot2docker)" ""
shell:
	boot2docker ssh ;
endif

stop:
	docker stop $(DOCKER_PS) ;

volume:
	docker inspect -f {{.Volumes}} $(DOCKER_PS) ;

rm:
	docker rm -v $(DOCKER_PS) ;

ifeq "$(DOCKER_PS)" ""
rmi:
	docker rmi $(DOCKER_ID) ;
else
rmi: rm
	docker rmi $(DOCKER_ID) ;
endif

ifneq "$(shell command -v boot2docker)" ""
.PHONY: default build run shell stop volume rm rmi
else
.PHONY: default build run stop volume rm rmi
endif
