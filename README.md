# Self Driving Car using Deep Learning

Requirements
[+] IDE (Atom, Notepad++, Visual Studio Code etc)
[+] Anaconda Navigator
[+] numpy
[+] openCV (Open Source Computer Vision Library)


Steps Taken
[+] Load image
[+] Render image
[+] Change image to grayscale (cvtColor())
[+] Reduce Noise and Smoothen Image (Gaussian Blur)
[+] Simple Edge Detection (get outline of image using Canny Method)
[+] Identify Lane Lines in the image by using matplotlib library and get the coordinates which is your area of interest.
    Get the coordinates of the endpoints of the lines that constitutes your area of interest. After forming the polygons, give the polygons white background. Perfom bitwise operation of the image and the polygons to fetch your area of interest.
