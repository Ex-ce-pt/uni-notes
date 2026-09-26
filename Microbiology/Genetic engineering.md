
**Recombinant DNA** - DNA modified *in vitro*.

What might be used:
- Molecular cloning (PCR)
- Plasmids
- Restriction enzymes etc.

**Transgenic organism** - organism that has recombinant DNA.

DNA replication *in vitro* mimics the natural replication process.

## PCR
Polymerase chain reaction

Solution contains:
- Primers - like RNA primers.
- dNTPs - nucleotides.
- Buffer - keeps the pH stable.
- Template DNA - starting material.
- Thermal cycler - repeatedly denatures DNA to open up the double helix.
- DNA Polymerase - does the copying; high-temperature one is used.
	- Taq polymerase - DNA Polymerase from *Thermus aquaticus*.
	- Bacteriophage T7 polymerase - RNA Polymerase for *in vitro* transcription.

Process:
- $95\degree$ - DNA double strand is denatured.
- $55\degree$ - primers anneal to the DNA.
- $72\degree$ - DNA Polymerase extends the DNA.
- Repeat 35 times.

![[pcr.png]]

## Analysing DNA

Agarose gel electrophoresis

Solution moves through the gel.
Bigger molecules move slower.
Fluorescent dye is used to visualise the bands.

## Cutting DNA

**Restriction enzymes** - endonucleases, cut dsDNA.
Defense against phages in bacteria.
Recognise 4-8 bp.
Palindromic
Can make blunt cuts or overhang cuts ("sticky ends").

==Q: overhang cut terminology==
==does depend on enzyme or one can do both?== particular

If the DNA is cut/pasted, the phosphate backbone must be fixed using DNA ligase - **uses ATP**.

## Cloning plasmids

Used to get foreign DNA into bacteria.
Plasmids are engineered.

Antibiotic resistance gene is often used because otherwise bacteria have no motivation to replicate the plasmid.

**Multiple cloning site** - site that lets a lot of different restriction enzymes cut it.
**Markers** - show that the plasmid is in the bacterium (e.g. GFP/antibiotic resistance).

Eukaryotic regulatory sequences - used to clone eukaryotes, because they need more specific conditions.

DNA is pasted by cutting both foreign DNA and the plasmid with sticky ends that can bind together.

## Genomic library

Genomic library - complete genome of an organism divided into multiple cells in the form of recombinant plasmids.

Use restriction enzyme to shred the bacterial chromosome into pieces - **all ends are the same**!
Use the same enzyme to cut plasmids - same ends as the pieces of the chromosome.
The pieces of the chromosome get inserted into the plasmids.
Plasmids now contain the whole genome of the bacterium in them.

Can use plasmids to sequence or to see how other bacteria can use these genes by giving them the plasmids.

## DNA sequencing

#### Sanger sequencing (chain termination method)


Uses dideoxynucleotides - **cannot make another phosphodiester bond**!

Solution contains:
- All same things as normal PCR solution
- ddNTPs that are labeled (fluorescent?).

Process:
- Perform PCR
- Analyse the resulting DNA strands

The assumption is that it is equally likely that normal NTPs are used or ddNTPs.
Therefore there will (probably) be a strand that terminates at every position with a labeled nucleotide.
Can reconstruct the whole sequence.

#### Real time PCR

Generally done with RNA.
Uses dyes that bind to dsDNA of specific sequences.
Camera monitors the fluorescence every PCR cycle.
Can tell how many times greater the concentration of DNA/RNA is in comparison to another solution.
Doesn't tell the absolute concentration/amount.


## Synthetic biology

http://parts.igem.org/Main_Page 

Creating artificial biological systems and machinery.

## Eukaryotic cloning

DNA is more complicated.
Introns, exons, capping, RNA processing, transcription & translation decoupled.

The processed mRNA can be reverse transcribed to only get the exonic sequences - **can implant into prokaryotes**!


Transfection - DNA + polymers, make cell engulf polymers and DNA with it
Electroporation - DNA moves in the electric field in the direction of the cell
Transduction - through a virus
Microinjection - inject with a needle
Conjugation - through a pilus from a different cell


## Gene fusions

To measure gene activity.

Transcriptional fusion
is gene trnascribed
==woulnd't rna pol disconnect?==
if want to know if a gene is promoter
put gene of interest upstream of a reporter gene (that tells you if it's transcribed)


translational fusion
is protein produced
same at prev but remove stop codon on gene of interest
creates a fusion protein - gene of interest + reporter gene

## Cas9

Restriction enzyme system of bacteria.
Recognises an RNA sequence of a phage and cuts it.
If it's successful, it takes a sample of the phage RNA and incorporates it into the bacterial DNA for future reference.
