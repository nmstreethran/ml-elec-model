#!/bin/bash

# change directory to docs
cd docs

# build sphinx html and pdf via latex
make html
make latexpdf LATEXMKOPTS="-silent"

# change directory back to the previous level
cd ..
