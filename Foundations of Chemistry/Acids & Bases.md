Widely used definition:
Brønsted-Lowry:
- **acid** - proton donor
- **base** - proton acceptor

Lewis:
- **acid** - $e^-$ pair acceptor
- **base** - $e^-$ pair donor

## Acids

**Monoprotic** - acid releases 1 proton.
**Polyprotic** - acid releases multiple protons.

In inorganic acids, the acidic hydrogen is written first ($\ce{H2SO4}$), in organic acids, in carboxyl groups ($\ce{CH3COOH}$).

**Strong** - completely deprotonated (dissociated) in a solution.
**Weak** - incompletely deprotonated (dissociated) in a solution.

Strong acids: $\ce{HCl, \space HBr \space HI, \space HNO3, \space HClO4, \space HClO3, \space H2SO4} \space \text{(first proton)}$

All carboxylic acids are weak in water.

Some acids are of moderate strength: $\ce{H3PO4, \space HF}$

**Lewis acid** - substance that has unoccupied orbitals that can be used to accept a bond.

## Acidity constant

$K_a$ - acid dissociation constant, how deprotonated the acid gets.
$\ce{HA (aq) + H2O (l) \rightleftharpoons H3O+ (aq) + A- (aq)}$
$K_a = \frac{a_{\ce{H3O+}} \cdot a_{\ce{A-}}}{a_{\ce{HA}} \cdot a_{\ce{H2O}}} = \frac{\ce{[H+][A-]}}{\ce{[HA]}} \text{ for an acid } \ce{HA} \text{ in water}$

$\ce{[X]}$ - molar concentration of $\ce{X}$ at equilibrium.

High $K_a$ → stronger acid.
Low $K_a$ → weaker acid.

---
$pK_a$ - negative logarithm of $K_a$.
Easier to interpret (smaller values).
Used to determine if the reaction takes place.
**How basic the acid is in water**.
$pK_a = -log(K_a) = -log(\frac{\ce{[H+][A-]}}{\ce{[HA]}}) = log(\frac{\ce{[HA]}}{\ce{[H+][A-]}})$

High $pK_a$ - weaker acid
Low $pK_a$ - stronger acid
![[pKa table.png]]
$\Delta pK_a = pK_a(\text{resulting acid}) - pK_a(\text{reactant acid})$
If $\Delta pK_a > 10$ → generally irreversible reaction, if $\leq 10$ → equilibrium.
If $\Delta pK_a > 0$ → equilibrium lies to the right side, if $< 0$ → to the left side **OR**
The side that has an acid /w higher $pK_a$ is favored.
[Further reading](https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_(Morsch_et_al.)/02%3A_Polar_Covalent_Bonds_Acids_and_Bases/2.08%3A_Predicting_Acid-Base_Reactions_from_pKa_Values)

---
> When construction an ICE table for deprotonation of a weak acid, the change in the concentration of the acid molecules $x$ can be neglected, if $\frac{\ce{[HA]}}{K_a} \geq 400, \space \ce{HA} - x \approx \ce{[HA]}$.
> This is because that condition shows the majority of the acid molecules did not deprotonate and the larger the ratio is, the less significant the change in the concentration becomes.

#### Acid constant examples

Ex. 1
$\ce{HCl \rightleftharpoons H+ + Cl-}$ ($\ce{HCl + H2O \rightleftharpoons H3O+ + Cl-}$)
Reactant acid: $\ce{HCl}$, Resulting acid: $\ce{H+ (H3O+)}$
$\ce{HCl}$ - strong acid, low $pK_a \space (-7)$.
$\ce{H+ (H3O+)}$ - weaker acid, higher $pK_a \space (-1.7)$.
$\Delta pK_a = (-1.7) - (-7) = 5.3 > 0 \Rightarrow$ reaction equilibrium goes to the right.

