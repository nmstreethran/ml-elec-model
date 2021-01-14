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
copyright = (
    '2018-2021, Nithiya Streethran. Except where otherwise noted, ' +
    'content on this site is licensed under a Creative Commons ' +
    'Attribution 4.0 International (CC-BY-4.0) license')
author = 'Nithiya Streethran'
# version = '0.1.0'
# release = '0.1.0'


# -- General configuration ---------------------------------------------------

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

# last updated date format
html_last_updated_fmt = '%-d %B %Y'

# directories of .py files for bokeh plots
bokeh_plot_pyfile_include_dirs = ['../scripts']
