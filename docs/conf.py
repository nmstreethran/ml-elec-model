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
copyright = '2018-2020, Nithiya Streethran. Except where otherwise noted, \
content on this site is licensed under a Creative Commons Attribution 4.0 \
International (CC BY 4.0) license'
author = 'Nithiya Streethran'
# version = '0.1.0'
# release = '0.1.0'


# -- General configuration ---------------------------------------------------

# import libraries

# override default master doc from contents
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'bokeh.sphinxext.bokeh_plot',
    # 'jupyter_sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

html_logo = '_static/house.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'external_links': [
        {'url': 'https://gitlab.com/nithiya/ml-elec-model',
            'name': 'GitLab'},
        {'url': 'https://www.zotero.org/groups/2327899/ml-elec-model/library',
            'name': 'Zotero'},
        {'url': 'https://gitlab.com/nithiya/ml-elec-model-data',
            'name': 'Datasets'}
    ]
}

# directories of .py files for bokeh plots
bokeh_plot_pyfile_include_dirs = ['../scripts']

# # -- LaTeX options ---------------------------------------------------------
# latex_documents = [('index', project + '.tex', project + ' docs',
#     author, 'manual', True)]

# latex_elements = {
#     'papersize': 'a4paper',
#     'pointsize': '11pt',
#     'sphinxsetup':
#         'verbatimwithframe=false, \
#         TitleColor={rgb}{0,0,0}, \
#         VerbatimColor={rgb}{1,.98,.98}, \
#         InnerLinkColor={rgb}{.86,.08,.24}, \
#         OuterLinkColor={rgb}{1,.49,0}',
#     'fncychap': '',
#     'printindex': '',
#     'figure_align': '!htb',
#     'preamble': r'''
#         % % fix headheight issue
#         \geometry{headheight=13.6pt}

#         % % fonts
#         \usepackage{mathtools}
#         \usepackage{newpxtext}
#         \usepackage{newpxmath}
#         \usepackage[defaultsans]{lato}
#         \usepackage[zerostyle=c,straightquotes]{newtxtt}
#         % remove emphasis from glossary references
#         \protected\def\sphinxtermref#1{#1}
#         % change toc title font
#         \usepackage{tocloft}
#         \renewcommand{\cfttoctitlefont}{\Huge\bfseries\sffamily}

#         % % titlepage and metadata
#         \hypersetup{
#             pdfkeywords={machine learning, electricity system model,
#             open source},
#             pdfsubject={License: CC BY 4.0}
#         }

#         % % tables and captions
#         % change table heading style
#         \renewcommand{\sphinxstyletheadfamily}{\rmfamily\bfseries}
#         % change longtable continuation style and font size
#         \renewcommand{\sphinxtablecontinued}{\rmfamily}
#         \let\oldlongtable\longtable
#         \renewcommand{\longtable}{\footnotesize\oldlongtable}
#         % change tabulary font size
#         \let\oldtabulary\tabulary
#         \renewcommand{\tabulary}{\footnotesize\oldtabulary}
#         % captions
#         \usepackage[font=small,labelfont=bf,figurename=Figure~]{caption}
#         % use booktabs and remove all table rules
#         \usepackage{booktabs}
#         \setlength{\arrayrulewidth}{0pt}

#         % % remove section numbering
#         \setcounter{secnumdepth}{0}
#         % reset numbering for figures, tables, and footnotes
#         \usepackage{chngcntr}
#         \counterwithout{footnote}{chapter}
#         \counterwithout{figure}{chapter}
#         \counterwithout{table}{chapter}
#         % remove chapter numbers and labels
#         \titleformat{\chapter}[display]{\bfseries\sffamily}{}{-40pt}{\Huge}
#         \renewcommand{\thechapter}{}
#         % adjust chapter alignments in toc
#         \setlength{\cftchapnumwidth}{0em}

#         % % header and footer
#         % for all pages
#         \makeatletter
#             \fancypagestyle{normal}{
#                 \fancyhf{}
#                 \fancyfoot[C]{\sffamily\thepage}
#                 \fancyhead[LE,RO]{\sffamily\textit{\@title}}
#                 \renewcommand{\headrulewidth}{1pt}
#             }
#             % for the first page of the chapter
#             \fancypagestyle{plain}{
#                 \fancyhf{}
#                 \fancyfoot[C]{\sffamily\thepage}
#                 \renewcommand{\headrulewidth}{0pt}
#             }
#         \makeatother

#         % % bibliography
#         \renewenvironment{sphinxthebibliography}[1]{
#             % remove automatically-generated bibliography title
#             % and page break
#             \renewcommand{\chapter}[2]{}
#             \begin{thebibliography}{#1}
#             }{\end{thebibliography}
#         }
#     '''
# }
