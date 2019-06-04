# Self Driving Car using Deep Learning<br/>
<br/>

Requirements<br/>
[+] IDE (Atom, Notepad++, Visual Studio Code etc)<br/>
[+] Anaconda Navigator<br/>
[+] numpy<br/>
[+] openCV (Open Source Computer Vision Library)<br/>
<br/>
<br/>
Steps Taken<br/>
[+] Load image<br/>
[+] Render image<br/>
[+] Change image to grayscale (cvtColor())<br/>
[+] Reduce Noise and Smoothen Image (Gaussian Blur)<br/>
[+] Simple Edge Detection (get outline of image using Canny Method)<br/><br/>
[+] Identify Lane Lines in the image by using matplotlib library and get the coordinates which is your area of interest.
    Get the coordinates of the endpoints of the lines that constitutes your area of interest. After forming the polygons, give the polygons white background. Perform bitwise operation of the image and the polygons to fetch your area of interest.<br/>
[+] Line Detection - Hough transformation : This technique detects straight lines in the image. Eqn of a line is Y = MX + B. Plot (M,B) in a cartesian. For a straight line, we got a point in Hough Space, what if there was a point in cartesian and we wanted to plot it into Hough Space, for a single line, there lies infinite lines passing through that point. We will get a line in the Hough Space for a single point in the cartesian plane. Hough Space can be used to find a line that passes through a set of given points as for each point in cartesian we have a line in hough space, so the intersection of lines in the hough space gives a value (M, B) that can be substituted in y=mx+b to get the appropriate line. This method is also used to find the line of best fit. Suppose there exists a set of points in cartesian and we need to find the best line that fits into the given points. We will get lines corresponding to each point in the hough space. We first divide the hough space into grids or bins. Now, there may exist inter of lines in multiple regions. We select the bin that has the maximum no of intersections in it to get the value (M, B) for the line of best fit.<br/>

<b><p align="center">
    Sometimes, the gradient is equal to infinity for which our equation of line is not the best suited equation to work with, to solve this problem, we use the polar equation of a line p = x cosƟ + y sinƟ. Using the polar equation, for each line in the cartesian, we get a sinusoidal curve in hough space. Here the hough space gives values in (Ɵ, p)
    </p></b>
