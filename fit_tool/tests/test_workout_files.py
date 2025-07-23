import logging
import os
import sys

from fit_tool.fit_file import FitFile
from fit_tool.utils.logging import formatter, logger


def test_decode_trainer_road():
    path = os.path.join(os.path.dirname(__file__), 'data/trainerroad_744490.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        print(f'Profile version: {fit_file.header.profile_version}')
        fit_file.to_rows()
