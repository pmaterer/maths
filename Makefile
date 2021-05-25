.PHONY: images

notebook:
	jupyter notebook

format:
	black .

images:
	manim render --output_file right_triangle manim.py RightTriangle
	manim render --output_file polar_cartesian manim.py PolarCartesian