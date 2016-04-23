# Image2font - Docker

[![travis-badge][]][travis] [![license-badge][]][license]

[travis-badge]: https://travis-ci.org/limaconoob/Image2font.svg?branch=docker&style=flat-square
[travis]: https://travis-ci.org/limaconoob/Image2font
[license-badge]: http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square
[license]: https://github.com/limaconoob/Image2font/blob/docker/LICENSE

##### How to use:
```shell
make build run

export IMAGE=neko.png
export FONT_INPUT=sazanami-gothic.ttf
export FONT_OUTPUT=neko.ttf

docker cp $IMAGE $(make get):/root/image2font/$IMAGE
docker cp $FONT_INPUT $(make get):/root/image2font/$FONT_INPUT
docker exec $(make get) python image2font --input-font $FONT_INPUT --output-font $FONT_OUTPUT $IMAGE
docker cp $(make get):/root/image2font/$FONT_OUTPUT $FONT_OUTPUT
cp -f $FONT_OUTPUT $HOME/.local/share/fonts
```
