from pathlib import Path

from setuptools import find_packages, setup


# This is the package name as shown in "pip list"
PACKAGE_NAME = "netbox-external-data-list"


def get_version():
    version_file = Path(__file__).parent / PACKAGE_NAME.replace("-", "_") / "version.py"
    with version_file.open() as f:
        for line in f.readlines():
            if "__version__" not in line:
                continue
            delimiter = "'" if "'" in line else '"'
            return line.split(delimiter)[1]
    raise RuntimeError("Could not find the version number")


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    description="An example NetBox plugin",
    url="https://github.com/markkuleinio/netbox-external-data-list",
    author='Markku Leiniö',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    # MANIFEST.in helps finding the data files:
    include_package_data=True,
    zip_safe=False,
)
