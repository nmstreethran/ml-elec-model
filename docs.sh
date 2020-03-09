#!/bin/bash

# change directory to wiki
cd wiki

# create Home.rst from index.rst
cp -n index.rst Home.rst

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

# convert reStructuredText files to markdown via pandoc
pandoc --standalone index.rst --output Home.md
pandoc --standalone background.rst --output Background.md
pandoc --standalone regions.rst --output Regions.md
pandoc --standalone entso-e-data.rst --output ENTSO-E-data.md
pandoc --standalone german-meteorological-data.rst --output German-meteorological-data.md
pandoc --standalone glossary.rst --output Glossary.md
pandoc --standalone license.rst --output LICENSE.md

# build readthedocs html
make html

# change directory back to the previous level
cd ..
