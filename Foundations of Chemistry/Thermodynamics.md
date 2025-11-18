
## Definitions

Energy is transferred & transformed between different forms.
Heat is transferred between objects until equilibrium is reached.

**First law of thermodynamics** - energy cannot be created or destroyed; it can only be converted between different forms.
$\Delta U = q + w$
$\Delta U = 0$ - for the isothermal expansion of an ideal gas.

**Second law of thermodynamics** - no transfer of energy is 100% effective; there is always a loss.
**Third law of thermodynamics** - as temperature approaches 0, all processes slow down.

---
**System** - a given set of energy & matter.
**Surroundings** - everything but the system.
**Universe** - all existing the energy & matter combined.

$\text{Universe} = \text{System} \cup \text{Surroundings}$

**Open system** - can exchange both energy & matter /w the surroundings.
**Closed system** - can exchange energy /w the surroundings but not matter.
**Isolated system** - cannot exchange neither energy nor matter /w the surroundings.

**Adiabatic system** - cannot exchange energy (says nothing about the flow of matter).
**Diathermic system** - can exchange energy (says nothing about the flow of matter).

| Exchange     | Matter ✓ | Matter ✗ | Either     |
| ------------ | -------- | -------- | ---------- |
| **Energy ✓** | Open     | Closed   | Diathermic |
| **Energy ✗** |          | Isolated | Adiabatic  |

**Reversible process** - process that can be reversed by an infinitesimal change in a variable.
**Irreversible process** - process that cannot be reversed by an infinitesimal change in a variable.

**State functions** - properties of a system that depend only on the current state of the system, not how it reached that state. (Internal energy, pressure, temperature, density)

