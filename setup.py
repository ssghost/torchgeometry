import os
import io
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


readme = open('README.rst').read()
# remove logo
long_description = '\n'.join(readme.split('\n')[7:])


VERSION = find_version('torchgeometry', '__init__.py')


requirements = [
    'torch==1.0.0',
]


setup(
    # Metadata
    name='torchgeometry',
    version=VERSION,
    author='Edgar Riba',
    author_email='edgar.riba@gmail.com',
    url='https://github.com/arraiy/torchgeometry',
    description='differential geometric computer vision for deep learning',
    long_description=long_description,
    license='BSD',

    # Test
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    # Package info
    packages=find_packages(exclude=('docs', 'test', 'examples',)),

    zip_safe=True,
    install_requires=requirements,
)
