# ml-elec-model <!-- omit in toc -->

Machine learning-based electricity system model.

Repository: <https://gitlab.com/nithiya/ml-elec-model>

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please refer to the contributing guidelines if you would like to contribute.**

## Table of contents <!-- omit in toc -->

- [About](#about)
- [Installing dependencies](#installing-dependencies)
- [Documentation](#documentation)
- [Data](#data)
- [License](#license)
- [Credits](#credits)

## About

Due to the global transition into a low-carbon energy system, there is an increase in electrification and decentralisation of the energy system with renewable energy resources. Intermittent renewable energy resources, namely solar and wind, are supplying more and more of the electricity demand in Europe, with Germany having the highest share. Advancement in technology means that larger amounts of high-resolution data describing the electricity system will be collected, which can be exploited to better manage the intermittent system in the short term. This project will investigate how machine learning algorithms and publicly available electricity system and meteorological data can be used by wind and solar energy generating companies in Germany for short-term forecasting of generation, load, and market prices, and subsequently management of their portfolio and bids in the electricity market. In contrast to the proprietary nature of existing tools used by energy companies, this project will propose a fully open-source solution.

**Focus:**

- Forecasting of electricity generation, load, and market prices using regression algorithms
- Data for the first half of 2018
  - German meteorological measurements and power plants
  - Generation, load, and market prices for the DE-AT-LU bidding zone
- Initial analysis of wind energy

## Installing dependencies

Running scripts and building the documentation locally require a clone of this repository and installation of [Python 3](https://www.python.org/).

First, clone this repository (including datasets) via either HTTPS or SSH:

- via HTTPS:

  ```sh
  # HTTPS
  git clone --recurse-submodules https://gitlab.com/nithiya/ml-elec-model.git
  ```

- via SSH:

  ```sh
  # SSH
  git clone --recurse-submodules git@gitlab.com:nithiya/ml-elec-model.git
  ```

Then, navigate to the directory of the cloned repository:

```sh
cd ml-elec-model
```

Using either `venv` or [Anaconda](https://www.anaconda.com/products/individual), create and activate a virtual environment, and install all dependencies:

- using `venv`:

  ```sh
  python3.8 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  ```

- using Anaconda:

  ```sh
  conda create --name ml-elec-model python=3.8
  conda activate ml-elec-model
  conda install --channel conda-forge --file requirements.txt
  ```

Note that some packages installed via [conda-forge](https://conda-forge.org/) may be outdated compared to the pip version.

To view the full list of dependencies, see [`requirements.txt`](requirements.txt).

## Documentation

The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and hosted using GitLab Pages. It is available at <https://nithiya.gitlab.io/ml-elec-model/>. The files can be found in the `docs` folder.

To build the documentation locally, clone this repository and install all requirements, as detailed above. Then, change the directory to `docs` by running `cd docs`, and run `make html`. Local builds of the documentation in HTML format can be viewed in `docs/_build/html/index.html`.

A list of references used is available on [Zotero](https://www.zotero.org/groups/2327899/ml-elec-model/library).

## Data

Datasets used and their descriptions are available at <https://gitlab.com/nithiya/ml-elec-model-data>.

Raw data can be accessed using the [GitLab API](https://docs.gitlab.com/ee/api/repository_files.html#get-raw-file-from-repository):

```md
GET /projects/:id/repository/files/:file_path/raw
```

The required parameters are `file_path`, which is [URL (percent) encoded](https://en.wikipedia.org/wiki/Percent-encoding) (e.g., `/` to `%2F`), and `ref`, which is the name of the branch, tag, or commit.

For example, the following URL points to `data/meteorology/stations.csv`:

```md
https://gitlab.com/api/v4/projects/19753809/repository/files/meteorology%2Fstations%2Ecsv/raw?ref=master
```

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License (MIT)](https://opensource.org/licenses/MIT).
- content, images, and documentation are licensed under a [Creative Commons Attribution 4.0 International (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/).

## Credits

This repository is a continuation and improvement of the work done by Nithiya Streethran in [ENSYSTRA](https://ensystra.eu/). ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines are adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source). The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal (CC0-1.0) license](https://creativecommons.org/publicdomain/zero/1.0/).

The Creative Commons license in markdown format is imported from [idleberg/Creative-Commons-Markdown](https://github.com/idleberg/Creative-Commons-Markdown).

The HTML documentation uses the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/). Copyright (c) 2019, PyData Community. Licensed under [The 3-Clause BSD License (BSD-3-Clause)](https://opensource.org/licenses/BSD-3-Clause).

The HTML documentation uses [Twemoji](https://twemoji.twitter.com/). Copyright (c) Twitter. The graphics are licensed under a [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).
