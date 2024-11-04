#show heading: set text(font: "Linux Biolinum")

#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommend resume text size is from `10pt` to `12pt`
#set text(
  size: 10pt,
)

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 0.9cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/

#set par(justify: true)

#show link: underline
#show link: set text(blue)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}
#set align(center) 


= Dennis Melamed
#link("dennis@dennismelamed.me") | #link("dennismelamed.me") | Minneapolis, MN\
#link("github.com/DennisMelamed") | #link("linkedin.com/in/dennismelamed/") | (+1) 763-656-9518\

#set align(left) 
== Experience
#chiline()
*Kitware*, _Research & Development Engineer_  #h(1fr) Aug 2021 -- Present \
- Trained building damage identification systems for satellite imagery, reducing training data needs 1000x.@melamed_rapid_2023
- Created & released open dataset for training building damage detectors @melamed_uncovering_2024
- Designed framework to deconflict multiple object detectors using prior information and detector trust metrics @davila_multi-atr_2023
- Architected & developed inspection tool (as lead of 5 person team) for localizing defects on large airframe to 5 cm accuracy.
- Developed pose estimation algorithms & experimental hardware for event-camera star tracking, achieving 10-20 arcsecond accuracy.

*Nextdroid Robotics*, _Software Intern_  #h(1fr) June 2018 -- Aug 2018 \
- Achieved sensorless high-precision motor speed control for subsea robotic platform
- Co-developed high-accuracy image processing on military hardware for aerial scene understanding

*National Instruments*, _Software Intern_  #h(1fr) June 2017 -- Aug 2017 \
- Implemented network interfaces for measurement device drivers to maintain stability on newer platforms
- Developed encryption systems to allow first-in-company secure device firmware/driver communication

*Robotic Sensor Networks Lab, University of Minnesota*, _Research Assistant_  #h(1fr) Feb 2015 -- May 2019 \
- Developed GPS-denied micro-UAV platform for agriculture using ROS, C, and V-REP simulation
- Designed and trialed computer vision system for micro-UAV control using low-resolution imaging

*Dept. of Civil Engineering, University of Minnesota*, _Research Assistant_  #h(1fr) Oct 2015 -- May 2016 \
- Parallelized state-of-art wave propagation algorithms to speed concrete simulations by 10x
- Designed MN Dept. of Transport user interfaces to ease ground-penetrating radar data analysis

== Education
#chiline()
*M.S. in Robotics* #h(1fr) Aug 2019 -- July 2021 \
Carnegie Mellon University, Prof. Kris Kitani #h(1fr) Pittsburgh, PA \
- Thesis: Learnable Spatio-Temporal Map Embeddings for Deep Inertial Localization@melamed_learnable_2022 \
- Selected Coursework: Kinematics, Dynamics & Control, Localization & Mapping, Reinforcement Learning\
*B.Sci. in Computer Engineering, Summa Cum Laude with Distinction* #h(1fr) Sept 2015 -- May 2019 \
University of Minnesota, Prof. Volkan Isler #h(1fr) Minneapolis, MN \
- Thesis: Indoor Micro-UAV Navigation with Minimal Sensing (Profs. Volkan Isler & Derya Aksaray) \
- IEEE-Eta Kappa Nu – Omicron Student Chapter – Vice President 2018-2019
== Skills
#chiline()
*Programming Languages*: Python, C++, Embedded C, MATLAB, Java\
*Robotics Tools*: Robotics Operating System (ROS), Gazebo, V-REP\
*Other Tools*: Git, Pytorch, OpenCV, scikit-learn, Linux, Latex, Windows Kernel, Blender, QGIS, ONNX, Triton, DVC\
*Languages*: English (native), Russian (native), Spanish (proficient)\
== Publications
#chiline()
#cite(<sun_idol_2021>, form:none)
#cite(<melamed_learnable_2022>, form:none)
#cite(<melamed_uncovering_2024>, form:none)
#cite(<davila_multi-atr_2023>, form:none)
#cite(<melamed_rapid_2023>, form:none)
#bibliography("my_pubs.bib", title:none, style:"super_simple_cite.csl")