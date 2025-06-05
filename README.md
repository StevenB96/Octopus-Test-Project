Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, Django takes care of much of the hassle of web development, allowing you to focus on writing your app without needing to reinvent the wheel. It’s free and open source.

---

Table of Contents

1. Key Features
2. Requirements
3. Installation

   * From PyPI
   * From Source
4. Quickstart

   * Creating a Project
   * Running the Development Server
5. Running the Test Suite
6. Documentation
7. Contributing

   * Code of Conduct
   * Submitting Issues & Pull Requests
   * Development Workflow
8. Community & Support
9. License

---

Key Features

* Rapid Development
  Includes an ORM, URL routing, template engine, form handling, and more, so you can get your applications up and running quickly.

* Batteries-Included
  Comes with an authentication system, admin interface, internationalization, and caching frameworks out of the box.

* Security
  Protects against common web vulnerabilities (CSRF, XSS, SQL injection) by default.

* Scalability
  Proven in high-traffic sites. Easily integrates with caching, load-balancing, and multiple database backends.

* Extensible
  A pluggable app ecosystem and a large selection of third-party packages available on the Django Packages site: [https://djangopackages.org/](https://djangopackages.org/)

* Versatile
  Suitable for content management systems, social networks, scientific computing platforms, and more.

---

Requirements

* Python

  * Django 4.x and later: Python 3.8, 3.9, 3.10, 3.11, or 3.12
  * Django 3.2 LTS: Python 3.6, 3.7, 3.8, 3.9, or 3.10

* Databases (one or more of the following)

  * PostgreSQL (recommended)
  * MySQL
  * MariaDB
  * SQLite (default for development)
  * Oracle

* Other Dependencies (for optional features)

  * Pillow (for ImageField support)
  * psycopg2 (for PostgreSQL support)
  * mysqlclient (for MySQL/MariaDB support)
  * pyyaml (for reading YAML fixtures)
  * gunicorn or uwsgi (WSGI servers for deployment)

---

Installation

From PyPI

The recommended way to install Django for most users is via PyPI. You can install Django and its dependencies in a virtual environment:

# Create a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate       (macOS/Linux)
venv\Scripts\activate          (Windows)

# Upgrade pip

pip install --upgrade pip

# Install the latest stable release of Django

pip install Django

To install a specific version (for example, 4.2.1):
pip install Django==4.2.1

To verify the installation:
python -c "import django; print(django.get\_version())"

From Source

If you want to work with the bleeding-edge version (e.g., for contributing or testing upcoming features), clone the official repo and install from source:

# Clone the Django repository

git clone [https://github.com/django/django.git](https://github.com/django/django.git)
cd django

# Optionally, switch to a branch or tag:

# git checkout stable/4.2.x

# Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

# Install development dependencies

pip install --upgrade pip setuptools wheel
pip install -r requirements/py3.txt

# Install Django locally in editable mode

pip install -e .

# Verify the installation

python -c "import django; print(django.get\_version())"

---

Quickstart

This section walks you through creating a minimal Django project and app. Built-in commands will scaffold everything you need.

Creating a Project

1. Start a new project
   django-admin startproject mysite
   cd mysite

2. Inspect project structure
   mysite/
   manage.py
   mysite/
   **init**.py
   settings.py
   urls.py
   asgi.py
   wsgi.py

3. Configure the database (optional)
   By default, Django uses SQLite. To use PostgreSQL, for example, update mysite/settings.py:

   DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'mydatabase',
   'USER': 'mydbuser',
   'PASSWORD': 'mypassword',
   'HOST': 'localhost',
   'PORT': '5432',
   }
   }

4. Apply initial migrations
   python manage.py migrate

5. Create a superuser
   python manage.py createsuperuser

Running the Development Server

Start the development server with:
python manage.py runserver

Open your browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the welcome page.
Access the admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials you created.

---

Running the Test Suite

Django includes an extensive test suite. To run tests in your local checkout:

