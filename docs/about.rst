About
=====

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please open an issue or refer to the contributing guidelines in the main repository if you would like to contribute.**

Machine learning-based electricity system model.

Requirements
------------

**Packages:**

- `Bokeh <https://bokeh.org/>`__
- `entsoe-py <https://pypi.org/project/entsoe-py/>`__
- `GeoPandas <https://geopandas.org/>`__
- `Matplotlib <https://matplotlib.org/>`__
- `NumPy <https://numpy.org/>`__
- `Pandas <https://pandas.pydata.org/>`__
- `pyproj <https://pypi.org/project/pyproj/>`__
- `requests <https://pypi.org/project/requests/>`__
- `Shapely <https://pypi.org/project/Shapely/>`__

**Installation:**

1. (Recommended) Create and activate a virtual environment:

    .. code:: sh

        python3 -m venv env
        source env/bin/activate

2. Install dependencies:

    .. code:: sh

        pip install pandas numpy requests matplotlib pyproj shapely geopandas bokeh entsoe-py

*Using Anaconda:*

1. (Recommended) Create and activate a virtual environment:

    .. code:: sh

        conda create --name ml-elec-model python=3
        conda activate ml-elec-model

2. Install required packages:

    .. code:: sh

        conda install pandas numpy requests matplotlib pyproj shapely geopandas bokeh
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

The documentation is maintained in this repository's `GitHub Wiki <https://github.com/nmstreethran/ml-elec-model/wiki>`__ and built using `Sphinx <https://www.sphinx-doc.org/en/master/>`__ and `Read the Docs <https://readthedocs.org>`__. It is available at https://ml-elec-model.rtfd.io. The files can be found in the ``docs`` folder.

To build the documentation locally, clone this repository (including submodules) and install a TeX distribution (such as `TeX Live <http://tug.org/texlive/>`__). Then, install the required Sphinx Python packages as follows:

.. code:: sh

    pip install sphinx sphinx-rtd-theme

The GitHub wiki has been included in this repository as a submodule. All changes must be made to the files within this submodule (i.e., the ``wiki`` directory). Once changes are made, the following bash script must be executed to compile the documentation:

.. code:: sh

    bash docs.sh

Then, commit and push all changes to the wiki's branch. Finally, commit and push to the main repository's branch.

Local builds of the documentation in HTML and PDF formats can be viewed after running the above bash script by opening ``docs/_build/html/index.html`` and ``docs/_build/latex/ml-elec-model.pdf`` respectively.

A list of references used is available on `Zotero <https://www.zotero.org/groups/2327899/ml-elec-model/library>`__.

License
-------

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the `MIT License <https://opensource.org/licenses/MIT>`__.
- content, images, and documentation are licensed under a `Creative Commons Attribution 4.0 International (CC BY 4.0) License <https://creativecommons.org/licenses/by/4.0/>`__.

Credits
-------

This repository is a continuation and improvement of the work done by Nithiya Streethran in `ENSYSTRA/short-term-forecasting <https://github.com/ENSYSTRA/short-term-forecasting>`__.
ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines is adapted from the `Open Science MOOC <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source>`__. The contents of the MOOC are licensed under a `Creative Commons Zero v1.0 Universal License <https://creativecommons.org/publicdomain/zero/1.0/>`__.

The Creative Commons license in markdown format is imported from `idleberg/Creative-Commons-Markdown <https://github.com/idleberg/Creative-Commons-Markdown>`__.
