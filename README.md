<h1 align="center">
  <a href="https://github.com/matthewloh/CS-ALL-Project-1-Development">
  <font size="+5"> A Desktop-based Event Platform<br>built for INTI Penang
  </font>
  <br>
  <br>
  <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050454379037208586/image.png" alt="Made in Tkinter">
  </a>
  <br>
  <font size="+2" color="Orange"> Made completely using Tkinter
  </font>
  <br>
</h1>
<h4 align="center">
    <font size="+1">Computer Science Activity Led Learning Project - 1 
    <br>
    By: Matthew, Adnan, and Zi Hao
    </font>
</h4>

<!-- <h1></h1> -->

<!-- <p align="center">
  <a href=""><img src="https://img.shields.io/pypi/pyversions/dearpygui" alt="Python versions"></a>
  <a href="https://pypi.org/project/dearpygui/"><img src="https://img.shields.io/pypi/v/dearpygui" alt="PYPI"></a>
  <a href="https://pepy.tech/project/dearpygui"><img src="https://pepy.tech/badge/dearpygui" alt="Downloads"></a>
  <a href="#license"><img src="https://github.com/hoffstadt/DearPyGui/blob/assets/readme/mit_badge.svg" alt="MIT License"></a>
</p>

<p align="center">
   <a href="https://github.com/hoffstadt/DearPyGui/actions?workflow=Embedded%20Build"><img src="https://github.com/hoffstadt/DearPyGui/workflows/Embedded%20Build/badge.svg?branch=master" alt="static-analysis"></a>
   <a href="https://github.com/hoffstadt/DearPyGui/actions?workflow=Static%20Analysis"><img src="https://github.com/hoffstadt/DearPyGui/workflows/Static%20Analysis/badge.svg?branch=master" alt="static-analysis"></a>
   <a href="https://github.com/hoffstadt/DearPyGui/actions/workflows/Deployment.yml"><img src="https://github.com/hoffstadt/DearPyGui/actions/workflows/Deployment.yml/badge.svg?branch=master" alt="Deployment"></a>
   <a href="https://dearpygui.readthedocs.io/en/latest/?badge=latest"><img src="https://readthedocs.org/projects/dearpygui/badge/?version=latest" alt="Documentation Status"></a>
</p> -->

<!-- <h1></h1> -->
<!-- 
<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> • 
  <a href="#demo">Demo</a> •
  <a href="#resources">Resources</a> •
  <a href="#support">Support</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> •
  <a href="#gallery">Gallery</a>
</p> -->

<!-- <h1></h1> -->

