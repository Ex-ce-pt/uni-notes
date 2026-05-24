On the inner membrane of mitochondria.

Sequential flow of $e^-$ over 4 complexes.
**Final $e^-$ acceptor - $\ce{O2}$**.
Moves protons from inside into the intermembrane space, then letting them diffuse back spontaneously to power **ATP synthase**.

**Protonmotive force** - energy from protons spontaneously moving from one place to another.

**Cristae** - folds of the inner membrane of a mitochondrion.

Outer membrane → very porous, permeable.
Inner membrane → very selective.

Strong electrochemical gradient:
	Low $\ce{[H+]}$ within the matrix.
	High $\ce{[H+]}$ outside.

> ETC is only the $e^-$ flow through the 4 complexes.
> The actual synthesis of $\ce{ATP}$ is oxidative phosphorylation!

**Respirasome** - supercomplex of complexes I, III, and IV for efficiency and entrapment of toxic reactive oxygen species.
Complex II is free-floating.
That's why oxygen can be toxic and cause DNA damage!

Respirasomes are on the flat parts of the cristae
ATP synthase is on the folds on cristae

---

Summary: $\ce{2 NADH + 22 H+_N + O2 -> 2 NAD+ + 20 H+_P + 2 H2O}$

$\ce{10 H+}$ per $\ce{NADH}$.
$6 \ce{H+}$ per $\ce{FADH2}$.

#### Complex I

34 subunits.

$e^-$ flow: $\ce{NADH -> FMN -> Q}$

Pumps $\ce{4 H+}$ out of the matrix per $\ce{NADH}$.

**P side** - intermembrane space; $(+)$ charge.
**N side** - mitochondrial matrix space; $(-)$ charge.

$\ce{FMN}$ is used because flavins can take one $e^*$ at a time, forming radicals.
This is important for the next step.

$\ce{Cys-S-Fe-...-Fe-S-Cys}$ complexes act as nanowires, transporting $e^-$ **one at a time**.
$\ce{Fe^{3+} + e^- -> Fe^{2+}}$

Final $e^-$ acceptor of this complex - $\ce{Q}$ (ubiquinone).
$\ce{QH2}$ freely diffuses in the inner membrane, travelling to the next complex. ==complex III?

Overall reaction: $\ce{NADH + 5 H+_N + Q -> NAD+ + QH2 + 4 H+_P}$

#### Complex II
**SDH - succinate dehydrogenase**

Oxidizes succinate, $\ce{Succinate + FAD -> Fumarate + FADH2}$
$\ce{FAD}$ is covalently bound to SDH and is never released.
After the reaction, $\ce{FADH2}$ is oxidized again to $\ce{FAD}$, passing the $e^-$ further.

$e^-$ transferred one by one via $\ce{Fe-S}$ wires.
Again, $\ce{FADH2 + Q -> FAD+ + QH2}$

**Does not pump any $\ce{H+}$!**

#### Complex III

Transfers $e^-$ from $\ce{QH2}$ to protein cytochrome c & pumps more $\ce{H+}$.

Cytochromes are proteins that have **heme groups** (rings with metal ions inside).
**Cytochrome c** is diffusible and can move around.
Can accept $1 \space e^-$ at a time, reducing $\ce{Fe^{3+}}$ to $\ce{Fe^{2+}}$.

Since cytochromes can only accept $1 \space e^-$, the $e^-$ transfer is split.
**Q cycle** - the way to transfer $e^-$ onto cytochrome c one by one while pumping $\ce{H+}$ out.

Step 1:
	$\ce{QH2}$ uses $1 \space e^-$ to reduce cytochrome c & pump out $\ce{2 H+}$.
	The other $e^-$ goes to another $\ce{Q}$ molecule, forming a radical.
	Equation: $\ce{QH2 + Q + cyt c(red) + 2 H+_N -> Q + Q^{\cdot-} + cyt c(ox) + 2 H+_P}$
Step 2:
	Another $\ce{QH2}$ molecule reduces another cytochrome c & pumps out $\ce{2 H+}$.
	The second $e^-$ is transferred onto the radical, forming the normal $\ce{QH2}$.
	Equation: $\ce{QH2 + Q^{\cdot-} + cyt c(red) + 2 H+_N -> Q + QH2 + cyt c(ox) + 2 H+_P}$

> The $\ce{H+}$ from $\ce{QH2}$ get pumped out.
> $\ce{H+_N}$ are only used to transform $\ce{Q^{\cdot-}}$ into $\ce{QH2}$.

> Cytochrome c is on the N-side (intermembrane space).

Overall reaction: $\ce{QH2 + 2 cyt c(red) + 2 H+_N -> Q + 2 cyt c(ox) + 4 H+_P}$

#### Complex IV

Cytochrome c transports $e^-$ to $\ce{O2}$, forming $\ce{H2O}$.
**Pumps out $\ce{2 H+}$ per cycle.**
Dimer of 13 subunits, 26 subunits in total.
Contains $\ce{Cu^{2+}}$.

![[_media/Metabolic Pathways/Electron Transport Chain/ETC-complex-IV.png]]

## Oxidative Phosphorylation

Proton gradient alone is enough to power ATP synthesis.

![[_media/Metabolic Pathways/Electron Transport Chain/atp-synthase-structure.png]]

2 functional domains:
	F0 - in the inner membrane.
		A ring of c protein.
	F1 - poking out of the inner membrane, looks like a mushroom, catalytic domain.
		$\alpha$ and $\beta$ subunits form an alternating ring.
		$\gamma$ forms a long stalk at the center.
		Synthesis happens in $\beta$.
		$b_2$ holds $\alpha$ & $\beta$ in place so they don't rotate with $\gamma$.

$\beta$ conformations:
- **O - open** - release of $\ce{ATP}$.
- **L - loose**, binding $\ce{ADP}$ + $\ce{Pi}$
- **T - tight** - catalysis of the reaction.

$\gamma$ rotates and cycles the conformation of $\beta$.
The rotation is because Glu in $\gamma$ is protonated by the $\ce{H+}$ from the intermembrane space, which makes it move favourable for Arg to attract the next Glu in the ring, rotating it.

![[_media/Metabolic Pathways/Electron Transport Chain/atp-synthase-gamma-rotation.png]]

#### P/O ratio

$\ce{1 NADH -> 10 H+}$
$\ce{1 FADH2 -> 6 H+}$
~$\ce{4 H+ -> 1 ATP}$
$\ce{1 NADH -> 2.5 ATP}$ (in humans)
$\ce{1 FADH2 -> 1.5 ATP}$ (in humans)

## Shuttles

$\ce{NADH}$ cannot get through the inner membrane into the mitochondria.
Shuttles solve this problem.

#### Glycerol 3-prosphate shuttle

In brain and skeletal muscle.
$e^-$ are transferred onto $\ce{G\text{3}P}$, then $\ce{FAD}$, then $\ce{Q}$.

#### Malate-aspartate shuttle

In liver, kidney, and heart.
A complicated bypass system involving oxaloacetate, malate, aspartate, and transamination reactions.
