
Analyses reaction rates.
Rates are **always positive**.

## Reaction rate

**Average reaction rate** - change in concentration of reactants over time.

For reactants (rate of consumption): $R = |\frac{\Delta \ce{[R]}}{\Delta t}| = -\frac{\Delta \ce{[R]}}{\Delta t}$
For products (rate of production): $P = |\frac{\Delta \ce{[P]}}{\Delta t}| = \frac{\Delta \ce{[P]}}{\Delta t}$

---

**Unique average rate** - reaction rate of species divided by its stoichiometric coefficient.
Unique average rate is **unique to a reaction**, it is the same for all the species in the reaction.
It shows how many moles of reactions have happened during the given time interval.

$\ce{a A + b B -> c C + d D}$
$\text{Unique average rate: } -\frac{1}{a}\frac{\Delta \ce{[A]}}{\Delta t} = -\frac{1}{b}\frac{\Delta \ce{[B]}}{\Delta t} = \frac{1}{c}\frac{\Delta \ce{[C]}}{\Delta t} = \frac{1}{d}\frac{\Delta \ce{[D]}}{\Delta t}$

---

**Instantaneous rate** - rate of change of the reaction at a specific point in time.

$\text{Instantaneous rate (reactants): } |\frac{d\ce{[R]}}{dt}| = -\frac{d\ce{[R]}}{dt}$
$\text{Instantaneous rate (products): } |\frac{d\ce{[P]}}{dt}| = \frac{d\ce{[P]}}{dt}$

---

**Unique instantaneous rate** - same as unique average rate but at a specific point in time.

$\ce{a A + b B -> c C + d D}$
$\text{Unique instantaneous rate: } -\frac{1}{a}\frac{d\ce{[A]}}{dt} = -\frac{1}{b}\frac{d\ce{[B]}}{dt} = \frac{1}{c}\frac{d\ce{[C]}}{dt} = \frac{1}{d}\frac{d\ce{[D]}}{dt}$

## Rate law

**Rate law** - relation between the reaction rate & the concentration of species in the system.

> Rate law cannot be deduced from a chemical equation, determined experimentally.

==fig.: concentration against time & initial rate against concentration

**Rate constant ($k_r$)** - characteristic of the reaction; determined by the reaction & the temperature it happens at.

**Reaction order** - sum of the exponents of the concentrations appearing in the expression for the rate law.
$\text{Rate: } k_r \cdot [\ce{A}]^a[\ce{B}]^b$
$\text{Order with respect to } \ce{A}: \space a, \text{ Order with respect to } \ce{B}: \space b$
$\text{Overall order of the reaction: } a + b$

The units of $k_r$ depend on the reaction order: $M^{-(\text{(order)-1})} \cdot s^{-1} = mol^{-(\text{(order)-1})} \cdot l^{\text{(order)-1}} \cdot s^{-1}$

#### Examples of reaction orders

$$
\begin{flalign}
&\ce{2 NH3 (g) ->[Pt] N2 (g) + 3 H2 (g)}, \text{ rate: } k_r, \text{ 0th order} \\
&\ce{2 N2O5 -> 4 NO2 + O2}, \text{ rate: } k_r\ce{[N2O5]}, \text{ 1st order} \\
&\ce{2 NO2 -> 2 NO + O2}, \text{ rate: } k_r \cdot \ce{[NO2]}^2 \\
&\ce{S2O8^{2-} + 3 I- -> 2 SO4^{2-} + I3-}, \text{ rate: } k_r\ce{[S2O8^{2-}][I3-]}, \text{ 2nd order} \\
&\ce{2 O3 -> 3 O2}, \text{ rate: } k_r\ce{[O3][O2]}^{-1}, \text{ 0th order (product inhibiting the reaction)} \\
&\ce{2 SO2 + O2 ->[Pt] 2 SO3}, \text{ rate: } k_r\ce{[SO2][SO3]}^{-1/2}, \text{ 0.5th order}
&\end{flalign}
$$

## Integrated rate laws

Used to predict concentrations of reactants/products in the future.

**Half-life** - time needed for the concentration to decrease to a half of its initial value.
Then $t = t_{1/2}, \space \ce{[A]}_t = \frac{1}{2}\ce{[A]}_0$

| Order        | Rate law<br>(instantaneous rate of change) | Integrated rate law                                                                                                      | Half-life                           | What is linear in time |
| ------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ---------------------- |
| $\text{0th}$ | $\frac{d\ce{[A]}}{dt} = k_r$               | $\ce{[A]}_t = \ce{[A]}_0 - k_rt$                                                                                         | $t_{1/2} = \frac{\ce{[A]}_0}{2k_r}$ | $\ce{[A]}$             |
| $\text{1st}$ | $-\frac{d\ce{[A]}}{dt} = k_r\ce{[A]}$      | $ln(\frac{\ce{[A]}_t}{\ce{[A]}_0}) = -k_rt \Leftrightarrow ln(\ce{[A]}_t) = ln(\ce{[A]}_0) - k_rt$                       | $t_{1/2} = \frac{ln(2)}{k_r}$       | $ln(\ce{[A]})$         |
| $\text{2nd}$ | $-\frac{d\ce{[A]}}{dt} = k_r\ce{[A]}^2$    | $\frac{1}{\ce{[A]}_0} - \frac{1}{\ce{[A]}_t} = -k_rt \Leftrightarrow \frac{1}{\ce{[A]}_t} = \frac{1}{\ce{[A]}_0} + k_rt$ | $t_{1/2} = \frac{1}{k_r\ce{[A]}_0}$ | $\frac{1}{\ce{[A]}}$   |

