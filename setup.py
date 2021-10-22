from setuptools import setup

setup(
    name='pip-autoremove-3',
    version='0.10.2',
    description='Remove a package and its unused dependencies',
    py_modules=['pip_autoremove'],
    license='Apache License 2.0',
    url='https://github.com/imba-tjd/pip-autoremove',
    entry_points='''
    [console_scripts]
    pip-autoremove = pip_autoremove:main
    ''',
)
