
Biological catalysts, **highly specific**; proteins.
Essentially all biological reactions are catalyzed.
A quarter of genes encode enzymes.

Enzymes speed up reactions by orders of magnitude!

**Proteases** - catalyze the hydrolysis of peptide bonds (break down proteins).

Name: \[the reaction catalysed] + "-ase"
Mostly historical naming is used.

Many enzymes require **cofactors** - metal ions/small organic molecules.
**Coenzymes** - cofactors that are small organic molecules.

**Prosthetic group** - cofactor that is covalently bound to an enzyme.

## Thermodynamics

$\ce{A + B \rightleftharpoons C + D},  \space \Delta G$
$\Delta G < 0$ - exergonic, spontaneous.
$\Delta G > 0$ - endergonic, nonspontaneous.

> Enzymes do not alter the laws of thermodynamics! The reaction still has to be thermodynamically favoured to happen.

Enzymes lower the activation energy of reactions and help them to reach the equilibrium faster.

## Active site

Enzymes bind the substrates in a way that favours the formation of the transition state.

**Active site** - region in the enzyme where the substrate in bound.

Specificity comes from the shape of the active site - possible to distinguish even between a couple differing atoms in the substrate!

#### Induced fit

Enzymes are often flexible and dynamic.
The active site is rearranged slightly when the substrate binds.
That allows for tighter bond and higher specificity.

## Kinetics

Michaelis-Menten kinetics is the core.

![[enzyme-reaction.png]]

Needs a couple assumptions:
1. **Ignoring the reverse reaction**
	Assume that the reaction of $\ce{P -> S}$ almost does not happen and can be ignored for simplicity.
2. **Steady State Assumption**
	The rate of formation of $\ce{ES}$ is equal to the rate of its breakdown; no weird situations when $\ce{ES}$ suddenly runs out or skyrockets.
	$\text{Rate of formation: } k_1(\ce{[E]_0} - \ce{[ES]})\ce{[S]}$
	$\text{Rate of breakdown: } k_{-1}\ce{[ES]} + k_2\ce{[ES]}$
3. **Constant enzyme concentration**
		The "constants" discussed are only constants when the concentration of the enzyme stays constant as well.

$$
\begin{flalign}
&\textcolor{grey}{\text{Begin with the Steady State Assumption: }} \\
&\textcolor{grey}{k_1(\ce{[E]_0} - \ce{[ES]})\ce{[S]} = k_{-1}\ce{[ES]} + k_2\ce{[ES]}} \\
&\textcolor{grey}{\text{Solve for } \ce{[ES]} \text{ and eventually arrive to:}} \\
&\textcolor{grey}{\ce{[ES]} = \frac{\ce{[E]_0[S]}}{\ce{[S]} + (k_{-1} + k_2)/k_1}} \\
&\textcolor{grey}{\text{Michaelis constant: } K_M = \frac{k_{-1} + k_2}{k_1}} \\
&\textcolor{grey}{\ce{[ES]} = \frac{\ce{[E]_0[S]}}{\ce{[S]} + K_M}} \\
&\textcolor{grey}{k_2\ce{[ES]} = \frac{k_2\ce{[E]_0[S]}}{\ce{[S]} + K_M}} \\
&\textcolor{grey}{\text{@ full saturation, } \ce{[E]_0} = \ce{[ES]}, \space v_0 = k_2\ce{[ES]}, \space v_{\text{max}} = k_2\ce{[ES]}} \\
&v_0 = \frac{v_{\text{max}}\ce{[S]}}{K_M +\ce{[S]}}
&\end{flalign}
$$

$k_{\text{cat}} = k_2$ - "turnover number"; fraction of the substrate converted per second.
$v_0 = k_{\text{cat}} \ce{[ES]}$
$v_{\text{max}} = k_{\text{cat}} \ce{[E]_0}$ @ full saturation; all enzyme molecules bound the substrate molecules.
$K_M = \ce{[S]}$ when $v_0 = v_{\text{max}}$

$K_M$ - measure of substrate affinity to the enzyme molecules.
$\frac{k_{\text{cat}}}{K_M}$ - measure of catalytic efficiency; allows to compare the enzymes between each other.

How it's done:
1. Measure $\ce{[P]}$ (usually in some roundabout way, like measuring the absorptivity of light), plot against time. Constant $\ce{[E]_0}$, vary $\ce{[S]}$. Find the initial reaction rates ($v_0$).
	Plot:
	==TODO: plot
2. Plot $v_0$ against $\ce{[S]}$. See the data points approaching a limit - $v_{\text{max}}$.
	==TODO: plot
3. Plot $1/v_0$ against $1/\ce{[S]}$. **Lineweaver-Burk plot**. The intersection points tell you the kinetic parameters
	==TODO: plot

## Inhibition

Enzymes can be inhibited with certain compounds.

Can use kinetics to determine the type of inhibition.

Types of inhibition:
- Reversible inhibition
	- Competitive
	- Uncompetitive
	- Noncompetitive
- Irreversible inhibition

#### Competitive

Inhibitor binds to enzyme instead of the substrate.
Adding a lot of substrate can outcompete the inhibitor.

==TODO: add plot

- $v_{\text{max}}$ - no change.
- $K_m$ - increases.
- Plot - slope increases.

#### Uncompetitive

Inhibitor traps the bound substrate in the enzyme.
Some of the enzyme is taken out of the equation.

==TODO: add plot

- $v_{\text{max}}$ - decreases.
- Plot - shifts higher.

#### Noncompetitive

Inhibitor binds to any part of the enzyme; substrate is not involved.
Some of the enzyme is taken out of the equation.

==TODO: add plot

- $v_{\text{max}}$ - decreases.
- $K_m$ - no change.

#### Irreversible

Do something that cannot be reversed; e.g. modify the functional groups.


## Catalytic strategies

Mostly the AA sidechains do the work.

1. **General acid-base** - enzyme helps with the charge distribution by acting as a Bronsted acid/base.
2. **Covalent** - a group on the active site binds to the substrate first to provide an alternate route with lower activation energy.
3. **Metal ions** - different strategies, e.g. can help hold the substrate in a certain orientation or cancel out the charge.

**Allosteric enzymes** - multiple active sites; binding one substrate changes the properties of the other active sites.
Important for metabolism - adapting to changes in the environment.

> Michaelis-Menten kinetics does not work for allosteric enzymes!
