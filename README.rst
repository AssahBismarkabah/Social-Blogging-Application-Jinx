JINX
======

Description:
Welcome to FlaskSocialBlogger by ```JINX``` an enterprise based on innovation and expertise, an open-source social blogging application built on Flask, the Python web framework. This repository houses a feature-rich platform that empowers users to share their stories, thoughts, and experiences within a vibrant community. With a focus on simplicity, flexibility, and extensibility, FlaskSocialBlogger offers a robust set of features for both bloggers and developers.

Key Features:

    User Authentication:
        Secure user registration and login system.
        Token-based authentication for enhanced security.

    Profile Management:
        Customizable user profiles with avatars and bio sections.
        Editable user profiles for personal expression.

    Blogging Functionality:
        Easy-to-use interface for creating and editing blog posts.
        Markdown support for rich and expressive content.
        Categorization and tagging for efficient content organization.

    Interactive Comment System:
        Threaded comments for organized discussions.
        Real-time comment updates for an engaging user experience.

    Like and Share Features:
        Like and share blog posts to enhance user engagement.
        Seamless social media integration.

    Notification System:
        Personalized notifications for new comments, likes, and shares.
        Centralized notification hub for easy tracking.

    Search and Discovery:
        Powerful search functionality for finding specific blogs or topics.
        Trending and popular sections for content discovery.

    Responsive Design:
        Mobile-friendly design for a seamless experience on various devices.
        Intuitive navigation for an enjoyable user experience.

    Security Measures:
        Implementation of secure coding practices.
        Protection against common web vulnerabilities.

    Deployment and Dockerization:
        Dockerized for easy deployment and scalability.
        Deployment guides for various hosting environments.


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/AssahBismarkabah/Social-Blogging-Application-Jinx.git
    $ cd jinx

Create a virtualenv and activate it::

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv .venv
    $ .venv\Scripts\activate.bat

Install Flaskr::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before
installing Flaskr::

    $ pip install -e ../..
    $ pip install -e .


Run
---

.. code-block:: text

    $ flask --app flaskr init-db
    $ flask --app flaskr run --debug

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser:
