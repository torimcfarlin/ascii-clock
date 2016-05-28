from setuptools import setup, find_packages


setup(
    name='ascii-clock',
    version='0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=['pytest==2.9.1', 'pytest-cov==2.2.1']
)
