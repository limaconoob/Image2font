# Image2font

[![travis-badge][]][travis] [![license-badge][]][license]

[travis-badge]: https://travis-ci.org/limaconoob/Image2font.svg?branch=master&style=flat-square
[travis]: https://travis-ci.org/limaconoob/Image2font
[license-badge]: http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square
[license]: https://github.com/limaconoob/Image2font/blob/master/LICENSE

##### Usage
By example:
```shell
git clone https://github.com/limaconoob/Image2font.git image2font && cd image2font
python image2font --input-font tests/assets/ttf/sazanami-gothic.ttf tests/assets/neko_wikipe-tan.png
cp -f sazanami-gothic.ttf $HOME/.local/share/fonts
```

For more information, see the **help**'s command:
```text
Usage:  [options] arg1.png [...]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -w GRID_WIDTH, --grid-width=GRID_WIDTH
                        Sets the cell width unity from picture.
  -a GRID_HEIGHT, --grid-heigth=GRID_HEIGHT
                        Sets the cell height unity from picture.
  -c CELL_WIDTH, --cell-width=CELL_WIDTH
                        Sets the cell width pixel from picture.
  -b CELL_HEIGHT, --cell-heigth=CELL_HEIGHT
                        Sets the cell height pixel from picture.
  -i INPUT, --input-font=INPUT
                        Modify this existent font.
  -o OUTPUT, --output-font=OUTPUT
                        Specify the namefont to create.
  -s INDEX, --start-index=INDEX
                        Start to write the glyphs at 0xE000's index if there
                        is `input-font` else at 0x0000.
  -n NAME, --name-font=NAME
                        Is the name of font.
```

#### License

**image2font**'s code in this repo uses the [GNU GPL v3](http://www.gnu.org/licenses/gpl-3.0.html) [license](https://raw.githubusercontent.com/limaconoob/Image2font/master/LICENSE).

##### Dependencies
Many thanks goes to **command/etc**'s project:
* [python](https://www.python.org/ftp/python)
* [fontforge](https://github.com/fontforge/fontforge)
* [convert](https://github.com/ImageMagick/ImageMagick)
* [potrace](http://potrace.sourceforge.net)
* [Wikipedia (for the picture **neko**!)](https://en.wikipedia.org/wiki/Catgirl)
