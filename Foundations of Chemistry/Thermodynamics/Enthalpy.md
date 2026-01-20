
**Enthalpy** ($H$) - a state function that keeps track of losses of energy to expansion work during heat transfer at constant pressure.

$H = U + pV$

At constant pressure:
$$
\begin{flalign}
&\textcolor{grey}{H = U + pV} \\
&\textcolor{grey}{\Delta H = \Delta U + p \cdot \Delta V, \space p = \text{const}} \\
&\textcolor{grey}{\Delta H = q + w + p \cdot \Delta V} \\
&\textcolor{grey}{\text{If no non-expansion work: } w = -p_{\text{ext}} \cdot \Delta V} \\
&\textcolor{grey}{\text{If the vessel is open or adjusts to the volume of the substance: } p_{\text{ext}} = p} \\
&\textcolor{grey}{\Delta H = q - p \cdot \Delta V + p \cdot \Delta V} \\
&\Delta H = q
&\end{flalign}
$$
At constant pressure & no non-expansion work: $\Delta H = q$.

**Exothermic reaction** - reaction that releases heat ($\Delta H < 0$).
**Endothermic reaction** - reaction that absorbs heat ($\Delta H > 0$).

**Molar enthalpy** - enthalpy per $1 \space mol$ of substance.
$H_m = \frac{H}{n}$

## Physical change

|              | $\Delta H_{\text{state change}} = H_m(\text{target state}) - H_m(\text{source state})$                        | $\Delta H_{\text{fwd change}} = -\Delta H_{\text{bwd change}}$ |
| ------------ | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Gas/Liquid   | $\Delta H_{\text{vap}} = H_m(\text{gas}) - H_m(\text{liquid})$                                                | $\Delta H_{\text{cond}} = -\Delta H_{\text{vap}}$              |
| Liquid/Solid | $\Delta H_{\text{fus}} = H_m(\text{liquid}) - H_m(\text{solid})$                                              | $\Delta H_{\text{freeze}} = -\Delta H_{\text{fus}}$            |
| Gas/Solid    | $\Delta H_{\text{sub}} = H_m(\text{gas}) - H_m(\text{solid}) = \Delta H_{\text{vap}} + \Delta H_{\text{fus}}$ | $\Delta H_{\text{depos}} = -\Delta H_{\text{sub}}$             |

## Reaction enthalpy

**Reaction enthalpy** - the change in enthalpy between the products of the reaction & its reactants.

**Thermochemical equation**:
$\ce{CH4 (g) + 2 O2 (g) -> CO2 (g) + 2 H2O (l)}, \space \Delta H = -890 \space kJ$

> The enthalpies of reactants & products are measured at $298 \space K$, so the reaction enthalpy is also for $298 \space K$.

> Reaction enthalpy assumes $N_A$ reactions have taken place! So it is actually measured in $kJ \cdot mol^{-1}$, even if it doesn't look like it!

#### Reactions with gases

For reactions without gases involved; $\Delta H \approx \Delta U$.

If an (ideal) gas is consumed and/or produced during the reaction, it has to do expansion work.
The reaction enthalpy then depends on the change in the amount of gas molecules.

$$
\begin{flalign}
&H_1 = U_1 + pV_1 = U_1 + n_1RT, \space H_2 = U_2 + n_2RT \\
&\Delta H = \Delta U + \Delta n_{\text{gas}}RT, \space \Delta n_{\text{gas}} = n_2(g) - n_1(g)
&\end{flalign}
$$

## Standard reaction enthalpy

**Standard state**:
- Pure form;
- (usually) $298.15 \space K \space (25 \degree C)$;
- Gases at $1 \space bar$;
- Solutes at $1 \space M$.
$\ce{C (s), H2O (l), O2 (g)}$

**Standard reaction enthalpy** ($\Delta H \degree$) - reaction enthalpy when both the reactants & products are in their standard states.

$\ce{C2H4 (g) + 3 O2 (g) -> 2 CO2 (g) + 2 H2O (g)}$ - not standard state, gaseous water.
$\ce{C2H4 (g) + 3 O2 (g) -> 2 CO2 (g) + 2 H2O (l)}$ - standard state.

