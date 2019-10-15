#!/usr/bin/env python

""" MultiQC module to parse output from duplex_seq """

from __future__ import print_function
import logging

from multiqc.modules.base_module import BaseMultiqcModule

# Initialise the logger
log = logging.getLogger(__name__)

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):
        super(MultiqcModule, self).__init__(name='Duplex Seq', anchor='duplex_seq')



