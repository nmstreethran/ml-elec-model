# ml-elec-model <!-- omit in toc -->

<!-- start badges -->
[![Action: links](https://github.com/nmstreethran/ml-elec-model/workflows/links/badge.svg)](https://github.com/nmstreethran/ml-elec-model/actions?query=workflow%3Alinks)
[![Documentation build status](https://readthedocs.org/projects/ml-elec-model/badge/?version=latest)](https://ml-elec-model.rtfd.io)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-yellow?labelColor=darkslategray)](https://opensource.org/licenses/MIT)
[![Content license: CC BY 4.0](https://img.shields.io/badge/content%20license-CC%20BY%204.0-blue?labelColor=darkslategray)](https://creativecommons.org/licenses/by/4.0/)
<!-- end badges -->

by Nithiya Streethran (nmstreethran at gmail dot com)

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please refer to the contributing guidelines if you would like to contribute.**

Machine learning-based electricity system model.

## Table of contents <!-- omit in toc -->

- [Installing dependencies](#installing-dependencies)
- [Documentation](#documentation)
- [Charts](#charts)
- [License](#license)
- [Credits](#credits)

## Installing dependencies

Running scripts and building the documentation locally require a clone of this repository and installation of [Python 3](https://www.python.org/).

First, clone this repository via either HTTPS or SSH:

```sh
# HTTPS
git clone https://github.com/nmstreethran/ml-elec-model.git

# SSH
git clone git@github.com:nmstreethran/ml-elec-model.git
```

Then, create and activate a virtual environment (recommended):

```sh
python3 -m venv env
source env/bin/activate
```

Alternatively, if using [Anaconda](https://www.anaconda.com/products/individual):

```sh
conda create --name ml-elec-model python=3
conda activate ml-elec-model
```

Finally, install the dependencies:

```sh
pip install -r requirements.txt
```

If using Anaconda, the required packages can alternatively be installed via [conda-forge](https://conda-forge.org/), instead of using `pip install`:

```sh
conda install --channel conda-forge --file requirements.txt
```

To view the full list of dependencies, see [`requirements.txt`](requirements.txt).

## Documentation

The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and hosted using [Read the Docs](https://readthedocs.org). It is available at <https://ml-elec-model.rtfd.io>. The files can be found in the `docs` folder.

To build the documentation locally, clone this repository and install all requirements. Local builds of the documentation in HTML format can be viewed in `docs/_build/html/index.html` after running the following in the `docs` directory:

```sh
make html
```

A list of references used is available on [Zotero](https://www.zotero.org/groups/2327899/ml-elec-model/library).

## Charts

Charts generated are available at <https://github.com/nmstreethran/charts/tree/ml-elec-model>.

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License (MIT)](https://opensource.org/licenses/MIT).
- content, images, and documentation are licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/).
- charts are licensed under the [Apache 2.0 License (Apache-2.0)](https://www.apache.org/licenses/LICENSE-2.0.html).

## Credits

This repository is a continuation and improvement of the work done by Nithiya Streethran in [ENSYSTRA/short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting). ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines are adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source). The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal (CC0 1.0) license](https://creativecommons.org/publicdomain/zero/1.0/).

The Creative Commons license in markdown format is imported from [idleberg/Creative-Commons-Markdown](https://github.com/idleberg/Creative-Commons-Markdown).

The HTML documentation uses the [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/). Copyright (c) 2019, PyData Community. Licensed under [The 3-Clause BSD License (BSD-3-Clause)](https://opensource.org/licenses/BSD-3-Clause).

The HTML documentation uses [Material design icons](https://google.github.io/material-design-icons/). Copyright (c) Google. Licensed under the [Apache 2.0 License (Apache-2.0)](https://www.apache.org/licenses/LICENSE-2.0.html).
