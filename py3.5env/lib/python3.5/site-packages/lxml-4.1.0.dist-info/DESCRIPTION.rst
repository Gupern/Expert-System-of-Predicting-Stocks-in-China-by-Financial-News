lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

To contact the project, go to the `project home page
<http://lxml.de/>`_ or see our bug tracker at
https://launchpad.net/lxml

In case you want to use the current in-development version of lxml,
you can get it from the github repository at
https://github.com/lxml/lxml .  Note that this requires Cython to
build the sources, see the build instructions on the project home
page.  To the same end, running ``easy_install lxml==dev`` will
install lxml from
https://github.com/lxml/lxml/tarball/master#egg=lxml-dev if you have
an appropriate version of Cython installed.


After an official release of a new stable series, bug fixes may become
available at
https://github.com/lxml/lxml/tree/lxml-4.1 .
Running ``easy_install lxml==4.1bugfix`` will install
the unreleased branch state from
https://github.com/lxml/lxml/tarball/lxml-4.1#egg=lxml-4.1bugfix
as soon as a maintenance branch has been established.  Note that this
requires Cython to be installed at an appropriate version for the build.

4.1.0 (2017-10-13)
==================

Features added
--------------

* ElementPath supports text predicates for current node, like "[.='text']".

* ElementPath allows spaces in predicates.

* Custom Element classes and XPath functions can now be registered with a
  decorator rather than explicit dict assignments.

* Static Linux wheels are now built with link time optimisation (LTO) enabled.
  This should have a beneficial impact on the overall performance by providing
  a tighter compiler integration between lxml and libxml2/libxslt.

Bugs fixed
----------

* LP#1722776: Requesting non-Element objects like comments from a document with
  ``PythonElementClassLookup`` could fail with a TypeError.




