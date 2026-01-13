
|               | Galvanic cell              | Electrolytic cell     |
| ------------- | -------------------------- | --------------------- |
| **Reaction**  | Spontaneous                | Nonspontaneous        |
| **Energy**    | Chemical → Electrical      | Electrical → Chemical |
| **Structure** | 2 half-cells + salt bridge | 1 compartment         |
| **Anode**     | $(-)$                      | $(+)$                 |
| **Cathode**   | $(+)$                      | $(-)$                 |

## Redox reactions

**Oxidation** - loss of $e^-$.
**Reduction** - gain of $e^-$.

**Oxidizing agent (oxidant)** - oxidizes *another* reagent.
**Reducing agent (reductant)** - reduces *another* reagent.

|                      | Oxidant                 | Reductant            |
| -------------------- | ----------------------- | -------------------- |
| **Behavior**         | causes oxidation        | causes reduction     |
| **Electrons**        | gained                  | lost                 |
| **Oxidation number** | decreases               | increases            |
| **Typical example**  | $\ce{O2, \space H2SO4}$ | $\ce{H2, \space CO}$ |

**Half-reactions** - oxidation/reduction reaction in isolation.
**Redox couple** - a pair of species in a half-reaction in the form Ox/Red.

$$
\begin{flalign}
&\ce{Zn^0 (s) -> Zn^{2+} (aq) + 2 e^-} \text{ - oxidation} \\
&\ce{Cu^{2+} (s) + 2 e^- -> Cu^0 (aq)} \text{ - reduction} \\
&\ce{Zn^0 (s) + Cu^{2+} (aq) -> Zn^{2+} (aq) + Cu (s)} \text{ - Redox} \\
&\ce{Zn^{2+}/Zn}, \space \ce{Cu^{2+}/Cu} \text{ - redox couples}
&\end{flalign}
$$

#### Balancing redox reactions

Steps to balance Redox reactions:
1. Identify species being oxidized/reduced:
	$\ce{Cu (s) + HNO3 (aq) -> Cu(NO3)2 (aq) + NO (g)}$
	$\ce{Cu} \text{ - oxidized}, \space \ce{N} \text{ - reduced}$
2. Write the skeletal half-reactions for oxidation & reduction:
	$\ce{Cu^0 (s) -> Cu^{2+} (aq)}$
	$\ce{NO3- (aq) -> NO (g)}$
3. Balance all the **elements** except for $\ce{H}$ & $\ce{O}$:
	$\ce{Cu^0 (s) -> Cu^{2+} (aq)}$
	$\ce{NO3- (aq) -> NO (g)}$
4. Balance $\ce{H}$ & $\ce{O}$ by adding $\ce{H2O}$ & $\ce{H+}$ in acidic solution and $\ce{H2O}$ & $\ce{OH-}$ in basic solution:
	$\ce{Cu^0 (s) -> Cu^{2+} (aq)}$
	$\ce{2 NO3- (aq) + 8 H+ (aq) -> 2 NO (g) + 4 H2O (l)}$
5. Balance the charge by adding $e^-$:
	$\ce{Cu^0 (s) -> Cu^{2+} (aq) + 2 e^-}$
	$\ce{2 NO3- (aq) + 6 e^- + 8 H+ (aq) -> 2 NO (g) + 4 H2O (l)}$
6. Match the \# of $e^-$ and combine the half-reactions:
	$\ce{3 Cu^0 (s) -> 3 Cu^{2+} (aq) + 6 e^-}$
	$\ce{2 NO3- (aq) + 6 e^- + 8 H+ (aq) -> 2 NO (g) + 4 H2O (l)}$
	$\ce{3 Cu^0 (s) + 2 NO3- (aq) + 6 e^- + 8 H+ (aq) -> 3 Cu^{2+} (aq) + 6 e^- + 2 NO (g) + 4 H2O (l)}$
