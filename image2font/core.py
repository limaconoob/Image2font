import fontforge;
import subprocess;

class ToTtf:
    index = 0;

    def __init__ (self, option):
        """ The `__init__` constructor function inits the font's option. """
        if not option.input:
            self.font = fontforge.font();
        else:
            self.font = fontforge.open(option.input);
            self.font.encoding = 'UnicodeBmp';
            self.font.version = '2.000;PS 1;hotconv 1.0.49;makeotf.lib2.0.14853';
            self.font.weight = 'Book'
            self.font.fontname = option.name;
            self.font.familyname = option.name;
            self.font.fullname = option.name;
            self.font.ascent = 1000;
            self.font.descent = 200;
            self.font.em = 1000;
            self.font.addLookup('liga', 'gsub_ligature', (), (
                (
                    'liga',
                    (
                        ('latn', ('dflt')),
                    )
                ),
            ));
            self.font.addLookupSubtable('liga', 'liga');
        self.output = option.output;
        self.index = option.index;

    def __del__ (self):
        """ The `__del__` destructor function generates the output new font
            and closes the input source file. """
        self.font.generate(self.output);
        self.font.close();

    def run (self, vectors):
        """ The `run` function appends all vector's glyph. """
        for vector in vectors:
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
            glyph.importOutlines (
               vector,
               self.index,
            );
            self.index += 1;

class Core:
    build = "obj"; # source_build

    def __init__(self, option):
        """ The `__init__` constructor function inits the source's option. """
        self.option = option;

    def run (self, source):
        """ The `run` function resizes, crops and runs the `svg2pnm` module. """
        to_ttf = ToTtf(self.option);
        vectors = [];
        index = 0;

        self.resize(source);
        self.crop();
        width =  self.option.grid_width * self.option.cell_width;
        height = self.option.grid_height * self.option.cell_height;
        for x in range(width / self.option.cell_width):
            for y in range(height / self.option.cell_height):
                coordinate = str(x) + '-' + str(y);
                self.to_pnm(index, coordinate);
                self.to_svg(coordinate);
                vectors.append (
                    self.build + '/' + self.option.name \
                               + '.' + coordinate + ".svg"
                );
                index += 1;
        to_ttf.run(vectors);

    # Command:
    # ```shell
    # convert image.png -resize $(echo $(($GRID_WIDTH*CELL_WIDTH))
    #                                 x$(($GRID_HEIGHT*CELL_HEIGHT))'!')
    #                   -gravity center images.png
    # ```

    def resize (self, source, name=""):
        """ The `resize` function returns the resized image source. """
        name = (bool(name) and name) or str(self.build + '/' + self.option.name);
        width = str(self.option.grid_width * self.option.cell_width);
        height = str(self.option.grid_height * self.option.cell_height);
        return subprocess.check_call([
            "convert",
            source,
            "-resize",
            width + 'x' + height + '!',
            "-gravity",
            "center",
            name + ".png",
        ]);

    # Command:
    # ```shell
    # convert -crop $(echo "$CELL_WIDTH"
    #                     x"$CELL_HEIGHT") images.png image-%d.png.
    # ```

    def crop (self, name=""):
        """ The `crop` function returns the cropped image. """
        name = (bool(name) and name) or str (
            self.build + '/' + self.option.name
        );
        width = str(self.option.cell_width);
        height = str(self.option.cell_height);
        return subprocess.check_call([
            "convert",
            "-crop",
            width + 'x' + height,
            name + ".png",
            name + "-%d.png",
        ]);

    # Command:
    # ```shell
    # convert {}.png -alpha Remove {}.pnm.
    # ```

    def to_pnm (self, index, coordinate, name=""):
        """ The `to_pnm` function returns the unalphed image. """
        name = (bool(name) and name) or self.build + '/' + self.option.name;
        source = name + '-' + str(index);
        destination = name + '.' + str(coordinate);
        return subprocess.check_call([
            "convert",
            source + ".png",
            "-alpha",
            "Remove",
            destination + ".pnm",
        ]);

    # Command:
    # ```shell
    # potrace -s {}.pnm --color=#FFFFFF -o {}.svg.
    # ```

    def to_svg (self, coordinate, name=""):
        """ The `to_svg` function returns and vectorized image
            with a white backgroud. """
        name = (bool(name) and name) or self.build + '/' + self.option.name \
                                                   + '.' + coordinate;
        return subprocess.check_call([
            "potrace",
            "-s",
            name + ".pnm",
            "--color=#FFFFFF",
            "-o",
            name + ".svg",
        ]);

def run_eg (option, images):
    core = Core(option);

    for image in images:
        core.run(image);
