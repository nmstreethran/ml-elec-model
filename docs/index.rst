Welcome to ml-elec-model's documentation!
=========================================

.. toctree::
   :maxdepth: 3
   :caption: Contents
   :hidden:

   literature/index
   method
   data_used/index
   glossary
   references

Machine learning-based electricity system model.

Repository: https://gitlab.com/nithiya/ml-elec-model

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please open an issue or refer to the contributing guidelines in the main repository if you would like to contribute.**

About
-----

Due to the global transition into a low-carbon energy system, there is an increase in electrification and decentralisation of the energy system with renewable energy resources. There is an increasing share of intermittent renewable energy resources, namely solar and wind, in supplying the electricity demand in Europe, with Germany having the highest share. Advancement in technology means that larger amounts of high-resolution data describing the electricity system will be collected, which can be exploited to better manage the intermittent system in the short term. This project will investigate how machine learning algorithms and publicly available electricity system and meteorological data can be used by wind and solar energy generating companies in Germany for short-term forecasting of the generation, load, and market prices, and subsequently manage their portfolio and bids in the electricity market. Due to the proprietary nature of existing tools used by energy companies, this project will propose a fully open-source solution.

**Focus:**

- Forecasting of electricity generation, load, and market prices using regression algorithms
- Data for the first half of 2018
   - German meteorological measurements and power plants
   - Generation, load, and market prices for the DE-AT-LU bidding zone
- Starting off with wind energy

Installing dependencies
-----------------------

Running scripts and building the documentation locally require a clone of this repository and installation of `Python 3 <https://www.python.org/>`__.

First, clone this repository via either HTTPS or SSH:

.. code:: sh

   # HTTPS
   git clone https://gitlab.com/nithiya/ml-elec-model.git

   # SSH
   git clone git@gitlab.com:nithiya/ml-elec-model.git

Then, create and activate a virtual environment (recommended):

.. code:: sh

   python3 -m venv env
   source env/bin/activate

Alternatively, if using `Anaconda <https://www.anaconda.com/products/individual>`__:

.. code:: sh

   conda create --name ml-elec-model python=3
   conda activate ml-elec-model

Finally, install the dependencies:

.. code:: sh

   pip install -r requirements.txt

If using Anaconda, the required packages can be alternatively be installed via `conda-forge <https://conda-forge.org/>`__, instead of using ``pip install``:

.. code:: sh

   conda install --channel conda-forge --file requirements.txt

To view the full list of dependencies, see ``requirements.txt``.

Documentation
-------------

The documentation is built using `Sphinx <https://www.sphinx-doc.org/en/master/>`__ and hosted using GitLab Pages. It is available at https://nithiya.gitlab.io/ml-elec-model/. The files can be found in the ``docs`` folder.

To build the documentation locally, clone this repository and install all requirements.

Local builds of the documentation in HTML format can be viewed in ``docs/_build/html/index.html`` after running ``make html`` in the ``docs`` directory.

A list of references used is available on `Zotero <https://www.zotero.org/groups/2327899/ml-elec-model/library>`__.

Data
----

Datasets used and their descriptions are available at https://gitlab.com/nithiya/ml-elec-model-data. To clone the repository with the data included, add ``--recurse-submodules`` after ``git clone``.

Raw data can be accessed using the GitLab API. For example, the following URL points to ``data/meteorology/stations.csv``. Slashes in the file path are URL encoded to ``%2F``.

.. code:: md

   https://gitlab.com/api/v4/projects/19753809/repository/files/meteorology%2Fstations.csv/raw?ref=master

License
-------

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the `MIT License (MIT) <https://opensource.org/licenses/MIT>`__.
- content, images, and documentation are licensed under a `Creative Commons Attribution 4.0 International (CC BY 4.0) license <https://creativecommons.org/licenses/by/4.0/>`__.

Credits
-------

This repository is a continuation and improvement of the work done by Nithiya Streethran in ENSYSTRA. ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines is adapted from the `Open Science MOOC <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source>`__. The contents of the MOOC are licensed under a `Creative Commons Zero v1.0 Universal (CC0 1.0) license <https://creativecommons.org/publicdomain/zero/1.0/>`__.

The Creative Commons license in markdown format is imported from `idleberg/Creative-Commons-Markdown <https://github.com/idleberg/Creative-Commons-Markdown>`__.

The HTML documentation uses the `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`__. Copyright (c) 2019, PyData Community. Licensed under `The 3-Clause BSD License (BSD-3-Clause) <https://opensource.org/licenses/BSD-3-Clause>`__.

The HTML documentation uses `Twemoji <https://twemoji.twitter.com/>`__. Copyright (c) Twitter. The graphics are licensed under a `CC BY 4.0 license <https://creativecommons.org/licenses/by/4.0/>`__.
