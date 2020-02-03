# ml-elec-model <!-- omit in toc -->

<!-- start licence badges -->
[![Build Status](https://travis-ci.org/nmstreethran/ml-elec-model.svg?branch=master)](https://travis-ci.org/nmstreethran/ml-elec-model)
[![Markdown link checker GitHub issues](https://img.shields.io/github/issues/nmstreethran/ml-elec-model/link%20checker?color=limegreen&label=Link%20checker%20issues&labelColor=darkslategray)](https://github.com/nmstreethran/ml-elec-model/issues?q=is%3Aissue+is%3Aopen+label%3A%22link+checker%22)
[![Code license: MIT](https://img.shields.io/badge/Code%20license-MIT-yellow.svg?labelColor=darkslategray)](https://opensource.org/licenses/MIT)
[![Content license: CC BY 4.0](https://img.shields.io/badge/Content%20license-CC%20BY%204.0-blue.svg?labelColor=darkslategray)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub Wiki](https://img.shields.io/badge/-GitHub%20Wiki-purple.svg?logo=github&labelColor=black)](https://github.com/nmstreethran/ml-elec-model/wiki)
<!-- end license badges -->

by nmstreethran at gmail dot com

**This project is a work-in-progress. Feedback and suggestions are always welcome. Please refer to the [contributing guidelines](CONTRIBUTING.md) if you would like to contribute.**

Machine learning-based electricity system model.

## Table of contents <!-- omit in toc -->

- [Requirements](#requirements)
- [Documentation](#documentation)
- [Cloning the repository](#cloning-the-repository)
  - [Using HTTPS](#using-https)
  - [Using SSH](#using-ssh)
- [License](#license)
- [Credits](#credits)

## Requirements

- Python 3
- Git
- [ENTSO-E API Python client](https://github.com/EnergieID/entsoe-py)

## Documentation

Documentation is written in the repository's [GitHub Wiki](https://github.com/nmstreethran/ml-elec-model/wiki). The files can also be found in the [docs](docs/) folder.

## Cloning the repository

To clone the latest version of this repository, including the contents of the submodule:

### Using HTTPS

```sh
git clone --recurse-submodules https://github.com/nmstreethran/ml-elec-model.git
```

### Using SSH

```sh
git clone --recurse-submodules git@github.com:nmstreethran/ml-elec-model.git
```

The GitHub wiki has been included in this repository as a submodule. Once changes to the wiki within the submodule are made (e.g., new markdown files, images), these changes are first committed and pushed to the wiki's branch, before committing and pushing to the main repository's branch.

## License

Unless otherwise stated:

- Python scripts, Jupyter notebooks and any other form of code or snippets (e.g., shell scripts) in this repository are licensed under the [MIT License](https://opensource.org/licenses/MIT).
- content, images and documentation are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/).

## Credits

The documentation in PDF format incorporates the following fonts:

- [EB Garamond by Georg Duffner](https://fonts.google.com/specimen/EB+Garamond), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web)
- [Lato by Łukasz Dziedzic](https://fonts.google.com/specimen/Lato), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web)
- [Fira Code by Nikita Prokopov](https://github.com/tonsky/FiraCode), licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web)

This repository is a continuation and improvement of the work done by [nmstreethran](https://github.com/nmstreethran) in [ENSYSTRA/short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting).

Contributing guidelines is adapted from the [Open Science MOOC](https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source). The contents of the MOOC are licensed under a [Creative Commons Zero v1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).
