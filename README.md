# magicpi-socket
A python script designed to run on a Raspberry Pi, enabling connection to a computer running a tweaked version of Magic-Sand using websockets.

## Background
The script is planned to read GPIO inputs from connected buttons and a potmeter. These inputs will then send a signal to the computer running the Magic-Sand software that will then execute different functions.
Originally, the software was planned to run on the Raspberry Pi. Challenges arose when attempting to compile the program to the Raspberry Pi, such as problems running legacy OpenGL functions.

For a project in the course TFE4850


## How to operate
Create a .env file named .dev.env
This file needs two variables HOST and PORT, containing whatever host and port you are using. 

Added a basic server-client structure for testing before incorparting the socket structure in Magic-Sand