Install testing dependencies (if you cloned from source):
pip install -r requirements/tests.txt

Run all tests:
python -Wall manage.py test

-W error can be used to treat warnings as errors.

You can target specific apps:
python manage.py test django.contrib.auth

Using tox (optional): If you have tox installed, you can run the entire test matrix:
tox

This will create virtual environments for each supported Python version and run the tests.

---

Documentation

Comprehensive and up-to-date documentation is available at:

Official Docs:
[https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
(Choose your version at the top of the page, e.g., 4.2)

Tutorial:
[https://docs.djangoproject.com/en/stable/intro/](https://docs.djangoproject.com/en/stable/intro/)
A step-by-step tutorial to build your first app from scratch.

API Reference:
Detailed reference for all modules, classes, and functions used internally by Django.

Release Notes:
[https://docs.djangoproject.com/en/stable/releases/](https://docs.djangoproject.com/en/stable/releases/)
Find changelogs for each release with backward-incompatibility notices, deprecations, and bug fixes.

---

Contributing

We welcome contributions from the community! Please read through this section to get started.

Code of Conduct

Django adopts a code of conduct to foster a welcoming and respectful community. By participating, you agree to abide by this code:
[https://www.djangoproject.com/conduct/](https://www.djangoproject.com/conduct/)

Submitting Issues & Pull Requests

1. Find or report an issue
   Search existing issues before opening a new one: [https://github.com/django/django/issues](https://github.com/django/django/issues)
   If it’s a bug or feature request, ensure it follows the issue templates:
   [https://github.com/django/django/tree/main/.github/ISSUE\_TEMPLATE](https://github.com/django/django/tree/main/.github/ISSUE_TEMPLATE)

2. Fork the repository
   Click “Fork” in the top-right corner of the Django GitHub page.
   Clone your fork locally:
   git clone [https://github.com/](https://github.com/)<your-username>/django.git
   cd django

3. Create a branch
   git checkout -b issue-<number>-description

4. Write code & tests
   Develop your changes with adherence to Django’s coding style guidelines:
   [https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/)
   Add or update tests to cover your changes.
   Run the test suite to ensure everything passes:
   python manage.py test

5. Commit and push
   git add .
   git commit -m "Fixed issue #<number>: <brief description>"
   git push origin issue-<number>-description

6. Open a Pull Request
   Go to your fork on GitHub, select the branch, and click “Compare & pull request.”
   Provide a clear title, description, and reference the issue number.
   Django maintainers will review and discuss feedback on your PR.

Development Workflow

* Follow Git branching conventions when creating feature/bugfix branches:
  [https://docs.github.com/en/get-started/quickstart/github-flow](https://docs.github.com/en/get-started/quickstart/github-flow)
* Keep commits small, atomic, and descriptive.
* Rebase your branch on main frequently to reduce merge conflicts.
* Ensure your code passes:

  * flake8 (PEP8 compliance)
  * isort (imports ordering)
  * tox (multi-version testing)

---

Community & Support

* Mailing Lists
  [https://groups.google.com/g/django-users](https://groups.google.com/g/django-users)
  [https://groups.google.com/g/django-developers](https://groups.google.com/g/django-developers)

* IRC/Matrix

  * IRC: #django on Libera.Chat
  * Matrix: #django\:matrix.org

* Stack Overflow
  Tag your questions with “django”:
  [https://stackoverflow.com/questions/tagged/django](https://stackoverflow.com/questions/tagged/django)

* Reddit
  [https://www.reddit.com/r/django/](https://www.reddit.com/r/django/)

* Conferences & Meetups
  [https://www.djangoproject.com/community/](https://www.djangoproject.com/community/)

---

License

Django is licensed under the BSD 3-Clause “New” or “Revised” License. See the LICENSE file for details:
[https://github.com/django/django/blob/main/LICENSE](https://github.com/django/django/blob/main/LICENSE)
