#!/bin/bash

# change directory to wiki
cd wiki

# create Home.rst from index.rst
cp index.rst Home.rst

# change directory back to the previous level
cd ..

# copy wiki files to docs folder
cp -a wiki/* docs/

# change directory to docs
cd docs

# remove copies of homepage, footer and sidebar
rm _Footer.md
rm _Sidebar.md
rm Home.rst

# build readthedocs html and pdf via latex
make html
make latexpdf LATEXMKOPTS="-silent"

# change directory back to the previous level
cd ..
