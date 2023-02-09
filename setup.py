from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='py-auto-start',  # package name
    version=VERSION,  # package version
    description='cross-platform auto start',  # package description
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/shi-hou/py-auto-start',
    license='MIT',
    packages=find_packages(),
    platforms=['windows', 'macos', 'linux'],
    zip_safe=False,
    classifiers=[
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
    ],
)
