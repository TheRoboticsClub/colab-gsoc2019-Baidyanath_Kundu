# The Final Report

|Contents                                 |
|-----------------------------------------|
|1. [VisualStates Tool](#visualstates)    |
|2. [The Task](#task)                     |
|3. [Work Completed](#completed)          |
|4. [Work Left](#left)                    |
|5. [Explanation Videos](#videos)         |
|6. [People Involved](#people-involved)   |
|7. [Links](#links)                       |
|8. [Development Status](#status)         |
|9. [Documentation](#documentation)       |



<a name="visualstates"/>

## VisualStates Tool
VisualStates is a tool for programming robot behaviors using automata.
It combines a graphical language to specify the states and the transitions
with a text language (Python or C++). Hierarchical Finite State Machines
are used to program robot behaviors and each state is a reactive controller
which can be active or not at a particular instant. It automatically
generates a Robotics Operating System node as output, in C++ or Python, 
which connects to the configured drivers at runtime and implements the automata. 
This tool speeds up the development of robot applications, reducing the code 
that has to be manually created.

<a name="task"/>

## The Task
Visual States is a great tool but some features were felt missing. I had to work on two of these.

- The variables inside the tool had to be dug out from the heaps of code. 
This was a problem as it took a lot of time to tweak variables whose values had to be tuned perfectly.
Hence parameterization had become a necessity for the tool.
- The main objective of creating the tool was to make the creation of automata behaviours easy 
and promote faster development. One of of the ways to promote this was code reuse. So I was tasked with the
creation of a library(which is a github repository) of prebuilt behaviours. The library was to be made accessible such that the user could access it 
through the tool. The list of behaviours were to be listed inside the tool and imported right there. The user could even
add his behaviour to the library.

The task also involved developing examples that would show the working of these features.

<a name="completed"/>

## Work Completed
**[Parameterization of Visual States](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1):**
This feature has been added but it hasn't been merged with master. The code has been thoroughly reviewed by my mentors
and the bugs fund has been squashed. One of the previously existing examples in the VisualStates examples 
repository has been modified to use parameters to show it working.

**[Online Library Import and Export](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/5):**
The code for this has been created but it is pending to be reviewed by the mentors. The library repository 
hasn't been created. It has to go through these before it can be merged. 

<a name="left"/>

## Work Left
- The online library and importer need to be checked for bugs and both of them are to be merged to master.
- More examples need to be created that can be added to the library and uses parameters.
- ArDrone2 model is being changed so that it uses ROS publishers and subscribers instead of ICE drivers.
- The VisualStates tool would benefit from a tabbed design. The design has to be discussed before it can be executed
which is done [here](https://github.com/JdeRobot/VisualStates/issues/120).

## Explanation Videos
- [Demonstrating Parameterization of States](https://www.youtube.com/watch?v=cRWVHkjcYvw): Explaians why should 
one use parameters and why was it added to the tool
- [Usage of Parameter](https://drive.google.com/file/d/1nuJuUHtd9Fs08b9c9AcmKaN3_HClEmUg/view?usp=sharing): Explains how to use parameters in VisualStates.

<a name="people-involved"/>

## People Involved
- Baidyanath Kundu (kundubaidya99 [at] gmail [dot] com) [GSoC Student]
- Pushkal Katara (katarapushkal [at] gmail [dot] com) [Mentor]
- Okan Aşık (asik [dot] okan [at] gmail [dot] com) [Mentor]
- José María Cañas Plaza (jmplaza [at] gsyc [dot] es) [Mentor]

<a name="links"/>

## Links
- [Official Repository](https://github.com/JdeRobot/VisualStates)
- [Development Repository](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu)
- [Tutorials](http://jderobot.org/Tutorials#VisualStates_tool)

<a name="status"/>

## Development Status

|S.No.| Sub-Project                                 | Status | Timeline                    |
|----:|---------------------------------------------|:------:|:---------------------------:|
|     |**Phase 1: Parameterization of VisualStates**|        |May 27, 2019 - June 16, 2019 |
|1.   |Add the feature to Visual States Tool        | Done   |                             |
|2.   |Create example with parameters               | Done   |                             |
|     |**Phase 2: Creating a library of automatas** |        |June 17, 2019 - July 21, 2019|
|1.   |Create the repository for online library     |        |                             |
|2.   |Add feature to export to online library      | Done   |                             |
|3.   |Add feature to import from online library    | Done   |                             |
|4.   |Create examples for the library              |        |                             |

<a name="documentation"/>

## Documentation
The weekly documentation is available [here](https://theroboticsclub.github.io/colab-gsoc2019-Baidyanath_Kundu/).