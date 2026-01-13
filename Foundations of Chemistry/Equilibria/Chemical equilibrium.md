
All chemical equilibria are **dynamic**.
Equilibria respond to changes in:
- Temperature;
- Pressure;
- Addition/removal of reagents.

**Heterogeneous equilibrium** - different phases appear in the reaction.
**Homogeneous equilibrium** - only one phase appears in the reaction.

## Equilibrium constant

**Equilibrium constant** ($K$) - ratio between the activities of reactants & products of the reaction **at equilibrium**.

$K = \{\frac{(\text{activities of products})^n}{(\text{activities of reactants})^n}\}_{\text{equilibrium}}$
$K = \frac{\prod_i a_i^{n_i}}{\prod_j a_j^{n_j}}$

| Activity                           | Property used          | Activity                                                 | Homogeneous equilibrium                     |
| ---------------------------------- | ---------------------- | -------------------------------------------------------- | ------------------------------------------- |
| **Ideal gas**                      | Partial pressure       | $a_{\ce{J}} = \frac{p_{\ce{J}}}{p \degree} = p_{\ce{J}}$ | $K = \frac{(p_C)^c(p_D)^d}{(p_A)^a(p_B)^b}$ |
| **Solute in a<br>dilute solution** | Molar<br>concentration | $a_{\ce{J}} = \frac{\ce{[J]}}{c \degree} = \ce{[J]}$     | $K = \frac{[C]^c[D]^d}{[A]^a[B]^b}$         |
| **Pure solid/liquid**              | $1.$                   | $a_{\ce{J}} = 1$                                         | $K = 1$                                     |

> Spectator ions in ionic reactions do not appear in the calculation of the equilibrium constant!
> Even if they were to appear, they would simply cancel out.

For multiples of reactions, $K$ should be raised to the power of the \# of the reactions happening:
$$
\begin{flalign}
\ce{a A + b B &\leftrightharpoons c C + d D}, \space \space K_1 = K \\
\ce{N(a A + b B &\leftrightharpoons c C + d D)}, \space K_2 = K^N \\
\ce{c C + d D &\leftrightharpoons a A + b B}, \space \space K_3 = K^{-1}
&\end{flalign}
$$

For reactions happening one after the other, the $K_i$ are multiplied together:
$$
\begin{flalign}
&\ce{a A + b B \leftrightharpoons c C + d D}, \space K = K_1 \\
&\ce{c C + d D \leftrightharpoons e E + f F}, \space K = K_2 \\
&\ce{a A + b B \leftrightharpoons e E + f F}, \space K = K_1 \cdot K_2
&\end{flalign}
$$

From the definition of $K$:
- $K > 10^3$ (large values) - favors products;
- $K \in [10^{-3}; 10^3]$ (around $1$) - neither strongly favored;
- $K < 10^{-3}$ (small values) - favors the reactants.

**Potential to go to completion** ($K > 1$) - Gibbs free energy curve's minimum is close to pure products.
**Little tendency to form products** ($K < 1$) - Gibbs free energy curve's minimum is close to pure reactants.

**Van't Hoff's equation** (same as Clausius-Clapeyron equation, but for the equilibrium constant):
$ln(\frac{K_2}{K_1}) = -\frac{\Delta H \degree}{R}(\frac{1}{T_2} - \frac{1}{T_1})$

#### Reaction quotient

**Reaction quotient** ($Q$) - ratio between the reactants & products of the reaction **at a specific point in time**.

Reaction quotient is calculated the same way as the equilibrium constant.

$Q < K$ - more reactants present, more products will be formed.
$Q = K$ - equilibrium.
$Q > K$ - more products present, more reactants will be formed.

#### Relation to Gibbs free energy

$\Delta G = \Delta G \degree + RT \cdot ln(Q)$
$\Delta G \degree = -RT \cdot ln(K)$
**Works for any reaction, not only the ones involving gases!**

$G_m(\ce{J}) = G_m \degree (\ce{J}) + RT \cdot ln(a_{\ce{J}})$

#### ICE table

**ICE table** - used to help calculations /w concentration of chemicals in a reaction.

Ex.
$\ce{2 N2 (g) + O2 (g) \leftrightharpoons 2 N2O (g)}, \space K = 3.2 \cdot 10^{-28}$
$p_{\ce{N2}} = 3.21 \space bar, \space p_{\ce{O2}} = 6.21 \space bar, \space p_{\ce{N2O}} = 0 \space bar$

|                 | $\ce{N2}$ | $\ce{O2}$ | $\ce{N2O}$ |
| --------------- | --------- | --------- | ---------- |
| **Initial**     | $3.21$    | $6.21$    | $0$        |
| **Change**      | $-2x$     | $-x$      | $+2x$      |
| **Equilibrium** | $3.21-2x$ | $6.21-x$  | $0+2x$     |
$$
\begin{flalign}
&K = \frac{p_{\ce{N2O}}^2}{p_{\ce{N2}}^2 \cdot p_{\ce{O2}}} = \frac{(2x)^2}{(3.21-2x)^2(6.21-x)} \\
&\text{For convenience, assume the change is much smaller than the initial partial pressures: } \\
&x << 3.21 \wedge x << 6.21 \Rightarrow 3.21-2x \approx 3.21, \space 6.21-x \approx 6.21 \\
&K = 3.2 \cdot 10^{-28} = \frac{(2x)^2}{(3.21)^2(6.21)} \\
&x = \sqrt{3.2 \cdot 10^{-28} \cdot 3.21^2 \cdot 6.21 \cdot 0.25 } \approx 5 \cdot 10^{-27}
&\end{flalign}
$$

## Equilibrium constant of gases in terms of their molar concentrations

Sometimes it may be useful to treat gases according to their molar concentrations, rather than partial pressures.

**Equilibrium constant** $K_c$ - equilibrium constant for ideal gases from their molar concentrations.

$\ce{a A (g) + b B (g) \leftrightharpoons c C (g) + d D (g)}$

$K_c = \frac{\ce{[C]^c[D]^d}}{\ce{[A]^a[B]^b}}$
$\ce{[J]} = \frac{n_{\ce{J}}}{V}$

$K = (\frac{c \degree RT}{p \degree})^{\Delta n_r}K_c$
$\Delta n_r$ - difference in stochiometric coefficients for gas-phase species

$\Delta n_r = 0, \space K_c = K$

## Response of equilibria to changes in conditions

When stress is applied to a system in dynamic equilibrium, the equilibrium tends to adjust to minimize the effect of the stress.

The value of the [reaction quotient](#Reaction%20quotient) changes when stress is applied.

**Le Chatelier's principle**:
After a change in conditions, the equilibrium shifts in the opposite direction.

| Applicable | Positive change | Effect                         | Negative Change | Effect                           |
| ---------- | --------------- | ------------------------------ | --------------- | -------------------------------- |
| **Always** | + reagents      | + products form                | - reagents      | + reagents form                  |
| **Always** | + products      | + reagents form                | - products      | + products form                  |
| **Always** | + temperature   | Endothermic favored            | - temperature   | exothermic favored               |
| **Gases**  | + pressure      | Side /w lower $n_{\text{gas}}$ | - pressure      | Side /w greater $n_{\text{gas}}$ |

> Increasing pressure must happen by compression!
> Increasing temperature by introducing an inert gas does nothing!
> If the pressure is increased via adding another gas, the reacting gases occupy the same volume & have the same partial pressures, meaning the reaction has the same reaction quotient.

> When the temperature changes, the equilibrium constant changes too!
> Don't forget to use the Van't Hoff's equation!
