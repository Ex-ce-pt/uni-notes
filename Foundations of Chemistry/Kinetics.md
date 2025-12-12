
Analyses reaction rates.

## Reaction rate

**Average reaction rate** - change in concentration of reactants over time.

For reactants (rate of consumption): $R = |\frac{\Delta \ce{[R]}}{\Delta t}| = -\frac{\Delta \ce{[R]}}{\Delta t}$
For products (rate of production): $P = |\frac{\Delta \ce{[P]}}{\Delta t}| = \frac{\Delta \ce{[P]}}{\Delta t}$

---

**Unique average rate** - reaction rate of species divided by its stoichiometric coefficient.
Unique average rate is **unique to a reaction**, it is the same for all the species in the reaction.

$\ce{a A + b B -> c C + d D}$
$\text{Unique average rate: } -\frac{1}{a}\frac{\Delta \ce{[A]}}{\Delta t} = -\frac{1}{b}\frac{\Delta \ce{[B]}}{\Delta t} = \frac{1}{c}\frac{\Delta \ce{[C]}}{\Delta t} = \frac{1}{d}\frac{\Delta \ce{[D]}}{\Delta t}$

---

**Instantaneous rate** - rate of change of the reaction at a specific point in time.

$\text{Instantaneous rate of change: } -\frac{d\ce{[R]}}{dt}$

**Unique instantaneous rate** - same as unique average rate but at a specific point in time.


#### Rate law

==fig.: as init concentration increaces, the slope at 0 becomes steeper

Increasing the initial concentration of a reactant increases the instantaneous rate of change.
The slope to the concentration graph becomes steeper.

**Reaction order** - exponent of the concentration of the reactants.

$\text{Rate: } k_r \cdot [\ce{A}]^a[\ce{B}]^b$
Overall order of the reaction: $a + b$

> Rate law **does not depend on stoichiometry**!
> It is all determined experimentally!

$\ce{2 NH3 (g) ->[Pt] N2 (g) + 3 H2 (g)}, \text{ rate: } k, \text{ 0th order}$
$\ce{2 N2O5 -> 4 NO2 + O2}, \text{ rate: } k_r\ce{[N2O5]}, \text{ 1st order}$
$\ce{2 NO2 -> 2 NO + O2}, \text{ rate: } k_r \cdot \ce{[NO2]}^2$
$\ce{S2O8^{2-} + 3 I- -> 2 SO4^{2-} + I3-}, \text{ rate: } k_r\ce{[S2O8^{2-}][I3-]}, \text{ 2nd order}$
$\ce{2 O3 -> 3 O2}, \text{ rate: } k_r\ce{[O3][O2]}^{-1}, \text{ 0th order (product inhibiting the reaction)}$
$\ce{2 SO2 + O2 ->[Pt] 2 SO3}, \text{ rate: } k_r\ce{[SO2][SO3]}^{-1/2}, \text{ 0.5th order}$

> Rate law cannot be deduced from a chemical equation, determined experimentally.

The units for the reaction rate depend on the reaction order: $M^{-(\text{(order)-1})} \cdot s^{-1}$

## Integrated rate laws

Used to predict concentrations of reactants/products in the future.

**Half-life** - time needed for the concentration to decrease to a half of its initial value.
Then $t = t_{1/2}, \space \ce{[A]}_t = \frac{1}{2}\ce{[A]}_0$

| Order        | Rate law<br>(instantaneous rate of change) | Integrated rate law                                                                                                      | Half-life                           | What is linear       |
| ------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | -------------------- |
| $\text{0th}$ | $\Delta \ce{[A]} = k_r$                    | $\ce{[A]}_t = \ce{[A]}_0 - k_rt$                                                                                         | $t_{1/2} = \frac{\ce{[A]}_0}{2k_r}$ | $\ce{[A]}$           |
| $\text{1st}$ | $-\frac{d\ce{[A]}}{dt} = k_r\ce{[A]}$      | $ln(\frac{\ce{[A]}_t}{\ce{[A]}_0}) = -k_rt \Leftrightarrow ln(\ce{[A]}_t) = ln(\ce{[A]}_0) - k_rt$                       | $t_{1/2} = \frac{ln(2)}{k_r}$       | $ln(\ce{[A]})$       |
| $\text{2nd}$ | $-\frac{d\ce{[A]}}{dt} = k_r\ce{[A]}^2$    | $\frac{1}{\ce{[A]}_0} - \frac{1}{\ce{[A]}_t} = -k_rt \Leftrightarrow \frac{1}{\ce{[A]}_t} = \frac{1}{\ce{[A]}_0} + k_rt$ | $t_{1/2} = \frac{1}{k_r\ce{[A]}_0}$ | $\frac{1}{\ce{[A]}}$ |

==???? $\frac{\ce{[A]}_x}{\ce{[A]}_{x-1}} = const$ for 1st order??? why??

==practice: find energything from list of concentrations/pressures over time








## Reaction mechanisms


Chemical reactions are the outcome of multiple steps - elementary reactions.
Many routes for a chemical reaction might be possible.

One step mechanism (false): $\ce{O3 + O3 -> O2 + O2 + O2} \text{2 molecules collide and rearrange}$
Two step mechanism (true): $\ce{O3 + hv -> O2 + O}, \space \ce{O + O2 -> O2 + O2}$

#### Rate law for elementary reactions

| Molecularity | Elementary reaction | Rate law         |
| ------------ | ------------------- | ---------------- |
| 1            | $\ce{A -> }$        | $k_r\ce{[A]}$    |
| 2            | $\ce{A + B -> }$    | $k_r\ce{[A][B]}$ |
|              |                     |                  |
==fill table


==combining elementary reactions

Determining step - slow step; bottleneck.
The rate of the determining step makes the most contribution to the experimental rate law.

#### Rates and equilibrium

$\ce{A + B \rightleftharpoons C + D}, \space K = \frac{\ce{[C][D]}}{\ce{[A][B]}}$
$\ce{A + B -> C + D}, \space \text{rate: } k_r\ce{[A][B]}$
$\ce{C + D -> A + B}, \space \text{rate: } k_r'\ce{[C][D]}$
$\text{At equilibrium: } k_r\ce{[A][B]} = k_r'\ce{[C][D]} \Rightarrow K = \frac{k_r}{k_r'}$
