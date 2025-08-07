import os
import platform
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}',
        ]

        build_args = ['--config', 'Release']

        build_dir = os.path.join(self.build_temp, ext.name)
        os.makedirs(build_dir, exist_ok=True)
        
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=build_dir)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=build_dir)

setup(
    ext_modules=[CMakeExtension('arx_r5_sdk/lib/arx_r5_python', sourcedir='py/ARX_R5_python'), 
                 CMakeExtension('arx_r5_sdk/lib/kinematic_solver', sourcedir='py/ARX_R5_python')],
    cmdclass={'build_ext': CMakeBuild},
    zip_safe=False,
    package_dir={'': 'py/ARX_R5_python/src'},
    packages=['arx_r5_sdk'],
    package_data={
        'arx_r5_sdk': [
            '*.urdf',
            'lib/*.so*',
        ]
    },
)