**Path functions** - properties of a system that depend on how it reached that state. ([[#Work]], [enthalpy](#Enthalpy))

**Thermal equilibrium** - the heat flows in both directions at the same rate.

> Equilibrium does not mean the heat flow does not happen! It does happen, just at an equal rate in both directions, so the net effect is zero.

## Properties

#### Work

**Work** ($w$) - achieving motion against an **opposing force**.

$w = F \cdot l$

| Symbol | Unit | Explanation                                 |
| ------ | ---- | ------------------------------------------- |
| $w$    | $J$  | Work performed                              |
| $F$    | $N$  | **Opposing** force counteracting the motion |
| $l$    | $m$  | The distance an object is moved by          |
[Unit](Cheat%20Sheet#Units): $[w] = J = N \cdot m = kg \cdot m^2 \cdot s^{-2}$

$w > 0$ - energy is supplied (work done on the system).
$w < 0$ - energy is lost (the system does work).

Work - transfer of energy **into** a system.

> **Opposing** force is very important! If there is not opposing force (e.g. a gas expanding its vessel against vacuum), no work is done!

**Expansion work** - work from a change in volume.
**Non-expansion work** - work that does not involve change in volume.
**Free expansion** - expansion against vacuum (**no work is done**).

$w = -p_{\text{ext}} \cdot \Delta V$

| Symbol           | Unit  | Explanation                                  |
| ---------------- | ----- | -------------------------------------------- |
| $w$              | $J$   | Expansion work done                          |
| $p_{\text{ext}}$ | $Pa$  | External pressure **opposing** the expansion |
| $\Delta V$       | $m^3$ | Difference in volume the system experiences  |

#### Energy

**Energy** ($E$) - capacity of a system to do work.
**Kinetic energy** - energy of motion.
**Potential energy** - energy of interaction (electrostatic, gravitational, etc.).
Unit: $J$

**Internal energy** ($U$):
1. Translational - linear motion.
2. Rotational - rotational motion.
3. Vibrational - vibrations of molecules.

By the first law of thermodynamics, $\Delta U = q + w$.
Given no heating, $\Delta U = w$.
That is why the [work](#Work) is negative when a system performs work on the surroundings.

#### Heat

**Heat** ($q$) - energy transferred between a system and its surroundings due to a temperature difference.
Unit: $J$

Ways to transfer heat:
1. **Conduction** - 2 particles physically collide with one another, exchanging kinetic energy (heat). 
2. **Convection** - happens in liquids/gases; matter heats up, expands, and rises, giving space for the colder matter to heat up.
3. **Radiation** - the atoms are radiating away photons when $e^-$ return to their ground state.

**Exothermic process** - heat is released into the surroundings.
**Endothermic process** - heat is absorbed from the surroundings.

$q > 0$ - heat enters the system.
$q < 0$ - heat escapes the system.

Given no work takes place, $\Delta U = q$.

#### Heat capacity

**Heat capacity** - how much heat the substance can contain.
$C = \frac{\Delta q}{\Delta T}$

| Symbol     | Unit | Explanation                                         |
| ---------- | ---- | --------------------------------------------------- |
| $C$        | $J$  | Work                                                |
| $\Delta q$ | $J$  | The heat supplied to the substance                  |
| $\Delta T$ | $K$  | The change in temperature the substance experiences |

**Specific heat capacity** - heat capacity per $1 \space kg$ of the substance.
$C_s = \frac{C}{m}$

**Molar heat capacity** - heat capacity per $1 \space mol$ of the substance.
$C_m = \frac{C}{n}$

**Heat capacity at constant volume** - exactly what it says.
$C_V = \frac{\Delta U}{\Delta T}, \space \Delta U = q \space (V = \text{const} \text{, no expansion work})$
$C_{V, m} = \frac{C_V}{n}$

**Heat capacity at constant pressure** - again, self-explanatory.
$C_p = \frac{\Delta H}{\Delta T}, \space \Delta H = q \space (p = \text{const} \text{, no non-expansion work})$
$C_{p, m} = \frac{C_p}{n}$

For an ideal gas:
$$
\begin{flalign}
&H = U + pV = U + nRT \\
&\Delta H = \Delta U + nR \cdot \Delta T \\
&C_p = \frac{\Delta H}{\Delta T} = \frac{\Delta U + nR \cdot \Delta T}{\Delta T} = \frac{\Delta U}{\Delta T} + \frac{nR \cdot \Delta T}{\Delta T} = C_V + nR \\
&C_{p, m} = C_{V, m} + R
&\end{flalign}
$$

#### Enthalpy

**Enthalpy** ($H$) - a state function that keeps track of losses of energy to expansion work during heat transfer at constant pressure.

$H = U + pV$

$$
\begin{flalign}
&H = U + pV, \space p = \text{const} \\
&\Delta H = \Delta U + p \cdot \Delta V \\
&\Delta H = q + w + p \cdot V \\
&\text{If no non-expansion work: } w = -p_{\text{ext}} \cdot \Delta V \\
&\text{If the vessel is open or adjusts to the volume of the substance: } p_{\text{ext}} = p \\
&\Delta H = q - p \cdot \Delta V + p \cdot \Delta V \\
&\Delta H = q
&\end{flalign}
$$
At constant pressure & no non-expansion work: $\Delta H = q$.

**Exothermic reaction** - reaction that releases heat ($\Delta H < 0$).
**Endothermic reaction** - reaction that absorbs heat ($\Delta H > 0$).

Since enthalpy is a state function, **it does not matter which steps were taken, only the current state of the system**: $H_1 \rightarrow H_2 \rightarrow H_3 \Leftrightarrow H_1 \rightarrow H_3$.

Physical change:
For substances, $H_m = \frac{H}{n}$ - molar enthalpy.

|              | $\Delta H_{\text{state change}} = H_m(\text{target state}) - H_m(\text{source state})$                        | $\Delta H_{\text{forward change}} = -\Delta H_{\text{backwards change}}$ |
| ------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Gas/Liquid   | $\Delta H_{\text{vap}} = H_m(\text{gas}) - H_m(\text{liquid})$                                                | $\Delta H_{\text{cond}} = -\Delta H_{\text{vap}}$                        |
| Liquid/Solid | $\Delta H_{\text{fus}} = H_m(\text{liquid}) - H_m(\text{solid})$                                              | $\Delta H_{\text{freeze}} = -\Delta H_{\text{fus}}$                      |
| Gas/Solid    | $\Delta H_{\text{sub}} = H_m(\text{gas}) - H_m(\text{solid}) = \Delta H_{\text{vap}} + \Delta H_{\text{fus}}$ | $\Delta H_{\text{desub}} = -\Delta H_{\text{sub}}$                       |

## Calorimetry

**Calorimetry** - a technique used to calculate enthalpy changes for a chemical or physical process.

**Calorimeter** - a tool used for calorimetry.

The heat from a sample is transferred to water and the temperature difference before and after the experiment is compared.

## Heating curve

**Heating curve** - a curve describing the temperature & phase changes during the process of heating/cooling.

Temperature does not rise until a phase change has been completed fully.

**Superheating** - rapidly heating up a substance higher than its boiling point.
**Supercooling** - rapidly cooling down a substance below its freezing point.

When a substance in superheated or supercooled, the temperature immediately returns to the boiling point as soon as the phase transition starts.
