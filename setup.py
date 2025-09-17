# Ultralytics YOLO 🚀, GPL-3.0 license

import re
from pathlib import Path

import pkg_resources as pkg
from setuptools import find_packages, setup

# Settings
FILE = Path(__file__).resolve()
ROOT = FILE.parent  # root directory
README = (ROOT / "README.md").read_text(encoding="utf-8")
REQUIREMENTS = [f'{x.name}{x.specifier}' for x in pkg.parse_requirements((ROOT / 'requirements.txt').read_text())]


def get_version():
    file = ROOT / 'ultralytics/__init__.py'
    return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(), re.M)[1]


setup(
    name="ultralytics",  # name of pypi package
    version=get_version(),  # version of pypi package
    python_requires=">=3.7.0",
    license='GPL-3.0',
    description='Ultralytics YOLOv8 and HUB',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ultralytics/ultralytics",
    project_urls={
        'Bug Reports': 'https://github.com/ultralytics/ultralytics/issues',
        'Funding': 'https://ultralytics.com',
        'Source': 'https://github.com/ultralytics/ultralytics',},
    author="Ultralytics",
    author_email='hello@ultralytics.com',
    packages=find_packages(),  # required
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        'dev':
        ['pytest', 'pytest-cov', 'coverage', 'mkdocs', 'mkdocstrings[python]', 'mkdocs-material'],},
    entry_points={
        'console_scripts': ['yolo = ultralytics.yolo.cli:cli', 'ultralytics = ultralytics.yolo.cli:cli'],})