<!-- <BR>![Themes](https://raw.githubusercontent.com/hoffstadt/DearPyGui/assets/linuxthemes.PNG)  -->
  
## Features  
- **Modern appearance** — Widgets designed in Figma and made into Tkinter widgets using Pillow
- **Easy to use** — Easy to use and navigate through using the Navigation Bars
- **Integration DALL·E API** —  DALL·E API is used to generate images from text provided by admins.
- **Made completely in Python and Tkinter** - Programmed using some Ttk widgets and Pillow to create PhotoImage objects.
- **I'll write some more later** — I'll write some more later
<!-- <h1></h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/wiki/epezent/implot/screenshots3/stem.gif" width="380">&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;<img src="https://raw.githubusercontent.com/wiki/epezent/implot/screenshots3/tables.gif" width="380">
</p>
<h1></h1> -->

<!-- <h1></h1>
<p align="center"> 
<img src="https://raw.githubusercontent.com/wiki/epezent/implot/screenshots3/pie.gif" width="380">&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;<img src="https://raw.githubusercontent.com/wiki/epezent/implot/screenshots3/candle.gif" width="380"> 
</p>
<h1></h1> -->
  
## Installation

This project was built using Python 3.10.x. You can download it [here](https://www.python.org/downloads/). The project was developed for systems with resolutions of 1920x1080. It is recommended to run the project on a system with a resolution of 1920x1080 or higher.

The codebase will have you install third party libraries onto your system, including openai, Pillow, tkcalendar and pyglet. 
<br>These libraries will be installed in the following commands.
```Python

import subprocess

try:
    from PIL import Image, ImageOps, ImageTk
except:
    print('Installing PIL.')
    subprocess.check_call(['pip', 'install', 'pillow'])
    print('Done.')
    from PIL import Image, ImageOps, ImageTk

try:
    from tkcalendar import Calendar as tkCalendar
    from tkcalendar import DateEntry
except:
    print('Installing tkcalendar.')
    subprocess.check_call(['pip', 'install', 'tkcalendar'])
    print('Done.')
    from tkcalendar import Calendar as tkCalendar
    from tkcalendar import DateEntry

try:
    import openai 
except:
    print('Installing openai.')
    subprocess.check_call(['pip', 'install', 'openai'])
    print('Done.')
    import openai

```
 
## How to use?
 
To use the system, clone the repo and run the following command in a terminal of your choice from the folder containing the repository.
  
```Python
py InteractiveSystemUserView.py
```

<!-- <br/>
<p align="center"><a href="https://dearpygui.readthedocs.io/en/latest/tutorials/first-steps.html#first-run"><img src="https://raw.githubusercontent.com/hoffstadt/DearPyGui/assets/readme/first_app.gif" alt="Dear PyGui example window"></a></p> -->
                                                                                           
## Design
The following shows all of the application's preliminary designs. The creations made in Figma show most, but not nearly all, of the available widgets and features. 

### Login and Registration Pages
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376383001546832/image.png" height="400px">
</p>

### Main Page
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376507035496498/image.png" height="400px">
</p> 

### Event View and Event Registration Pages
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376532566233098/image.png" height="400px">
</p> 

### Management Suite 
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376554963816448/image.png" height="400px">
</p> 

### Management Suite - Event Creation Page
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376582721712158/image.png" height="400px">
</p> 

### Management Suite - Manage Events Page
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376601700946000/image.png" height="400px">
</p> 

### Management Suite - View Participants by Event or Registrant Pages
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376631660847134/image.png" height="400px">
</p> 

### Additional Features List
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376658663776346/image.png" height="400px">
</p> 

### Additional Features - Feedback Form and Calendar Pages
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050376680935534632/image.png" height="400px">
</p> 

## Resources

### Development Roadmap🗺️
<br>
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050459223395422328/image.png" height="400px">
</p> 
  

## Support

If you are having issues or want to help, here are some places you can go.
  -  Find me on discord at kabo#2277 :)


## Tech stack
**Going off the grid - a revolutionary way to create a dazzling Tkinter app.
Our solution to the Tkinter grid manager elevates your design -
create visually appealing labels and buttons in no time with Figma!** 

<br>

The application, which goes by many names, is built on top of Tkinter, including the Themed Tkinter extensions for widgets, and is drastically different than other Tkinter Python GUI framework applications. Under the hood, it is built using assets made for a fixed resolution. Featuring widescreen 16:9 support, the application is designed to be used on a 1920x1080 resolution. The application is also designed to be used on a 4K resolution, but the user interface is not optimized for it. A class-based approach was used to engineer the system's architecture, with due credit to Bryan Oakley on StackOverflow. Credit also goes to GUI Pie, for that is where I found how to utilize the Tkinter grid manager to a greater degree.

In terms of database architecture, SQLite was chosen for its learning curve and easy implementation in recent Python iterations. 
<br>
In order to use the Generate Image functionality, you will need to ensure that your system is set up with the following dependencies:
- An OpenAI API key, which can be obtained by signing up for an account at https://beta.openai.com/ and creating an API key.
- A system environment variable named `OPENAI_API_KEY` that contains your OpenAI API key.
- The Python package `openai` installed on your system. This can be done by running `pip install openai` in a terminal of your choice. The system will attempt to do this for you.
<br/>
  
## Credits

- Developed painstakingly and with love by Matthew, an undergrad student in INTI International College Penang and Coventry University.
- Lots of thanks to the small subset of Tkinter developers who have made the Tkinter experience a lot more bearable on StackOverflow.
- The beautiful Figma designs and seamless implementation of Figma to create the application's assets were by me too.
- Assets including most of the background images were taken from Abstruct by award-winning OnePlus wallpaper artist Hampus Olsson. 
- Thank you to Dr. Vaithegy as well as INTI Penang and Coventry University for the opportunity to work on this project.

## License
I'll figure out how to accredit the license later. For now, it's probably going to be MIT.
  
## Gallery
Some screenshots of actually using the application. These screenshots were taken at 2560x1440 resolution, where the window bar of the application does not need to be removed for assets to appear properly.

### Registering for Events
<br>
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050463029529157632/image.png" height="400px">
</p> 

### Managing Events 
<br>
<p align="center">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050464073663397958/image.png" height="400px">
   <img src="https://cdn.discordapp.com/attachments/887627854706249769/1050464377343586394/image.png" height="400px">
</p>
