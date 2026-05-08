
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
Also helps to keep the unwanted water & other substances out and the substrate & reactive intermediates in.

## Kinetics

Michaelis-Menten kinetics is the core.

![[enzyme-reaction-general.png]]

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

$k_{\text{cat}} = k_2$ - "turnover number"; # of $\ce{S -> P}$ conversions per second.
$v_0 = k_{\text{cat}} \ce{[ES]}$
$v_{\text{max}} = k_{\text{cat}} \ce{[E]_0}$ @ full saturation; all enzyme molecules bound the substrate molecules.
$K_M = \ce{[S]}$ when $v_0 = v_{\text{max}}$

$K_M$ - measure of substrate affinity to the enzyme molecules; **inversely proportional to the affinity**.
$\frac{k_{\text{cat}}}{K_M}$ - measure of catalytic efficiency; allows to compare the enzymes between each other.

How it's done:
1. Measure $\ce{[P]}$ (usually in some roundabout way, like measuring the absorptivity of light), plot against time. Constant $\ce{[E]_0}$, vary $\ce{[S]}$. Find the initial reaction rates ($v_0$).
	Plot:
	![[P-against-time-plot.png|393]]
2. Plot $v_0$ against $\ce{[S]}$. See the data points approaching a limit - $v_{\text{max}}$.
	Plot:
	![[S-against-v_0-plot.png|396]]
	![[S-against-v_0-plot-details.png|397]]
3. Plot $1/v_0$ against $1/\ce{[S]}$. **Lineweaver-Burk plot**. The intersection points tell you the kinetic parameters.
	Plot equation: $\frac{1}{v_0} = \textcolor{red}{\frac{K_M}{v_{\text{max}}}} \cdot \frac{1}{\ce{[S]}} + \textcolor{cyan}{\frac{1}{v_{\text{max}}}}$ (derived from the MM equation)
	Plot:
	![[LB-plot-details.png|392]]

## Inhibition

Enzymes can be inhibited with certain compounds.
Can use kinetics to determine the type of inhibition.

Types of inhibition:
- Reversible inhibition
	- [[#Competitive]]
	- [[#Uncompetitive]]
	- [[#Noncompetitive]]
- [Irreversible inhibition](#Irreversible)

#### Competitive

Inhibitor takes S's place in the E's active site.
Adding a lot of substrate can outcompete the inhibitor.

![[competitive-inhibitor-LB-plot.png|597]]

| Parameter        | Change                                         | Comment                                                                                                                                                          |
| ---------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v_{\text{max}}$ | None                                           | Can still reach the same speed, but need more S to outcompete the inhibitor                                                                                      |
| $K_M$            | $\uparrow$                                     | Lower affinity, because it's harder for the S to bind to E                                                                                                       |
| Plot             | Rotated around y-intercept;<br>Slope increases | Slope: $\frac{K_M}{v_{\text{max}}}$, if $K_M \uparrow$, then $\frac{K_M}{v_{\text{max}}} \uparrow$<br>y-intercept: $\frac{1}{v_{\text{max}}}$, remains unchanged |

#### Uncompetitive

Inhibitor traps the bound S in E.
Some of E is taken out of the equation.

![[uncompetitive-inhibitor-LB-plot.png]]

| Parameter        | Change       | Comment                                                                                                                                                                                                 |
| ---------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v_{\text{max}}$ | $\downarrow$ | Less free E remains to work react                                                                                                                                                                       |
| $K_M$            | $\downarrow$ | Higher affinity, because now there are constantly some ES present (inhibited)                                                                                                                           |
| Plot             | Moves up     | y-intercept: $\frac{1}{v_{\text{max}}}$, if $v_{\text{max}} \downarrow$, then $\frac{1}{v_{\text{max}}} \uparrow$<br>x-intercept: $\frac{-1}{K_M}$, if $K_M \downarrow$, then $\frac{-1}{K_M} \uparrow$ |

#### Noncompetitive

Inhibitor binds to any part of the E or ES.
Some of E is taken out of the equation.

![[non-competitive-inhibitor-LB-plot.png|547]]

| Parameter        | Change                                         | Comment                                                                                                           |
| ---------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| $v_{\text{max}}$ | $\downarrow$                                   | Less free E remains to react                                                                                      |
| $K_M$            | None                                           | Same affinity, because same proportion of E and ES (?)                                                            |
| Plot             | Rotated around x-intercept;<br>Slope increases | y-intercept: $\frac{1}{v_{\text{max}}}$, if $v_{\text{max}} \downarrow$, then $\frac{1}{v_{\text{max}}} \uparrow$ |

#### Irreversible

Does something that cannot be reversed:
- Modifies of the functional groups.
- Covalently bonds to E.

## Catalytic strategies

Mostly the AA sidechains do the work.

1. **General acid-base** - enzyme helps with the charge distribution by acting as a Brønsted acid/base.
2. **Covalent** - a group on the active site binds to the substrate first to provide an alternate route with lower activation energy.
3. **Metal ions** - different strategies, e.g. can help hold the substrate in a certain orientation or cancel out the charge.

**Allosteric enzymes** - multiple active sites; binding one substrate changes the properties of the other active sites.
Important for metabolism - adapting to changes in the environment.

> Michaelis-Menten kinetics does not work for allosteric enzymes!
