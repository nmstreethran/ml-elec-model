# elec-sys-data <!-- omit in toc -->

[![Build Status](https://travis-ci.com/nmstreethran/elec-sys-data.svg?branch=master)](https://travis-ci.com/nmstreethran/elec-sys-data)

<!-- start licence badges -->
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Content License: CC BY 4.0](https://img.shields.io/badge/Content%20License-CC%20BY%204.0-blue.svg?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub Wiki](https://img.shields.io/badge/-GitHub%20Wiki-green.svg?style=flat-square&logo=github&labelColor=black)](https://github.com/nmstreethran/elec-sys-data/wiki)
<!-- end license badges -->

by nmstreethran at gmail dot com

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please refer to the [contributing guidelines](CONTRIBUTING.md) if you would like to contribute.**

Automated extraction of open electricity system data from meteorological services, electricity system operators and electricity market operators.

## Table of contents <!-- omit in toc -->
- [Requirements](#requirements)
- [Documentation](#documentation)
- [Cloning the repository](#cloning-the-repository)
- [License](#license)
- [Credits](#credits)

## Requirements

* Python 3
* Git
* [ENTSO-E API Python client](https://github.com/EnergieID/entsoe-py)

## Documentation

Documentation is written in the repository's [GitHub Wiki](https://github.com/nmstreethran/elec-sys-data/wiki). The files can also be found in the [docs](docs/) folder.

## Cloning the repository

To clone the latest version of this repository, including the contents of the submodule:

**Using HTTPS**

```sh
git clone --recurse-submodules https://github.com/nmstreethran/elec-sys-data.git
```

**Using SSH**

```sh
git clone --recurse-submodules git@github.com:nmstreethran/elec-sys-data.git
```

The GitHub wiki has been [included in this repository as a submodule](https://brendancleary.com/2013/03/08/including-a-github-wiki-in-a-repository-as-a-submodule/). Once changes to the wiki within the submodule are made (e.g., new markdown files, images), these changes are first committed and pushed to the wiki's branch, before committing and pushing to the main repository's branch.

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License](https://opensource.org/licenses/MIT). [[Link to license file](license/LICENSE_code.md)]
- content, images and documentation are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/). [[Link to license file](license/LICENSE_content.md)]

## Credits

This repository is a continuation and improvement of the work done by [nmstreethran](https://github.com/nmstreethran) in [ENSYSTRA/short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting).

Contributing guidelines is adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source).
The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).
