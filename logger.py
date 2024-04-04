#!/usr/bin/env python
# -*-coding:UTF-8-*-
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='## %Y-%m-%d %H:%M:%S')

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

# logger.debug("This is a debug log")
# logger.info("This is an info log")
# logger.critical("This is critical")
# logger.error("An error occurred\n")
