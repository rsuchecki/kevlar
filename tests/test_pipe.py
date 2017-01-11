#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of kevlar (http://github.com/standage/kevlar) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import glob
import pytest
import re
import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import kevlar


@pytest.mark.long
def test_trio2():
    findouts = [StringIO() for i in range(4)]
    for i in range(4):
        args = type('', (), {})()
        args.controls = glob.glob('tests/data/trio2/ctrl[1,2].fq.gz')
        args.ctrl_max = 1
        args.case_min = 8
        args.ksize = 31
        args.memory = 2e5
        args.max_fpr = 0.2
        args.out = findouts[i]
        args.flush = False
        args.collapse = False
        args.batch = [4, i+1]
        args.upint = 10000
        args.logfile = StringIO()
        args.case = 'tests/data/trio2/case1.fq.gz'

        kevlar.find.main(args)
        findouts[i].seek(0)

    args = type('', (), {})()
    args.memory = 5e3
    args.ksize = 31
    args.out = StringIO()
    args.max_fpr = 0.02
    args.collapse = True
    args.find_output = findouts
    args.logfile = StringIO()
    kevlar.collect.main(args)
    assert '1 collapsed linear paths' in args.logfile.getvalue()
    lastline = args.out.getvalue().strip().split('\n')[-1]
    contig, contigrc = lastline.split(',')[0:2]
    assert 'AGCCTCTG' in contig or 'AGCCTCTG' in contigrc