#### Derivation

Integrated rate laws are found using calculus.

Take first-order reaction as an example.
By the definition of instantaneous reaction rate, $\text{rate: } -\frac{d\ce{[A]}}{dt}$.
At the same time, by the rate law, $\text{rate: } k_r\ce{[A]}$
From here,
$$
\begin{flalign}
&-\frac{d\ce{[A]}}{dt} = k_r\ce{[A]} \\
&\frac{d\ce{[A]}}{\ce{[A]}} = -k_r dt \\
&\text{Time varies from 0 to the desired time } t \\
&\text{Concentration varies from } \ce{[A]}_0 \text{ to the concentration at the desired time } \ce{[A]}_t \\
&\int_{\ce{[A]}_0}^{\ce{[A]}_t} \frac{d\ce{[A]}}{\ce{[A]}} = \int_0^t -k_r dt \\
&ln(\ce{[A]}_t) - ln(\ce{[A]}_0) = -k_r t \\
&ln(\frac{\ce{[A]}_t}{\ce{[A]}_0}) = -k_r t \Leftrightarrow ln(\ce{[A]}_t) = ln(\ce{[A]}_0) - k_r t
&\end{flalign}
$$

## Reaction mechanisms

#### Elementary reactions

Chemical reactions are the outcome of multiple steps - **elementary reactions**.
**Reaction mechanism** - a sequence of elementary reactions.
Many routes for a chemical reaction might be possible.

One step mechanism (false): $\ce{O3 + O3 -> O2 + O2 + O2} \text{ - 2 molecules collide and rearrange}$
Two step mechanism (true): $\ce{O3 + hv -> O2 + O}, \space \ce{O + O3 -> O2 + O2}$

**Reaction intermediate** (here $\ce{O}$) - species that plays part in the elementary reactions but does not appear in the overall chemical equation.

Elementary reactions are written without state symbols & stoichiometric coefficients.

#### Rate law for elementary reactions

Rate laws for elementary reactions follow the same structure as the regular rate laws.

**Molecularity** - \# of species reacting.

| Molecularity | Elementary reaction     | Rate law            |
| ------------ | ----------------------- | ------------------- |
| **1**        | $\ce{A -> ...}$         | $k_r\ce{[A]}$       |
| **2**        | $\ce{A + B -> ...}$     | $k_r\ce{[A][B]}$    |
| **2**        | $\ce{A + A -> ...}$     | $k_r\ce{[A]^2}$     |
| **3**        | $\ce{A + B + C -> ...}$ | $k_r\ce{[A][B][C]}$ |
| **3**        | $\ce{A + A + B -> ...}$ | $k_r\ce{[A]^2[B]}$  |
| **3**        | $\ce{A + A + A -> ...}$ | $k_r\ce{[A]^3}$     |

| Molecularity | Reaction name |
| ------------ | ------------- |
| **1**        | Unimolecular  |
| **2**        | Bimolecular   |
| **3**        | Termolecular  |


==combining elementary reactions

**Determining step** - the slowest step; bottleneck.
The rate of the determining step makes the most contribution to the experimental rate law.

#### Rates and equilibrium

