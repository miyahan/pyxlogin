"""pyxlogin setup file."""
from setuptools import find_packages
from setuptools import setup

setup(
    name='pyxlogin',
    version='0.1',
    description='Python telnet client',
    long_description='telnet helper',
    license='MIT',
    author='Miyahan',
    author_email='miyahan.com@gmail.com',
    url='https://github.com/miyahan/pyxlogin',
    keywords='telnet xlogin router',
    packages=find_packages(),
    platforms=['POSIX'],
    install_requires=['pexpect']
)
