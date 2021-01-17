#!/bin/bash

DIR="$1"

mkdir "${DIR%.*}"
pdfimages -j "${DIR}" "./${DIR%.*}/page"

find ./"${DIR%.*}" -type f |\
grep -e "[.]ppm$" -e "[.]pgm$" -e "[.]pbm$" \
-e "[.]PPM$" -e "[.]PGM$" -e "[.]PBM$" \
-e "[.]jpeg$" -e "[.]JPEG$" -e "[.]JPG$" |\
sort -n |\
while IFS= read -r FILENAME
do 
	convert -verbose "${FILENAME}" "${FILENAME%.*}.jpg" 
	rm -v "${FILENAME}"
done

zip -jr "${DIR%.*}.zip" ./"${DIR%.*}"/*
mv -v "${DIR%.*}.zip" "${DIR%.*}.cbz" 
rm -rv "${DIR}" "${DIR%.*}"