Ex. 2
$\ce{CH3OH \rightleftharpoons H+ + CH3O-}$ ($\ce{CH3OH + H2O \rightleftharpoons H3O+ + CH3O-}$)
Reactant acid: $\ce{CH3OH}$, Resulting acid: $\ce{H+ (H3O+)}$
$\ce{CH3OH}$ - weak acid, high $pK_a \space (15.5)$.
$\ce{H+ (H3O+)}$ - stronger acid, lower $pK_a \space (-1.7)$.
$\Delta pK_a = (-1.7) - 15.5 = -17.2 < 0 \Rightarrow$ reaction equilibrium goes to the left.

Ex. 3
$\ce{HCl + NH3 -> Cl- + NH4+}$
Reactant acid: $\ce{HCl}$, Resulting acid: $\ce{NH4+}$
$pK_a(\ce{HCl}) = -6$
$pK_a(\ce{NH4+}) = 10$
$\Delta pK_a = 10 - (-6) = 16 > 10 > 0 \Rightarrow$ complete reaction (right side favored).

> When deciding the equilibrium, only the ions that are actually participating in the reaction make a difference! All the observer ions don't matter! Don't forget to decompose the compounds into ions when determining which acid/base is stronger as well!

Ex. 4
$\ce{NaCN + Na2HPO4 \rightleftharpoons Na3PO4 + HCN}$
Sodium does nothing here: $\ce{CN- + HPO4^{2-} \leftrightharpoons PO4^{3-} + HCN}$
Reactant acid: $\ce{HPO4^{2-}}$, Resulting acid: $\ce{HCN}$
$pK_a(\ce{HPO4^{2-}}) = 12.3$
$pK_a(\ce{HCN}) = 9.3$
$\Delta pK_a = 9.3 - 12.3 = -3 < 0 \Rightarrow$ equilibrium goes to the left.

## Bases

**Strong** - completely dissociated in a solution.
**Weak** - incompletely dissociated in a solution.

Strong bases: $\text{Group 1 hydroxides, Group 1 and 2 oxides, } \ce{Ca(OH)2, \space Sr(OH)2, \space Ba(OH)2}$

**All amines are weak** in water.

Hydroxide ions are strong bases themselves:
$\ce{H2O (l) + OH- (aq) \rightleftharpoons OH- (aq) + H2O (l)}$

**Lewis base** - substance that has free $e^-$ pairs that are not already used in bonding.

## Basicity constant

$K_b$ - base dissociation constant, how much protons the base accepts from water.
$\ce{B (aq) + H2O (l) \rightleftharpoons HB+ (aq) + OH- (aq)}$
$K_b = \frac{a_{\ce{HB+}} \cdot a_{\ce{OH-}}}{a_{\ce{B}} \cdot a_{\ce{H2O}}} = \frac{\ce{[HB+][OH-]}}{\ce{[B]}}$

Larger $K_b$ → stronger base.
Smaller $K_b$ → weaker base.

$pK_b = -log(K_b)$

Larger $pK_b$ → weaker base.
Smaller $pK_b$ → stronger base.

## Autoprotolysis of water

**Autoprotolysis/autoionization** - amphiprotic compound protonating itself.
Water molecules and hydroxide ions interchange, even in pure water.
$\ce{H2O (l) + H2O (l) \rightleftharpoons H3O+ (aq) + OH- (aq)}$

$K_w = \frac{\ce{[H3O+][OH-]}}{1 \cdot 1} = \ce{[H3O+][OH-]} = 10^{-7} \cdot 10^{-7} = 10^{-14} \space (\text{at } 25 \degree C)$

For a conjugate acid-base pair:
$K_a(\text{acid}) \cdot K_b(\text{base}) = K_w$
$pK_a(\text{acid}) + pK_b(\text{base}) = pK_w$

Autoprotolysis must be taken into account when working with very dilute solutions of acids & bases ($c < 10^{-6} \space M$). Otherwise, its effect is negligible.

> Do not remember these formulas! Learn to derive them!

