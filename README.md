# Fix the weed problem 
Brought to you by pdp group 25

# Purpose of this code
The goal is to develop a product that is able to remove weeds from the gravel that is in between and next to the SBB train tracks. This method will not use harmful chemicals and will not require human input to operate.

# Current State of Code
This code is currently under development

# Hardware Components
## Definitive compoents
- Raspberry pi 3
## Potential components
- stepper motors
- camera
- laser

# What to Look for in PDP2
## Program structure
- Use functions! The smaller the functions the easier they are to debug.
- Comment code! Even small comments help a lot.

## Implementing New Hardware
- Get it working by itself first
- Find libraries online whenever possible
    - add functions to these libraries as needed to make it easier to interface
      with the library
- Kinds of libraries you will probably need (in no particular order)
    - raspberry Pi I2C library
    - raspberry Pi SPI library
    - raspberry Pi Stepper Motor library
        - will probably have an I2C or SPI library within it
    - raspberry Pi DC motor library 
    - (part number of distance sensor) library 
- Make sure to use functions to interact with the hardware while in your main
  function.
    - Examples: 
    - get_motor_angle()
    - set_motor_rpm(200)
    - get_distance()

## Color Detection
- OpenCV will probably be the best/easiest to implement
- There is a lot of documentation and should take ~5/10 hours or so to get a 
  basic program that can box green colors
