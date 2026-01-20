
$\Delta S_{\text{tot}} = 0, \space \Delta G = 0$

**Dynamic equilibrium** - same rate in both directions.

> All equilibriums in chemistry are dynamic. Processes are still ongoing on the microscopic level, but there is no net change.

## Vapor pressure

Temperature is a measure of average kinetic energy of the molecules in a substance. Some of the molecules naturally have a higher kinetic energy and are able to escape (evaporate) even below the boiling temperature of the liquid. These particles transition into the gaseous phase & start contributing to the external pressure, holding the other molecules down. At the same time, these same particles loose their kinetic energy by chance & condensate. At some point the pressure is high enough so that evaporation & condensation are in equilibrium.

![[equilibrium/vapor-pressure.png]]

$\ce{H2O (l) \rightleftharpoons H2O (g)}, \space \Delta S = 0, \space \Delta G = 0$

**Vapor pressure** - pressure of the **vapor** of a liquid (or a solid) at the equilibrium between evaporation & condensation.

> Vapor pressure is, as the name implies, the pressure of the **vapor**. That means that if the system's gas has other substances, the vapor pressure is the **partial pressure of the vapor** only.

Substances w/ less/weaker [intermolecular interactions](Intermolecular%20interactions) are more **volatile** & have a higher vapor pressure.

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
At the boiling point, instead of the surroundings pushing on the vapor, the vapor starts pushing on the surroundings, making more room for itself, and letting the rest of the liquid evaporate (boil) easily.

![[equilibrium/boiling.png]]

| Process         | Location   | Temperature   | Pressure                   | Bubbles | External energy |
| --------------- | ---------- | ------------- | -------------------------- | ------- | --------------- |
| **Evaporation** | Surface    | Any           | $\text{vp} < \text{ext.p}$ | No      | Not mandatory   |
| **Boiling**     | Throughout | Boiling point | $\text{vp} = \text{ext.p}$ | Yes     | Must supply     |

## Phase diagram

#### One component phase diagram

**Phase diagram** - diagram showing the most stable phase at particular conditions.

**Phase boundary** (line) - conditions at which the substance transitions between phases; 2 phases exist in equilibrium.
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

| Symbol  | Unit | Comment                                         |
| ------- | ---- | --------------------------------------------------- |
| $p_A$   | $Pa$ | Vapor pressure of the substance $A$ in the solution |
| $x_A$   | $-$  | Molar fraction of the substance $A$ in the solution |
| $p_A^*$ | $Pa$ | Vapor pressure of the substance $A$ if it were pure |
Put simply: a substance contributes vapor pressure proportionally to its content in the solution.

Using Dalton's law:
$p = \sum p_i = \sum x_i \cdot p_i^*$
The total vapor pressure of a solution is the sum of the vapor pressures of the parts of the solution.

> A solid solute always lowers the vapor pressure of a solvent.

**Ideal solution** - the solvent and the solute have exactly the same [intermolecular interactions](Intermolecular%20interactions). Both components obey Raoult's law at all concentrations. $\Delta H_{\text{sol}} = 0$.
**Real solution** - does not obey Raoult's law at all concentrations. The smaller the concentration of the solute, the more resembles an ideal solution ($c < 0.1 \space M$).

Raoult's law predicts that the phase diagram for an ideal solution is a straight line.

Phase diagrams also work w/ two-component systems, but they are usually more complicated than this simple one. Pressure is assumed to be constant at $p = 1 \space atm$ for practical purposes.
![[equilibrium/phase-diagrams-binary-example.png]]

**Enthalpy of mixing** ($\Delta H_{\text{mix}}$) - difference in enthalpy between the mixture & pure components.

==mb enthalpy of solution is the same???

When a solution boils, there will be more molecules of the more volatile liquid in the gaseous phase. Phase diagrams like this show the concentration of a part of the solution in both phases. At a specific concentration ($x(l)$), the solution boils at a specific temperature ($T_b$). The second graph then shows the concentration ($x(g)$) of the part of the solution in the vapor at the same temperature.
![[equilibrium/phase-diagrams-binary-vapor.png]]

Deviations from Raoult's law:

| Positive                                                   | Negative                                                    |
| ---------------------------------------------------------- | ----------------------------------------------------------- |
| $\Delta H_{\text{mix}} > 0$, endothermic                   | $\Delta H_{\text{mix}} < 0$, exothermic                     |
| Interactions between the same molecules are more favorable | Interactions between different molecules are more favorable |


#### Fractional distillation

Method for separating mixtures of liquids w/ similar boiling points. Works well w/ solutions close to ideal solutions.

![[equilibrium/phase-diagrams-binary-fractional-distillation.png]]

The mixture is boiled. The composition of the more volatile component in the vapor is greater than in the original liquid. The vapor condensates. The new liquid is boiled again, once again increasing the concentration of the more volatile component. The process is repeated many times.

In practice, fractional distillation happens as a single process in fractionating columns. The vapor continuously evaporates & condensates inside the column, and the more volatile component comes out on top.

**Distillate** - the condensed vapor from the distillation process; the liquid coming out of the fractionating column.
**Fraction** - a component of the original mixture separated using fractional distillation.

#### Azeotropes

**Azeotrope** - a mixture, the vapor of which has the same composition as the mixture itself; cannot be separated w/ fractional distillation.

Azeotropes are formed by real solutions.

| Minimum boiling azeotrope                                                                                | Maximum boiling azeotrope                                                                                 |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ![[equilibrium/azeotrope-minimum.png]]                                                                   | ![[equilibrium/azeotrope-maximum.png]]                                                                    |
| The vapor of the mixture approaches the azeotropic concentration & as much of it is created as possible. | The leftover mixture approaches the azeotropic concentration & the rest of the components are boiled off. |
| The more volatile azeotropic mixture is obtained as a distillate.                                        | The less volatile azeotropic mixture is left in the flask.                                                |
| Positive deviation from Raoult's law                                                                     | Negative deviation from Raoult's law                                                                      |

> Don't mix these graphs up with the graphs of vapor pressure vs composition!

> Remember, vapor pressure and boiling point have an inverse relationship, so the graphs of boiling point vs composition are exactly opposite of the graphs of vapor pressure vs composition.

[Another explanation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Equilibria/Physical_Equilibria/Non-Ideal_Mixtures_of_Liquids)

