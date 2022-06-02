# DeepCar-5.0


![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/96300226/146679203-916341b0-5313-4f2a-a305-0e82a76da73b.gif)


![third (1)](https://user-images.githubusercontent.com/96300226/147329610-bce852ff-3dbf-46ff-a1ba-bfd4876bb5d6.gif)




****I) Introducing a New Dataset****

**II) Handcraft Annotation**

**III) Fine-Grained Visual Classification via MAS and Ensembling CNN**

Introducing a new dataset - called DeepCar 5.0

Including more than 40K images in 480 different models belonging to the top 50 world automakers.

All images have been taken from the front view and the front three-quarter directions.

All images clearly show the main vehicle sections, including the headlights, upper grill, lower grill, bumper, hood, etc. 

DeepCar 5.0 has focused mainly on the 2017-2022 car models, some of which have been displayed just recently in various auto shows.

# Dataset Agreement
* The DeepCar 5.0 dataset is available for **non-commercial research and educational purposes only!**



*Download Dataset [**(Train set - 13GB)**](https://drive.google.com/file/d/1Hx1jz6HI7oolQbv7F5Kd68My0SW9jrny/view?usp=sharing) **/** [**(Test set - Part 1 - 12.8GB)**](https://drive.google.com/file/d/1C5kM2DVIPdNCaX1Du_OJhiQaIpEAHeO3/view?usp=sharing) **/** [**(Test set - Part 2 - 12GB)**](https://drive.google.com/file/d/1otwKQJESgbA-77ZdamrFXAKGeeuCBQPy/view?usp=sharing) **/** [Traffic Enforcement Camera][]


*Download [**The Attributes**](https://docs.google.com/spreadsheets/d/1Uv2_WADMuWnmJO777CENOycF7etM64Gx/edit?usp=sharing&ouid=113921680243179511172&rtpof=true&sd=true)

*Download [**Pascal/VOC Annotations**](https://drive.google.com/file/d/18bFrR9dC_38wEFUF9PfT__CJOwegNo1e/view?usp=sharing)

*Download [**Yolo Annotations**](https://drive.google.com/file/d/1PVn49TV88E6j-GCkZayHpdyx27SkUExa/view?usp=sharing)



[Traffic Enforcement Camera]: https://www.youtube.com/watch?v=1EiC9bvVGnk/


# Mannual Annotation
* Left & Right Headlights
* Left & Right Fog Lamp/ Scope
* Hood Scope (i.e. AirIntake)
* Front Bumper
* Upper Grill
* Car Face


![lable (1)](https://user-images.githubusercontent.com/96300226/148178487-84e539ec-2213-4990-92d8-bffe3465ca40.jpg)

# Attributes
Containing Color, Engine Size, Cylinder Arrangement, Horsepower, Length,	Width,	Height, etc.

Support 34 Body Styles:
* Sedan, SUV, Coupe Sports, Spider, Sport Sedan, Compact SUV, Roadster, Hatchback, Turismo, GT, CUV, TT, Minivan, Liftback, Crossover, etc.




![image](https://user-images.githubusercontent.com/96300226/148179069-4c66b79a-12c8-4227-84af-79983924afb5.png)



# Attention Mechanism
Employing the Attention Module to Determine the ROI
![Similarities](https://user-images.githubusercontent.com/96300226/146680188-3d60e449-fdf5-4168-a487-b5e5e24a88cb.jpg)



# Design a Specific Filters for Each Part
* Identity Watermarks
* Gabor Filter Bank
* Style Transfer
* DexiNed: Dense EXtreme Inception Network for Edge Detection


# Vehicle Make and Model Recognition
Introducing a New Method for Fine-grained Classification by Using Multi-Agent Systems and Enseembling CNN
* Using Blackboard System for Decision & Voting
* VGG19
* ...





# Acknowledgment
Special Thanks to:

[DexiNed Official Page](https://github.com/xavysp/DexiNed) For Using Their Code In Our "Grill Agent"

[CompVis Heidelberg Research Group](https://github.com/CompVis/adaptive-style-transfer) For Using Their Code In Our "Scoop & Air Intake Agent"

