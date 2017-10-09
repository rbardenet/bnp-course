.. counter documentation master file, created by
   sphinx-quickstart on Mon Oct  9 15:59:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx tutorial
===============

This webpage is a digested tutorial for sphynx and readthedocs.
This tutorial collects and resumes part of the information from: http://www.sphinx-doc.org/en/stable/tutorial.html

Local Setup
=================

Read the docs documentation is based on sphynx docs. This documentation can be written in several kind of markup languages such as markdown and rst. To setup sphynx in your environment you can execute the following snippet of code in your shell::

    $ mkdir -p sphinx && cd sphinx
    $ virtualenv sphinx
    $ source ./sphinx/bin/activate
    $ pip install Sphinx

Once sphynx is installed, you can execute its facility ``sphinx-quickstart`` to setup your documentation folder into your project::

    $ mkdir -p docs
    $ cd docs
    $ sphinx-quickstart

I just pressed [enter] to all options but default except by the project name and the author.
This creates a lot of files, for example:

- ``conf.py`` contains all the metadata to build the doc's project
- ``index.rst`` is the main page of your generated site

Without touching anything, this is already set to go and generate html. You can do a first build by executing::

    $ make html

Then, open in your browser the generated index.html file that you will find in ``_build``.

Changing the theme
========================

To set new themes, you need to install the theme you want and then configure it in your ``conf.py``. For example, to install the read the docs theme::

$ pip install sphinx_rtd_theme

Then set the conf.py html_theme to::

    html_theme = "sphinx_rtd_theme"

More infor about available themes and possible tweaks are at: http://www.sphinx-doc.org/en/stable/theming.html

Documenting your project
===========================

One of the nicest features of sphinx is that its closely related to your project's source code. Specially if it's written in python. In general, we need to configure sphynx to tell it where to find our source code. This is done by configuring the  modifying the path environment variable from your ``conf.py``. For that you can uncomment and modify the following lines of code::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..')) //Put the relative path to your src folder

Importing doc strings from your source code
################################################

Autodoc is a sphynx plugin that allows us to embed your source code's doc strings into your documentation.

Install the ``autodoc`` extensions in the conf.py by adding the 'sphinx.ext.autodoc' string in the extensions list::

    extensions = ['sphinx.ext.autodoc'].
    
Then documentation will be automatically loaded if you import it with the autoXXX (autofunction, automodule, autoclass and autoexception directives). For example, importing a class::

    .. autoclass:: mymodule.Counter

yields the following output:

.. autoclass:: mymodule.Counter

and importing a method::

    .. automethod:: mymodule.Counter.increment

yields:

.. automethod:: mymodule.Counter.increment


Testing your documentation
################################################

Your documentation can be tested with a special sphynx builder called doctest. This means that instead of calling the html generation doing::

    $ make html
    
You can call it with the special builder as follows::

    $ make doctest
    
So doctest will find and execute your snippets of code and tell you if they're still ok! You'll get an output such as ::

    Doctest summary
    ===============
        1 test
        1 failure in tests
        0 failures in setup code
        0 failures in cleanup code
    build finished with problems.
    Testing of doctests in the sources finished, look at the results in _build/doctest/output.txt.
    make: *** [doctest] Error 1

This is of course very useful to check that your documentation is still up to date. Specially when used together with continuous integration techniques!

Adding tested documentation in your source code
***********************************************

Following sphinx doctest documentation, there are three main kind of snippets:

- ``testsetup`` are snippets used to initializer your code. Use this to import your module and setup initial values::

    .. testsetup:: *
    
       import counter

- ``testcode`` is used to show some snippet you'd like to test::

    .. testcode::
    
       1+1        # this will give no output!
       print 2+2  # this will give output

- ``testcode`` can be followed by ``testoutput``, specifying what is the expected output::

    .. testoutput::
    
       4

- also: ``doctest`` works on normal doctests as the following. You can put doctest blocks with the expected value in the next line and doctest will evaluate and validate that for you:

    >>> print 1
    2
    
More about it can be found in: http://www.sphinx-doc.org/en/stable/ext/doctest.html
