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

latex_elements = {
    'papersize': 'a4paper',

    'pointsize': '11pt',

    'sphinxsetup':
        'verbatimwithframe=false, TitleColor={rgb}{0,0,0}, VerbatimColor={rgb}{242,243,244}',
    
    'extraclassoptions': 'openany',

    'preamble': r'''
        % hyperlinks
        \hypersetup{linkcolor=blue,urlcolor=blue}
        %% fonts and encoding
        \usepackage{ebgaramond}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
        %% tables
        % table fonts
        \renewcommand{\sphinxstyletheadfamily}{\rmfamily\bfseries}
        \renewcommand{\sphinxtablecontinued}{\rmfamily}
        \let\oldlongtable\longtable
        \renewcommand{\longtable}{\footnotesize\oldlongtable}
        \let\oldtabulary\tabulary
        \renewcommand{\tabulary}{\footnotesize\oldtabulary}
        % captions
        \usepackage[font=small,labelfont=bf]{caption}
        % table rules
        \usepackage{booktabs}
        \setlength{\arrayrulewidth}{0pt}
        %% graphics
        % set default figure placement to htb
        \makeatletter
        \def\fps@figure{!htb}
        \makeatother
        %% numbering
        \setcounter{secnumdepth}{0}
        % reset numbering
        \usepackage{chngcntr}
        \counterwithout{footnote}{chapter}
        \counterwithout{figure}{chapter}
        \counterwithout{table}{chapter}
    '''
}
