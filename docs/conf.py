# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ml-elec-model'
copyright = '2020, Nithiya Streethran'
author = 'Nithiya Streethran'


# -- General configuration ---------------------------------------------------

# import libraries
import sphinx_rtd_theme

# override default master doc from contents
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- LaTeX options -----------------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

# preamble
    'preamble': r'''
        %% fonts and encoding
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{CormorantGaramond}
        \usepackage[defaultsans]{lato}
        \usepackage{FiraMono}
        %% sections
        \setcounter{secnumdepth}{0}
        %% graphics
        \usepackage{graphicx,grffile,tikz,tikzpagenodes}
        \usetikzlibrary{positioning}
        \makeatletter
        \def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
        \def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
        \makeatother
        % Scale images if necessary, so that they will not overflow the page
        % margins by default, and it is still possible to overwrite the defaults
        % using explicit options in \includegraphics[width, height, ...]{}
        \setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}
        % set default figure placement to htbp
        \makeatletter
        \def\fps@figure{!htb} %%% modified
        \makeatother
        %% tables
        \usepackage{longtable,booktabs}
        % table font size
        \let\oldtabular\longtable
        \renewcommand{\longtable}{\footnotesize\oldtabular}
        \usepackage[font=small,labelfont=bf]{caption}
    ''',
}