7. Cancel out the same species & finish the equation:
	$\ce{3 Cu^0 (s) + 2 NO3- (aq) + 8 H+ (aq) -> 3 Cu^{2+} (aq) + 2 NO (g) + 4 H2O (l)}$
	$\ce{3 Cu (s) + 8 HNO3 (aq) -> 3 Cu(NO3)2 (aq) + 2 NO (g) + 4 H2O (l)}$

## Galvanic cells

**Galvanic cell (voltaic cell)** - electrochemical cell that uses a spontaneous reaction to generate electric current. Chemical energy → electrical energy.
**Battery** - a set of galvanic cells connected sequentially, so the total voltage is the sum of voltages of individual cells.

==fig.: galvanic cell

**Electrode** - conductor submerged into an electrolyte solution.
**Cathode** - electrode that provides $e^-$; reduction takes place.
**Anode** - electrode that takes away $e^-$; oxidation takes place.

$e^-$ are dumped at the anode → anode is $(-)$.
$e^-$ are spontaneously attracted to the cathode → cathode is $(+)$.

Electrodes can be made of the **same metals** that participate in the redox reaction (anode slowly dissolves, cathode slowly grows) or of **inert metals** (e.g. $\ce{Pt, Au}$) or **graphite** (only conduct $e^-$, are not involved in the reaction).

> $\ce{Pt}$ is often used for a **hydrogen electrode** for the reaction $\ce{2 H+ (aq) + 2 e- -> H2 (g)}$.

**Half-cell** - electrode /w the electrolyte in its immediate surroundings.

The salt bridge is used because mixing the ions in a single solution could cause disturbances in the cell potential.
It also makes sure to balance the charge in the half-cells - it would stop the $e^-$ flow.
Salt bridge is picked so it does not disturb the cell reaction (usually $\ce{KCl}$ because it is stable and would not react readily with the majority of ions).

#### Cell diagram

Used to represent the structure of a galvanic cell in an abstract way.

**anode electrode | anode electrolyte || cathode electrolyte | cathode electrode**
**oxidation | solution formed from oxidation || solution being reduced | reduction**

**|** - phase change
**||** - salt bridge

Example: $\ce{Zn (s) | Zn^{2+} (aq) || Cu^{2+} (aq) | Cu (s)}$

> When determining the redox reaction that is happening in the cell, only take into account the phases directly next to the electrodes, since this is where the half-reactions happen.

#### Energy of the cell

**Voltage ($U$)** - ability to push electric current through a circuit (potential difference).
**Cell potential** ($E_{\text{cell}}$) - ability to force $e^-$ through a circuit; voltage of a cell working reversibly.

$w_e = qE_{\text{cell}} = -neN_AE_{\text{cell}} = -nFE_{\text{cell}}$
$\Delta G = -nFE_{\text{cell}}, \space \Delta G \degree = -nFE_{\text{cell}} \degree$

