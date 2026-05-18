
## Metabolism

Metabolism is organised in pathways - a series of linked reactions.
Common intermediates occur in many pathways.
Metabolic pathways are highly regulated.

**Catabolism** - degrades substances; releases energy.
**Anabolism** - synthesises substances; uses energy.

Endergonic ($\Delta G > 0$) biological reactions are coupled to the ATP degradation ($\Delta G < 0$).
The overall $\Delta G < 0$ is the sum of the reactions.

Why is ATP hydrolysis favourable?
1. high density of $(-)$ charges on ATP
2. water molecules can solvate one phosphate ion better
3. resonance stabilization of $\ce{Pi}$
BUT, high activation energy, so without enzymes the degradation takes days.

Phosphoryl transfer potential - ability to get $\ce{Pi}$ group from ATP.
Measured in the energy of hydrolysis.
The more negative, the more ready the molecule is to get rid of the $\ce{Pi}$ group.

## Glycolysis

Almost universal pathway.
Very ancient.
**Anaerobic** - doesn't need oxygen.
In **cytoplasm** (in the plasma of cells).

Summary:
	Glucose (C6) -> 2 pyruvate (C3) in 10 steps
	$\ce{\text{Glucose} + 2 ATP + \textcolor{grey}{\ce{2 NAD+ + 2 ADP}} -> 2 \space \text{pyruvate} + 4 ATP + 2 NADH + 2 H2O + 2 H+}$

Divided into the **preparation phase** (steps 1-5) and the **payoff phase** (steps 6-10).


**Dehydrogenases** - catalyse redox reactions, $\ce{NAD+}$ is usually the $e^-$ acceptor.

![[_media/Metabolic Pathways/Glycolysis/glycolysis-full.png]]

#### Step 1 - phosphorylation

$\ce{\text{Glucose} + ATP -> \text{Glucose-6-phosphate} + ADP + H+}$

Enzyme: **hexokinase** ($\ce{Mg^{2+}}$)

Traps the glucose in the cell; tags a molecule for metabolism.
Uses induced fit to shield the ATP from water.
Irreversible.

#### Step 2 - isomerization

$\ce{\text{Glucose-6-phosphate} \rightleftharpoons \text{Fructose-6-phosphate}}$

Enzyme: **Phosphohexose isomerase**

Turns glucose into fructose.
$\ce{C}1$ now has an $\ce{OH}$ that can be phosphorylated.

#### Step 3 - phosphorylation

$\ce{\text{Fructose-6-phosphate} + ATP -> \text{Fructose-1,6-bisphosphate}}$

Enzyme: **Phosphofructokinase**

First committed step of glycolysis.
Phosphofructokinase is heavily regulated.
Irreversible.

#### Step 4 - lysis

$\ce{\text{Fructose-1,6-bisphosphate} \rightleftharpoons DHAP + GAP}$

Enzyme: **Aldolase**

Splits the fructose body (C6) into 2 C3 bodies.

#### Step 5 - isomerization

$\ce{DHAP \rightleftharpoons GAP}$

Enzyme: **Triose phosphate isomerase**

Makes sure both products from the last step are used.

#### Step 6 - phosphorylation/dehydrogenation

$\ce{GAP + NAD+ + Pi \rightleftharpoons \text{1,3-bisphosphoglycerate} + NADH + H+}$

Enzyme: **G3P dehydrogenase**

Inorganic $\ce{Pi}$ is added, 2 $e^-$ are removed.
The product has a very **high phosphoryl transfer potential** - favourable to give $\ce{Pi}$ away to $\ce{ADP}$.

#### Step 7 - dephosphorylation

$\ce{\text{1,3-bisphosphoglycerate} + ADP \rightleftharpoons \text{3-phosphoglycerate} + ATP }$

Enzyme: **Phosphoglycerate kinase**

**Substrate-level phosphorylation** - transferring $\ce{Pi}$ group from substrate to $\ce{ADP}$ forming $\ce{ATP}$.

#### Step 8 - shift of the phosphoryl group

$\ce{\text{3-phosphoglycerate} \rightleftharpoons \text{2-phosphoglycerate}}$

Enzyme: **Phosphoglycerate mutase**

Setup for the following reactions.

#### Step 9 - dehydration

$\ce{\text{2-phosphoglycerate} \rightleftharpoons \text{phosphoenolpyruvate} + H2O}$

Enzyme: **Enolase**

Adjacent double bond makes $\ce{Pi}$ a better leaving group.

#### Step 10 - dephosphorylation

$\ce{\text{phosphoenolpyruvate} + ADP + H+ -> \text{pyruvate} + ATP}$

Enzyme: **Pyruvate kinase**

Irreversible.

## Source of glucose

Stored polysaccharides (glycogen) & dietary carbohydrates become glucose via mutation/hydrolysis.
Fructose enters at the fructose-6-phosphate or DHAP+G3P steps.

## After glycolysis

Must regenerate $\ce{NAD+}$ to continue doing glycolysis.

Under aerobic conditions:
	Pyruvate is an intermediate in the complete oxidation of pyruvate to $\ce{CO2}$

Under anaerobic conditions (e.g. in anaerobic bacteria):
	**Fermentation** - extracting $\ce{ATP}$ from pyruvate without oxygen.
	$\ce{NADH}$ transfers the $e^-$ back to pyruvate.
	![[fermentation-pyruvate-ethanol.png]]

In oxygen deprivation in animal muscles:
	![[_media/Metabolic Pathways/Glycolysis/fermentation-pyruvate-lactate.png]]


## Gluconeogenesis

Glucose is synthesised from pyruvate and lactate.
Takes place primarily in the **liver**.

3 reactions in glycolysis are not reversible, for these we have bypass reactions.

> Gluconeogenesis is engaged when the body doesn't have enough sugars.
> It's not the method to store energy, but a quick method to scrap together some fuel.

## Regulation

$\ce{ATP}$ inhibits **phosphofructokinase**, $\ce{ADP}$ & $\ce{AMP}$ reverse inhibition.

**Fructose-2,6-bisphosphate** promotes glycolysis, inhibits gluconeogenesis.

> **NOT fructose-1,6-bisphosphate!**

**Glucagon** - hormone that signals the liver to produce glucose.
Glucagon inhibits glycolysis, promotes gluconeogenesis.

**Insulin** - hormone that signals the liver to use glucose.
Insulin promotes glycolysis, inhibits gluconeogenesis.

| Substrate                                   | Glycolysis | Gluconeogenesis |
| ------------------------------------------- | ---------- | --------------- |
| $\ce{ATP}$ (via phosphofructokinase)        | ↓          | ↑               |
| $\ce{ADP \& AMP}$ (competing w/ $\ce{ATP}$) | ↑          | ↓               |
| **Fructose-2,6-bisphosphate**               | ↑          | ↓               |
| **Glucagon**                                | ↓          | ↑               |
| **Insulin**                                 | ↑          | ↓               |
