# Baidyanath-colab


|Contents                                 |
|-----------------------------------------|
|1. [VisualStates Tool](#visualstates)   |
|2. [People Involved](#people-involved)            |
|3. [Links](#links)                       |
|4. [Development Status](#status)         |
|5. [Documentation](#documentation)|

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
|1.   |Add feature to Visual States Tool            | Done   |                             |
|2.   |Create example with parameters               |        |                             |
|     |**Phase 2: Creating a library of automatas** |        |June 17, 2019 - July 21, 2019|
|1.   |Create the repository for online library     |        |                             |
|2.   |Add feature to import from online library    |        |                             |
|3.   |Create examples for the library              |        |                             |

<a name="documentation"/>

## Documentation
#### Week 1-2: 27 May, 2019 - 9 June, 2019
##### Tasks
- Test all the examples present in VisualStates-examples
- Create a kobuki obstacle avoidance behaviour to internalize the tool
- Add parameterization to the VisualStates Tool

##### Progress
- Added parameterization to the Visual States - [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1)