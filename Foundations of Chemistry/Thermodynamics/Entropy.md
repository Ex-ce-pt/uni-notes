
**Spontaneous change** - process that has a tendency to happen without external influence. (diffusion, cooling)

**Entropy** ($S$) - a measure of disorder/energy dispersion.
State function.
Energy that cannot be used to do work.

$\Delta S = \frac{q_{\text{rev}}}{T}, \space T = \text{const}$

| Symbol           | Unit             | Explanation                                                         |
| ---------------- | ---------------- | ------------------------------------------------------------------- |
| $\Delta S$       | $J \cdot K^{-1}$ | Change in entropy of the system                                     |
| $q_{\text{rev}}$ | $J$              | The heat the system acquired during a reversible isothermic process |
| $T$              | $K$              | The temperature of the system (the process is isothermic, const)    |

> As $T \rightarrow 0, \space S \rightarrow 0$, [the 3rd law of thermodynamics](Thermodynamics#Third%20law%20of%20thermodynamics)

Since temperature is constant, the temperature of the system must only be infinitesimally smaller than that of the surroundings for heat to be transferred.

Since entropy is a state function that can only be calculated for a reversible isothermal process (if using the equation above), a reversible process must be found such that the system ends up in the same desired state, with the same entropy.
Example: if it is asked to calculate entropy for an isothermally freely-expanded ideal gas, the same entropy can be achieved by calculating the entropy of an isothermally reversibly expanded ideal gas.

$S = k \cdot ln(W)$

| Symbol | Unit             | Explanation                                                                                                      |
| ------ | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| $S$    | $J \cdot K^{-1}$ | Entropy of the system                                                                                            |
| $k$    | $J \cdot K^{-1}$ | [Boltzman's constant](Cheat%20sheet#Constants)                                                                   |
| $W$    | $-$              | The \# of microstates of the system;<br>The \# of ways the molecules can be arranged<br>/w the same total energy |

Microstates link entropy to disorder. The more states are possible for the system, the more statistically likely it is that the state of the system is chaotic, rather than one of the less probable, orderly states.
They also link to [the 3rd law of thermodynamics](Thermodynamics#Third%20law%20of%20thermodynamics). As $T \rightarrow 0, \space S \rightarrow 0$ and further $k \cdot ln(W) \rightarrow 0 \Rightarrow ln(W) \rightarrow 0 \Rightarrow W \rightarrow 1$. At absolute zero (**unachievable**) any system would be in a single possible state.

#### Entropy and volume

Dispersion of matter in greater volume or mixing increase the entropy of the substance, because more microstates are possible.

Isothermal reversible expansion of an ideal gas (see [Work](Thermodynamics#Work)):
$$
\begin{flalign}
&\textcolor{grey}{\text{For an ideal gas: } \Delta U = q + w = 0 \Rightarrow q = -w} \\
&\textcolor{grey}{\text{For reversible isothermal expansion: } w = -nRT \cdot ln(\frac{V_2}{V_1})} \\
&\textcolor{grey}{\Delta S = \frac{q_{\text{rev}}}{T} = \frac{-w}{T} = \frac{-(-nRT\cdot ln(\frac{V_2}{V_1}))}{T} = nR \cdot ln(\frac{V_2}{V_1})} \\
&\Delta S = nR \cdot ln(\frac{V_2}{V_1})
&\end{flalign}
$$
Using this formula, the change in entropy in **both reversible and irreversible processes at any constant temperature** can be computed.

#### Entropy and pressure

[Boyle's law](States%20of%20matter#Derivation%20of%20the%20ideal%20gas%20equation): $p \cdot V = \text{const} \Rightarrow p \propto \frac{1}{V} \Rightarrow \frac{V_2}{V_1} = \frac{p_1}{p_2}$
$\Delta S = nR \cdot ln(\frac{p_1}{p_2})$

> Mind that the order changes!

#### Entropy and temperature

Increasing the temperature of the system increases the entropy, since the particles get more kinetic energy & move more vigorously.

$$
\begin{flalign}
&\textcolor{grey}{\text{Since the equation of entropy only works for constant temperatures,}} \\
&\textcolor{grey}{\text{consider a series of infinitesimal reversible isothermic transfers}} \\
&\textcolor{grey}{\text{of heat that would make up the whole process.}} \\
&\textcolor{grey}{S = \frac{q_{\text{rev}}}{T} \Rightarrow dS = \frac{dq_{\text{rev}}}{T}} \\
&\textcolor{grey}{C = \frac{q}{\Delta T} \Rightarrow q = C \cdot \Delta T \Rightarrow dq = C \cdot dT} \\
&\textcolor{grey}{dS = \frac{C}{T}dT} \\
&\textcolor{grey}{T_1 \text{ - initial temperature, } T_2 \text{ - final temperature.}} \\
&\textcolor{grey}{\Delta S = \int_{T_1}^{T_2} \frac{C}{T} dT \text{ - general case.}} \\
&\textcolor{grey}{\text{Assume } C = \text{const}: \Delta S = C \cdot [ln(T_2) - ln(T_1)]} \\
&\Delta S = C \cdot ln(\frac{T_2}{T_1})
&\end{flalign}
$$

Assuming the substance is a perfect crystal (no positional disorder at $T = 0$; $S(0) = 0$):
$\Delta S(T) = \int_{0}^{T} \frac{C(T)}{T}dT$

#### Entropy and physical state

**Normal melting/boiling point** - melting/boiling point at $1 \space atm$.
**Standard melting/boiling point** ($T_{\text{f}}$/$T_{\text{b}}$) - melting/boiling point at $1 \space bar$.

At the transition temperatures, temperature stays constant and all of the heat is used to drive the phase transition. (therefore, can use the temperature to compute the entropy change)
Assume phase transition happens at constant pressure, then $\Delta H = q$.

$\Delta S_{\text{vap}} = \frac{\Delta H_{\text{vap}}}{T_{\text{b}}}$

**Trouton's rule**: many standard entropies of vaporization are close to $85 \space J \cdot K^{-1} \cdot mol^{-1}$.
If a substance does not obey Trouton's rule, it probably has a more orderly structure while liquid than other substances.

$\Delta S_{\text{fus}} = \frac{\Delta H_{\text{fus}}}{T_\text{f}}$

If there is a need to find entropy of vaporization/fusion for other temperatures:
1. Heat the substance to the transition temperature.
2. Perform a phase transition.
3. Cool the transformed substance back to the starting temperature.

## Standard entropies

**Standard molar entropy** ($S_m \degree$) - entropy of $1 \space mol$ of substance at $1 \space bar$ and $298.15 \space K$.
**Standard reaction entropy** ($\Delta S \degree$) - the change in entropy of the system after the reaction.

$\Delta S \degree = \sum nS_m \degree (\text{products}) - \sum nS_m \degree  (\text{reactants})$

Some observations about molar entropy:
1. $S_m \degree (g) > S_m \degree (l) > S_m \degree (s)$
	The more intermolecular interactions are there in the substance, the less possibility for disorder there is. On the other hand, the less intermolecular interactions there are, the more freedom of movement there is.
2. $S_m \degree (\text{heavy}) > S_m \degree (\text{light})$
	The energy levels of heavier molecules are closer together, so at the same temperature the heavier molecules have more states to be in that the lighter molecules.
3. $S_m \degree (\text{complex}) > S_m \degree (\text{simple})$

## Global changes in entropy

$\Delta S_{\text{tot}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}}$

Exothermic reaction: $\Delta S_{\text{surr}} > 0$.
Endothermic reaction: $\Delta S_{\text{surr}} < 0$.

$\Delta S_{\text{tot}} > 0$ - spontaneous in forward direction.
$\Delta S_{\text{tot}} < 0$ - spontaneous in backwards direction.
$\Delta S_{\text{tot}} = 0$ - equilibrium.

> Even endothermic reactions can be spontaneous! For endothermic reactions, $\Delta S_{\text{surr}} < 0$, but if $\Delta S_{\text{sys}}$ increases enough to make $\Delta S_{\text{tot}} > 0$, the process is still spontaneous.

Surroundings:
1. Since they are generally large, assume **their temperature is always constant**.
2. Assume that any transfer of heat into them, from their perspective, is reversible.
	Both of these mean that $\Delta S_{\text{surr}} = \frac{q_{\text{surr}}}{T}$ **can be used always**!

$$
\begin{flalign}
&\textcolor{grey}{\text{For a system at constant pressure: } \Delta H = q_{\text{sys}}} \\
&\textcolor{grey}{\text{By the 1st law of thermodynamics: } q_{\text{surr}} = -q_{\text{sys}}} \\
&\textcolor{grey}{\Delta S_{\text{surr}} = \frac{q_{\text{surr}}}{T} = \frac{-q_{\text{sys}}}{T} = -\frac{\Delta H}{T}} \\
&\Delta S_{\text{surr}} = -\frac{\Delta H}{T}, \space T = \text{const}, \space p = \text{const}
&\end{flalign}
$$
$\Delta H$ is a state function - can use the equation in both reversible & irreversible processes.

> Though, *somehow*, $\Delta S_{\text{surr}}$ specifically can be thought of as a path function. Depending on the process, the surroundings can be left in a different state after different processes.

**Clausius inequality**:
$\Delta S \geq \frac{q}{T}$
$\Delta S = \frac{q}{T} \text{ for a reversible process, since } q_{\text{rev}} > q_{\text{irrev}}$
$\text{For an isolated system: } q = 0 \Rightarrow \Delta S \geq 0$ - [the 2nd law of thermodynamics](Thermodynamics#Second%20law%20of%20thermodynamics)

## Equilibrium


**Mechanical equilibrium** - same pressure in the system & the surroundings.
**Chemical equilibrium** - the reactions produce the same \# of reactants & products.

## Gibbs free energy

At **constant temperature & pressure**. Expansion work!
Allows to deduce spontaneity by only taking into account the system.

$G = H - TS, \space \Delta G = \Delta H - T \Delta S$

$\Delta G< 0$ - spontaneous in forward direction.
$\Delta G > 0$ - spontaneous in backwards direction.
$\Delta G = 0$ - equilibrium.

$\Delta G = w_{\text{e, max}} \text{ - maximum non-expansion work a system can do.}$
Proof:
$$
\begin{flalign}
&\textcolor{gray}{\text{Assume constant temperature and pressure.}} \\
&\textcolor{gray}{G = H - TS \Rightarrow dG = dH - TdS} \\
&\textcolor{gray}{dG = dU + pdV - TdS, \space dH = dU + pdV \space \text{(at constant pressure)}} \\
&\textcolor{gray}{dG = dw + dq + pdV - TdS} \\
&\textcolor{gray}{dG = dw_{\text{rev}} + dq_{\text{rev}} + pdV - TdS, \space \text{(maximum work done ina  reversible process)}} \\
&\textcolor{gray}{dG = dw_{\text{rev}} + TdS + pdV - TdS = dw_{\text{rev}} + pdV, \space dS = \frac{dq_{\text{rev}}}{T} \text{(at constant temperature)}} \\
&\textcolor{gray}{dG = dw_{\text{e, rev}} + dw_{\text{exp, rev}} + pdV, \space dw_{\text{rev}} = dw_{\text{e, rev}} + dw_{\text{exp, rev}}} \\
&\textcolor{gray}{dG = dw_{\text{e, rev}} - pdV + pdV = dw_{\text{e, rev}}, \space dw_{\text{exp, rev}} = -pdV \space \text{(at constant pressure)}} \\
&\textcolor{gray}{dG = dw_{\text{e, rev}}} \\
&\Delta G = w_{\text{e, max}}
&\end{flalign}
$$

$\Delta G \degree = \sum n \Delta G \degree _{f, \text{ products}} - \sum n \Delta G \degree _{f, \text{ reactants}}$

Over small temperature differences, assume $\Delta G$ does not change.

For an ideal gas: $G_m = G_m \degree + RT \cdot ln(\frac{p}{p \degree}), \space p \degree = 1 \space bar$
For a liquid: $G_m \approx G_m \degree$

**Thermodynamically stable compound** - compound /w $\Delta G \degree _f < 0$; its elements have a tendency to spontaneously combine into this compound.
**Thermodynamically unstable compound** - compound /w $\Delta G \degree _f > 0$; it has a tendency to spontaneously decompose.
**Nonlabile/inert compound** - compound that does not decompose in practice, despite being thermodynamically unstable.
**Labile compound** - compound that does decompose.
