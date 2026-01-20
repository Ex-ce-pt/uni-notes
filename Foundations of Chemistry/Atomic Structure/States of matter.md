
**Intensive property** - does not depend on the amount of substance (density, temperature, color, boiling point, etc.).
**Extensive property** - depends on the amount of substance (volume, mass, length, etc.).

**Microscopic property** - property of single molecule (kinetic energy, molecular weight, packing, volume, intermolecular forces, collisions).
**Macroscopic property** - property of ensembles of molecules (temperature, density, boiling point, pressure).

## Gases

Gases take the shape of the vessel they're in & fill the entire volume of the vessel.

Pressure depends on:
- Force of impact → Kinetic energy → Temperature
- Collisions over area → Volume, concentration
The function of pressure would have the form: $p(T, V, n)$.

Units:
$Pa \space (pascal) =\frac{N}{m^2}$
$atm \space (atmosphere) = 101 \space 325 \space Pa \approx 760 \space mmHg$
$bar \space (bar) = 10^5 \space Pa$
$torr = 1 \space mmHg$

> Temperature is measured in Kelvin because Kelvin does not have negative values.

#### Manometer

**Manometer** - a tool for measuring pressure.

![[states-of-matter/U-tube-manometer.jpg]]

$p_{\text{gas}} > p_{\text{atm}}$
$p_{\text{gas}} = p_{\text{Hg}} + p_{\text{atm}}$
$p_{\ce{Hg}} = \frac{F}{A} = \frac{m \cdot g}{A} = \frac{\rho_{\ce{Hg}} \cdot V_{\ce{Hg}} \cdot g}{A} = \frac{\rho_{\ce{Hg}} \cdot h \cdot A \cdot g}{A} \Rightarrow p_{\ce{Hg}}= \rho_{\ce{Hg}} \cdot g \cdot h$
Cross-section area of the manometer does not matter. Pressure is proportional to the height.

#### Derivation of the ideal gas equation

| Law                          | Formula                      | Alternate form          | Conditions                |
| ---------------------------- | ---------------------------- | ----------------------- | ------------------------- |
| **Boyle's law (1662)**       | $p \cdot V = \text{const}$   | $p \cdot V = f(T, n)$   | **isothermic & no leaks** |
| **Charles' law (1787)**      | $p \cdot V = \text{const}$   | $\frac{V}{T} = g(p, n)$ | **isobaric & no leaks**   |
| **Gray-Lussac's law (1808)** | $\frac{p}{T} = \text{const}$ | $\frac{p}{T} = h(V, n)$ | **isochoric & no leaks**  |
| **Avogardo's law (1811)**    | $\frac{V}{n} = \text{const}$ | $\frac{V}{n} = j(p, T)$ | **isobaric & isothermic** |
$$
\begin{flalign}
&\text{From the Gray-Lussac's law \& Avogardo's law:} \\
&\frac{p}{T} \cdot \frac{V}{n} = h(V, n) \cdot j(p, T) \\
\\
&\text{1) Assume } p = \text{const}, \space T = \text{const}: \\
&\frac{p}{T} = \text{const} \\
&j(p, T) = \frac{V}{n} = \text{const} \\
&\frac{p}{T} \cdot \frac{V}{n} = h(V, n) \cdot j(p, T) = \text{const} \\
&h(V, n) = \text{const} \\
&h \text{ is not a function of } V \text{ and }n \\
&\therefore \frac{p}{T} \cdot \frac{V}{n} = h \cdot j(p, T), \space h = \text{const} \\
\\
&\text{2) Assume } V = \text{const}, \space n = \text{const}: \\
&h = \text{const} \Rightarrow \frac{p}{T} = \text{const} \\
&\frac{V}{n} = j(p, T) = \text{const} \\
&\frac{p}{T} \cdot \frac{V}{n} = h \cdot j(p, T) = \text{const} \\
&j \text{ is not a function of } p \text{ and } T \\
&\therefore \frac{p}{T} \cdot \frac{V}{n} = h \cdot j, \space h = \text{const}, \space j = \text{const} \\
\\
&\text{Let } \space R = h \cdot j = k_B \cdot N_A \\
&\frac{p}{T} \cdot \frac{V}{n} = R \\
&\therefore pV = nRT
&\end{flalign}
$$

