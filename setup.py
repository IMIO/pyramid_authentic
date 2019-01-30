import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README.rst')).read()
changes = open(os.path.join(here, 'CHANGES.rst')).read()


setup(
    name='pyramid_authentic',
    version='0.1.0',
    description='Authentic authentification for Pyramid',
    long_description=readme + '\n' + changes,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Pylons",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=['pyramid_authentic'],
    install_requires=[
        'pyramid',
    ],
    author='IMIO',
    author_email='support@imio.be',
    license='GPL',
    url='https://github.com/IMIO/pyramid_authentic',
    keywords='pyramid authentic pylons web',
    test_suite='pyramid_authentic',
)
