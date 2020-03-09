#!/bin/bash

# change directory to wiki
cd wiki

# convert wiki to pdf via latex using pandoc
pandoc \
    --template=pandoc.latex \
    --pdf-engine=xelatex \
    --metadata title="ml-elec-model" \
    --metadata author="Nithiya Streethran" \
    --variable date="`date '+%-d %B %Y'`" \
    --variable keywords="electricity system data, open source" \
    --metadata colorlinks \
    --variable fontsize=10pt \
    --variable geometry:margin=2.5cm \
    --variable mainfont="EB Garamond" \
    --variable sansfont="Lato" \
    --variable monofont="Fira Code Retina" \
    --variable papersize="a4" \
    --variable classoption="twoside" \
    --from markdown+backtick_code_blocks-markdown_in_html_blocks-native_divs \
    --highlight-style syntax.theme \
    --toc \
    --variable toc-title="Table of Contents" \
    Home.md \
    Background.md \
    Regions.md \
    ENTSO-E-data.md \
    German-meteorological-data.md \
    Glossary.md \
    --output docs.pdf

# change directory back to the previous level
cd ..

# copy wiki files to docs folder
cp -a wiki/* docs/

# remove copies of footer and sidebar
rm docs/_Footer.md
rm docs/_Sidebar.md

# convert md to rst
pandoc --standalone --to rst docs/Home.md --output docs/home.rst
pandoc --standalone --to rst docs/Background.md --output docs/background.rst
pandoc --standalone --to rst docs/Regions.md --output docs/regions.rst
pandoc --standalone --to rst docs/ENTSO-E-data.md --output docs/entso-e-data.rst
pandoc --standalone --to rst docs/German-meteorological-data.md --output docs/german-meteorological-data.rst
pandoc --standalone --to rst docs/Glossary.md --output docs/glossary.rst
pandoc --standalone --to rst docs/LICENSE.md --output docs/license.rst
