#!/bin/bash

# copy wiki files to docs folder
cp -a wiki/* docs/

# change directory to docs
cd docs

# remove copies of footer and sidebar
rm _Footer.md
rm _Sidebar.md

# build readthedocs html and pdf via latex
make html
make latexpdf LATEXMKOPTS="-silent"

# change directory back to the previous level
cd ..
