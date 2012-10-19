#!/bin/sh
sed -n 's/'"$1"'/&/p
#sedgrep '[A-Z][A-Z]' <file
#must have <
#but in cmd sed -n 's/space/&/p' 1015noon  is alse right'
