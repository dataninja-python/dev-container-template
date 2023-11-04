from setuptools import setup, find_packages

setup(
    name='YourAppName',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'yourappname=app.cli:main',
        ],
    },
)
