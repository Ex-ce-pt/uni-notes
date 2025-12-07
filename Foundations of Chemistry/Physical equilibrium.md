
$\Delta S_{\text{tot}} = 0, \space \Delta G = 0$

**Dynamic equilibrium** - same rate in both directions.

> All equilibriums in chemistry are dynamic. Processes are still ongoing on the microscopic level, but there is no net change.

## Vapor pressure

Temperature is a measure of average kinetic energy of the molecules in a substance. Some of the molecules naturally have a higher kinetic energy and are able to escape (evaporate) even below the boiling temperature of the liquid. These particles transition into the gaseous phase & start contributing to the external pressure. At the same time, these same particles loose their kinetic energy by chance & condensate. At some point the pressure is high enough so that evaporation & condensation are in equilibrium.

![[equilibrium/vapor-pressure.png]]

$\ce{H2O (l) \leftrightharpoons H2O (g)}, \space \Delta S = 0, \space \Delta G = 0$

**Vapor pressure** - pressure of the **vapor** of a liquid (or a solid) at the equilibrium between evaporation & condensation.

> Vapor pressure is, as the name implies, the pressure of the **vapor**. That means that if the system's gas has other substances, the vapor pressure is the **partial pressure of the vapor** only.

Substances /w less/weaker [intermolecular interactions](Intermolecular%20interactions) are more **volatile** & have a higher vapor pressure.

Higher vapor pressure:
- More volatile;
- More molecules in the gaseous phase;
- (usually) Lower boiling point;
- Lower $\Delta H_{\text{vap}}$.

**Higher temperature** → more kinetic energy → particles escape more → **higher vapor pressure**

**Clausius-Clapeyron equation**:
$ln(\frac{p_2}{p_1}) = -\frac{\Delta H_{\text{vap}} \degree}{R}(\frac{1}{T_2} - \frac{1}{T_1})$
$p_1, \space p_2 \text{ - vapor pressures of the substance at temperatures } T_1, \space T_2 \text{ respectfully}$

$ln(p) = A - \frac{B}{T}$
$A, \space B \text{ - depend on the substance, meant to be looked up in the tables}$

#### Boiling

**Boiling** happens when the vapor pressure is equal to the external (atmospheric) pressure.
At the boiling point, instead of the surroundings pushing on the vapor, the vapor starts pushing on the surroundings instead, making more room for itself, and letting the rest of the liquid evaporate (boil) easily.

![[equilibrium/boiling.png]]

| Process         | Location   | Temperature   | Pressure                   | Bubbles | External energy |
| --------------- | ---------- | ------------- | -------------------------- | ------- | --------------- |
| **Evaporation** | Surface    | Any           | $\text{vp} < \text{ext.p}$ | No      | Not mandatory   |
| **Boiling**     | Throughout | Boiling point | $\text{vp} = \text{ext.p}$ | Yes     | Must supply     |

## Phase diagram

#### One component phase diagram

**Phase diagram** - diagram showing the most stable phase at particular conditions.

**Phase boundary** (line) - conditions at which the substance transitions phases; 2 phases exist in equilibrium.
**Triple point** (intersection) - conditions at which 3 phases of the substance exist in equilibrium.
**Critical point** (end of a line) - point beyond which the substance becomes a supercritical fluid. Liquid and gas phases cease to exist as separate phases.
**Supercritical fluid** - density of a liquid, flow of a gas. Used as a solvent.

![[equilibrium/phase-diagram-example.png]]

| Liquid denser than solid (water)         | Solid denser than liquid (most)          |
| ---------------------------------------- | ---------------------------------------- |
| Pressure increases → melting point falls | Pressure increases → melting point rises |
| ![[equilibrium/phase-diagram-water.png]] | ![[equilibrium/phase-diagram-CO2.png]]   |

#### Two component phase diagram

**Raoult's law**:
$p_A = x_A \cdot p_A^*$

| Symbol  | Unit | Explanation                                         |
| ------- | ---- | --------------------------------------------------- |
| $p_A$   | $Pa$ | Vapor pressure of the substance $A$ in the solution |
| $x_A$   | $-$  | Molar fraction of the substance $A$ in the solution |
| $p_A^*$ | $Pa$ | Vapor pressure of the substance $A$ if it were pure |
Put simply: a substance contributes vapor pressure proportionally to its content in the solution.

Using Dalton's law:
$p = \sum p_i = \sum x_i \cdot p_i^*$
The total vapor pressure of a solution is the sum of the vapor pressures of the parts of the solution.

> A solute always lowers the vapor pressure of a solvent.

**Ideal solution** - the solvent and the solute have exactly the same [intermolecular interactions](Intermolecular%20interactions). Both components obey Raoult's law at all concentrations. $\Delta H_{\text{sol}} = 0$.
**Real solution** - does not obey Raoult's law at all concentrations. The smallel the concentration of the solute, the more resembles an ideal solution ($c < 0.1 \space M$).

Phase diagrams also work /w two-component systems, but they are usually more complicated than this simple one. Pressure is assumed to be constant at $p = 1 \space atm$ for practical purposes.
![[equilibrium/phase-diagrams-binary-example.png]]

**Enthalpy of mixing** ($\Delta H_{\text{mix}}$) - difference in enthalpy between the mixture & pure components.

When a solution boils, there will be more molecules of the more volatile liquid in the gaseous phase. Phase diagrams like this show the concentration of a part of the solution in both phases. At a specific concentration ($x(l)$), the solution boils at a specific temperature ($T_b$). The second graph then shows the concentration ($x(g)$) of the part of the solution in the vapor at the same temperature.
![[equilibrium/phase-diagrams-binary-vapor.png]]

#### Fractional distillation

Method for separating mixtures of liquids /w similar boiling points. Works well /w solutions close to ideal solutions.

