
Resonance stabilization makes benzene very stable.
All 6 bonds in benzene are **equal in length** - all 6 bonds are equal.
$e^-$ are **equally spread** among the 6 carbon atoms.

Represented vs real structure:
```smiles
C1=CC=CC=C1
c1ccccc1
```

> It's better to represent benzene rings w/ double bonds because that way it is easier to count the \# of bonds.
> The aromatic bonds of benzene count as 2 bonds!

## Aromaticity

Criteria:
- **Cyclic system**
- **Planar molecule (sp2)** - to make conjugation possible; one p orbital is empty, participating in the aromatic system.
- **Conjugation** - for resonance & stability.
- **Hückels rule** - for stability.

**Hückel's rule:**
Stable conjugated cyclic systems have $(4n+2) \space e^-$.

| Compound                    | Structure                                                             | $\pi \space e^-$ | Aromatic? |
| --------------------------- | --------------------------------------------------------------------- | ---------------- | --------- |
| cyclobutadiene              | ![[_media/Aromatic compounds/aromatic-cyclobutadiene.png]]            | 4                | ✗         |
| "cyclohexatriene" (benzene) | ![[_media/Aromatic compounds/aromatics-cyclohexatriene.png]]          | 6                | ✓         |
| cyclooctatetraene           | ![[_media/Aromatic compounds/aromatics-cyclooctatetraene.png]]        | 8                | ✗         |
| cyclooctatetraenyl anion    | ![[_media/Aromatic compounds/aromatics-cyclooctatetraenyl-anion.png]] | 10               | ✓         |

In cyclopentadiene, for example, the hydrogens on the $sp^3$ hybridized carbon are acidic, because donating a proton would leave cyclopentadiene with a lone $e^-$ pair, making it follow Hückel's rule.

#### Heteroaromatics

Aromatic compounds with one or more carbons in the ring replaced by other atoms. Usually $\ce{O, N, S}$.

Pyridine, furan, purrole:
```smiles
C1=CN=CC=C1
C1=CC=CO1
C1=CC=CN1
```

In heteroaromatics, the lone $e^-$ pairs on the heteroatoms contribute to aromaticity.
For example, pyrrole is aromatic by Hückel's rule: $2 \cdot 2 = 4 \space e^-$ from the double bonds + $2 \space e^-$ from $\ce{N}$'s $p$ orbital. This is the only lone $e^-$ pair on the $\ce{N}$ atom, meaning protonating pyrrole even more would remove that pair and destroy the molecule's aromaticity.

## Reactions

Aromatic compounds are more stable than usual alkenes, so the reactions are different.
**Electrophiles** often need to be activated with a catalyst before the reaction.
The reaction intermediate formed is not aromatic any more, but as a final step, the **aromatic ring is regenerated**.

Rate-determining step: the loss of aromaticity; requires a lot of energy.

#### Activating and deactivating groups

The substituents on the benzene ring affect the outcome of the reactions.

**Summary:**

| Kind       | Activating                 | Deactivating                  |
| ---------- | -------------------------- | ----------------------------- |
| **Nature** | $e^-$ rich; $e^-$ donating | $e^-$ poor; $e^-$ withdrawing |
| **In EAS** | ortho-para directing       | meta-directing                |
| **In NAS** | meta-directing             | ortho-para directing          |
| **Rate**   | Faster                     | Slower                        |

| Kind         | Activating                      | Deactivating                      |
| ------------ | ------------------------------- | --------------------------------- |
| **Strong**   | $\ce{-NH2, -OH}$ (+derivatives) | $\ce{-NO2, -NR3+, -CF3}$          |
| **Moderate** | $\ce{-NH(=O)R, -OOR}$           | $\ce{-COOH, -COH}$ (+derivatives) |
| **Weak**     | $\ce{-R, -Ph, -X}$              | $\ce{-CN, -SO3H}$                 |

Ortho-para directors (activating groups) are such because of:
- **Resonance** - they might have lone $e^-$ pairs that can be used in the resonance structures during the course of reactions
- **Hyperconjugation** - alkyl groups can stabilize the carbocations that are formed in the resonance structures of the reaction intermediate.

