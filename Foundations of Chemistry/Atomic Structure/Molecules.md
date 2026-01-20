
**Molecule** - combination of multiple bonded atoms.

## Bond types

| Bond type          | Electron sharing | Electrostatic forces        | Example                |
| ------------------ | ---------------- | --------------------------- | ---------------------- |
| Non-polar covalent | Equal            | Between subatomic particles | $\ce{N2}$, $\ce{O2}$   |
| Polar covalent     | Shifted          | Between subatomic particles | $\ce{H2O}$, $\ce{CO2}$ |
| Ionic              | None             | Between whole ions          | $\ce{Na+Cl-}$          |

No clear boundaries between different bonds - it's a spectrum.
The distinction between bond types is usually drawn using [electronegativity](#Pauling%20electronegativity).

## Covalent bond

Competing forces:
- $e^--p^+$ attraction - dominating, because atoms are big and electrons are smeared all over them.
- $p^+-p^+$ repulsion - weaker, because the nucleus is very concentrated and a lot smaller than the full atom + electrons shield the nuclear charge.
- $e^--e^-$ repulsion

$\Delta E$ - the energy/strength of the bond.
$r_0$ - bond length at $0 \space K$ (absolute minimum of energy, the most stable state possible).

With temperature (additional energy) the bond length starts to vary.
If $\Delta E$ or more energy is supplied, the bond is broken - **cracking**.

Morse potential diagram:
![[molecules/morse-potential.png]]


Non-polar bond occurs between identical atoms, e.g. diatomic molecules: $\ce{H2}$, $\ce{O2}$, $\ce{N2}$, $\ce{F2}$, etc.
Polar bond occurs between different atoms.

![[molecules/polar-bond.png]]

Dipole arrow points from $(+)$ to $(-)$.

**Dipole** - system with 2 electric poles.
We can talk about a bond having a dipole or about a molecule being a dipole itself.
These should not be mixed up.

A molecule's dipole is a sum of the dipoles of all the bonds in it.

## Ionic bond

Bond between a cation and an anion.
Since electrostatic forces act in all directions, the geometry of the bond doesn't matter.
Important: length of the bond.

![[molecules/ionic-bond.png]]

## Pauling electronegativity

**Electronegativity** - propensity of an atom to attract $e^-$.
There are various systems and values for $e^-$-neg., **Pauling electronegativity** is used the most.

Most electronegative elements: $\ce{N}$, $\ce{O}$, $\ce{F}$
Least electronegative element: $\ce{Fr}$

Electronegativity grows towards the top right corner of the periodic table.

$\Delta \chi = |\chi_a - \chi_b|$ - difference between $e^-$-neg. of 2 atoms.

| Compound      | $\Delta \chi$ | Bond type          |
| ------------- | ------------- | ------------------ |
| $\ce{H2}$     | $0.0$         | non-polar covalent |
| $\ce{H-F}$    | $1.9$         | polar covalent     |
| $\ce{Na+Cl-}$ | $2.1$         | ionic              |
| $\ce{Fr+Cl-}$ | $3.3$         | ionic              |

| $\Delta \chi$ | Bond type                              |
| ------------- | -------------------------------------- |
| $< 0.5$       | non-polar covalent                     |
| $0.5 - 1.6$   | polar covalent                         |
| $1.6 - 2.0$   | depends, polar covalent for non-metals |
| $> 2.0$       | ionic                                  |

More polarized bond (greater $\Delta \chi$) → stronger bond.

| Bond       | $\Delta \chi$ | $\Delta E \space (kJ/mol)$, energy of the bond |
| ---------- | ------------- | ---------------------------------------------- |
| $\ce{O-O}$ | $0.0$         | $145$                                          |
| $\ce{O-N}$ | $0.5$         | $200$                                          |
| $\ce{O-C}$ | $1.0$         | $360$                                          |

| Compound   | Length ($pm$) | $\Delta E \space (kJ/mol)$ |
| ---------- | ------------- | -------------------------- |
| $\ce{HF}$  | $92$          | $565$                      |
| $\ce{HCl}$ | $127$         | $430$                      |
| $\ce{HBr}$ | $141$         | $360$                      |
| $\ce{HI}$  | $161$         | $245$                      |

**Bond order** - \# of bonds; $\frac{e^- \text{ in a bond}}{2}$.
Bonds of different bond order have different properties.

| Bond              | $\ce{C-C}$ | Aromatic | $\ce{C=C}$ | $\ce{C#C}$ |
| ----------------- | ---------- | -------- | ---------- | ---------- |
| Length            | longer     |          |            | shorter    |
| Strength          | weaker     |          |            | stronger   |
| Energy ($kJ/mol$) | 348        | 518      | 612        | 837        |

electronegativity reflects how effective nuclear charge affects atomic orbital energies (and through that molecular orbital energies)
==NOTE: what?

## Lewis structures

Structures for representing the bonds and shared electrons.

> Lewis structures assume we're dealing with covalent bonds! Whether the bond is covalent or not should be checked beforehand!

Rules:
1. **Count** total \# of valence $e^-$.
	$\ce{H2CO}, \space 1 \cdot 2 + 4 + 6 = 12 \space e^- \space (6 \text{ pairs})$
2. Put the **least $e^-$-neg. element in the center** (except $\ce{H}$).
	![[molecules/lewis-tutorial-step-2.png]]
3. **Bond** all atoms once.
	![[molecules/lewis-tutorial-step-3.png]]
4. Add $e^-$ **to terminal atoms** to make octets.
	Terminal atoms are only bonded to a single atom, so you can easily redistribute electron pairs from there. Central atoms are bonded to multiple atoms at one and it becomes confusing.
	![[molecules/lewis-tutorial-step-4.png]]
5. Give **leftover $e^-$ to the central atom**.
6. **Make octets** by using multiple bonds.
	Action: bonding, sharing $e^-$ pair w/ neighboring atom. Effect: removing 1 $e^-$ from one atom, giving 1 $e^-$ to another atom.
	![[molecules/lewis-tutorial-step-6.png]]
7. **Minimize charges**.
	Charge is the \# of $e^-$ relative to what this atom has normally. Count $1e^-$ per a bond.
	If possible, create more bonds to neutralize adjacent charges.
8. **No hypervalent 2nd row elements**.
	The 2nd shell of 2nd row elements can't sustain more than 8 $e^-$, but the next shells can, even if only 8 are needed for a stable configuration.
	![[molecules/valency-vs-charge.png]]

Dots - electrons.
Pairs of dots - electron pairs.
Instead of a pair of dots, lines can be used.

Simple examples:
![[molecules/lewis-examples-simple.png]]

**Octet rule** - an atom wants to have $8 \space e^-$ on its valence shell by donating/accepting/sharing $e^-$ w/ other atoms. Not applicable for 1st period.
**Hypervalent** - more than $8 \space e^-$ on the valence shell.
**Hypovalent** - less than $8 \space e^-$ pm the valence shell.

| Trends          | Elements             | Example                      |
| --------------- | -------------------- | ---------------------------- |
| **Hypervalent** | from 3rd row         | ![[molecules/SO2-lewis.png]] |
| **Hypovalent**  | $\ce{B, Al, Be, Mg}$ | ![[molecules/BH3-lewis.png]] |

> Positive charge on an $e^-$-neg. atom is always discouraged, negative charge - encouraged! If possible, make a central atom hypovalent instead.

![[molecules/hypo-vs-charge.png]]

> 2nd row - prioritize octet rule (can bear charge, can't go hypervalent).
> Others - prioritize minimizing charge (want to stay neutral, can go hypervalent).

![[SO2-vs-O3-lewis.png]]

Here $\ce{SO2}$ and $\ce{O3}$ are **isoelectronic** (same \# of $e^-$), but since $\ce{S}$ is in the 3rd row, it can be hypervalent in order to minimize charges.

#### Coordination numbers

Different atoms tend to form different \# of bonds and types of bonds.
**Coordination number** - \# of different atoms a given atom is bonded to.

| Coordination \# | $\ce{C}$                                         | $\ce{N}$                     | $\ce{O}$            | $\ce{F}$            | $\ce{B}$            |
| --------------- | ------------------------------------------------ | ---------------------------- | ------------------- | ------------------- | ------------------- |
| $1$             | -                                                | ![[N-1-triple.png]]          | ![[O-1-double.png]] | ![[F-1-single.png]] | -                   |
| $2$             | ![[C-2-double.png]] ![[C-1-triple-1-single.png]] | ![[N-1-double-1-single.png]] | ![[O-2-single.png]] | -                   | -                   |
| $3$             | ![[C-1-double-2-single.png]]                     | ![[N-3-single.png]]          | -                   | -                   | ![[B-3-single.png]] |
| $4$             | ![[C-4-single.png]]                              | ($\ce{N+}$?)                 | -                   | -                   | -                   |

#### Resonance structures

Sometimes there's no difference between atoms when assigning a multiple bond.
In this case, the $e^-$ pair is constantly jumping back and forth between the atoms.
**Resonance structures** - alternate possible Lewis structures for the same molecule.
Sometimes resonance structures appear in an equal proportion, sometimes one is favored.
In reality, the structures are superimposed.

![[molecules/resonance-O3.png]]
![[molecules/resonance-NO3.png]]

> In resonance structures, only $e^-$ move! Atoms stay in place!

## VSEPR

**Valence Shell Electron Pair Repulsion**
Since $e^-$ (and by extension $e^-$ pairs) are negatively charged, they repulse each other.
Repulsion arranges $e^-$ pairs in space to maximize their distance from one another.

**Electron domain** - volume of space occupied by an $e^-$ pair.

![[molecules/bond-shapes.png]]

The angles between the bonds are influenced by these bonds & the atoms around them.
A trigonal planar structure would ideally have bonds angled at $120 \degree$, since it's exactly $\frac{1}{3}$ of a circle (equal spacing), but for example in $\ce{H2CO}$ the double bond $\ce{C=O}$ is shorter than the $\ce{H-C}$ bonds + $\ce{O}$ is $e^-$-neg., so the $\ce{H-C}$ bonds end up being repelled more from the oxygen.

## VBT

**Valence Bond Theory**
Developed by Linus Pauling.
Visualizes bonds using the Schrödinger model.
Explains the geometry of bonds.

Bonds form by sharing $e^-$ between the orbitals of 2 atoms.
> For bonding to happen, atoms must have half-full orbital, so they can share/accept 1 $e^-$ per ($\sigma$) bond.

When atoms form a bond, the orbitals the $e^-$ are from merge together, creating a shared space.
The greater the overlap of atomic orbitals, the stronger the bond.

![[molecules/sigma-bond-formation.png]]
![[molecules/H2-bond-energy.png]]

**$\sigma$-bond** - cylindrically symmetrical, no nodal planes through the internuclear axis.
A $\sigma$-bond is formed from atomic orbitals that point to one another.
$\sigma$-bond - strong bond (a lot of overlap).

**$\pi$-bond** - has a single nodal plane going through the internuclear axis.
A $\pi$-bond is formed when 2 atomic orbitals are located parallel to each other, side-by-side, rather than directly pointing towards one another.
$\pi$-bond - weaker bold (significantly less overlap).

![[molecules/pi-bond-formation.png]]

If this logic is used alone, predictions don't always correspond to reality.

Wrong structure:
![[molecules/CH2-wrong.png]]

For atoms w/ more $e^-$, orbitals are hybridized.

**Hybridization** - mixing of different orbitals to produce a set of new, degenerate orbitals.
**Promotion** - transfer of $e^-$ to orbitals higher in energy.

Hybridization is caused by the interference among the orbitals' $e^-$ density.

![[molecules/hybrids.png]]

Hybridization explains the structure of molecules:
Imagine that [[#VSEPR]] applies to the hybridized orbitals separately. In this case, if there are 4 equivalent $sp^3$ hybrids, thus a tetrahedral structure. Or there could be 3 equivalent $sp^2$ hybrids, thus a trigonal planar structure.

| $e^-$ domains | Hybridization | Structure       | \# of $\sigma$-bonds | \# of $\pi$ bonds |
| ------------- | ------------- | --------------- | -------------------- | ----------------- |
| $4$           | $sp^3$        | Tetrahedral     | 4                    | 0                 |
| $3$           | $sp^2$        | Trigonal planar | 3                    | 1                 |
| $2$           | $sp$          | Linear          | 2                    | 2                 |

> Hybridization applies to both atoms in a bond!

![[molecules/H2CO-hybridization.png]]

Since $\sigma$-bonds are cylindrically symmetrical → they can rotate.
$\pi$-bonds are not cylindrically symmetrical → they are rigid, they cannot rotate.
This explains stereoisomers (cis- and trans-isomers).

![[molecules/rotation-of-bonds.png]]

$\pi$-bonds are overall rare among elements, since $p$-orbitals can't keep up w/ the increasing atomic radius → less and less overlap → weaker and weaker bond.

VBT can't explain:
- Phases (signs) of orbitals
- Diamagnetic/paramagnetic molecules
	**Diamagnetic** - no unpaired $e^-$, repulsed by magnets.
	**Paramagnetic** - unpaired $e^-$, weakly attracted by magnets.
- Spectroscopy

## MO Theory
**Molecular Orbital Theory**

Best model so far.
Treats $e^-$ as fully delocalized and smeared out across the whole molecule.

In MO, atomic orbitals are used to create molecular orbitals.

Important concepts:
- **LCAO (Linear Combination of Atomic Orbitals)** - $ax+by$, AOs are combined in different proportions.
- \# of AOs = \# of MOs - no orbitals are lost.

The wavefunctions of 2 AOs can combine in 2 ways:
- Constructive interference (addition) - $\Psi_{\ce{H}1s} + \Psi_{\ce{H}1s}$
	![[molecules/constructive-interference.png]]
- Destructive interference (subtraction) - $\Psi_{\ce{H}1s} - \Psi_{\ce{H}1s}$
	![[molecules/destructive-interference.png]]

> Subtraction can be thought of as addition of perfectly out-of-phase waves.
> $\Psi_{\ce{H}1s} - \Psi_{\ce{H}1s} = \Psi_{\ce{H}1s} + (-\Psi_{\ce{H}1s})$

Example: MO diagram of $\ce{H2}$
1. Combine AOs. Determine the energy levels of the MOs. The bonding MO must be below the lower AO (to justify bonding) and the anti-bonding MO must be above the higher AO. Keep in mind: the difference in energy $\Delta E = |\sigma_{\text{orbital}} - (\text{lower AO})| = |\sigma_{\text{orbital}}^{*} - (\text{higher AO})|$.
2. Take the $e^-$ from the AOs and distribute them on the MOs according to Aufbau.
3. Compute the bond order.
![[molecules/H2-bonding-antibonding.png]]

$\sigma_{1s}$ - bonding orbital, ($\sigma$ like in [[#VBT]])
$\sigma_{1s}^*$ - anti-bonding orbital
$\text{Bond order} = \frac{(\text{\# of bonding } e^-) - (\text{\# of antibonding } e^-)}{2}$

**Bonding MOs** create bonding - lower in energy, 2 nuclei are acting on $e^-$.
**Anti-bonding MOs** inhibit bonding - higher in energy, $e^-$ are far from the nuclei.
**Non-bonding AOs** - do not mix w/ any AOs of another atom. Usually core orbitals, can be some lower valence orbitals as well.
**LUMO** - Lowest Unoccupied Molecular Orbital.
**HOMO** - Highest Occupied Molecular Orbital.

#### Examples of molecular orbitals

![[molecules/He2-MO.png]]
Here the bond order is 0 - there is no bond between 2 neutral $\ce{He}$.

![[molecules/He2(^+1)-MO.png]]
Here the bond order is 0.5 - there is a slight attraction between $\ce{He}$ and $\ce{He+}$, but they will not stay together for long.

![[molecules/He2(^-1)-MO.png]]
He we end up with the same bond order as in the previous case.

![[molecules/Li2-MO.png]]
Here the bond order is 1. There is a bond in $\ce{Li2}$.

> Key: core $e^-$ cancel themselves out. Only the valence shell $e^-$ are important when making MO diagrams.

> Key: just as AOs go down in energy for every next element in the periodic table, the MOs get closer and closer to the AOs they were made from. This is because the atomic radius grows → the distance between AOs grows → the overlap between AOs decreases → AOs loose connection.

![[molecules/F2-MO.png]]
From here it is apparent that $\ce{F2}$ has a bond and will exist as a molecule. The MOs of the molecule can be written down as $\ce{F2}: \sigma_{2s}^2 \space \sigma_{2s}^{*2} \space \sigma_{2p}^2 \space [\pi_{2px}^2 \space \pi_{2py}^2] \space [\pi_{2px}^{*2} \space \pi_{2py}^{*2}]$

![[molecules/HF-MO.png]]
Here the molecule is diatomic & polar. $\ce{F} \space 2p_z$ is able to bond w/ $\ce{H} \space 1s$. All the other orbitals of $\ce{F}$ ($2s, 2p_x, 2p_y$) are non-bonding - they are too far away from $\ce{H} \space 1s$. Note, the energy difference between $\ce{H} \space 1s$ & $\sigma_{sp}^*$ is the same as between $\ce{F} \space 2p$ & $\sigma_{2p}$.
An AO makes a **"larger contribution"** to a MO, if it is closer to a MO than the AO of another atom. Here $\ce{F} \space 2p_z$ makes a larger contribution to $\sigma_{2p}$ than $\ce{H} \space 1s$ and $\ce{H} \space 1s$ makes a larger contribution to $\sigma_{2p}^*$ than $\ce{F} \space 2p_z$.

#### Variants of molecular orbitals

![[molecules/MO-variants.png]]

- Both $\pi_{px}$ and $\pi_{py}$ MOs form in the same way.
- $p_x$ and $p_y$ AOs **cannot** form a $\pi_{pxpy}$ MO, since they are perpendicular and overlap between them is almost nonexistent.

#### Orbital mixing

Happens for $\ce{B, C, N}$.
If orbitals have the same symmetry & are close in energy.

![[molecules/sigma-pi-crossover.png]]

$2s$ and $2p$ are close in energy.
$\sigma$-$\pi$ crossover - when the $\sigma$ MO happens to be higher in energy than the $\pi$ MOs.

#### Diamagnetism & paramagnetism

MO Theory, unlike [[#VBT]], can explain diamagnetism and paramagnetism.

**Diamagnetic** - no unpaired $e^-$, repulsed by magnets.
**Paramagnetic** - unpaired $e^-$, weakly attracted by magnets.

| Diamagnetic - $\ce{N2}$ | Paramagnetic - $\ce{O2}$ |
| ----------------------- | ------------------------ |
| ![[N2-MO.png]]          | ![[O2-MO.png]]           |

#### Drawbacks

> MO Theory still assumes the bond is covalent, still need to use electronegativity to check.

> In MO Theory, every $e^-$ in every atom contributes to every single bond to some extend, which is not practical. e are fully delocalized.


