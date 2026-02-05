
A number used to estimate the \# of multiple bonds or rings in a molecule based on its molecular formula.

Difference in the *\# of pairs* of $\ce{H}$ atoms between the compound in question & an acyclic alkane w/ the same \# of $\ce{C}$ atoms.

Aka. **Degree of unsaturation**, **\# of double bond equivalences**.

If one were to construct a molecule in question from an acyclic alkane, they would have to give up:
- $1$ double bond → $2 \space \ce{H}$
- $1$ triple bond → $4 \space \ce{H}$
- $1$ ring → $2 \space \ce{H}$

## Rules

1. Write the molecular formula of the compound in question and a reference acyclic alkane w/ the same \# of carbon atoms as in the compound in question.
2. If there are any oxygens in the molecule, ignore them.
3. If there are any nitrogens, subtract as many hydrogens as there are nitrogens and ignore the nitrogens.
4. ==sulfur?

## Examples

**Ex. 1:**
```smiles
C=C
CC
```
$$
\begin{flalign}
&\ce{C2H6} \text{ - ethane, the reference acyclic alkane} \\
&\ce{C2H4} \text{ - ethene, the compound in question} \\
&\text{Diff.: } 6 - 4 = 1 \Rightarrow 1 \text{ pair of } \ce{H} \Rightarrow \text{IHD} = 1
&\end{flalign}
$$

**Ex. 2:**
```smiles
C1CCCCC1
CCCCCC
```
$$
\begin{flalign}
&\ce{C6H14} \text{ - hexane, the reference acyclic alkane} \\
&\ce{C6H12} \text{ - cyclohexane, the compound in question} \\
&\text{Diff.: } 14 - 12 = 2 \Rightarrow 1 \text{ pair of } \ce{H} \Rightarrow \text{IHD} = 1
&\end{flalign}
$$

**Ex. 3:**
```smiles
C1CC(C)O1
CCCC
```
$$
\begin{flalign}
&\ce{C4H10} \text{ - butane, the reference acyclic alkane} \\
&\ce{C4H8O} \text{ - the compound in question} \\
&\text{Diff.: } 10 - 8 = 2 \Rightarrow 1 \text{ pair of } \ce{H} \Rightarrow \text{IHD} = 1
&\end{flalign}
$$

**Ex. 4:**
```smiles
C1C=NC=CC=1
CCCCC
```
$$
\begin{flalign}
&\ce{C5H12} \text{ - pentane, the reference acyclic alkane} \\
&\ce{C5H5N} \text{ - pyridine, the compound in question} \\
&\text{Diff.: } 12 - (5 - 1) = 8 \Rightarrow 4 \text{ pair of } \ce{H} \Rightarrow \text{IHD} = 4
&\end{flalign}
$$