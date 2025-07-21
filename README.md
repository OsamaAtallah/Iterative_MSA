# Iterative_MSA
This script performs multiple sequence alignment (MSA) on nucleotide sequences from a FASTA file, then iteratively moves 50 nucleotides from the beginning to the end and reruns the alignment 5 times.
**Requirements**
1. Biopython: Install with pip install biopython
2. Clustal Omega: Must be installed and in your PATH
2.1. Download from http://www.clustal.org/omega/
2.2. Or install via package manager (e.g., sudo apt-get install clustalo on Ubuntu)

**Usage**
python script_name.py input_sequences.fasta

**Options**
--shift: Number of nucleotides to shift (default: 50)
--iterations: Number of iterations to perform (default: 5)

**Output**
The script will save:
1. initial_alignment_result.fasta - Alignment before any shifting
2. alignment_after_iteration_X.fasta - Alignment after each iteration (X = 1-5)

**Notes**
1. The script creates temporary files during execution but cleans them up automatically
2. Each iteration shifts the sequences and realigns them
3. The shifting operation moves N nucleotides from the beginning to the end of each sequence
