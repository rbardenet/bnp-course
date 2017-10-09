# Python paper template

[![Template Build Status](https://travis-ci.org/guillep/python-paper-template.svg?branch=master)](https://travis-ci.org/guillep/python-paper-template)

This project is a template for python scientific projects. This template comes with utilities to easily setup continuous integration, project configurations and more. Follow the next instructions to setup your own project.

## Main setup

1. Download this template and put it into your git repository
2. Rename the `mypackage` directory as your project's name
3. Put your code inside your package directory
4. Put any tests you have inside the `tests` directory
5. Put any data files you use under the `data` directory
6. Update the `README.md` to relate to your project
 - change the project name
 - update the pre-requirements if any (or remove them if none)
 - update the installation instructions
 - put your usage examples and other documentation on it
7. Remove this `INSTRUCTIONS.md` file

### How to fill the template

This repository is a template of a python project integrating several good software engineering practices and new documentation tools. This document will lead you in the path of filling the template and create your python project easily.

### Get a Name

One of the first things you need to do is to name your project. Brand it. People will know it by its name. The name can be an acronym such as (CaBAnA = Can Be An Acronym) or it can be a fantasy name. It may include a metaphore or not. The only important thing is that it should be easy to remember. Long project names, or acronyms with too many consonants are not good for that. 
Think also that depending on the technology or the conventions, some tools require special casing: start with uppercase or lowercase, spaces allowed or forbidden, underscores or not... Choose wisely.

Once you have that, you can replace all tags such as [Project Name] and [project_name] all over the readme.

### Get a Project Description

Tell me what your project is about. Is it a library, a framework, or a tool? Why is this important, what is the problem it solves? Is it something really new and cool? Tell me. You should convince the reader that he should download your project and not the neighbour's one.

### Choose a Licence

Choose a licence and update the text into the [LICENCE](LICENCE) file.

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

### Setting up Travis

1. Update the `.travis.yml` with your own configuration matrix. The template already comes with scripts to run on linux and osx. Read the comments and documentation set in the file for specificities of osx.
2. Update the `.travis.yml` install with your installation instructions
3. Update the `.travis.yml` script with your testing instructions. This could be calling `pytest` or executing an arbitrary program of yours.
4. Log in into (https://travis-ci.org/) and activate your project
5. Update the build status button with your project's corresponding travis URLs. Travis gives you a copy-past alternative also: go to your project's travis page and click on the button next to github's cat. That will give you several copy-paste options.