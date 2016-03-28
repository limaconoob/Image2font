import itertools;
import core;

from optparse import OptionParser;

if __name__ == '__main__':
    parser = OptionParser (
        usage = "%prog [options] arg1.png [...]",
        version = "%prog 1.0",
    );
    parser.add_option ("-w", "--grid-width",
        dest = "grid_width",
        default = 10,
        help = "sets the cell width unity from picture",
    );
    parser.add_option ("-a", "--grid-heigth",
        dest = "grid_height",
        default = 5,
        help = "sets the cell height unity from picture",
    );
    parser.add_option ("-c", "--cell-width",
        dest = "cell_width",
        default = 50,
        help = "sets the cell width pixel from picture",
    );
    parser.add_option ("-b", "--cell-heigth",
        dest = "cell_height",
        default = 100,
        help = "sets the cell height pixel from picture",
    );
    parser.add_option ("-i", "--input-font",
        dest = "input",
        default = "",
        help = "modify this existent font",
    );
    parser.add_option ("-o", "--output-font",
        dest = "output",
        default = "a.out.ttf",
        help = "specify the namefont to create",
    );
    parser.add_option ("-s", "--start-index",
        dest = "index",
        default = (bool(parser.parse_args()[0].input) and 0xe000) or 0x0000,
        help = "start to write the glyphs at this index",
    );
    parser.add_option ("-n", "--name-font",
        dest = "name",
        default = (''.join(itertools.takewhile(lambda x: x != '.', parser.parse_args()[0].input))).split('/')[-1:][0],
        help = "is the name of font",
    );

    arg = parser.parse_args();
    core.run_eg(arg[0], arg[1]);
