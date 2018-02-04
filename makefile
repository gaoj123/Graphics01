all:
	python image.py

run: all

convert: run
	convert image.ppm image.png

clean:
	rm image.ppm
	rm image.png
