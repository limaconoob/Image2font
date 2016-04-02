# Image2font - Docker

##### How to use:
```shell
make build run

export IMAGE=neko.png
export FONT_INPUT=sazanami-gothic.ttf
export FONT_OUTPUT=neko.ttf

docker cp $IMAGE $(make get):/root/image2font/$IMAGE
docker cp $FONT_INPUT $(make get):/root/image2font/$FONT_INPUT
docker exec $(make get) python image2font --input-font $FONT_INPUT --output-font $FONT_OUTPUT $IMAGE
docker cp $(make get):/root/image2font/$(FONT_OUTPUT) $FONT_OUTPUT
```
