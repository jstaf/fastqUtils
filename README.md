# fqutils

A couple Python-based FASTQ QC tools that perform several useful file handling operations, 
notably check read-pairing, repair read-pairing, and trim reads. 
Notably, `fq-repair` is the only tool (to my knowledge) 
that can successfully re-pair reads from gzipped FASTQ input.
All tools are designed to be as fast and memory-efficient as possible.
Input is assumed to be 4-line FASTQ and may be gzipped.

## Installation and tests

To install as a python package (can also just be run as-is after cloning this repository): `pip install .`  

To run tests: `pytest`

## Current scripts

Run `commandname --help` for individual usage instructions.
Sample commands can also be found in the `tests/` directory.

* **fq-checkpair** - Check if two FASTQ files are properly paired and highlight errors.

* **fq-trim** - Starting from both ends, trim a read so that bases below a certain Phred quality score are removed. Resulting reads shorter than a minimum length are removed. Fast, dirty, and idiot-proof trimming.

* **fq-repair** - Re-pair the reads in two FASTQ files if reads have been filtered out or otherwise reordered. 

* **fq-zwc** - Just a wrapper around `wc -l` for gzipped files.
