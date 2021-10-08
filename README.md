# Image_diversity
calculate image color diversity by fractal dimension using box-counting method

# Library
- numpy
- opencv
- matplotlib.pyplot
- collections Counter
- scipy.optimize curve_fit

# How to use
You can use module like this

- image_diversity(image_path, fractal_dimension(default = 5 => 2^5), e_ne_graph(default = false), fractal_graph(default = false))
- ex)  image_diversity('./Lenna.png', 5, e_ne_graph=True, fractal_graph=True)

# Result
This function will return **(Image_diversity, Number of Boxes, Completion_time)**
- ex)  image_diversity('./Lenna.png', 5, e_ne_graph=True, fractal_graph=True) - > (1.8258348160993132, [37270, 19535, 6572, 1557, 335, 81], 3.2434229850769043)

**return graphs**   
1. e_ne_graph   
<img src="https://user-images.githubusercontent.com/80665546/136632113-99eb5fe1-73e3-4e7d-96fe-7d464b3478e4.png" width="400" height="400"/> <img src="https://user-images.githubusercontent.com/80665546/136632025-aa9885db-93de-427c-9e17-c9015a20e1ee.jpg" width="400" height="400"/>

2. fractal_graph   

<img src="https://user-images.githubusercontent.com/80665546/136632309-fdf16bd4-a6a9-4222-9e94-598b1c3c923e.jpg" width="250" height="250"/><img src="https://user-images.githubusercontent.com/80665546/136632354-dbf142c1-eb04-48da-b130-66148058238c.jpg" width="250" height="250"/><img src="https://user-images.githubusercontent.com/80665546/136632372-4e7709ab-837f-4ec3-8e9b-8ce27a5065cf.jpg" width="250" height="250"/>   
<img src="https://user-images.githubusercontent.com/80665546/136632449-97e9cd11-2b4d-4643-bc3f-543af24d13e9.jpg" width="250" height="250"/><img src="https://user-images.githubusercontent.com/80665546/136632453-c70c16e9-9c4a-4fe8-8f61-c7608150a1b9.jpg" width="250" height="250"/><img src="https://user-images.githubusercontent.com/80665546/136632454-490f6916-0d9f-48bf-a2d2-0be0fe517c77.jpg" width="250" height="250"/>

