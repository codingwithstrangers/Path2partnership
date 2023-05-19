# -*- coding: utf-8 -*-

import os
import pathlib
import re
from setuptools import setup


ROOT = pathlib.Path(__file__).parent
on_rtd = os.getenv("READTHEDOCS") == "True"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

if on_rtd:
    with open("docs/requirements.txt") as f:
        requirements.extend(f.read().splitlines())

with open(ROOT / "twitchio" / "__init__.py", encoding="utf-8") as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

readme = ""
with open("README.rst") as f:
    readme = f.read()


sounds = [
    "yt-dlp>=2022.2.4",
    'pyaudio==0.2.11; platform_system!="Windows"',
]
speed = [
    "ujson>=5.2,<6",
    "ciso8601>=2.2,<3",
    "cchardet>=2.1,<3"
]
extras_require = {"sounds": sounds, "speed": speed}

setup(
    name="twitchio",
    author="TwitchIO",
    url="https://github.com/TwitchIO/TwitchIO",
    version=VERSION,
    packages=[
        "twitchio",
        "twitchio.ext.commands",
        "twitchio.ext.pubsub",
        "twitchio.ext.routines",
        "twitchio.ext.eventsub",
        "twitchio.ext.sounds",
    ],
    license="MIT",
    description="An asynchronous Python IRC and API wrapper for Twitch.",
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
