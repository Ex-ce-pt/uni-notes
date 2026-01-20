
## Laws of thermodynamics

#### Zeroth law of thermodynamics

If 2 systems are in thermal equilibrium with a 3rd, then they are in thermal equilibrium with each other.
The state of being in a thermal equilibrium is transitive: $A=B, \space B=C \Rightarrow A=C$.

#### First law of thermodynamics

**First law of thermodynamics** - energy cannot be created or destroyed; it can only be converted between different forms.
$\Delta U = q + w$
$\Delta U = 0 \Leftrightarrow q = -w$ - for the isothermal expansion of an ideal gas.
Isothermal → no heat goes towards heating the gas, all the heat goes towards expansion work.

#### Second law of thermodynamics

**Second law of thermodynamics** - no transfer of energy is 100% effective; there is always a loss.
The [entropy](Entropy) of an isolated system increases in the course of any spontaneous process.
$\Delta S_{\text{tot}} \geq 0$
"Isolated system" in practice usually means the universe.

#### Third law of thermodynamics

**Third law of thermodynamics** - as temperature approaches $0$, all processes slow down.
The entropy of all perfect crystals approaches $0$ as the absolute temperature approaches $0$.
$T \rightarrow 0, \space S \rightarrow 0$ - from the definition of [entropy](Entropy).

## Definitions

Energy is transferred & transformed between different forms.
Heat is transferred between objects until equilibrium is reached.

**System** - a given set of energy & matter.
**Surroundings** - everything but the system.
**Universe** - all existing energy & matter combined.

$\text{Universe} = \text{System} \cup \text{Surroundings}$

**Open system** - can exchange both **energy** & **matter** w/ the surroundings.
**Closed system** - can exchange **energy** w/ the surroundings but **not matter**.
**Isolated system** - cannot exchange **neither energy nor matter** w/ the surroundings.

**Adiabatic walls** - cannot exchange energy (says nothing about the flow of matter).
**Diathermic walls** - can exchange energy (says nothing about the flow of matter).

| Exchange     | Matter ✓ | Matter ✗ | Either     |
| ------------ | -------- | -------- | ---------- |
| **Energy ✓** | Open     | Closed   | Diathermic |
| **Energy ✗** |          | Isolated | Adiabatic  |

**Reversible process** - process that can be reversed by an infinitesimal change in a variable (the system is in equilibrium during the whole process).
**Irreversible process** - process that cannot be reversed by an infinitesimal change in a variable.

