import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brads-badass-canary-r351574nc3",
    version="0.0.1",
    author="Leo Przybylski",
    author_email="r351574nc3@gmail.com",
    description="Teams/Email/SMS notifications via Azure Logic Apps provisioning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r351574nc3/brads-badass-canary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)