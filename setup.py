from setuptools import setup

setup (
    name = 'Image2font',
    version = '0.0.1',
    license = 'GPL 3',
    author = 'limaconoob, adjivas',
    author_email = 'limaconoob@users.noreply.github.com, adjivas@users.noreply.github.com',
    url = 'https://github.com/limaconoob/Image2font',
    description = 'Add an image or vectoriel to a font',

    packages = ['image2font'],
    install_requires = [],
    package_data = {
        'assets': [
            'ttf/*.ttf',
        ],
    },
    entry_points = {
        'console_scripts': [
            'image2font=image2font.main:main',
        ],
    },
    zip_safe = False,
)