![[equilibrium/phase-diagrams-binary-fractional-distillation.png]]

The mixture is boiled. The composition of the more volatile component in the vapor is greater than in the original liquid. The vapor condensates. The new liquid is boiled again, once again increasing the concentration of the more volatile component. The process is repeated many times.

In practice, fractional distillation happens as a single process in fractionating columns. The vapor continuously evaporates & condensates inside the column, and the more volatile component comes out on top.

**Distillate** - the condensed vapor from the distillation process; the liquid coming out of the fractionating column.
**Fraction** - a component of the original mixture separated using fractional distillation.

#### Azeotropes

**Azeotrope** - a mixture, the vapor of which has the same composition as the mixture itself; cannot be separated /w fractional distillation.

Azeotropes are formed by real solutions.

| Minimum boiling azeotrope                                                                                | Maximum boiling azeotrope                                                                                 |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ![[equilibrium/azeotrope-minimum.png]]                                                                   | ![[equilibrium/azeotrope-maximum.png]]                                                                    |
| The vapor of the mixture approaches the azeotropic concentration & as much of it is created as possible. | The leftover mixture approaches the azeotropic concentration & the rest of the components are boiled off. |
| The more volatile azeotropic mixture is obtained as a distillate.                                        | The less volatile azeotropic mixture is left in the flask.                                                |

## Solubility

Measured in either mass of solute per volume of solvent ($g \cdot l^{-1}$) or molar concentration ($mol \cdot l^{-}$).

**Saturated solution** - solution has maximum amount of solute at given conditions.
**Molar solubility** ($s$) - molar concentration of the solute in a saturated solution.

In saturated solutions, the dissolved & undissolved solute are in dynamic equilibrium.

> Like-dissolves-like
> Substance dissolves in the solvent, if they both have the same kind of [intermolecular interactions](Intermolecular%20interactions).

Solute lowers the [Gibbs free energy](Entropy#Gibbs%20free%20energy) of the solvent by increasing [entropy](Entropy).
The solution is then less volatile than the pure solvent & more condensation takes place.

#### Gases

**Henry's law**:
$s = k_H \cdot p$

| Symbol | Unit                             | Explanation                                                                   |
| ------ | -------------------------------- | ----------------------------------------------------------------------------- |
| $s$    | $mol \cdot l^{-1}$               | Molar solubility of a gas in the solvent                                      |
| $k_H$  | $mol \cdot l^{-1} \cdot Pa^{-1}$ | Henry's contant; depends on the gas, solvent, and temperature                 |
| $p$    | $Pa$                             | Pressure of the gas (or partial pressure, if there is a mixture of the gases) |

Higher pressure → more of gas dissolves in a liquid

#### Temperature

Higher temperature → higher **rate** of dissolving

Most solids: higher temperature → higher solubility
Most gases: higher temperature → lower solubility

#### Enthalpy of solution

**Enthalpy of solution** ($\Delta H_{\text{sol}}$) - change in molar enthalpy when a substance dissolves.
$\Delta H_{\text{sol}} = \Delta H_{\text{L}} + \Delta H_{\text{hyd}}$
$\Delta H_{\text{L}} > 0 \text{ - lattice enthalpy to separate the ions of the solute}$
$\Delta H_{\text{hyd}} < 0 \text{ - enthalpy of hydration to place ions between solvent molecules}$

Dissolving can be both exothermic ($\ce{CaCl2}$) or endothermic ($\ce{NH4Cl}$).

#### Colloids

**Colloid** - dispersion of small solid particles ($1 \space nm$ to $1 \space \mu m$) in a solvent.

| Type         | Constituents        | Examples          |
| ------------ | ------------------- | ----------------- |
| **Sol**      | solid in liquid     | Blood, paint, mud |
| **Emulsion** | liquid in liquid    | Milk              |
| **Foam**     | gas in liquid/solid | Soap, sponge      |

**Brownian motion** - motion of a small particle from constant bombardment of solvent molecules.

**Colligative properties** - depend only on the relative amount of solute & solvent, independent of the chemical identity of the solute.

- Molar concentration: $c = \frac{n}{V}$
- Mole fraction: $x_{\text{solute}} = \frac{n_{\text{solute}}}{n_{\text{tot}}}$
- Molality: $b = \frac{n_{\text{solute}}}{m_{\text{solvent}}}$
- $\Delta T_{\text{f}}$

Solute increases boiling point and lowers freezing point.

$\Delta T_{\text{f}} = i \cdot k_\text{f} \cdot b$

| Symbol                | Unit | Explanation             |
| --------------------- | ---- | ----------------------- |
| $\Delta T_{\text{f}}$ | $K$  | ??                      |
| $i$                   | $-$  | Van't Hoff factor       |
| $k_{\text{f}}$        | $?$  | Freezing-point constant |
| $b$                   | $Pa$ | Molality of the solute  |

Most non-electrolytes in water: $i \approx 1$

#### Osmosis

**Osmosis** - movement of the solvent molecule across a semi-permeable membrane from a region of high concentration into a region of low concentration.
==?????????

**Osmosis pressure** ($\Pi$) - pressure needed to stop osmosis.
Measures now strongly osmosis pulls the solvent in.

$\Pi = iRTc$

| Symbol | Unit               | Explanation                                   |
| ------ | ------------------ | --------------------------------------------- |
| $\Pi$  | $Pa$               | Osmosis pressure                              |
| $i$    | $-$                | Van't Hoff factor                             |
| $R$    | $Pa$               | [Ideal gas constant](Cheat%20Sheet#Constants) |
| $T$    | $K$                | Temperature of the solution                   |
| $c$    | $mol \cdot l^{-1}$ | Concentration of the solute in the solution   |



Cryoscopy - ...

Osmometry - ...