$\ce{A + B \rightleftharpoons C + D}, \space K = \frac{\ce{[C][D]}}{\ce{[A][B]}}$
$\ce{A + B -> C + D}, \space \text{rate: } k_r\ce{[A][B]}$
$\ce{C + D -> A + B}, \space \text{rate: } k_r'\ce{[C][D]}$
$\text{At equilibrium: } k_r\ce{[A][B]} = k_r'\ce{[C][D]} \Rightarrow \frac{k_r}{k_r'} = \frac{[C][D]}{[A][B]} \Rightarrow K = \frac{k_r}{k_r'}$

---

**Arrhenius equation**:
$k_r = A \cdot e^{-\frac{E_a}{RT}}$
$ln(k_r) = ln(A) - \frac{E_a}{RT}$

| Symbol | Unit                            | Explanation                                   |
| ------ | ------------------------------- | --------------------------------------------- |
| $k_r$  | $M^{-n} \cdot s^{-1}$           | Rate constant of a reaction                   |
| $A$    | $M^{-n} \cdot s^{-1}$           | Frequency factor (pre-exponential factor)     |
| $E_a$  | $J \cdot mol^{-1}$              | Activation energy of the reaction             |
| $R$    | $J \cdot K^{-1} \cdot mol^{-1}$ | [Ideal gas constant](Cheat%20Sheet#Constants) |
| $T$    | $K$                             | Temperature the reaction is happening at      |
$A$ & $E_a$ are determined empirically.
$E_a \geq 0$

---

Temperature increases → $k_r$ increases

$ln(\frac{k_r2}{k_r1}) = \frac{E_a}{R}(\frac{1}{T_1} - \frac{1}{T_2})$

The plot of $ln(k_r)$ against $\frac{1}{T}$ is a straight line.

==fig.: plot

Higher $E_a$ → more responsive to temperature

==fig.: plot of reaction energy for endothermic

endothermic reaction
forward reaction -> higher E_a -> more responsive to T
reverse reaction -> lower E_a -> less responsive to T

T inc. => K inc.

exothermal reaction
T inc. => K dec.

#### Collision theory

A model that explains the Arrhenius equation.
**A reaction can take place only if molecules collide & have enough energy.**

Assume gases $\ce{A}$ and $\ce{B}$.

collision density
$z_{AB} = \sigma \cdot \bar v_{rel} \cdot N_A^2 \ce{[A][B]}$

| Symbol                | Unit                              | Explanation                                                                          |
| --------------------- | --------------------------------- | ------------------------------------------------------------------------------------ |
| $z_{\ce{AB}}$         | $m^3 \cdot s^{-1} \cdot mol^{-1}$ | Collision density                                                                    |
| $\sigma$              | $m^2$                             | Collision area; a plane between 2 molecules passing through their center             |
| $\bar v_{\text{rel}}$ | $m \cdot s^{-1}$                  | Mean speed of the molecules relative to each other (assume one is always stationary) |
| $N_A$                 | $mol^{-1}$                        | [Avogadro's number](Cheat%20Sheet#Constants)                                         |

$\bar v_{\text{rel}} = (\frac{8RT}{\pi M})^{1/2}, \space M = \frac{M_\ce{A} M_\ce{B}}{M_\ce{A} + M_\ce{B}}$

$\sigma \cdot \bar v_{rel}$ - swept area; how much volume a molecule travels through during a timespan.
$N_A \ce{[A]}$ - number density;  \# of molecules of $\ce{A}$ per volume.

$x_{\ce{B}} = e^{-\frac{E_{min}}{RT}}$

$x_{\ce{B}}$ - mole fraction of $\ce{B}$ having enough energy to react.

**Steric requirement** ($P$) - molecules need to be oriented in a certain way in order to react.
Determined empirically.
Fraction of the possible orientations that lead to reaction.


Transition state theory


### Catalysis

**Catalyst** - molecule that increases the rate of the reaction without being consumed.

Usually it is a part of the reaction mechanism.
Lowers the activation energy of the reaction.
Both forward & reverse reactions are accelerated.

$$
\begin{flalign}
&\ce{I3- (aq) + 2 N3- (aq) ->[CS2] 3 I- (aq) + 3 N2 (g)} \\
&\text{Step 1: } \ce{CS2 + N3- -> S2NC3-} \text{ (slow, rate determining step)} \\
&\text{Step 2: } \ce{2 S2CN3- + I3- -> 2 CS2 + 3 N2 + 3 I-} \text{ (fast)} \\
&\text{Rate of consumption of } \ce{I3-} \text{: } k_r \ce{[CS2][N3-]}
&\end{flalign}
$$

**Homogeneous catalyst** - catalyst that is in the same phase as the reactants.
**Heterogeneous catalyst** - catalyst that is not in the same phase as the reactants.

**Chemisorption** - adsorption by covalent bonding to the surface.
Can fix the molecule in place so it's easier to make bond /w other reactants.
Molecules have a better chance of meeting on a 2D surface than in 3D space.

$\ce{H2C=CH2 (g) + H2 (g) ->[Ni] H3C-CH3 (g)}$

Here, the reactants are stuck and react on the surface of the nickel metal.

---

**Enzymes** - biocatalysts.

$\ce{E + S \rightleftharpoons ES -> E + P}$
Step 1:
forward: $k_1 \ce{[E][S]}$
reverse: $k_1' \ce{[ES]}$
Step 2:
forward: $k_2 \ce{[ES]}$

At steady state of ES formation: $k_1 \ce{[E][S]} - k_1' \ce{[ES]} - k_2 \ce{[ES]} = 0$ (All intermediates used up as they are produced).
$\ce{[E]}_0 \ce{[E]} + \ce{[ES]}$
$\frac{(\ce{[E]}_0 - \ce{[ES]}) \ce{[S]}}{\ce{[ES]}} = \frac{k_1' + k_2}{k_1}$

Michaelis constant: $K_M = \frac{k_1' + k_2}{k_1}$
$\ce{[ES]} = \frac{\ce{[E]}_0 \ce{[S]}}{K_M + \ce{[S]}}$

Michaelis-Menten equation:
rate of P formation (velocity): $v = k_2 \ce{[ES]} = \frac{k_2 \ce{[E]}_0 \ce{[S]}}{K_M + \ce{[S]}}$
Velocity is max when [S] is high & all of A is converted to ES
$v_{max} = k_2 \ce{[ES]} = k_2 \ce{[E]}_0$

$v = \frac{v_{max} \ce{[S]}}{K_M + \ce{[S]}}$

$[S] = K_M$ at $v = \frac{1}{2} v_{\text{max}}$
