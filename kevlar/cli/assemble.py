#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of kevlar (http://github.com/dib-lab/kevlar) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import khmer


def subparser(subparsers):
    """Define the `kevlar assemble` command-line interface."""

    desc = "Use a simple greedy algorithm to assemble a single variant's reads"

    subparser = subparsers.add_parser('assemble', description=desc)
    subparser.add_argument('-d', '--debug', action='store_true',
                           help='print debugging output')
    subparser.add_argument('-o', '--out', metavar='FILE',
                           help='output file; default is terminal (stdout)')
    subparser.add_argument('--gml', metavar='FILE',
                           help='write graph to .gml file')
    subparser.add_argument('-n', '--min-abund', type=int, metavar='N',
                           default=2, help='discard interesting k-mers that '
                           'occur fewer than N times')
    subparser.add_argument('-x', '--max-abund', type=int, metavar='X',
                           default=500, help='discard interesting k-mers that '
                           'occur more than X times')
    subparser.add_argument('--jca', action='store_true', help="use khmer's "
                           "junction count assembler instead of kevlar's "
                           "greedy assembler")
    subparser.add_argument('--ignore', metavar='KMER', nargs='+',
                           help='ignore the specified k-mer(s) when in --jca '
                           'mode')
    subparser.add_argument('--collapse', action='store_true', help='in --jca '
                           'mode, collapse contigs that are contained within '
                           'other contigs')
    subparser.add_argument('-M', '--memory', default='1e6', metavar='MEM',
                           type=khmer.khmer_args.memory_setting,
                           help='memory to allocate for assembly graph in '
                           '--jca mode; default is 1M')
    subparser.add_argument('--max-fpr', type=float, metavar='FPR',
                           default=0.001, help='terminate if the expected '
                           'false positive rate of the assembly graph is '
                           'higher than the specified FPR; default is 0.001')
    subparser.add_argument('augfastq', help='annotated reads in augmented '
                           'Fastq format')
