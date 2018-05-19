"""
Setup script for youtube_music_metadata
"""
from setuptools import setup, find_packages

setup(
    name='youtube_music_metadata',
    description='Fetch music related metadata for a YouTube video',
    version='1.0.0b1',
    url='https://github.com/lttkgp/YouTube-Music-Metadata',
    author='Naresh R',
    author_email='ghostwriternr@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['youtube', 'metadata', 'parse', 'music'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'youtube_music_metadata=youtube_music_metadata.core:main'
        ],
    }
)
