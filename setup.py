import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meterpreter-traffic-parser",
    version="0.0.1",
    author="SpartaEN",
    author_email="nya@sparta-en.org",
    description="Meterpreter traffic parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpartaEN/meterpreter_traffic-parser",
    project_urls={
        "Bug Tracker": "https://github.com/SpartaEN/meterpreter_traffic-parser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
