#!/usr/bin/env python3
from Bio import SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Align.Applications import ClustalOmegaCommandline
import os
import tempfile
from Bio import AlignIO

def run_clustal_alignment(input_file, output_file):
    """Run Clustal Omega alignment on the input FASTA file"""
    clustalomega_cline = ClustalOmegaCommandline(infile=input_file, outfile=output_file, verbose=True, auto=True)
    clustalomega_cline()
    return AlignIO.read(output_file, "fasta")

def shift_sequences(alignment, shift_length=50):
    """Shift nucleotides from beginning to end for each sequence in the alignment"""
    shifted_sequences = []
    for record in alignment:
        shifted_seq = record.seq[shift_length:] + record.seq[:shift_length]
        shifted_record = record[:]  # Create a copy
        shifted_record.seq = shifted_seq
        shifted_sequences.append(shifted_record)
    return MultipleSeqAlignment(shifted_sequences)

def write_fasta_from_alignment(alignment, output_file):
    """Write an alignment object to a FASTA file"""
    with open(output_file, "w") as f:
        for record in alignment:
            f.write(f">{record.id}\n{record.seq}\n")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Run iterative multiple sequence alignment with nucleotide shifting")
    parser.add_argument("input_fasta", help="Input FASTA file containing nucleotide sequences")
    parser.add_argument("--shift", type=int, default=50, help="Number of nucleotides to shift in each iteration")
    parser.add_argument("--iterations", type=int, default=5, help="Number of iterations to perform")
    args = parser.parse_args()

    # Check if Clustal Omega is installed
    try:
        ClustalOmegaCommandline()
    except:
        print("Error: Clustal Omega is not installed or not found in PATH")
        return

    # Create a temporary directory for intermediate files
    with tempfile.TemporaryDirectory() as temp_dir:
        current_alignment = None
        
        # Initial alignment
        initial_output = os.path.join(temp_dir, "initial_alignment.fasta")
        current_alignment = run_clustal_alignment(args.input_fasta, initial_output)
        print("\nInitial alignment completed")
        
        # Save the initial alignment
        with open("initial_alignment_result.fasta", "w") as f:
            AlignIO.write(current_alignment, f, "fasta")
        
        # Iterative shifting and alignment
        for i in range(1, args.iterations + 1):
            print(f"\nStarting iteration {i}")
            
            # Shift sequences
            shifted_alignment = shift_sequences(current_alignment, args.shift)
            shifted_file = os.path.join(temp_dir, f"shifted_{i}.fasta")
            write_fasta_from_alignment(shifted_alignment, shifted_file)
            
            # Run alignment on shifted sequences
            aligned_file = os.path.join(temp_dir, f"aligned_{i}.fasta")
            current_alignment = run_clustal_alignment(shifted_file, aligned_file)
            
            # Save the result
            with open(f"alignment_after_iteration_{i}.fasta", "w") as f:
                AlignIO.write(current_alignment, f, "fasta")
            
            print(f"Completed iteration {i}")

    print("\nAll iterations completed. Alignment results saved as:")
    print("- initial_alignment_result.fasta")
    for i in range(1, args.iterations + 1):
        print(f"- alignment_after_iteration_{i}.fasta")

if __name__ == "__main__":
    main()