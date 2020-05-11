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

html_theme_options = {
     'style_external_links': True
}

# -- LaTeX options -----------------------------------------------------------

latex_elements = {
    'releasename': 'latest',
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'sphinxsetup':
        'verbatimwithframe=false, TitleColor={rgb}{0,0,0}, VerbatimColor={rgb}{255,255,240}', 
    'extraclassoptions': 'openany',
    'fncychap': '',
    'printindex': '',
    'figure_align': '!htb',
    'preamble': r'''
        %% hyperlinks and metadata
        \hypersetup{
            linkcolor=purple,
            urlcolor=purple,
            citecolor=purple,
            pdfkeywords={machine learning, electricity system model, open source},
            pdfsubject={ml-elec-model documentation (CC BY 4.0)}}
        % remove emphasis from glossary references
        \protected\def\sphinxtermref#1{#1}
        %% fonts
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{newpxtext}
        \usepackage{newpxmath}
        \usepackage[defaultsans]{lato}
        \usepackage[zerostyle=c,straightquotes]{newtxtt}
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
        %% toc font
        \usepackage{tocloft}
        \renewcommand{\cfttoctitlefont}{\Huge\bfseries\sffamily}
        %% numbering
        \setcounter{secnumdepth}{0}
        % reset numbering
        \usepackage{chngcntr}
        \counterwithout{footnote}{chapter}
        \counterwithout{figure}{chapter}
        \counterwithout{table}{chapter}
        % remove chapter numbers and labels
        \titleformat{\chapter}[display]{\bfseries\sffamily}{}{-40pt}{\Huge}
        \renewcommand{\thechapter}{}
        \setlength{\cftchapnumwidth}{0em}
        %% header and footer
        \makeatletter
            \fancypagestyle{normal}{
                \fancyhf{}
                \fancyfoot[LO,RE]{{\py@HeaderFamily\thepage}}
                \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \textit{\py@release}}}
                \renewcommand{\headrulewidth}{0.4pt}
                \renewcommand{\footrulewidth}{0.4pt}
            }
        \makeatother
        %% bibliography
        \renewenvironment{sphinxthebibliography}[1]{%
            \renewcommand{\chapter}[2]{}
            \begin{thebibliography}{#1}%
            }{\end{thebibliography}
        }
    '''
}
