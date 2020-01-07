#!/bin/bash

# change directory to docs/
cd docs

# convert wiki to pdf via latex using pandoc
pandoc \
    --template=pandoc.tex \
    --pdf-engine=xelatex \
    --metadata title="elec-sys-data" \
    --metadata author="Nithiya Streethran" \
    --variable date="`date '+%-d %B %Y'`" \
    --variable keywords="electricity system data, open source" \
    --metadata copyright="Copyright (c) `date '+%Y'` Nithiya Streethran. Licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License." \
    --metadata licenseurl="https://creativecommons.org/licenses/by/4.0/" \
    --metadata contactemail="nmstreethran@gmail.com" \
    --metadata colorlinks \
    --variable fontsize=10pt \
    --variable geometry:margin=2.5cm \
    --variable mainfont="EB Garamond" \
    --variable sansfont="Lato" \
    --variable papersize="a4" \
    --variable classoption="twoside" \
    --from markdown+backtick_code_blocks-markdown_in_html_blocks-native_divs \
    --highlight-style syntax.theme \
    --toc \
    --variable toc-title="Table of Contents" \
    Home.md \
    Background.md \
    Regions.md \
    Data.md \
    --output docs.pdf

# change directory back to the previous level
cd ..
