#!/bin/bash

find . -mindepth 1 -maxdepth 1 -type d |\
sort -n |\
while IFS= read -r DIRNAME
do 
	echo "${DIRNAME}" |\
	cut -d' ' -f1 |\
	{ IFS= read -r NEWDIRNAME; mv -v "${DIRNAME}" "${NEWDIRNAME}"; }
done

find . -mindepth 2 -type f |\
grep -e "[.]jpg$" -e "[.]JPG$" \
-e "[.]jpeg$" -e "[.]JPEG$" \
-e "[.]png$" -e "[.]PNG$" \
-e "[.]webp$" -e "[.]WEBP$" |\
sort -n |\
while IFS= read -r FILENAME
do 
	if [ ! -z "${FILENAME##*.jpg}" ]; then
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
	fi
	echo "${FILENAME%/*}" "${FILENAME##*/}" |\
	{ IFS=' ' read -r DIR FILE; mv -v "${FILENAME%.*}.jpg" "${FILENAME%/*}/${DIR##*/}_${FILE%.*}.jpg";  }
done
