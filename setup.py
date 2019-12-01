import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="MultiChoice",
    module="MultiChoice",
    author="Robert Sharp",
    author_email="webmaster@sharpdesigndigital.com",
    version="0.3.2",
    description="Framework for generating formatted user input questions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
    keywords=[
        "Questionnaire",
        "Multiple Choice",
        "Quiz Framework",
        "Terminal Survey",
    ],
    license="Free for non-commercial use",
)
