# Iterative_MSA
This script performs multiple sequence alignment (MSA) on nucleotide sequences from a FASTA file, then iteratively moves 50 nucleotides from the beginning to the end and reruns the alignment 5 times.
Requirements
Biopython: Install with pip install biopython

Clustal Omega: Must be installed and in your PATH

Download from http://www.clustal.org/omega/

Or install via package manager (e.g., sudo apt-get install clustalo on Ubuntu)

Usage
bash
python script_name.py input_sequences.fasta
Options
--shift: Number of nucleotides to shift (default: 50)

--iterations: Number of iterations to perform (default: 5)

Output
The script will save:

initial_alignment_result.fasta - Alignment before any shifting

alignment_after_iteration_X.fasta - Alignment after each iteration (X = 1-5)

Notes
The script creates temporary files during execution but cleans them up automatically

Each iteration shifts the sequences and realigns them

The shifting operation moves N nucleotides from the beginning to the end of each sequence