Meta directors (deactivating groups) are such because:
- **Resonance** - in the resonance structures of the meta substitution, the positive charge misses the carbon attached to the group, making the transition state less unstable. In ortho/para substitution the charge would be right next to an $e^-$ withdrawing group, which is unstable.

> Meta directors do not make the meta substitution more stable, they only make it **less unstable**.

Usually, the stronger **activating group** determines the overall outcome.

> Don't forget about steric effects when deciding which position is more likely to be substituted.

> Halogens especially prioritize para substitution because of the steric effects.

https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Map%3A_Organic_Chemistry_(Wade)_Complete_and_Semesters_I_and_II/Map%3A_Organic_Chemistry_(Wade)/18%3A_Reactions_of_Aromatic_Compounds
https://www.organicchemistrytutor.com/topic/directing-effects-in-electrophilic-aromatic-substitution-reactions/

## Electrophilic aromatic substitution

#### Halogenation

**Reagents:**
- Aromatic compound
- Halogen ($\ce{X-X}$)

**Requirements:**
- Lewis acid catalyst (to activate the halogen)

![[_media/Aromatic compounds/aromatics-halogenation.png]]

Usual Lewis acids:
- $\ce{Cl}$ → $\ce{AlCl3, FeCl3}$
- $\ce{Br}$ → $\ce{FeBr3}$

$2 \space \ce{Br}$ atoms are not added because the ring would loose aromaticity.

The intermediate has a single $sp^3$ hybridized carbon, but in the product all 6 are $sp^2$ hybridized once again.

#### Nitration

**Reagents:**
- Aromatic compound
- $\ce{HNO3}$ (concentrated)

**Requirements:**
- $\ce{H2SO4}$ (concentrated)

Sulfuric acid is used to increase the concentration of the $\ce{NO2+}$ ion (electrophile). Other acids may also be used.

![[_media/Aromatic compounds/aromatics-nitration.png]]

#### Sulfonation

Reagents:
- Aromatic compound
- Fuming $\ce{H2SO4}$ ($\ce{H2SO4 \text{(conc.)} + SO3}$)

Requirements:
- Acid catalyst (covered by $\ce{H2SO4}$)

It is an equilibrium reaction.
Sulfonation → concentrated sulfuric acid.
Desulfonation → dilute sulfuric acid.

![[_media/Aromatic compounds/aromatics-sulfonation.png]]

#### Friedel-Crafts alkylation

**Reagents:**
- Aromatic compound
- Alkyl halide/Alcohol

**Requirements:**
- Lewis acid (usually $\ce{AlCl3/BF3/HF}$)

![[_media/Aromatic compounds/aromatics-friedel-craft-alkylation.png]]


Even though in the mechanism the formation of a carbocation is shown, the primary alkyls can also react, but instead of forming a carbocation, they form a complex with the Lewis acid that reacts identically to the carbocation.

> Subject to rearrangements.

#### Friedel-Crafts acylation

**Reagents:**
- Aromatic compound
- Acid halide (usually acid chloride)

**Requirements:**
- Lewis acid (usually $\ce{AlCl3}$)

![[_media/Aromatic compounds/aromatics-friedel-craft-acylation.png]]

> Since the formation of a carbocation is required here, $\ce{CHOCl}$ **is not suitable for the reaction**!
> That is because the primary carbocations are unstable.




the substituents influence where the next substituents will be added

the ratios of the products are also influenced by the steric effect


amine - activating; lone pair
protonated amine - deactivating ; no lone pairs

phenyls and anilines and reactive on their own - don't need an additional lewis acid to react


## Nucleophilic aromatic substitution

Phenols are better acids than alkyl alcohols, because of the resonance stabilization.

==ether from phenol + MsOMe

==hydrolysis of ethers

Ar-O bond is never broken

nucl. ar. subs. - only when the aromatic compound carries a good leaving group and is activated for the reaction (ortho/para for e withdrawing groups (meta-directing))


==triple bonds
need a very strong base for that!