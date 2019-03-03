# encoding: utf-8
"""
设置logging
"""

import sys
import logging


def bootstrap():
    stdout_hdlr = logging.StreamHandler(sys.stdout)
    stdout_hdlr.setFormatter(logging.Formatter(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    ))

    logging.getLogger('').addHandler(stdout_hdlr)
    logging.getLogger('').setLevel(logging.INFO)

    return logging


bootstrap()
