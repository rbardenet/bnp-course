# How to fill the template

This repository is a template of a python project integrating several good software engineering practices and new documentation tools. This document will lead you in the path of filling the template and create your python project easily.

## Readme and Installation instructions

You'll see the readme already has some text. This text is merely a place holder to be replaced.

### Get a Name

One of the first things you need to do is to name your project. Brand it. People will know it by its name. The name can be an acronym such as (CaBAnA = Can Be An Acronym) or it can be a fantasy name. It may include a metaphore or not. The only important thing is that it should be easy to remember. Long project names, or acronyms with too many consonants are not good for that. 
Think also that depending on the technology or the conventions, some tools require special casing: start with uppercase or lowercase, spaces allowed or forbidden, underscores or not... Choose wisely.

Once you have that, you can replace all tags such as [Project Name] and [project_name] all over the readme.


### Get a Project Description

Tell me what your project is about. Is it a library, a framework, or a tool? Why is this important, what is the problem it solves? Is it something really new and cool? Tell me. You should convince the reader that he should download your project and not the neighbour's one.

### Make it Easy to Install

People knowing python will probably know `pip` and how it works. Maybe some C. But they for sure don't know the internals of your package. They want single-click or copy paste-install.
  - Explain the instructions to install strange dependencies
  - Create a setup.py with all the correct dependencies. So people just need to write `pip install .`
  
You should not modify too much this section. This should be standard, people should feel that they know the process, that "they know what they are doing", even if they are not.
To make that easy, we need to keep the `pip install` and just update the `setup.py` file with the correct dependency information.

## Continuous Integration Builds

### Travis of Unix and OSX

Continuous integration for Unix and MacOSX uses TravisCI (https://travis-ci.org).

1) Travis CI has a main configuration file named .travis.yml that needs to be updated for your needs. That is, set the versions of python you would like to test for, set special scripts to run tests, and so on.

2) On the README.md, there is a build tag that shows what is the status of your build. You should fill the template tag with your username, your project name, and the branch that is built (usually master?).

This tag looks like this:

[![Build Status](https://travis-ci.org/[your_username]/[project_name].svg?branch=[branch_to_test])](https://travis-ci.org/[your_username]/[project_name])

 =>
 
[![Build Status](https://travis-ci.org/guillep/project.svg?branch=master)](https://travis-ci.org/guille/project)

3) You should go to https://travis-ci.org/profile/[your_username] and activate the travis CI for your project