**Standard enthalpy of formation** ($\Delta H_f \degree$) - standard reaction enthalpy **per mole** of formula units  of a substance formed from its elements in **most stable form**.
**Most stable form**: $\ce{C}$ - graphite, $\ce{H2O}$ - water, $\ce{O2}$ - gas.
Exception: white phosphorus is used for its  $\Delta H_f \degree$ because it's easier to obtain.

$\ce{C (gr) + O2 (g) -> CO2 (g)}, \space \Delta H_f \degree$

**Standard enthalpy of combustion** ($\Delta H_c \degree$) - standard enthalpy **per mole** of a substance burned at standard conditions.

**Specific enthalpy**: $\frac{\Delta H_c \degree}{m}$
**Enthalpy density**: $\frac{\Delta H_c \degree}{V}$

## Hess's law

The overall reaction enthalpy is the sum of the reaction enthalpies of the steps into which the reaction can be divided.

![[thermochemistry/hess-law.png]]
Stems from the fact enthalpy is a state function.

Then, the $\Delta H \degree$ of a reaction is the difference in enthalpy between the formation enthalpies of the products & reactants.

$$
\begin{flalign}
&N(x) \text{ - the stochiometric coefficients of reagent } x \text{ in the reaction in question.}\\
&\text{Since enthalpy assumes } N_A \text{ reactions, we account for } N(x) \space mol \text{ of reagents.} \\
&\Delta H \degree (\text{reactants}) = \sum_{i \text{ - reactants}} N(i) \cdot \Delta H_{f} \degree (i) \\
&\Delta H \degree (\text{products}) = \sum_{j \text{ - products}} N(j) \cdot \Delta H_{f} \degree (j) \\
&\Delta H \degree (\text{reaction}) = \Delta H \degree (\text{products}) - \Delta H \degree (\text{reactants})
&\end{flalign}
$$
> Mind the signs!

Example:

$$
\begin{flalign}
&\text{Reaction: } \ce{CH4 (g) + 2O2 (g) -> CO2 (g) + H2O (l)}, \space \Delta H \degree (\text{reaction}) = ? \\
&\text{Formation of products: } \\
&\ce{C (gr) + O2 (g) -> CO2 (g)}, \space \Delta H_f \degree (\ce{CO2}) = -393.51 \space kJ \cdot mol^{-1} \\
&\ce{H2 (g) + \frac{1}{2} O2 (g) -> H2O (l)}, \space \Delta H_f \degree (\ce{H2O}) = -285.83 \space kJ \cdot mol^{-1} \\
&\Delta H \degree (\text{products}) = 1 \cdot (-393.51) \space kJ \cdot mol^{-1} + 2 \cdot (-285.83) \space kJ \cdot mol^{-1} = -965.17 \space kJ \cdot mol^{-1} \\
&\text{Formation of reagents: } \\
&\ce{C (gr) + 2 H2 (g) -> CH4 (g)}, \space \Delta H_f \degree (\ce{CH4}) = -74.81 \space kJ \cdot mol^{-1} \\
&\ce{O2 (g) -> O2 (g)} \text{ (null reaction)}, \space \Delta H_f \degree (\ce{O2}) = 0 \space kJ \cdot mol^{-1} \\
&\Delta H \degree (\text{reagents}) = 1 \cdot (-74.81) \space kJ \cdot mol^{-1} + 2 \cdot 0 \space kJ \cdot mol^{-1} = -74.81 \space kJ \cdot mol^{-1} \\
&\text{Standard reaction enthalpy: } \\
&\Delta H \degree (\text{reaction}) = -965.17 \space kJ \cdot mol^{-1} - (-74.81) \space kJ \cdot mol^{-1} = -890.36 \space kJ \cdot mol^{-1}
&\end{flalign}
$$

## Variation of reaction enthalpy with temperature

The enthalpies of reagents & products increase w/ temperature.
The difference between the enthalpies, then, changes accordingly.

==FIG.: 4D.6

**Kirchhoff's law**:
$\Delta H \degree (T_2) = \Delta H \degree (T_1) + (T_2 - T_1) \cdot \Delta C_p$
$\Delta C_p = C_p(\text{products}) - C_p(\text{reactants})$
$C_p(\text{products}), \space C_p(\text{reactants})$ - heat capacities of the reactants/products as a whole.