**State functions** - properties of a system that depend only on the current state of the system, not how it reached that state (e.g. [internal energy](#Energy), pressure, temperature, density).
**Path functions** - properties of a system that depend on how it reached that state ([work](#Work)).

**Thermal equilibrium** - the heat flows in both directions at the same rate.

> Equilibrium does not mean the heat flow does not happen! It does happen, just at an equal rate in both directions, so the net effect is zero.

## Properties

#### Work
**Path function.**

**Work** ($w$) - achieving motion against an **opposing force**.

$w = F \cdot l$

| Symbol | Unit | Comment                                 |
| ------ | ---- | ------------------------------------------- |
| $w$    | $J$  | Work performed                              |
| $F$    | $N$  | **Opposing** force counteracting the motion |
| $l$    | $m$  | The distance an object is moved by          |
[Unit](Cheat%20Sheet#Units): $[w] = J = N \cdot m = kg \cdot m^2 \cdot s^{-2}$

$w > 0$ - energy is supplied (work done on the system).
$w < 0$ - energy is lost (the system does work).

Work - transfer of energy **into** a system.

> **Opposing** force is very important! If there is no opposing force (e.g. a gas expanding its vessel against vacuum), no work is done!

**Expansion work** - work from a change in volume.
**Non-expansion work** - work that does not involve change in volume (biochemical synthesis, electrical work, mechanical work).
**Free expansion** - expansion against vacuum (**no work is done**).

$w = -p_{\text{ext}} \cdot \Delta V$

| Symbol           | Unit  | Comment                                  |
| ---------------- | ----- | -------------------------------------------- |
| $w$              | $J$   | Expansion work done                          |
| $p_{\text{ext}}$ | $Pa$  | External pressure **opposing** the expansion |
| $\Delta V$       | $m^3$ | Difference in volume the system experiences  |

Isothermal reversible expansion of an ideal gas:
$$
\begin{flalign}
&\textcolor{grey}{w = -p_{\text{ext}}V \Rightarrow dw = -p_{\text{ext}} \cdot dV} \\
&\textcolor{grey}{\text{Since the process is reversible, } p_{\text{ext}} = p} \\
&\textcolor{grey}{dw = -p \cdot dV = -\frac{nRT}{V} dV, \space (pV = nRT)} \\
&\textcolor{grey}{V_1 \text{ - initial volume, } V_2 \text{ - final volume}} \\
&\textcolor{grey}{\int_{V_1}^{V_2} dw = \int_{V_1}^{V_2} -\frac{nRT}{V} dV} \\
&\textcolor{grey}{w(V_2) - w(V_1) = -nRT [ln(V_2) - ln(V_1)]} \\
&\textcolor{grey}{\text{No work was done at initial volume: } w(V_1) = 0} \\
&\textcolor{grey}{w(V_2) = w = -nRT \cdot ln(\frac{V_2}{V_1})} \\
&w = -nRT \cdot ln(\frac{V_2}{V_1})
&\end{flalign}
$$
**The work performed during a reversible process is the maximum amount of work a system can perform.** It is because at every point in time the force opposing the work is only infinitesimally smaller (essentially equal) than the force of the system. That means that during the course of the process, the system pushed against the maximum possible force that would still result in the process ending successfully.

#### Energy
**State function.**

**Energy** ($E$) - capacity of a system to do work.
**Kinetic energy** - energy of motion.
**Potential energy** - energy of interaction (electrostatic, gravitational, etc.).
Unit: $J$

**Internal energy** ($U$):
1. Translational - linear motion.
2. Rotational - rotational motion.
3. Vibrational - vibrations of molecules.
4. [Intermolecular interactions](Atomic Structure/Intermolecular interactions) - stored chemical energy.

By the [first law of thermodynamics](#First%20law%20of%20thermodynamics), $\Delta U = q + w$.
Given no heating, $\Delta U = w$.
That is why the [work](#Work) is negative when a system performs work on the surroundings.

#### Heat
**Path function.**

**Heat** ($q$) - energy transferred between a system and its surroundings due to a temperature difference.
Unit: $J$

Ways to transfer heat:
1. **Conduction** - 2 particles physically collide with one another, exchanging kinetic energy (heat). 
2. **Convection** - happens in liquids/gases; matter heats up, expands, and rises, giving space for the colder matter to heat up.
3. **Radiation** - the atoms radiate away photons when $e^-$ return to their ground state.

**Exothermic process** - heat is released into the surroundings.
**Endothermic process** - heat is absorbed from the surroundings.

$q > 0$ - heat enters the system.
$q < 0$ - heat escapes the system.

Given no work takes place, $\Delta U = q$.
Alternative wording: constant volume & no non-expansion work: $\Delta U = q$.

> Heat is not the same as temperature! It is possible for a system to absorb heat without raising its own temperature! Example: absorbed heat immediately being used to do work.

#### Heat capacity

**Heat capacity** - how much heat the substance can contain.
$C = \frac{q}{\Delta T}$

| Symbol     | Unit             | Comment                                         |
| ---------- | ---------------- | --------------------------------------------------- |
| $C$        | $J \cdot K^{-1}$ | Heat capacity of the substance                      |
| $q$        | $J$              | The heat supplied to the substance                  |
| $\Delta T$ | $K$              | The change in temperature the substance experiences |

**Specific heat capacity** - heat capacity per $1 \space kg$ of the substance.
$C_s = \frac{C}{m}$

**Molar heat capacity** - heat capacity per $1 \space mol$ of the substance.
$C_m = \frac{C}{n}$

**Heat capacity at constant volume** - exactly what it says.
$C_V = \frac{\Delta U}{\Delta T}, \space \Delta U = q \space (V = \text{const} \text{, no non-expansion work})$
$C_{V, \space m} = \frac{C_V}{n}$

**Heat capacity at constant pressure** - again, self-explanatory.
$C_p = \frac{\Delta H}{\Delta T}, \space \Delta H = q \space (p = \text{const} \text{, no non-expansion work})$
$C_{p, \space m} = \frac{C_p}{n}$

For an ideal gas:
$$
\begin{flalign}
&\textcolor{grey}{H = U + pV = U + nRT} \\
&\textcolor{grey}{\Delta H = \Delta U + nR \cdot \Delta T} \\
&\textcolor{grey}{C_p = \frac{\Delta H}{\Delta T} = \frac{\Delta U + nR \cdot \Delta T}{\Delta T} = \frac{\Delta U}{\Delta T} + \frac{nR \cdot \Delta T}{\Delta T} = C_V + nR} \\
&C_{p, \space m} = C_{V, \space m} + R
&\end{flalign}
$$

For a monoatomic ideal gas:
$C_{V, \space m} = \frac{3}{2}R, \space C_{p, \space m} = \frac{5}{2}R$

## Calorimetry

**Calorimetry** - a technique used to calculate enthalpy changes for a chemical or physical process.

**Calorimeter** - a tool used for calorimetry.

The heat from a sample is transferred to water and the temperature difference before and after the experiment is compared.

**Cup calorimeter** - constant pressure.
**Bomb calorimeter** - constant volume.

## Heating curve

**Heating curve** - a curve describing the temperature & phase changes during the process of heating/cooling.

![[thermochemistry/heating-curve.png]]

Temperature does not rise until a phase change has been completed fully.

**Superheating** - rapidly heating up a substance higher than its boiling point.
**Supercooling** - rapidly cooling down a substance below its freezing point.

When a substance in superheated or supercooled, the temperature immediately returns to the boiling point as soon as the phase transition starts.
