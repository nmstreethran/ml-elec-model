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
copyright = '2020, Nithiya Streethran.'
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
        'verbatimwithframe=false, \
        TitleColor={rgb}{0,0,0}, \
        VerbatimColor={rgb}{1,.98,.98}, \
        InnerLinkColor={rgb}{.86,.08,.24}, \
        OuterLinkColor={rgb}{1,.49,0}',
    'fncychap': '',
    'printindex': '',
    'figure_align': '!htb',
    'preamble': r'''
        %% fonts
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{newpxtext}
        \usepackage{newpxmath}
        \usepackage[defaultsans]{lato}
        \usepackage[zerostyle=c,straightquotes]{newtxtt}
        % remove emphasis from glossary references
        \protected\def\sphinxtermref#1{#1}
        % change toc title font
        \usepackage{tocloft}
        \renewcommand{\cfttoctitlefont}{\Huge\bfseries\sffamily}

        %% titlepage and metadata
        \makeatletter
        \renewcommand{\sphinxmaketitle}{
            \hypersetup{
                pdftitle={\@title~docs, \py@release release},
                pdfauthor={\@author},
                pdfkeywords={machine learning, electricity system model, open source},
                pdfsubject={License: CC BY 4.0}
            }
            \hspace{0pt}\vfill
            {\sffamily
            \Huge\textbf{\@title}~docs \vskip2pt
            \LARGE\textit{\py@release}release \vskip20pt
            \Large\@author \vskip4pt
            \large\today \vskip20pt
            Documentation: \href{https://ml-elec-model.rtfd.io/}{ml-elec-model.rtfd.io} \vskip2pt
            GitHub: \href{https://github.com/nmstreethran/ml-elec-model}{nmstreethran/ml-elec-model}
            }
            \vfill\hspace{0pt}
        }
        \makeatother

        %% tables
        % change table heading style
        \renewcommand{\sphinxstyletheadfamily}{\rmfamily\bfseries}
        % change longtable continuation style and font size
        \renewcommand{\sphinxtablecontinued}{\rmfamily}
        \let\oldlongtable\longtable
        \renewcommand{\longtable}{\footnotesize\oldlongtable}
        % change tabulary font size
        \let\oldtabulary\tabulary
        \renewcommand{\tabulary}{\footnotesize\oldtabulary}
        % table captions
        \usepackage[font=small,labelfont=bf]{caption}
        % use booktabs and remove all table rules
        \usepackage{booktabs}
        \setlength{\arrayrulewidth}{0pt}

        %% remove section numbering
        \setcounter{secnumdepth}{0}
        % reset numbering for figures, tables, and footnotes
        \usepackage{chngcntr}
        \counterwithout{footnote}{chapter}
        \counterwithout{figure}{chapter}
        \counterwithout{table}{chapter}
        % remove chapter numbers and labels
        \titleformat{\chapter}[display]{\bfseries\sffamily}{}{-40pt}{\Huge}
        \renewcommand{\thechapter}{}
        % adjust chapter alignments in toc
        \setlength{\cftchapnumwidth}{0em}

        %% header and footer
        % for all pages
        \makeatletter
            \fancypagestyle{normal}{
                \fancyhf{}
                \fancyfoot[C]{\sffamily\thepage}
                \fancyhead[LE,RO]{\sffamily\@title, \textit{\py@release}}
                \renewcommand{\headrulewidth}{0pt}
            }
            % for the first page of the chapter
            \fancypagestyle{plain}{
                \fancyhf{}
                \fancyfoot[C]{\sffamily\thepage}
                \renewcommand{\headrulewidth}{0pt}
            }
        \makeatother

        %% bibliography
        \renewenvironment{sphinxthebibliography}[1]{
            % remove the bibliography title and page break
            \renewcommand{\chapter}[2]{}
            \begin{thebibliography}{#1}
            }{\end{thebibliography}
        }
    '''
}
