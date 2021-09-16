from setuptools import setup

readme = open("README.md", "r", encoding="utf-8").read()
requirements = open("requirements.txt", "r").read().strip().splitlines()

setup(
    name='GDRest',
    version='1.0.0',
    packages=["gdrest"],
    url='https://github.com/Silverflower67/GDRest',
    license='MIT',
    author='Silverflower67',
    author_email='',
    description='REST API for Geometry Dash, made with Python, gd.py and Starlette',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
        "Operating System :: OS Independent"
    ],
    install_requires=requirements,
    entry_points={"console_scripts": "gdrest=main"}
)
