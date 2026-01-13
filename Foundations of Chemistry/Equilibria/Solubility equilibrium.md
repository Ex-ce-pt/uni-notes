
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

**Enthalpy of solution** ($\Delta H_{\text{sol}}$) - change in molar enthalpy when a substance is dissolved.
$\Delta H_{\text{sol}} = \Delta H_{\text{L}} + \Delta H_{\text{hyd}}$
$\Delta H_{\text{L}} > 0 \text{ - lattice enthalpy to separate the ions of the solute}$
$\Delta H_{\text{hyd}} < 0 \text{ - enthalpy of hydration to place ions between solvent molecules}$

Dissolving can be both exothermic ($\ce{CaCl2}$) or endothermic ($\ce{NH4Cl}$).

#### Colloids

**Colloid** - dispersion of small solid particles ($1 \space nm$ to $1 \space \mu m$) in a solvent.

Colloids scatter light.

| Type         | Constituents        | Examples          |
| ------------ | ------------------- | ----------------- |
| **Sol**      | solid in liquid     | Blood, paint, mud |
| **Emulsion** | liquid in liquid    | Milk              |
| **Foam**     | gas in liquid/solid | Soap, sponge      |
| **Aerosol**  | solid/liquid in gas | Smoke, mist       |

**Brownian motion** - motion of a small particle from constant bombardment of solvent molecules.

#### Colligative properties

**Colligative properties** - depend only on the relative amount of solute & solvent, independent of the chemical identity of the solute.

- Molar concentration: $c = \frac{n}{V}$
- Mole fraction: $x_{\text{solute}} = \frac{n_{\text{solute}}}{n_{\text{tot}}}$
- Molality: $b = \frac{n_{\text{solute}}}{m_{\text{solvent}}}$
- Boiling point elevation: $\Delta T_b$ (insignificant)
- Freezing point depression: $\Delta T_{\text{f}}$
- [Osmotic pressure](#Osmosis): $\Pi$

Solute increases the boiling point a little and lowers the freezing point significantly.

$\Delta T_{\text{f}} = i \cdot k_\text{f} \cdot b$

| Symbol                | Unit                        | Explanation                                        |
| --------------------- | --------------------------- | -------------------------------------------------- |
| $\Delta T_{\text{f}}$ | $K$                         | Freezing point depression                          |
| $i$                   | $-$                         | Van't Hoff factor                                  |
| $k_{\text{f}}$        | $K \cdot kg \cdot mol^{-1}$ | Freezing-point constant; determined experimentally |
| $b$                   | $mol \cdot kg^{-1}$         | Molality of the solute                             |

For non-electrolyte solutions, $i = 1$.
$i$ accounts for the fact that in electrolytes, all the ions act as separate particles and contribute to the freezing point depression.
$\ce{NaCl} \rightarrow i = 2, \space \ce{Na2SO4} \rightarrow i = 3, \space ... \text{(assuming complete dissociation)}$

**Cryoscopy** - determining of the molar mass by measuring the freezing point depression.
Rarely used nowadays.

#### Osmosis

**Osmosis** - movement of the **solvent** molecules across a semi-permeable membrane from a region of high concentration into a region of low concentration.

**Semi-permeable membrane** - membrane that lets one type of particles pass, but not the others.

Solute particles are blocking the solvent molecules from escaping into a region o flow concentration and are also binding the solvent molecules. (water hydrates ions of electrolytes)

**Osmosis pressure** ($\Pi$) - pressure needed to stop osmosis.
Measures now strongly osmosis pulls the solvent in.

van't Hoff equation:
$\Pi = iRTc$

| Symbol | Unit               | Explanation                                   |
| ------ | ------------------ | --------------------------------------------- |
| $\Pi$  | $Pa$               | Osmotic pressure                              |
| $i$    | $-$                | Van't Hoff factor                             |
| $R$    | $Pa$               | [Ideal gas constant](Cheat%20Sheet#Constants) |
| $T$    | $K$                | Temperature of the solution                   |
| $c$    | $mol \cdot l^{-1}$ | Concentration of the solute in the solution   |

**Reverse osmosis** - applying pressure higher than osmotic pressure to forcefully move the solvent to a region of low concentration.

**Osmometry** - determining of the molar mass by measuring the osmotic pressure.
Rarely used nowadays.

## Solubility product

Solubility product ($K_{sp}$) - equilibrium constant between ionic solid & ions in the solution.
$\ce{Bi2S3 (s) \rightleftharpoons 2 Bi^{3+} (aq) + 3 S^{2-} (aq)}, \space K_{sp} = (a_{\ce{Bi^{3+}}})^2(a_{\ce{S^{2-}}})^3 = \ce{[Bi^{3+}]^2[S^{2-}]^3}$

In general:
$K_{sp} = (a_{\text{cation}})^x(a_{\ce{anion}})^y = [\text{cation}]^x [\text{anion}]^y$

Only applicable to **sparingly soluble salts**! Because the ion-ion interactions are very strong.

$K_{sp}$ can be determined from the molar solubility of the compound.

$$
\begin{flalign}
&\ce{Ag2CrO4 (s) \rightleftharpoons 2 Ag+ (aq) + CrO4^{2-} (aq)} \\
&\ce{[Ag+]} = 2s, \space \ce{[CrO4^{2-}]} = s \\
&K_{sp} = \ce{[Ag+]}^2 \ce{[CrO4^{2-}]} = (2s)^2(s) = 4s^3
&\end{flalign}
$$

## Common ion effect

2 salts are dissolved.
Salts have an ion in common.
The solubility of the salts is lower than if they were in separate solutions.

Hard to predict quantitatively because ions interact with each other so strongly.

**$pH$ effect** - solubility of some salts depends on the $pH$ of the solution.

## Precipitation

$Q_{sp} > K_{sp}$ - reaction favors the formation of reactants (solid).
