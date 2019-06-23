# Parameterization of VisualStates
## Introduction
Visual States tool was created to make the production of automata behaviours easier and faster. 
Some of these states are common between behaviours and only some variables are needed to be changed to add them to the behaviour.
Parameterization of VisualStates makes it easier to tweak these variables to perfection. 

## Design 
- Parameters have been designed to act and be used just like local variables are done in code
- They are added via a tab named Paramters in the Local Namespace dialog and are not available in the Global Namespace dialog. 
- They consist of four things:
	- **Name** - Should start with an alphabet and can only contain alphanumeric characters and underscores
	- **Type** - Could be String, Character, Boolean, Integer, Float
	- **Value** - Should match with type
	- **Description** - A short description to tell the user what the parameter does

## Why use parameters?
Parameters help to extend the use of of the behaviors made. It helps others by pointing them
to the variables that can be changed to modify the behaviour to their needs. 

## Future development 
Parameters will act as a base for selective import of states and online importer. 

## Problems encountered and lessons learnt
- The biggest problem in any project that can occur is miscommunication and it
  caused this project to finish behind schedule. It was caused by me assuming that the 
  design suggested by me was the final design and going ahead with it without asking 
  my mentors. Later when we discussed on it a better design came out which is what open 
  source is all about. Discussing each and every step is a good practice because more ideas leads
  to the creation of a stronger product.
- There were many other small problems that were faced but a Google search or talking to mentors
  was enough to mitigate them. I would like to thank the mentors who were kind enough to accept 
  my requests and help me through the problems.