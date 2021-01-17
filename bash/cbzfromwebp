#!/bin/bash
ls | grep "[.]webp$" | while IFS= read -r FILENAME
do 
	dwebp "${FILENAME}" -o "${FILENAME%.*}.png"
	convert "${FILENAME%.*}.png" "${FILENAME%.*}.jpg" 
done
rm ./*.{webp,png}
zip -jr "${PWD}.zip" ./*
mv -v "${PWD}.zip" "${PWD%.*}.cbz" 
