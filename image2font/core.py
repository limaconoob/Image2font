from PIL import Image;

from resizeimage import resizeimage;

import fontforge;

class ToTtf:
    def __init__ (self, option):
        """ The `__init__` constructor function inits the option. """
        if not option.input:
            self.font = fontforge.font();
        else:
            self.font = fontforge.open(option.input);
            self.font.encoding = 'UnicodeBmp'
            self.font.version = '2.000;PS 1;hotconv 1.0.49;makeotf.lib2.0.14853'
            self.font.weight = 'Book'
            self.font.fontname = option.name;
            self.font.familyname = option.name;
            self.font.fullname = option.name;
            self.font.ascent = 1000;
            self.font.descent = 200;
            self.font.em = 1000;
            self.font.addLookup('liga', 'gsub_ligature', (), (('liga', (('latn', ('dflt')), )), ));
            self.font.addLookupSubtable('liga', 'liga');
        self.output = option.output;
        self.index = option.index;

    def __del__ (self):
        self.font.generate(self.output);
        self.font.close();

    def run (self, images):
        for image in images:
            glyph = self.font.createChar (
                self.index,
            );
            glyph.left_side_bearing = 0.0;
            glyph.right_side_bearing = 500.0;
            glyph.temporary = None;
            glyph.texheight = 32767;
            glyph.texdepth = 32767;
            glyph.topaccent = 32767;
            glyph.verticalComponents = None;
            glyph.verticalComponentItalicCorrection = 0;
            glyph.verticalVariants = None;
            glyph.width = 500;
            glyph.vwidth = 1000;
            #glyph.importOutlines (
            #   image,
            #   self.index,
            #);
            self.index += 1;


class Core:
    def __init__(self, option):
        """ The `__init__` constructor function inits the option. """
        self.option = option;

    def run (self, source):
        """ The `run` function resizes, crops and runs the `svg2pnm` module. """
        to_ttf = ToTtf(self.option);

        with open(source, 'r+b') as f:
            with Image.open(f) as image:
                image = self.resize(image);
                images = self.crops(image);
                to_ttf.run(images);

    def resize (self, image):
        """ The `resize` function returns the resized image. """
        return resizeimage.resize_cover (
            image,
            [
                self.option.grid_width * self.option.cell_width,
                self.option.grid_height * self.option.cell_height,
            ]
        );

    def crops (self, image):
        """ The `crops` function returns a list of cropped images. """
        images = [];

        for x in range(self.option.cell_width / self.option.grid_width):
            for y in range(self.option.cell_height / self.option.grid_height):
                images.append (
                    self.crop(image, x, y)
                );
        return images;

    def crop (self, image, x, y):
        """ The `crop` function returns the cropped image. """
        return resizeimage.resize_crop (
            image,
            [
                self.option.cell_width,
                self.option.cell_height,
                x,
                y,
            ]
        );

def run_eg (option, images):
    core = Core(option);

    for image in images:
        core.run(image);
