#!/usr/bin/env python3

import sys, argparse, os
from Bio import SeqIO

parser = argparse.ArgumentParser(description='Remove reads above or below a certain length from a FASTQ file.')
parser.add_argument('--min', default=0, type=int, help='Minimum read length')
parser.add_argument('--max', default=99999999, type=int, help='Maximum read length')
parser.add_argument('inputFASTQ', nargs=1)
parser.add_argument('outputFASTQ', nargs=1)
argv = parser.parse_args()

if not os.path.isfile(argv.inputFASTQ[0]):
    sys.exit('Valid input file required')

with open(argv.outputFASTQ[0], 'w') as out:
    for record in SeqIO.parse(argv.inputFASTQ[0], 'fastq'):
        if argv.min <= len(record) <= argv.max:
            SeqIO.write(record, out, 'fastq')