from .tags import *
from .tempy import Content, Css, render_template, TagAttrs, TempyView

__version__ = '0.3.1'
VERSION = tuple(map(int, __version__.split('.')))
