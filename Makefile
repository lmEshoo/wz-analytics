USERNAME=lmestar
CONTAINER_NAME=wz
IMAGE=$(USERNAME)/$(CONTAINER_NAME):0.2

all: run

build:
	docker build -t $(IMAGE) .

log:
	docker logs $(CONTAINER_NAME) -f

up:
	docker run -d -it --rm \
	-v $(PWD):/app \
	-p 6901:6901 \
	-p 5901:5901 \
	-v /dev/shm:/dev/shm \
	-e USER=${USER} \
	-e TZ=America/Los_Angeles \
	--name $(CONTAINER_NAME) $(IMAGE) \
	bash -c "sleep 2 && python3 wz.py "

stop:
	docker stop $(CONTAINER_NAME)

run: up
	@while [[ ! `curl -sf http://localhost:6901/?password=vncpassword` ]]; do sleep 5; done
	open http://localhost:6901/?password=vncpassword
