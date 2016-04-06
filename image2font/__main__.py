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
        help = "Sets the cell width unity from picture.",
    );
    parser.add_option ("-a", "--grid-heigth",
        dest = "grid_height",
        default = 5,
        help = "Sets the cell height unity from picture.",
    );
    parser.add_option ("-c", "--cell-width",
        dest = "cell_width",
        default = 50,
        help = "Sets the cell width pixel from picture.",
    );
    parser.add_option ("-b", "--cell-heigth",
        dest = "cell_height",
        default = 100,
        help = "Sets the cell height pixel from picture.",
    );
    parser.add_option ("-i", "--input-font",
        dest = "input",
        default = "",
        help = "Modify this existent font.",
    );
    parser.add_option ("-o", "--output-font",
        dest = "output",
        default = "",
        help = "Specify the namefont to create.",
    );
    parser.add_option ("-s", "--start-index",
        dest = "index",
        default = 0xe000,
        help = "Start to write the glyphs at 0xE000's index if there is `input-font` else at 0x0000.",
    );
    parser.add_option ("-n", "--name-font",
        dest = "name",
        default = "",
        help = "Is the name of font.",
    );

    arg = parser.parse_args();
    arg[0].index = int(arg[0].index);
    if not bool(arg[0].input):
        arg[0].index = 0xe0000;
    if not bool(arg[0].name):
        arg[0].name = (''.join(itertools.takewhile(lambda x: x != '.', parser.parse_args()[0].input))).split('/')[-1:][0];
    if not bool(arg[0].output):
        arg[0].output = arg[0].name + ".ttf";
    core.run_eg(arg[0], arg[1]);