**Strong acids & bases**:
$$
\begin{flalign}
&\textcolor{grey}{\ce{HCl (aq) + H2O (l) -> H3O+ (aq) + Cl- (aq), H2O (l) + H2O (l) -> H3O+ (aq) + OH- (aq)}} \\
&\textcolor{grey}{\text{Species in the solution: } \ce{Cl-, H3O+, OH-}} \\
&\textcolor{grey}{\bullet \space \ce{[H3O+]} = \ce{[OH-]} + \ce{Cl-} \text{ - charge balance}} \\
&\textcolor{grey}{\bullet \space \ce{[HCl]}_{\text{initial}} = \ce{[Cl-]} \text{ - material balance}} \\
&\textcolor{grey}{\bullet \space K_w = \ce{[H3O+][OH-]} \text{ - autoprotolysis}} \\
&\textcolor{grey}{K_w = \ce{[H3O+]}(\ce{H3O+} - \ce{[HCl]}_{\text{initial}})} \\
&\ce{[H3O+]}^2 - \ce{[HCl]}_{\text{initial}}\ce{[H3O+]} - K_w = 0 \text{ - quadratic in terms of } \ce{[H3O+]}
&\end{flalign}
$$
A similar chain of logic can be followed for very dilute bases.

**Weak acids & bases**:
$$
\begin{flalign}
&\textcolor{grey}{\ce{HA (aq) + H2O (l) \rightleftharpoons A- (aq) + H3O+ (aq), 2 H2O (l) \rightleftharpoons H3O+ (aq) + OH- (aq)}} \\
&\textcolor{grey}{\text{Species in the solution: } \ce{HA, A-, H3O+, OH-}} \\
&\textcolor{grey}{\bullet \space \ce{[H3O+]} = \ce{[OH-]} + \ce{[A-]}} \\
&\textcolor{grey}{\bullet \space \ce{[HA]_{\text{initial}}} = \ce{[HA]} + \ce{[A-]}} \\
&\textcolor{grey}{\bullet \space K_w = \ce{[H3O+][OH-]}} \\
&\textcolor{grey}{\bullet \space K_a = \frac{\ce{[H3O+][A-]}}{\ce{[HA]}}} \\
&\textcolor{grey}{\ce{[A-]} = \ce{[H3O+]} - \frac{K_w}{\ce{H3O+}}} \\
&\textcolor{grey}{\ce{[HA]} = \ce{[HA]}_{\text{initial}} - (\ce{[H3O+]} - \frac{K_w}{\ce{H3O+}})} \\
&\text{Exact expression:} \\
&K_a = \frac{\ce{[H3O+]}(\ce{[H3O+]} - \frac{K_w}{\ce{H3O+}})}
{\ce{[HA]}_{\text{initial}} - \ce{[H3O+]} + \frac{K_w}{\ce{H3O+}}} \\
&\text{Simplified expression with some negligible terms omitted:} \\
&\ce{[H3O+]}^3 + K_a\ce{[H3O+]}^2 - (K_w + K_a\ce{[HA]}_{\text{initial}})\ce{[H3O+]} - K_aK_w = 0
&\end{flalign}
$$

## Conjugated Acids & Bases

Every acid has a **conjugated base**, every base has a **conjugated acid**.
Strong acid/base → weak conjugated base/acid.
Weak acid/base → **moderate** conjugated base/acid.

| Acid           | Conjugated Base | Base          | Conjugated Acid |
| -------------- | --------------- | ------------- | --------------- |
| $\ce{HCl}$     | $\ce{Cl-}$      | $\ce{NaOH}$   | $\ce{Na+}$      |
| $\ce{CH3COOH}$ | $\ce{CH3COO-}$  | $\ce{CH3NH2}$ | $\ce{CH3NH3+}$  |
A lot of the times, a compound can act both as an acid or a base, depending on the circumstances.
Thus, a lot of compounds have both a conjugated acid and a conjugated base at the same time.
**Amphiprotic compound** - compound that can act as both an acid & base (type of amphoteric).

