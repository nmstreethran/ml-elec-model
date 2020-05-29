About
=====

`Documentation <https://ml-elec-model.rtfd.io/>`__ // `Git repository <https://github.com/nmstreethran/ml-elec-model>`__

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please open an issue or refer to the contributing guidelines in the main repository if you would like to contribute.**

Machine learning-based electricity system model.

Requirements
------------

**Packages:**

- `Bokeh <https://bokeh.org/>`__
- `dwdweather2 <https://github.com/KartikTalwar/Duolingo>`__
- `entsoe-py <https://github.com/EnergieID/entsoe-py>`__
- `GeoPandas <https://geopandas.org/>`__
- `Matplotlib <https://matplotlib.org/>`__
- `NumPy <https://numpy.org/>`__
- `Pandas <https://pandas.pydata.org/>`__
- `pyproj <https://pyproj4.github.io/pyproj/stable/>`__
- `requests <https://requests.readthedocs.io/en/master/>`__
- `Shapely <https://shapely.readthedocs.io/en/latest/>`__
- `pytz <https://pythonhosted.org/pytz/>`__
- `beautifulsoup4 <https://www.crummy.com/software/BeautifulSoup/>`__

**Installation:**

1. (Recommended) Create and activate a virtual environment:

   .. code:: sh

      python3 -m venv env
      source env/bin/activate

2. Install dependencies:

   .. code:: sh

      pip install pandas numpy requests matplotlib pyproj shapely geopandas bokeh pytz beautifulsoup4 entsoe-py dwdweather2

*Using Anaconda:*

1. (Recommended) Create and activate a virtual environment:

   .. code:: sh

      conda create --name ml-elec-model python=3
      conda activate ml-elec-model

2. Install required packages:

   .. code:: sh

      conda install pandas numpy requests matplotlib pyproj shapely geopandas bokeh pytz beautifulsoup4
      pip install entsoe-py dwdweather2

Cloning the repository
----------------------

To clone the latest version of this repository:

**Using HTTPS:**

.. code:: sh

   git clone https://github.com/nmstreethran/ml-elec-model.git

**Using SSH:**

.. code:: sh

   git clone git@github.com:nmstreethran/ml-elec-model.git

Documentation
-------------

The documentation is maintained in this repository's `GitHub Wiki <https://github.com/nmstreethran/ml-elec-model/wiki>`__, built using `Sphinx <https://www.sphinx-doc.org/en/master/>`__, and hosted using `Read the Docs <https://readthedocs.org>`__. It is available at https://ml-elec-model.rtfd.io. The files can be found in the ``docs`` folder.

To build the documentation locally, clone this repository and install a TeX distribution (such as `TeX Live <http://tug.org/texlive/>`__). Then, install the required Sphinx Python package and Read the Docs theme as follows:

.. code:: sh

   pip install sphinx sphinx-rtd-theme

Local builds of the documentation in HTML and PDF formats can be viewed after running the following bash script by opening ``docs/_build/html/index.html`` and ``docs/_build/latex/ml-elec-model.pdf`` respectively:

.. code:: sh

   bash docs.sh

A list of references used is available on `Zotero <https://www.zotero.org/groups/2327899/ml-elec-model/library>`__.

Charts
------

Charts generated are available at https://github.com/nmstreethran/charts/tree/ml-elec-model.

License
-------

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the `MIT License <https://opensource.org/licenses/MIT>`__.
- content, images, and documentation are licensed under a `Creative Commons Attribution 4.0 International (CC BY 4.0) License <https://creativecommons.org/licenses/by/4.0/>`__.
- charts are licensed under the `Apache 2.0 License <https://www.apache.org/licenses/LICENSE-2.0.html>`__.

Credits
-------

This repository is a continuation and improvement of the work done by Nithiya Streethran in `ENSYSTRA/short-term-forecasting <https://github.com/ENSYSTRA/short-term-forecasting>`__.
ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines is adapted from the `Open Science MOOC <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source>`__. The contents of the MOOC are licensed under a `Creative Commons Zero v1.0 Universal License <https://creativecommons.org/publicdomain/zero/1.0/>`__.

The Creative Commons license in markdown format is imported from `idleberg/Creative-Commons-Markdown <https://github.com/idleberg/Creative-Commons-Markdown>`__.
