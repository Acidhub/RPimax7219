#!/usr/bin/env python3

from distutils.core import setup,Extension

setup(
    name = "RPimax7219",
    version = "0.1",
    author = "Fernando Manfredi",
    author_email = "contact@acidhub.click",
    description = ("A small library to drive a MAX7219 LED serializer using hardware spidev"),
    license = "MIT",
    keywords = "raspberry pi rpi led max7219 matrix seven segment",
    url = "https://github.com/Acidhub/RPimax7219",
    packages=['RPimax7219'],
)
