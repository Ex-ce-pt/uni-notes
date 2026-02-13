
**Elimination:** $\ce{A-B + C -> A + B-C}$

Can compete w/ substitution reactions.
The more hindered the substrate, the more elimination takes place.

**Summary:**

| Factor              | E1                      | E2                      |
| ------------------- | ----------------------- | ----------------------- |
| **Substrate**       | $2 \degree < 3 \degree$ | $2 \degree < 3 \degree$ |
| **Kinetics**        | First-order             | Second-order            |
| **Stereochemistry** | No preferred            | Antiperiplanar          |
| **Rearrangements**  | Common if favored       | No                      |

**Zaitsev's rule** - the formation of a **more substituted** alkene is favored, if a **small base** is used.
**Hoffman's rule** - the formation of a **less substituted** alkene is favored, if a **bulky base** is used.

![[_media/Elimination/E2-vs-SN2.png]]

## E1

Happens in multiple steps:
1. Carbocation spontaneously formed (slow, **rate-determining step**).
2. If the added reactant acts as a nucleophile, bonding to the positively charged carbon, [SN1](Nucleophilic%20substitution#SN1) takes place.
3. If the added reactant acts as a base, abstracting a proton from the neighbouring carbon, E1 takes place.

E1 almost always competes w/ [SN1](Nucleophilic%20substitution#SN1).
Can also be observed when the nucleophile is extremely weak but acts as a reasonable base.

![[_media/Elimination/E1-example.png]]

#### Methanide shift

[Stability of carbocations](Reaction%20intermediates#Carbocations): $0 \degree < 1 \degree < 2 \degree < 3 \degree$

As a 1st step of an E2 reaction, a carbocation is formed.
if this carbocation happens to be $2 \degree$ and there is a methyl group on a neighbouring carbon, it can shift to the positively charged carbon & stabilize the carbocation even more. $3 \degree$ carbocation is formed.

**Ex. ([dehydration of an alcohol](Dehydration%20of%20alcohols)):**
![[_media/Elimination/methanide-shift-ex.png]]


## E2

Happens in a single step (concerted reaction):
- The base bonds to a hydrogen on a neighbouring carbon, forces a double bond between carbons to form, pushing an $e^-$-pair onto the leaving group.

Needs a **strong base**, but preferably **not a strong nucleophile**.

![[_media/Elimination/E2-example.png]]

**Rate:** $k_r \ce{[\text{substrate}][\text{base}]}$
**Products in stereochemistry**: yields (almost) only the product favored by the reaction mechanism.

Since to create a $\pi$-bond, a proper overlap between the orbitals is needed, all 5 atoms ($\ce{H-C-C-X}$+ base) must be coplanar.
**Anti-coplanar/antiperiplanar manner** - the hydrogen & leaving group are anti to each other; preferred configuration.
**Syn-coplanar** - the hydrogen & leaving group are eclipsing each other; not favored, some rigid molecules have no other option.

The importance of the anti orientation:
![[_media/Elimination/E2-anti-importance.png]]

In cyclic molecules, a ring flip could be necessary to achieve the anti configuration.

> Naturally, the hydrogen that is being abstracted by the base must be bonded to a carbon neighbouring the carbon of the leaving group.

#### How to favour

1. Use a $2 \degree / 3 \degree$ carbocations, if possible.
	Steric hindrance will inhibit [substitution reactions](Nucleophilic%20substitution).
2. When using $1 \degree$ carbocation, use a bulky base.
	Again, inhibiting [substitution reactions](Nucleophilic%20substitution). Abstracting a small proton is easier than bonding to a hindered carbon
3. Use a high concentration of strong non-polarizable base.
	A weak base would not react efficiently enough, allowing [SN1](Nucleophilic%20substitution#SN1) & [[#E1]] reactions to happen as well. Use $\ce{EtONa/EtOH}$ or $\ce{t-BuOK/t-BuOH}$
4. Use heat.
	Elimination reactions are favoured over [substitution reactions](Nucleophilic%20substitution) with elevated temperature.
	More in [[#Dependence on temperature]].

## Dependence on temperature

Elimination reactions are favoured over [substitution reactions](Nucleophilic%20substitution) with elevated temperature.

Reason: the change in Gibbs free energy becomes more negative for elimination reactions.

$$
\begin{flalign}
&\Delta G = \Delta H - T \cdot \Delta S \\
&\text{Assume: } \Delta H \text{ is independent of temperature. Hydrolysis is taken as an example.} \\
&\text{SN1 reaction:} \\
&\ce{R-X + H2O -> R-OH + HX} \text{, 2 molecules } \rightarrow \text{ 2 molecules, } \Delta S \approx 0 \\
&\text{E1 reaction:} \\
&\ce{R-X + H2O -> R' + H2O + H+} \Rightarrow \ce{R-X -> R' + H+} \text{, 1 molecule } \rightarrow \text{ 2 molecules, } \Delta S > 0 \\
&\text{As } T \text{ grows, } \Delta G(\text{SN1}) \text{ stays the same, but } \Delta G(\text{E1}) \text{ becomes more negative.}
&\end{flalign}
$$

==graph of dG with temperature for SN1 and E1