| Compound      | Conjugated Acid | Conjugated Base  |
| ------------- | --------------- | ---------------- |
| $\ce{H2O}$    | $\ce{H3O+}$     | $\ce{OH-}$       |
| $\ce{NH3}$    | $\ce{NH4+}$     | $\ce{NH2-}$      |
| $\ce{H2PO4-}$ | $\ce{H3PO4}$    | $\ce{HPO4^{2-}}$ |

> In general, when an acid reacts /w a base, the weakest acid & base are formed.
> $\ce{HCl + H2O -> H3O+ + Cl-}$

## pH

$pH = -log(\ce{[H+]})$
$pOH = -log([\ce{OH-}])$
$pH + pOH = 14$

$$
\begin{flalign}
&\textcolor{grey}{K_a = \frac{\ce{[H+][A-]}}{\ce{[HA]}}} \\
&\textcolor{grey}{log(K_a) = log(\frac{\ce{[H+][A-]}}{\ce{[HA]}}) = log(\ce{[H+]}) + log(\frac{\ce{[A-]}}{\ce{[HA]}})} \\
&\textcolor{grey}{-log(K_a) = -log(\ce{[H+]}) - log(\frac{\ce{[A-]}}{\ce{[HA]}})} \\
&\textcolor{grey}{pK_a = pH - log(\frac{\ce{[A-]}}{\ce{[HA]}})} \\
&pH = pK_a + log(\frac{\ce{[A-]}}{\ce{[HA]}})
&\end{flalign}
$$

For strong acids, $pH$ is calculated directly: $pH = -log(\ce{[H3O+]})$.
For weak acids, to calculate $pH$ the concentration of $\ce{OH-}$ must be found using $K_a$.

Based on the first 2 examples, a rule can be formulated:
$pK_a < pH$ → deprotonation in water
$pK_a > pH$ → protonation in water

## Strength of acids

The **strength** of an acid is determined by the **polarity** of the $\ce{O-H}$ bond.
The more polar the bond, the stronger the acid, since $\ce{H}$ can escape more easily.

The polarity can be achieved through:
- The **size of the anion** determining the strength of the bond:
 ```smiles
F
Cl
Br
I
```
- The **electronegativity** of the central atom:
```smiles
ClO[H]
BrO[H]
IO[H]
```
- The \# of $\ce{O}$ atoms in oxoacids:
```smiles
ClO[H]
O=ClO[H]
O=Cl(=O)O[H]
O=Cl(=O)(=O)O[H]
```
- The electronegative **functional groups** in carboxylic acids:
```smiles
OCCC
OC(=O)CC
OC(=O)CCCl
OC(=O)CC(Cl)(Cl)(Cl)
```

## Lewis acids and bases

The Lewis definition allows to classify even more substances as acids & bases.

Lewis:
- **acid** - $e^-$ pair acceptor
- **base** - $e^-$ pair donor

**Lewis acid-base adduct** - compound formed in the reaction between a Lewis acid & base.

## Polyprotic acids

**Polyprotic acid** - Brønsted acid that can donate multiple protons. $\ce{H2SO4, H2CO3, H3PO4}$
**Polyprotic base** - Brønsted base that can accept multiple protons. $\ce{SO4^{2-}, CO3^{2-}, PO4^{3-}}$

Polyprotic acids are deprotonated one proton at a time:
$\ce{H2CO3 (aq) + H2O (l) \leftrightharpoons HCO3- (aq) + H3O+ (aq)}, \space K_{a1} = 4.3 \cdot 10^{-7}$
$\ce{HCO- (aq) + H2O (l) \leftrightharpoons CO3^{2-} (aq) + H3O+ (aq)}, \space K_{a1} = 5.6 \cdot 10^{-11}$

> Conjugate bases of polyprotic acids are amphiprotic.