$R$ - [ideal gas constant](Cheat%20Sheet#Constants)

#### Ideal gas

Ideal gas:
- Perfectly elastic collision - no energy lost during the collision.
- No intermolecular forces - particles only interact w/ the vessel.
- Molecules are point masses.

Ideal gas equation:
$pV = nRT$ / $pV = \frac{m}{M}RT$

| Symbol | Unit                    | Comment                                   |
| ------ | ----------------------- | --------------------------------------------- |
| $p$    | $Pa$                    | Pressure of the ideal gas                     |
| $V$    | $m^3$                   | Volume of the ideal gas                       |
| $n$    | $mol$                   | Amount of the particles in the ideal gas      |
| $T$    | $K$                     | Temperature of the ideal gas                  |
| $R$    | $\frac{J}{mol \cdot K}$ | [Ideal gas constant](Cheat%20Sheet#Constants) |

#### Dalton's law

In the ideal gas law, it does not matter which particles the gas consists of, only the quantity.
Assume 2 substances are present in the gas: $A$ and $B$.
$n_{\text{total}} = n_A + n_B$

$pV = nRT \Rightarrow p = \frac{nRT}{V}$
$p = \frac{n_{\text{total}} RT}{V} = \frac{(n_A + n_B) RT}{V} = \frac{n_A RT}{V} + \frac{n_B RT}{V} = p_A + p_B$

$p_A$, $p_B$ - partial pressures of the gases $A$ and $B$.

In general:
$\text{If } n_{\text{total}} = \sum n_i \text{, then } p_{\text{total}} = \sum p_i$

#### Density

From: $n = \frac{m}{M}$ and $\rho = \frac{m}{V}$
$$
\begin{flalign}
&pV = nRT \\
&pV = \frac{m}{M}RT \space (n = \frac{m}{M})\\
&p = \frac{m}{MV}RT \\
&p = \frac{m}{V} \cdot \frac{RT}{M} \space (\rho = \frac{m}{V})\\
&p = \rho \cdot \frac{RT}{M} \\
&\rho = \frac{p}{\frac{RT}{M}} \\
&\rho = \frac{pM}{RT}
&\end{flalign}
$$

Density of an ideal gas:
$\rho = \frac{p M}{RT}$

#### Maxwell's distribution of speeds

Shows at which speed different fractions of the particles in a gas travel.
$x \in [0; 1]$ - "molar fraction", fraction of a sample.
$\bar v$ - average velocity of a gas particle.

1\. Same gas (i.e. $\ce{He}$), different $T$:

![[states-of-matter/He-maxwell-distribution-of-speeds.png]]
The hotter the gas is, the more kinetic energy the particles have on average.

> $E_k = \frac{1}{2} mv^2$

2\. Same $T$, different gas:

![[states-of-matter/const-temp-maxwell-distribution-of-speeds.png]]
The lighter the particle in a gas is, the faster it travels.

> Since $x$ is a fraction of the sample, $\int_0^{\infty} x(\bar v) \space d\bar{v} = 1$ - the entire sample is accounted for.

#### Real gases

Real gases have intermolecular interactions.

Compressibility factor:
$Z = \frac{V}{V_i}, \space V \text{ - real volume}, \space V_i = \frac{nRT}{p} \text{ - ideal volume}$

![[states-of-matter/compressibility-factor-graph.png]]

Most molecules are naturally attracted to one another, so increasing $p$ lowers the volume at first.

Dilute gases - ideal behavior.
High $T$, $p$ - repulsion.
Low $T$, high $p$ - attraction.

To make $Z$ graphs useful, need to plot a graph for every temperature → inconvenient.

#### Van der Waals equation

$p + a(\frac{n}{V})^2 (\frac{V}{n} - b) = RT$
$p = \frac{nRT}{(V - nb)} - a(\frac{n}{V})^2$
$a$ - attraction between molecules.
$b$ - repulsion between molecules.

The parameters are to be looked up in the tables.

Still need 2 parameters, but can use the equation for any $T$.

## Liquids

Liquids take the shape of the vessel, but do have a defined volume.

#### Capillary action

Behavior of liquids in tight vessels.

Concave meniscus - liquid prefers to interact w/ the vessel material (i.e. $\ce{H2O}$ in glass).
Convex meniscus - liquid prefers to interact w/ itself (i.e. $\ce{H2O}$ in teflon, $\ce{Hg}$ in glass).

![[states-of-matter/capillary.png]]

Thinner capillary → longer meniscus.

#### Surface tension

Liquids behave differently on surfaces.
"Wettable" surface → smeared droplet.
Hydrophobic surface → droplet is a ball (ideally a perfect sphere) to minimize interaction w/ the surface.

![[states-of-matter/surface-tension.png]]

#### Viscosity

Difficult to explain.
Depends on the [intermolecular interactions](Intermolecular%20interactions.md) & **energy landscape**.

Energy landscape - how much rearrangement is needed to find a stable state?
Smaller molecules form stable states more frequently w/ less rearrangement → less viscous.
Bigger molecules need more time to find a stable state.

## Solids

Solids have defined shape & volume.

**Crystalline solid** - long-range order, the entire system is ordered.
**Amorphous solid** - short-range order, overall no order.

The difference between the types of crystalline solids is not always clear.

#### Ionic solids

**Salts**.

![[states-of-matter/NaCl-structure.png]]

- Held together by [ionic interaction](Intermolecular%20interactions.md#Coulombic/ionic/electrostatic).
- High melting point.
- Large anions, small cations → structure achieved by optimizing anion packing (*usually*).
- Brittle - ions repel each other, if displaced.

> RTIL - Room Temperature Ionic Liquid - salts w/ melting point below room temperature. Achieved by having big or asymmetric ions.

#### Molecular solids

![[states-of-matter/ice-structure.png]]

- Held together by various [intermolecular interactions](Intermolecular%20interactions.md).
- *(Typically)* low melting point - weaker forces holding molecules together.
- Brittle
- Soluble - solvent needs to participate in the same type of bonding.

> Like dissolves like.

#### Network solids

![[diamond-tetrahedrical-structure.svg]]

- No discrete molecular unit.
- Held together by various [intermolecular interactions](Intermolecular%20interactions.md).
	- More ionic bonding → ceramics.
- Do not melt - heating up cracks the bonds.

#### Metallic solids

![[states-of-matter/metal-structure.jpg]]

- Packed atoms of metal.
- Held together by metallic bonds - common $e^-$ cloud, **sea-of-electrons model**.
- Malleable.
- Melting point varies a lot.
- *(Typically)* silver in color - except for $\ce{Cu}$ & $\ce{Au}$.

> Malleable - possible to hammer into thin sheets.
> Ductile - possible to stretch into wires.

#### Packing

**ABA** - hexagonal close packing, every second layer is vertically aligned.
![[states-of-matter/hexagonal-close-packing.png]]

**ABC** - cubic close packing, layers come in a sequence of 3.
![[states-of-matter/cubic-close-packing.jpg]]

**Unit cell** - the smallest repeating part of the structure.
$\text{Packing efficiency} = \frac{\text{volume taken up by atoms}}{\text{volume of the unit cell}}$

**Primitive close packed** - 8 particles in the corners, $\text{PE} \approx 0.52$.
![[states-of-matter/primitive-close-packed.png]]

**Body-centered cubic structure** - 1 particle in the center & 8 particles in the corners, $\text{PE} \approx 0.68$.
![[states-of-matter/body-centered-cubic.png]]

**Face-centered cubic structure** - 8 particles in the corners & 6 particles in the faces, $\text{PE} \approx 0.74$.
![[states-of-matter/face-centered-cubic.png]]
