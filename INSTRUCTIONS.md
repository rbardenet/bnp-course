## Python paper template

[![Template Build Status](https://travis-ci.org/guillep/python-paper-template.svg?branch=master)](https://travis-ci.org/guillep/python-paper-template)

This project is a template for python scientific projects. This template comes with utilities to easily setup continuous integration, project configurations and more. Follow the next instructions to setup your own project.


### Main setup

1. Download this template and put it into your git repository
2. Rename the `mypackage` directory as your project's name
3. Put your code inside your package directory
4. Put any tests you have inside the `tests` directory
5. Update the `README.md` to relate to your project
 - change the project name
 - update the pre-requirements if any (or remove them if none)
 - update the installation instructions
 - put your usage examples and other documentation on it
 
### Setting up Travis

1. Update the `.travis.yml` with your own configuration matrix. The template already comes with scripts to run on linux and osx. Read the comments and documentation set in the file for specificities of osx.
2. Update the `.travis.yml` install with your installation instructions
3. Update the `.travis.yml` script with your testing instructions. This could be calling `pytest` or executing an arbitrary program of yours.
4. Log in into (https://travis-ci.org/) and activate your project
5. Update the build status button with your project's corresponding travis URLs. Travis gives you a copy-past alternative also: go to your project's travis page and click on the button next to github's cat. That will give you several copy-paste options.