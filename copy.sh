#!/bin/sh

cp README.rst docs/readme.rst

sed -i -e "s/nithiya.gitlab.io\/ml-elec-model\//\`& <.\/index.html>\`__/" docs/readme.rst
sed -i -e "1,3d" docs/readme.rst
