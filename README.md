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
|1.   |Add the feature to Visual States Tool        | Done   |                             |
|2.   |Create example with parameters               | Done   |                             |
|     |**Phase 2: Creating a library of automatas** |        |June 17, 2019 - July 21, 2019|
|1.   |Create the repository for online library     | Done   |                             |
|2.   |Add feature to export to online library      | Done   |                             |
|3.   |Add feature to import from online library    |        |                             |
|4.   |Create examples for the library              |        |                             |

<a name="documentation"/>

## Documentation
#### Week 7: 8 July 2019 - 14 July 2019
##### Discussion
- Design of the parameterization of the VisualStates
    - Tree of states with parameters are going to be shown during import 
    - The states can be selected in the dialog mentioned above 
    - The information of states would be collapsible for easy viewing
- Design of online importer and exporter
    - The download and upload of files are going to be done via QThreads for multithreading the operations
    - One Class in one file structure is to be followed
    - The exporter doesn't need to show messages in this stage of development

##### Task
- Complete the requested changes as mentioned above

##### Progress
- Design of the parameterization of the VisualStates. 
    [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1)
    - Completed all the required changes
- Design of online importer and exporter. 
    [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/5)
    - Completed all the required changes
    - Also found and added a way to show progress messages in the exporter dialog
    
#### Week 6: 1 July 2019 - 7 July 2019
##### Task
- Add a dialog to display imported parameters
- Add importer for the online library

##### Progress
- Added importer for the online library.
[Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/5)
- Added check to prevent duplicate inputs being added to the list. 
[Issue](https://github.com/JdeRobot/VisualStates/issues/119)
- Added XML Validation. [Issue](https://github.com/JdeRobot/VisualStates/issues/117)
- Added dialog to display imported parameters. 
[Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1)

#### Week 5: 24 June 2019 - 30 June 2019
##### Discussion
- Design of online importer and exporter
    - PyGitHub library will be used to access the repository
    - It could be better to show the tree of states with the parameters instead of a snapshot
    - There will be a main xml file in the repository containing the names, descriptions and 
      the folder name in which the behaviour and the snapshot/tree of states is present
    - A demo repository will be created by me which will be used to create the online importer
      and exporter and once its complete we will shift to a jderobot repository.
- Design of parameterization of VisualStates
    -A list of added parameters need to be displayed during the import of a file

#### Task
- Implement the design of the exporter and importer
- Display the list of added parameters during import

#### Progress
- Created the demo repository for the library. [Link](https://github.com/sudo-panda/automata-library)
- Added the exporter to visual states. [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/5)

#### Week 4: 17 June 2019 - 23 June 2019
##### Discussion
- The documentation will be better with a blog style appearance rather than the current one.
    - This way the documentation could be made more comprehensive 
- Design of parameterization of VisualStates
    - The parameters are going to act like local namespace variables in the the source code.
    - They are to be added from the local namespace UI
    - They are not needed to be shown while importing, later whn selective state import will be
      added they will be shown to the user as a part of the states
- Design of online importer and exporter
    - Each behaviour needs two details
        - Name
        - Description
    - A snapshot would be added that could be auto generated or created by user of the root state
    - The repo will contain folders for each behaviour where the snapshot and xml file will be stored
      and another file at the root of the repo to store a list of the behaviours.
    - The exporter will create a pull request to the repository and add required code automatically.

#### Task
- Make changes to design of parameters
- Change the documentation from a single page format to a blog type format.
- Create a video demontrating the parameterization of visual states

#### Progress
- Converted the documentation to a blog format. [Link](https://theroboticsclub.github.io/colab-gsoc2019-Baidyanath_Kundu/)
- Made necessary changes to parameterization code. [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1)
- Made a demonstration video for the parameterization of visual states. [Link](https://www.youtube.com/watch?v=cRWVHkjcYvw)

#### Week 3: 10 June 2019 - 16 June 2019
##### Discussion
- The issue [Child Automata doesn't start from initial state if
  parent state ran once](https://github.com/JdeRobot/VisualStates/issues/114).
    - This could be a design decision or a flaw needs to be looked into.
- The design of VisualStates could be improved by implementing a tabbed
  structure - Issue opened [here](https://github.com/JdeRobot/VisualStates/issues/120).
    - Further discussion will be held on an issue that will be opened
      on the VisualStates repository.
- The issue of [User Input Validation](https://github.com/JdeRobot/VisualStates/issues/96) .
    - The issue needs to be split into specific issues(by me) for
      specific inputs.
- Transition Code and Condition execution order.
- Instead of keeping a Python and a C++ radio button to change syntax 
  highlighting ask user for his language preference at the beginning of
  the new behaviour.
- An issue needs to be created (by me) for the parameter design documentation.
  It will help in taking inputs from everyone to better the design - Issue opened 
  [here](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/issues/2)

##### Task
- Solve the User Input Validation Issues
- Change design of parameterization as inputs are provided on the 
  [issue](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/issues/2)
- Add parameters to VisualStates examples

##### Progress
- Added [integer check for some input](https://github.com/JdeRobot/VisualStates/issues/116)
- Added [Ctrl G fix](https://github.com/JdeRobot/VisualStates/issues/118)
- Added parameters to kobuki obstacle avoidance

#### Week 1-2: 27 May, 2019 - 9 June, 2019
##### Tasks
- Test all the examples present in VisualStates-examples
- Create a kobuki obstacle avoidance behaviour to internalize the tool
- Add parameterization to the VisualStates Tool
- Add demo gifs to each example

##### Progress
- Added parameterization to the Visual States - [Pull Request](https://github.com/TheRoboticsClub/colab-gsoc2019-Baidyanath_Kundu/pull/1)
- Added demo gifs - [Pull Request](https://github.com/JdeRobot/VisualStates-examples/pull/20)
- Created kobuki obstacle avoidance and kobuki wall follower