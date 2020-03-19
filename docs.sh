#!/bin/bash

# copy wiki files to docs folder
cp -a wiki/* docs/

# change directory to docs
cd docs

# create index.rst from Home.rst
cp Home.rst index.rst

# remove copies of home, footer and sidebar
rm _Footer.md
rm _Sidebar.md
rm Home.rst

# build readthedocs html and pdf via latex
make html
make latexpdf LATEXMKOPTS="-silent"

# change directory back to the previous level
cd ..
