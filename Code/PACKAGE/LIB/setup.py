from setuptools import setup, find_packages

with open('PACKAGE/LIB/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="bmp_lib",
    version="0.1",
    include_package_data=True,
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    python_requires='>=3.9, <3.12',
    #url = github
    author="Taoufiq OUEDRAOGO",
    author_email="taoufiq.ouedraogo@edu.ece.fr",
    description="This package implement all the logic of Brief My Press.AI",
    #long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)