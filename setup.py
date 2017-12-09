from setuptools import setup

setup(
    name='conn',
    version='0.1',
    py_modules=['conn'],
    install_requires=[
        'Click',
        'pexpect',
    ],
    entry_points='''
        [console_scripts]
        conn=conn:pex
    ''',
)
