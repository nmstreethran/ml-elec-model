# ml-elec-model <!-- omit in toc -->

<!-- start badges -->
[![Action: links](https://github.com/nmstreethran/ml-elec-model/workflows/links/badge.svg)](https://github.com/nmstreethran/ml-elec-model/actions?query=workflow%3Alinks)
[![Documentation build status](https://readthedocs.org/projects/ml-elec-model/badge/?version=latest)](https://ml-elec-model.rtfd.io)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-yellow?labelColor=darkslategray)](https://opensource.org/licenses/MIT)
[![Content license: CC BY 4.0](https://img.shields.io/badge/content%20license-CC%20BY%204.0-blue?labelColor=darkslategray)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub repository](https://img.shields.io/badge/-repository-purple?logo=github&labelColor=black)](https://github.com/nmstreethran/ml-elec-model)
[![Download docs PDF](https://img.shields.io/badge/-docs%20pdf-darkslategray?logo=adobe-acrobat-reader&labelColor=red&logoColor=white)](https://ml-elec-model.readthedocs.io/_/downloads/en/latest/pdf/)
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

Running scripts and building the documentation locally require [Python 3](https://www.python.org/).

First, create and activate a virtual environment (recommended):

```sh
python3 -m venv env
source env/bin/activate
```

Alternatively, if using [Anaconda](https://www.anaconda.com/products/individual):

```sh
conda create --name ml-elec-model python=3
conda activate ml-elec-model
```

Then, install the dependencies:

```sh
pip install -r requirements.txt
```

If using Anaconda, the required packages can alternatively be installed via [conda-forge](https://conda-forge.org/) instead of `pip install`:

```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install bokeh geopandas sphinx_rtd_theme entsoe-py
```

## Documentation

The documentation is maintained in this repository's [GitHub Wiki](https://github.com/nmstreethran/ml-elec-model/wiki), built using [Sphinx](https://www.sphinx-doc.org/en/master/), and hosted using [Read the Docs](https://readthedocs.org). It is available at <https://ml-elec-model.rtfd.io>. The files can be found in the `docs` folder.

To build the documentation locally, clone this repository and install a TeX distribution (such as [TeX Live](http://tug.org/texlive/)).

<!-- 
The GitHub wiki has been included in this repository as a submodule. All changes must be made to the files within this submodule (i.e., the `wiki` directory). Once changes are made, the following bash script must be executed to compile the documentation:

```sh
bash docs.sh
```

Then, commit and push all changes to the wiki's branch. Finally, commit and push to the main repository's branch.
 -->
Local builds of the documentation in HTML and PDF formats can be viewed after running the following bash script by opening `docs/_build/html/index.html` and `docs/_build/latex/ml-elec-model.pdf` respectively:

```sh
bash docs.sh
```

A list of references used is available on [Zotero](https://www.zotero.org/groups/2327899/ml-elec-model/library).

## Charts

Charts generated are available at <https://github.com/nmstreethran/charts/tree/ml-elec-model>.

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks, and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License](https://opensource.org/licenses/MIT).
- content, images, and documentation are licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/).
- charts are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.html).

## Credits

This repository is a continuation and improvement of the work done by Nithiya Streethran in [ENSYSTRA/short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting).
ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

Contributing guidelines are adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source). The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).

The Creative Commons license in markdown format is imported from [idleberg/Creative-Commons-Markdown](https://github.com/idleberg/Creative-Commons-Markdown).
