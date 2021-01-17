#!/bin/bash

DIR="$1"

mkdir "${DIR}"

for VOLUME in "${@:2}"
do 
	find ./"${VOLUME}" -mindepth 1 -type f |\
	grep "[.]jpg$" |\
	sort -n |\
	while IFS= read -r FILENAME
	do 
		mv -v "${FILENAME}" "${DIR}"
	done
	rm -r "${VOLUME}"
done

zip -jr "${DIR}.zip" ./"${DIR}"/*
mv -v "${DIR}.zip" "${DIR}.cbz" 
rm -rv "${DIR}"