All the reactants/products heat up together, so their heat capacities must be added up.
Since there is $N(i) \space mol$ formula units of each compound $i$ in one mole of reactions:
$$
\begin{flalign}
&C_p = \sum_i N(i) \cdot C_{p, m}(i) 
&\end{flalign}
$$

Usually the difference between heat capacities is small enough to deem negligible.

## Ion formation

**Enthalpy of ionization** ($\Delta H_{\text{ion}}$) - change in standard enthalpy **per mole** of atoms for the loss of an $e^-$.

$\ce{X -> X+ (g) + e^- (g)}, \space \Delta H_{\text{ion}}$

Very similar in value to [ionization energy](Atom,%20orbitals#Cations) ($E_I$).
$\Delta H_{\text{ion}} = E_I + C$

**Enthalpy of electron gain** ($\Delta H_{\text{eg}}$) - change in standard enthalpy **per mole** of atoms for the gain of an $e^-$.

$\ce{X (g) + e^- (g) -> X- (g)}, \space \Delta H_{\text{eg}}$

Very similar numerically to [electron affinity](Atom,%20orbitals#Anions) ($E_a$), but w/ an opposite sign.
$\Delta H_{\text{ion}} = -(E_I + C)$

> Both are numerically only a couple $kJ \cdot mol^{-1}$ apart from their corresponding energies.

## Born-Haber cycle

**Lattice enthalpy** ($\Delta H_L$) - difference between the molar enthalpy of a gas & a solid of an ionic compound.
$\Delta H_L = H_m(\text{ions, g}) - H_m(\text{solid})$

**Born-Haber cycle** - procedure that helps to measure the lattice enthalpy.
Application of [[#Hess's law]].
Elements → ionized gas → ionic solid → elements
$\Delta H$ of the complete cycle is $0$.

Example ($\ce{NaCl}$):
$$
\begin{flalign}
&\Delta H_f \degree (\ce{NaCl}) = ? \\
&\text{By Hess's law } [\ce{Na (s) + Cl2 (g) -> NaCl (s)}] \text{ and } \\
&[\ce{Na (s) + Cl2 (s) -> Na (g) + Cl (g) -> Na+ (g) + Cl- (g) -> NaCl (s)}] \\
&\text{are equivalent ways to change the enthalpy of the reactants by } \Delta H_f \degree (\ce{NaCl}). \\
&\text{Equate:} \\
&\textcolor{orange}{\Delta H_f \degree (\ce{NaCl})} = \textcolor{cyan}{\Delta H_f \degree (\ce{Na}, g) + \Delta H_f \degree (\ce{Cl}, g) + \Delta H_{\text{ion}} (\ce{Na}) + \Delta H_{\text{eg}} (\ce{Cl})} - \textcolor{lime}{\Delta H_L (\ce{NaCl})} \\
&\textcolor{orange}{H_m (\ce{NaCl, s}) - H_m (\text{std. atoms})} = \textcolor{cyan}{H_m (\text{ions, g}) - H_m (\text{std. atoms})} - \textcolor{lime}{(H_m (\text{ions, g}) - H_m (\ce{NaCl, s}))}
&\end{flalign}
$$

## Bond enthalpy

**Bond enthalpy** ($\Delta H_B$) - difference between the standard molar enthalpies of a molecule ($\ce{X-Y}$) and its fragments ($\ce{X, Y}$) in the gas phase.
$\Delta H_B(\ce{X-Y}) = [H_m \degree (\ce{X, g}) + H_m \degree (\ce{Y, g})] - H_m \degree (\ce{X-Y, g})$
Heat required to break the bond.

$\Delta H_B >0$

> Bond breaking is always endothermic, bond formation is always exothermic.

> In practice, since in every molecule every atom acts on $e^-$ and bonds, the bond energies/enthalpies might be different depending on the molecule in question. Though the variation is not very big and **mean bond enthalpies** are used.

$\Delta H_B$ is numerically similar to dissociation energies.

Reaction enthalpy can be estimated by adding the enthalpies of the bonds broken and newly created in the substances.