| Symbol            | Unit               | Explanation                                    |
| ----------------- | ------------------ | ---------------------------------------------- |
| $w_e$             | $J$                | Electrical work; non-expansion work!           |
| $q$               | $C$                | Charge of the system doing work                |
| $E_{\text{cell}}$ | $V$                | Cell potential of the system                   |
| $n$               | $mol$              | Amount of $e^-$ doing work                     |
| $e$               | $C$                | [Elemental charge](Cheat%20Sheet#Constants)    |
| $N_A$             | $mol^{-1}$         | [Avogadro's constant](Cheat%20Sheet#Constants) |
| $F$               | $C \cdot mol^{-1}$ | [Faraday's constant](Cheat%20Sheet#Constants)  |
| $\Delta G$        | $J$                | Change in Gibbs free energy of the system      |

Electrochemical reaction is spontaneous when $E > 0$ (because then $\Delta G < 0$).

> When a redox reaction is multiplied by a factor, $\Delta G$ gets multiplied as well, but **$E$ stays the same no matter the size of the cell**.

Cell potential is written in the direction of reduction:
- when the cell diagram goes **anode → cathode**, $E > 0$,
- when it goes **cathode → anode**, $E < 0$

$E_{\text{cell}} \degree = E_{\text{cathode}} \degree - E_{\text{anode}} \degree = E_{\text{R}} \degree - E_{\text{L}} \degree$
.
> Negative sign because at the anode oxidizes the species and $E_L = -E_L \degree$.

> MAKE SURE TO USE THE STANDARD POTENTIALS IN THE EQUATION!!!

**Standard electrode** - electrode the standard potential of a half-cell is measured against.
Standard electrode: standard hydrogen electrode; $\ce{Pt}$ electrode reacting /w hydrogen.

$E \degree (\text{half-reaction}) > 0$ - the species in the half-reaction is an stronger oxidant than $\ce{H}$.
$E \degree (\text{half-reaction}) < 0$ - the species in the half-reaction is a stronger reductant than $\ce{H}$.

> If reactions happen **one after another**, you can't just add standard potentials of reactions together! You must account for the \# of $e^-$ transferred!

$$
\begin{flalign}
&\ce{Mn^{3+} + e^- -> Mn^{2+}}, \space E \degree = +1.51 \space V \\
&\ce{Mn^{2+} + 2 e^- -> Mn}, \space E \degree = -1.18 \space V \\
&\Delta G = -nFE \\
&\Delta G_r = \Delta G_1 + \Delta G_2 = -3 \cdot FE_{\text{tot}} = -1 \cdot F \cdot 1.51 - 2 \cdot F \cdot (-1.18) \\
&E_\text{tot} \degree = \frac{-1.51 + 2 \cdot 1.18}{-3} = -0.28 \space V
&\end{flalign}
$$
---

From $-nFE_{\text{cell}} \degree = \Delta G = -RT \cdot ln(K)$:
$E_{\text{cell}} \degree = \frac{RT \cdot ln(K)}{nF} \Leftrightarrow ln(K) = \frac{nFE_{\text{cell}} \degree}{RT}$
**Works for any reaction, not only the ones involving gases!**

#### Nernst equation

The redox reaction does not proceed at the same rate the entire time; **a battery grows weaker over time**.

This is an example of non-standard conditions.

$$
\begin{flalign}
&\text{From: } \Delta G = \Delta G \degree + RT \cdot ln(Q) \\
&-nFE_{\text{cell}} = -nFE_{\text{cell}} \degree + RT \cdot ln(Q) \\
&E_{\text{cell}} = E_{\text{cell}} \degree - \frac{RT}{nF} \cdot ln(Q) \\
&E_{\text{cell}} = E_{\text{cell}} \degree - \frac{RT}{nF} \cdot ln(\frac{[\text{products}]}{[\text{reactants}]})
&\end{flalign}
$$

## Concentration cell

Electrochemical cell for measuring the concentration of ions in the solution.

==fig.

Both half-cells have the same ions /w the same species being oxidized/reduced.
The concentration of ions in one of the half-cells is known, the concentration in the other half-cell is analyzed.
The reaction is driven by the difference in concentrations.
The reaction proceeds until the concentration in both half-cells is equal.

## pH meter

Uses the same principle as a concentration cell.

One electrode is sensitive to $\ce{H3O+/H+}$ - hydrogen electrode.
The other electrode has a known potential.

Example: $\ce{Hg2Cl2}$ electrode
$$
\begin{flalign}
\text{cell: } &\ce{Pt (s) | H2 (g) | H+ (aq) || Cl- (aq, \space sat.) | Hg (l) | H2Cl2 (s)} \\
\text{red.: } &\ce{H2Cl2 (s) + 2 e^- -> 2 Hg (l) + 2 Cl- (aq)}, \space E \degree = +0.27 \space V \\
\text{ox.: } &\ce{H2 (g) -> 2 H+ (aq) + 2 e^-}, \space E \degree = 0 \space V \text{ (by definition)} \\
\text{react.: } &\ce{Hg2Cl2 (s) + H2 (g) -> 2 H+ (aq) + 2 Hg (l) + 2 Cl- (aq)}, \space Q = \frac{\ce{[Cl-]^2[H+]^2}}{p_{\ce{H2}}}, \space n = 2 \\
&\text{If } p_{\ce{H2}} = 1 \space bar, \space E_{\text{cell}} = E_{\text{cell}} \degree - \frac{RT}{nF} \cdot ln(Q) = E_{\text{cell}} \degree - \frac{RT}{2F} \cdot ln(\ce{[Cl-]^2[H+]^2}) \\
&E_{\text{cell}} = E_{\text{cell}} \degree - \frac{RT}{F} \cdot ln(\ce{[Cl-][H+]}) = E_{\text{cell}} \degree - \frac{RT}{F} \cdot ln(\ce{[Cl-]}) - \frac{RT}{F} \cdot ln(10) \cdot log(\ce{[H+]}) \\
&-log(\ce{[H+]}) = pH = (E_{\text{cell}} - E_{\text{cell}} \degree + \frac{RT}{F} \cdot ln(\ce{[Cl-]})) \cdot \frac{F}{RT\cdot ln(10)}
&\end{flalign}
$$

The concentration of $\ce{Cl-}$ ions is constant because the solution at the electrode is saturated. 

More commonly a $\ce{Ag/AgCl}$ reference electrode is used.

$pH$ meters are calibrated against solutions of known $pH$.

## Electrolysis

**Electrolytic cell** - electrochemical cell that captures the energy of an electric current in chemicals. Electrical energy → chemical energy.

One compartment, one electrolyte.

$e^-$ from a power source are forced into the cathode → cathode is $(-)$.
$e^-$ are taken up by the anode → anode is $(+)$.

Usually to effectively form products, **overpotential** is required. At least $0.06 \space V$ more potential than the reverse reaction produces.

One must consider that ALL the species in the solution may be oxidized/reduced (even water!).
The oxidation/reduction half-reaction that required **less potential to reverse** will be preferred.
- The oxidized form of species /w higher potential is preferably reduced.
- The reduced form of species /w lower potential is preferably oxidized.


**Faraday's law**:
The amount of reactant consumed/product formed is proportional to the amount of $e^-$ supplied.
$\ce{Cu^{2+} (aq) + 2 e^- -> Cu (s)}, \space 2 \space mol \space e^- \leftrightarrow 1 \space mol \space \ce{Cu}$

$q = nF \Rightarrow n = \frac{q}{F} \Rightarrow n = \frac{It}{F}$

| Symbol     | Unit               | Explanation                                    |
| ---------- | ------------------ | ---------------------------------------------- |
| $q$        | $C$                | Total charge of the system doing work          |
| $n$        | $mol$              | Amount of $e^-$ doing work                     |
| $F$        | $C \cdot mol^{-1}$ | [Faraday's constant](Cheat%20Sheet#Constants)  |
| $I$        | $A$                | Electrical current doing work                  |
| $t$        | $s$                | Time the current is running for                |

Electrolysis is used in refining of metals & metal plating.

## Electrochemical series

**Electrochemical series** - series of redox couples in the order of increasing $E \degree$.

Helps to predict how different species would react.

Oxidized species oxidizes the reduced species **below** it.
Reduced species reduces the oxidized species **above** it.

$$
\begin{flalign}
&\text{Greatest } E \degree \\
&... \\
&\ce{Cu^{2+} + 2 e- -> Cu}, \space E \degree (\ce{Cu^{2+}/Cu}) \\
&... \\
&\ce{Zn^{2+} + e^- -> Zn}, \space E \degree (\ce{Zn^{2+}/Zn}) \\
&... \\
&\text{Lowest } E \degree
\end{flalign}
$$

$E \degree (\ce{Cu^{2+}/Cu}) > E \degree (\ce{Zn^{2+}/Zn})$

$\ce{Cu^{2+}}$ oxidizes $\ce{Zn}$, $\ce{Zn}$ reduces $\ce{Cu^{2+}}$.
$\ce{Zn^{2+}}$ **cannot** oxidize $\ce{Cu}$, $\ce{Cu}$ **cannot** reduce $\ce{Zn^{2+}}$.

> Another mnemonic: a spontaneous reaction happens, if the species can be connected with a diagonal line from top left to bottom right.
