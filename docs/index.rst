Welcome to ml-elec-model's documentation!
=========================================

.. image:: https://img.shields.io/badge/code%20license-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: Code license: MIT
.. image:: https://img.shields.io/badge/content%20license-CC%20BY%204.0-blue.svg
    :target: https://creativecommons.org/licenses/by/4.0/
    :alt: Content license: CC BY 4.0
.. image:: https://travis-ci.org/nmstreethran/ml-elec-model.svg?branch=master
    :target: https://travis-ci.org/nmstreethran/ml-elec-model
    :alt: Travis CI build status
.. image:: https://readthedocs.org/projects/ml-elec-model/badge/?version=latest
    :target: https://ml-elec-model.readthedocs.io/en/latest/?badge=latest
    :alt: Read the Docs build status
.. image:: https://img.shields.io/badge/-repository-purple.svg?logo=github&labelColor=black
    :target: https://github.com/nmstreethran/ml-elec-model
    :alt: GitHub Repository

.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: Contents

    background
    regions
    entso-e-data
    german-meteorological-data
    glossary
    license

by nmstreethran at gmail dot com

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please open an issue or refer to the contributing guidelines in the main repository if you would like to contribute.**

Machine learning-based electricity system model.

Requirements
------------

Packages
~~~~~~~~

- `Bokeh <https://bokeh.org/>`__
- `entsoe-py <https://pypi.org/project/entsoe-py/>`__
- `GeoPandas <https://geopandas.org/>`__
- `NumPy <https://numpy.org/>`__
- `Pandas <https://pandas.pydata.org/>`__
- `pyproj <https://pypi.org/project/pyproj/>`__
- `requests <https://pypi.org/project/requests/>`__
- `Shapely <https://pypi.org/project/Shapely/>`__

Installation
~~~~~~~~~~~~

1. (Recommended) Create and activate a virtual environment:

    .. code:: sh

        python3 -m venv env
        source env/bin/activate

2. Install dependencies:

    .. code:: sh

        pip install entsoe-py geopandas bokeh

**Using Anaconda:**

1. (Recommended) Create and activate a virtual environment:

    .. code:: sh

        conda create --name ml-elec-model python=3
        conda activate ml-elec-model

2. Install required packages:

    .. code:: sh

        conda install --channel conda-forge geopandas bokeh
        pip install entsoe-py

Cloning the repository
----------------------

To clone the latest version of this repository, including the contents of the submodule:

**Using HTTPS:**

.. code:: sh

    git clone --recurse-submodules https://github.com/nmstreethran/ml-elec-model.git

**Using SSH:**

.. code:: sh

    git clone --recurse-submodules git@github.com:nmstreethran/ml-elec-model.git

Documentation
-------------

The documentation is maintained in in the repository's `GitHub Wiki <https://github.com/nmstreethran/ml-elec-model/wiki>`__ and built using Sphinx and Read the Docs. The files can also be found in the ``docs`` folder.

The GitHub wiki has been included in this repository as a submodule. Once changes to the wiki within the submodule are made (e.g., new markdown files, images), these changes are first committed and pushed to the wiki's branch, before committing and pushing to the main repository's branch.

The documentation in PDF format incorporates the following fonts:

- `EB Garamond by Georg Duffner <https://fonts.google.com/specimen/EB+Garamond>`__, licensed under the `SIL Open Font License <http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web>`__
- `Lato by Łukasz Dziedzic <https://fonts.google.com/specimen/Lato>`__, licensed under the `SIL Open Font License <http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web>`__
- `Fira Code by Nikita Prokopov <https://github.com/tonsky/FiraCode>`__, licensed under the `SIL Open Font License <http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web>`__

Pandoc is Copyright (c) 2006-2019 John MacFarlane (jgm at berkeley dot edu), released under the `GNU General Public License version 2 <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>`__ or later.
To compile the documentation locally, Pandoc and Sphinx are required.
Install the required Sphinx Python packages as follows:

.. code:: sh

    pip install sphinx, sphinx-rtd-theme

Run the following bash script to compile:

.. code:: sh

    bash docs.sh

License
-------

Unless otherwise stated:

- Python scripts, Jupyter notebooks and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the `MIT License <https://opensource.org/licenses/MIT>`__.
- content, images and documentation are licensed under the `Creative Commons Attribution 4.0 International (CC BY 4.0) License <https://creativecommons.org/licenses/by/4.0/>`__.

Credits
-------

Badges are generated using `Shields.io <https://shields.io>`__.
Shields.io is licensed under a `Creative Commons Zero v1.0 Universal License <https://creativecommons.org/publicdomain/zero/1.0/>`__.

Icons used within badges are from `Simple Icons <https://simpleicons.org/>`__.
Simple Icons is licensed under a `Creative Commons Zero v1.0 Universal License <https://creativecommons.org/publicdomain/zero/1.0/>`__.

The Creative Commons license in markdown format is imported from `idleberg/Creative-Commons-Markdown <https://github.com/idleberg/Creative-Commons-Markdown>`__.

This repository is a continuation and improvement of the work done by Nithiya Streethran in `ENSYSTRA/short-term-forecasting <https://github.com/ENSYSTRA/short-term-forecasting>`__.
ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines is adapted from the `Open Science MOOC <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source>`__. The contents of the MOOC are licensed under a `Creative Commons Zero v1.0 Universal License <https://creativecommons.org/publicdomain/zero/1.0/>`__.
