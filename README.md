# Image2font

[![travis-badge][]][travis]

[travis-badge]: https://travis-ci.org/limaconoob/Image2font.svg?branch=master&style=flat-square
[travis]: https://travis-ci.org/limaconoob/Image2font

#### How to local use:
##### Example:
```shell
git clone https://github.com/limaconoob/Image2font.git image2font && cd image2font
python image2font --input-font tests/assets/ttf/sazanami-gothic.ttf tests/assets/neko_wikipe-tan.png
```

##### CLI:
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

#### Dependencies:
Many thanks goes to:

##### **Command/program**'s project:
* [python](https://www.python.org/ftp/python).
* [fontforge](https://github.com/fontforge/fontforge).
* [convert](https://github.com/ImageMagick/ImageMagick).
* [potrace](http://potrace.sourceforge.net).
