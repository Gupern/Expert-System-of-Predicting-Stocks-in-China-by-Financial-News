"""
设置模块
"""

import os
import logging


try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

CONFIG_FILE_PATH = os.path.join(CURRENT_DIR, 'config.ini')
CONFIG_FILE_SAMPLE_PATH = os.path.join(CURRENT_DIR, 'config.ini.sample')

config = ConfigParser.ConfigParser()

if os.path.exists(CONFIG_FILE_PATH):
    config.read(CONFIG_FILE_PATH)
elif os.path.exists(CONFIG_FILE_SAMPLE_PATH):
    logging.warning('config.ini not exists, use config.ini.sample instead')
    config.read(CONFIG_FILE_SAMPLE_PATH)
else:
    logging.error('config not exists')
    exit(1)
