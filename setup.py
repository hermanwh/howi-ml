import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="howi-ml",
    version="0.0.1",
    author="Herman Wika Horn",
    author_email="hermanwh@hotmail.com",
    description="A top-level machine learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermanwh/howi-ml",
    packages=['howiml', 'howiml.utils'],
    package_dir={'howiml': 'howiml'},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.8',
)