During deprotonation, the acidity of the acid involved is decreasing fast.
It is hard to separate a positively charged proton from a negatively charged anion.
That means that the majority of the $pH$ effect comes from the first deprotonation.

Only first dissociation can be considered, if $\frac{K_{a1}}{K_{a2}} \geq 1000$

[Further reading: Dissociation of polyprotic acids](https://staging.physicsclassroom.com/Chemistry-Tutorial/Solution-Equilibria/Dissociation-of-Polyprotic-Acids)

When determining the $pH$ of the solution, the deprotonations need to also happen sequentially. In the ICE table, the equilibrium concentrations from the previous step carry over as the initial concentrations of the next step.

#### Fractional composition

At a particular $pH$ there's a particular \# of different species of polyprotic acids in the solution.
High $pH$ → fully deprotonated species dominates; Low $pH$ → fully protonated species dominates.

For a diprotic acid:
$$
\begin{flalign}
&\textcolor{grey}{\ce{H2A (aq) + H2O (l) \rightleftharpoons HA- (aq) + H3O+ (aq)}, \space K_{a1}} \\
&\textcolor{grey}{\ce{HA- (aq) + H2O (l) \rightleftharpoons A^{2-} (aq) + H3O+ (aq)}, \space K_{a2}} \\
&\textcolor{grey}{\text{Let } f(\ce{X}) \text{ be the fraction the species } \ce{X} \text{ makes up from all the species combined:}} \\
&\textcolor{grey}{f(\ce{X}) = \frac{\ce{[X]}}{\ce{[H2A]} + \ce{HA-} + \ce{A^{2-}}}, \space X \in \{ \ce{H2A, HA-, A^{2-}} \}} \\
&\textcolor{grey}{f(\ce{X}) = \frac{\frac{\ce{[X]}}{\ce{[HA-]}}}{\frac{\ce{[H2A]}}{\ce{[HA-]}} + 1 + \frac{\ce{[A^{2-}]}}{\ce{[HA-]}}}} \\
&\textcolor{grey}{K_{a1} = \frac{\ce{[HA-][H3O+]}}{\ce{[H2A]}} \Rightarrow \frac{\ce{H2A}}{\ce{HA-}} = \frac{\ce{[H3O+]}}{K_{a1}}, \space K_{a2} = \frac{\ce{[A^{2-}][H3O+]}}{\ce{[HA-]}} \Rightarrow \frac{\ce{A^{2-}}}{\ce{HA-}} = \frac{K_{a2}}{\ce{[H3O+]}}} \\
&\textcolor{grey}{f(\ce{X}) = \frac{\frac{\ce{[X]}}{\ce{[HA-]}}}{\frac{\ce{[H3O+]}}{K_{a1}} + 1 + \frac{K_{a2}}{\ce{[H3O+]}}}} \\
&\textcolor{grey}{f(\ce{X}) = \frac{\frac{\ce{[X]}}{\ce{[HA-]}}\ce{[H3O+]}K_{a1}}{\ce{[H3O+]}^2 + \ce{[H3O+]}K_{a1} + K_{a1}K_{a2}}} \\
&f(\ce{H2A}) = \frac{\ce{[H3O+]}^2}{H}, \space f(\ce{HA-}) = \frac{\ce{[H3O+]}K_{a1}}{H}, \space f(\ce{A^{2-}}) = \frac{K_{a1}K_{a2}}{H} \\
&H = \ce{[H3O+]}^2 + \ce{[H3O+]}K_{a1} + K_{a1}K_{a2}
&\end{flalign}
$$

## pH of salts

Salts consist of ions. Ions are themselves acids & bases, meaning depending on the kind of ions, the $pH$ of a salt solution may vary.
The effects of the both ions need to be considered when assessing the $pH$ of a solution.

| Character | Cations                                    | Examples                                       |
| --------- | ------------------------------------------ | ---------------------------------------------- |
| Acidic    | Conjugate acids of weak bases              | $\ce{NH4+, CH3NH3+, ...}$                      |
| Acidic    | Highly charged metal cations (Lewis acids) | $\ce{Fe^{2+}, Fe^{3+}, Al^{3+}, Cu^{2+}, ...}$ |
| Neutral   | Group 1, 2 cations + cations /w charge $+$ | $\ce{Na+, Mg^{2+}, Ca^{2+}, Ag+}$              |
| Basic     | -                                          | -                                              |
Some cations are considered neutral because they are large or have too little charge to polarize the $\ce{O-H}$ bond in the surrounding water enough for the $\ce{H}$ to escape.

| Character | Anions                          | Examples                                 |
| --------- | ------------------------------- | ---------------------------------------- |
| Acidic    | Very few                        | $\ce{HSO4-, H2PO4-}$                     |
| Neutral   | Conjugate bases of strong acids | $\ce{Cl-, Br-, NO3-, ClO4-}$             |
| Basic     | Conjugate bases of weak acids   | $\ce{F-, O^{2-}, OH-, PO4^{3-}, R-COO-}$ |

For salts of polyprotic acids:
$\ce{[H2A]} >> K_{a1} \wedge \ce{[H2A]} >> \frac{K_w}{K_{a2}} \Rightarrow pH \approx 0.5(pK_{a1} + pK_{a2})$

## Oxides

#### Acidic oxides

**Acidic oxide** - oxide that reacts /w water to form a  solution of Brønsted acid.
Oxides of non-metals.
Molecular compounds.
Act as Lewis acids.

$\ce{CO2 (g) + H2O (l) \leftrightharpoons H2CO3 (aq)}$

React /w bases/basic oxides in a neutralization reaction:
$\ce{NaOH (aq) + CO2 (g) -> NaHCO3 (aq)}$

#### Basic oxides

**Basic oxide** - oxide that reacts /w water to form a solution of Brønsted base.
Oxides of metals.
Ionic compounds.
Act as Lewis bases.

$\ce{Na2O (g) + H2O (l) -> 2 NaOH (aq)}$

React /w acids/acidic oxides in a neutralization reaction:
$\ce{Na2O (s) + H2SO4 (aq) -> Na2SO4 (aq) + H2O (l)}$

#### Amphoteric oxides

**Amphoteric compound** - compound that can act as both an acid or a base.

Oxides of metals on the diagonal between metals an non-metals + some $d$-block elements.
$\ce{Al2O3, PbO, In2O3, ZnO, ...}$

$\ce{Al2O3 (s) + 6 HCl (aq) -> 2 AlCl3 (aq) + H2O (l)}$
$\ce{2 NaOH (aq) + Al2O3 (s) + 3 H2O (l) -> 2 Na[Al(OH)4] (aq)} \text{ - sodium aluminate}$

## History

Initially:
- acid - sour taste
- base - soapy feel

Svante Arrhenius's (Swedish) version (1884):
- acid - compound that reacts /w water to form $\ce{H+}$
- base - compound that reacts /w water to form $\ce{OH-}$

Ex.
- $\ce{HCl}$ - Arrhenius acid, $\ce{HCl + H2O -> H+ + Cl- + H2O}$
- $\ce{CH4}$ - **not** Arrhenius acid, $\ce{CH4 + H2O -/>}$
- $\ce{NaOH}$ - Arrhenius base, $\ce{NaOH + H2O -> Na+ + OH- + H2O}$
- $\ce{NH3}$ - Arrhenius base, $\ce{NH3 + H2O -> NH4+ + OH-}$
- $\ce{Na}$ - **not** Arrhenius base, not a compound

Thomas Lowry (English) & Johannes Brønsted (Danish) version (1923):
- acid - proton donor
- base - proton acceptor

A widely used definition today.

Ex.
$\ce{HCl (aq) + H2O (aq) -> H3O+ (aq) + Cl- (aq)}$
- $\ce{HCl}$ - Brønsted acid
- $\ce{H2O}$ - Brønsted base (in this example)