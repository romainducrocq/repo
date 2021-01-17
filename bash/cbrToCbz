#!/bin/bash

DIR="$1"

mkdir "${DIR%.*}"
mv -v "${DIR}" "${DIR%.*}.rar" 
rar x "${DIR%.*}.rar" "${DIR%.*}"

find ./"${DIR%.*}" -type f |\
grep -e "[.]JPG$" \
-e "[.]jpeg$" -e "[.]JPEG$" \
-e "[.]png$" -e "[.]PNG$" \
-e "[.]webp$" -e "[.]WEBP$" |\
sort -n |\
while IFS= read -r FILENAME
do 
	if [ -z "${FILENAME##*.JPG}" ] ||\
	[ -z "${FILENAME##*.jpeg}" ] || [ -z "${FILENAME##*.JPEG}" ] ||\
	[ -z "${FILENAME##*.png}" ] || [ -z "${FILENAME##*.PNG}" ]; then
		convert -verbose "${FILENAME}" "${FILENAME%.*}.jpg" 
	elif [ -z "${FILENAME##*.webp}" ] || [ -z "${FILENAME##*.WEBP}" ]; then
		dwebp "${FILENAME}" -o "${FILENAME%.*}.png"
		convert -verbose "${FILENAME%.*}.png" "${FILENAME%.*}.jpg" 
		rm -v "${FILENAME%.*}.png"
	fi
	rm -v "${FILENAME}"
done

zip -jr "${DIR%.*}.zip" ./"${DIR%.*}"/*
mv -v "${DIR%.*}.zip" "${DIR%.*}.cbz" 
rm -rv "${DIR%.*}.rar" "${DIR%.*}"
