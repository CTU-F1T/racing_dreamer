#!/usr/bin/env python
# setup.py
"""Install script for ROS1 catkin / ROS2 ament_python."""

from setuptools import setup

package_name = 'f1tenth_dreamer'

setup(
 name=package_name,
 version='0.0.0',
 packages=["agents", "models", "helpers"],
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 author='root',
 author_email='root@todo.todo',
 maintainer='root',
 maintainer_email='root@todo.todo',
 description='The f1tenth_dreamer package.',
 license='TODO',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'run_dreamer = agents.dreamer.src.agent:main',
             'run_td3 = agents.sb3.src.agent:main'
     ],
   },
)
