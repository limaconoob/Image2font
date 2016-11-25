# Image2font - Docker

[![travis-badge][]][travis] [![license-badge][]][license]

[travis-badge]: https://travis-ci.org/limaconoob/Image2font.svg?branch=docker&style=flat-square
[travis]: https://travis-ci.org/limaconoob/Image2font
[license-badge]: http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square
[license]: https://github.com/limaconoob/Image2font/blob/docker/LICENSE

##### How to use:
```shell
git clone -b docker https://github.com/limaconoob/Image2font.git Image2font && cd Image2font
make build run

export IMAGES=neko.png # curl https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Neko_Wikipe-tan.svg/220px-Neko_Wikipe-tan.svg.png > neko.png
export FONT_INPUT=sazanami-gothic.ttf # curl https://github.com/limaconoob/Image2font/raw/master/tests/assets/ttf/sazanami-gothic.ttf > sazanami-gothic.ttf
export FONT_OUTPUT=neko.ttf

docker cp $IMAGES $(make get):/root/image2font/$IMAGES
docker cp $FONT_INPUT $(make get):/root/image2font/$FONT_INPUT
docker exec $(make get) python image2font --input-font $FONT_INPUT --output-font $FONT_OUTPUT $IMAGES
docker cp $(make get):/root/image2font/$FONT_OUTPUT $FONT_OUTPUT
cp -f $FONT_OUTPUT $HOME/.local/share/fonts
```
