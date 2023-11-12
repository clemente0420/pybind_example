from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import os

__version__ = '0.0.1'

class get_pybind_include():
    def __str__(self):
        import pybind11
        return pybind11.get_include()

ext_modules = [
    Extension(
        'py_example',
        ['src/py_example.cc'],
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
        ],
        language='c++',
    ),
]

class BuildExt(build_ext):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = ['-std=c++11']
            # 如果需要DEBUG版本
            # Check for the environment variable before adding the '-g' flag
            if os.getenv('pybind_example_debug'):
                ext.extra_compile_args = ['-g']
        super().build_extensions()

setup(
    name='py_example',
    version=__version__,
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your project',
    long_description='',
    ext_modules=ext_modules,
    install_requires=['pybind11>=2.2'],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)
