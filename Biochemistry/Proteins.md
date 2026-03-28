
**Linear** polymers of amino acids, no branching!

Size can vary from less than 50 to more than 30 000 amino acids.

## Function

Protein functions:
- Mechanical (muscle)
- Structures in cells
- Enzymes (catalysts)
- Hormones
- Immune system (antibodies)
- Signaling, carriers, etc. (hemoglobin)

Comparing proteins to known ones can help predict its function.

> Evolution acts on proteins, not DNA.
> Useful proteins are passed down.

**Homologs** - similar function, common ancestor.
**Paralogs** - same function, same species.
**Orthologs** - same function, different species.

Comparing the sequence of multiple homologous proteins allows building the tree of life.

## Synthesis

The carboxylic group of one of the amino acids binds to the amino group of another.
Amido group (aka. peptide bond) is created.

**N-terminus** - the amino end of protein; the start of a protein.
**C-terminus** - carboxylate end of protein; the end of a protein.

Proteins are written **N-to-C**.

The sequence of the synthesised protein is determined at translation.

==TODO: synthesis

## Structures

Proteins fold into a 3D structure.

Folding is driven by weak interactions:
- Electrostatic (ionic)
- Hydrogen bonds
- Van der Waals interactions

Folding is thermodynamically favourable: $\Delta G = \Delta H - T \Delta S$
- $\Delta H < 0$ - whatever attracts is closer together
- $\Delta S(\text{protein}) < 0$ - limits the configuration of the protein
- $\Delta S(\text{water}) > 0$ - water molecules are more free to move wherever they want

==Q: how does it increase the entropy of water, exactly?

Structures:
- **Primary** - linear amino acid sequence
- **Secondary** - linear chain folded, twisted, in helices, etc.
- **Tertiary** - 3D configuration of the polypeptide
- **Quaternary** - different polypeptides form one protein

==NOTE: psi and phi angles

not all psi and phi combinations are possible - steric hindrance

**Ramachandran plot** - $\psi$ over $\phi$ angle plot showing which combinations are possible.

rare left-handed helices
right handed helices
majority flat sheets

==Glycene everywhere because of how small it is

#### Alpha helix

Stabilized by the $\ce{H}$ bonds between the $\ce{C=O}$ in amido group and the $\ce{N-H}$ of amino group 3-4 AAs down the helix.
~$3.6$ AAs per turn.
Side chains point out of the helix.
**Length**: $10-20$ AAs.
Most are right-handed, depends on the AAs used.
$(-)$-charged AAs towards the N-terminus and $(+)$-charged towards C-terminus.
Has a dipole moment.

**Alanine** - good helix former.
**Proline** - helix breaker (because of a very rigid structure).

==TODO: fig

#### Beta sheets

Stabilized by $\ce{H}$ bonds with other sheets - never occur alone!

**Length**: $<15$ AAs.
**Parallel** - both go N-to-C; $\ce{H}$ bonds are diagonal.
**Antiparallel** - one goes N-to-C, another C-to-N; $\ce{H}$ bonds perpendicular to the sheets.
**Beta turn** - at least 4 AAs, often glycine and proline.

No dipole moment.

==TODO: Gly for sure?

**Glycine** - common in turns, small and bendy.
**Proline** - sheet breaker, **but sometimes is absent**.

==TODO: fig

#### Fibrous proteins (secondary)

Insoluble in water.
Mostly simple secondary structures repeating.
Hydrophobic interactions + disulfide bonds.
Form helices and other structures.

Examples: keratin, collagen, silk.

==TODO: fig

#### Globular proteins (tertiary)

Soluble in water.
Spherical structure, mixture of secondary structures.
Hydrophobic residues inside, hydrophilic outside.
Stabilized by hydrophobic interactions + disulfide bonds inside, hydrogen bonds outside.

**Motif/fold** - segment that has a certain structure and is present in multiple proteins; not independently stable.
**Domain** - part of the sequence that is independently stable.

#### Intrinsically disordered proteins

Parts of a sequence.
Lack a defined structure.
High density of charged amino acids.
Can be important regions to interact with other proteins, then they take an ordered structure.

#### Quaternary structure

2 or more polypeptides (each in tertiary structure).

---

Generally - **1 sequence → 1 structure**.
Small proteins fold spontaneously.
Slowly but surely proteins fold, overcoming activation energy at each particular step.

**Chaperones** - proteins that help bigger proteins to fold.

Chaperones:
- Hsp70 - binds/unbinds hydrophobic regions of unfolded proteins.
- Chaperonins (GroEL) - hollow tube that threads proteins through to facilitate folding (water-free vessel, so hydrophobic parts of proteins have space to fold).
 
## Physical and chemical characteristics

Mostly dependent on the characteristics of side chains. 

- **Isoelectric point** - where the protein migrates in an electric field.
- **Molecular weight** - self-explanatory; average AA weighs ~$110 \space \text{Da}$
- **Prosthetic groups**:
	- **Lipoproteins**
	- **Glycoproteins**
	- **Metalloproteins**

## Purification

**Genetic engineering** - add a few specific AAs to make the protein easier to isolate.
**Extraction from cells/tissue** - crude extract (from certain organelles).
**Chromatography** using **size, charge, solubility**.
**Electrophoresis** - estimate molecular weight or purity; uses isoelectric point.

Determining structure:
- **x-ray crystallography** - proteins form crystals, look at interactions with x-rays.
- $\ce{^2H}$ **NMR**, $\ce{^{13}C}$ **NMR**
- **Cryo electron microscopy** - 
- **AlphaFold**
- **RoseTTAFold**
- other deep learning tools

