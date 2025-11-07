
## VSEPR

**Valence Shell Electron Pair Repulsion** - electron pairs strive to be as far as possible from each other.

![[VSEPR visualization.png]]

| # of bonds of C | Hybridization | Shape       |
| --------------- | ------------- | ----------- |
| 4               | $\text{sp}^3$ | tetrahedral |
| 3               | $\text{sp}^2$ | trigonal    |
| 2               | $\text{sp}$   | linear      |

How to draw a Lewis structure (example, $\ce{O3}$):
1. Figure out the placement of atoms (good luck!):
	$\ce{O \space O \space O \space}$
2. Count up all the valence electrons (accounting for the charge of ions, if needed):
	$6 + 6 + 6 = 18 \space (9 \text{ pairs})$
3. Fill the octet of all the atoms:
	![[lewis structure step 3.png]]
4. Now there are more electrons (20) than are available (18), add multiple bonds to account for that:
	![[lewis structure step 4.png]]
5. Count how many electrons each atom has. Bonds count as 1 electron. If there are more electrons than normally, put a (-) formal charge, if less (+) formal charge:
	![[lewis structure step 5.png]]
6. Adjust the geometry of the molecule and electron pairs according to VSEPR:
	![[lewis structure step 6.png]]


## (S, R) Nomenclature

Used in organic molecules /w **chiral carbon atoms** (4 bonds).

**Chiral** - not identical to its mirror image; not possible to achieve /w transpose & rotation.
**Structure isomers** (constitutional isomers) - same number and type of atoms, different bonds.
**Stereoisomers** - same atoms and order of binding, different shape in space.
**Enantiomers** - isomers that are mirror images of each other; **R** and **S** molecules.

![[Enantiomers-with-a-model.png]]

How to assign:
1. Find a chiral carbon - 4 bonds /w different groups.
2. Rank neighboring atoms 1-4:
	1. Higher atomic number/mass - higher rank.
	2. If atoms are the same, go further down the chain until there's difference.
	3. Multiple bonds count as multiple atoms of the same element: ($\ce{=O <-> (-O)(-O)}$).
	4. Consider all of the neighbors of the atoms in question: $\ce{-C(C2)H}$ ranks higher than $\ce{-C(C)H2}$.
	5. When considering neighbors, first look at the elements, only then at the \# of atoms: $\ce{-C(S)H2}$ ranks higher than $\ce{-C(=O)(O)H}$ because of $\ce{S}$, but $\ce{-C(=O)(O)H}$ ranks higher than $\ce{-C(O)H2}$ because it has more $\ce{O}$ (3, to be precise).
	6. Last group (\#4) is commonly $\ce{H}$.
3. Rotate the carbon atom so the neighbor /w rank 4 is pointing away from the viewer.
4. Count the neighbors 1→3.
5. If they're positioned clockwise - **R**, if counterclockwise - **S**.

![[S, R nomenclature assignment.png]]

> 3 atoms connecting to a carbon can't be in the same plane! If it looks like that in the structure, the orientation is unspecified! The plane passes through the carbon AND 2 of its neighbors!

```smiles
CCC(Cl)(C)O
CC[C@](Cl)(C)O
```
	