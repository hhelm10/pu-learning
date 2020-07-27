from setuptools import setup, find_packages

requirements = [
]

# Uncomment once README.md exists

# with open("README.md", "r") as readme_file:
#     readme = readme_file.read()



setup(
    name="pu_learning",
    version="0.0.1",
    package_dir={'mypkg': 'src'},
    # author="BD, HH",
    description="Weepa",
    # long_description=readme,
    # long_description_content_type="text/markdown",
    url='https://github.com/hhelm10/pu-learning',
    packages=find_packages(),
    install_requires=requirements,
)