#Metabolism 

## Catabolism

FAs provide way more energy than glucose, because they are less oxidized than glucose.

#### Lipid droplet

Storage of lipids (triacylglycerols).
The membrane is a phospholipid monolayer.

Glucagon & epinephrine trigger the splitting of triacylglycerols.

**Lipases** - enzymes that split FAs from glycerol; hydrolysis reaction.
**Serum albumin** - protein that transports FAs through the blood; ~50% of blood.

Glycerol itself gets converted to **dihydroxyacetone phosphate (DHAP)** and enters [[Metabolic Pathways/Glycolysis|glycolysis]].

![[_media/Metabolic Pathways/Fatty Acid Metabolism/glycerol-degradation.png]]

#### FA degradation

**Step 1 - activation of FA**
In cytoplasm, at the outer mitochondrial membrane.
Enzyme: **Fatty acyl-CoA synthetase** (uses ATP).

First, adenylyl transfer, then, binding to CoA.
**Adenylyl transfer** - transfer of the $\ce{Pi}$-Adenosine group, leaving the $\ce{PPi}$ group.
Adenylyl is a better leaving group than $\ce{Pi}$, so it can drive particularly unfavourable reactions.

![[_media/Metabolic Pathways/Fatty Acid Metabolism/FA-activation.png]]


**Step 2 - transfer into mitochondria**
**Carnitine shuttle** - transfers **activated** FAs into mitochondria.

![[_media/Metabolic Pathways/Fatty Acid Metabolism/carnitine-shuttle.png]]

#### Beta oxidation

In mitochondrial matrix.
Oxidizing $\beta$ position of the FA.
Stepwise removal of $\ce{C}2$ units in the form of Acetyl-CoA.
Acetyl-CoA goes into the [[Metabolic Pathways/Citric Acid Cycle (TCA Cycle)|TCA cycle]].
The $e^-$ from the $\ce{C-C}$ bonds get transferred onto $\ce{NADH}$ and enter [[Metabolic Pathways/Electron Transport Chain|ETC]].

For a saturated FA of length $2n$:
- $n$ acetyl-CoA molecules
- $(n-1)$ cycles of $\beta$ oxidation
- $(n-1)$ $\ce{NADH}$ molecules
- $(n-1)$ $\ce{FADH2}$ molecules

**Step 1 - oxidation to an alkene**

$\ce{R-CH2-CH2-CH2-C(=O)-S-CoA + FAD -> R-CH2-CH=CH-C(=O)-S-CoA + FADH2}$

Enzyme: **Acyl-CoA dehydrogenase**

Introduces a double bond between the $\alpha$ and $\beta$ positions.
ETF helps carry the $e^-$ to FAD, which then goes to [[Metabolic Pathways/Electron Transport Chain|ETC]].

> Creates a trans product!

**Step 2 - hydration**

$\ce{R-CH2-CH=CH-C(=O)-S-CoA -> R-CH2-CH(OH)-CH2-C(=O)-S-CoA}$

Enzyme: **Enoyl-CoA hydratase**

Places an $\ce{OH}$ group at the $\beta$ position.

**Step 3 - oxidation to a ketone**

$\ce{R-CH2-CH(OH)-CH2-C(=O)-S-CoA + NAD+ -> R-CH2-C(=O)-CH2-C(=O)-S-CoA + NADH}$

Enzyme: **$\beta$-hydroxyacyl-CoA dehydrogenase**

The NADH created goes into [[Metabolic Pathways/Electron Transport Chain|ETC]].

**Step 4 - cleavage of an acetyl group**

$\ce{R-CH2-C(=O)-CH2-C(=O)-S-CoA + CoA-SH -> R-CH2-C(=O)-S-CoA + CH3-C(=O)-S-CoA}$

Enzyme: **Acyl-CoA acetyltransferase**

CoA performs a nucleophilic attack on the ketone, splitting the molecule into acetyl-CoA and a new FA.

#### Monounsaturated Fatty Acids

Special enzyme (**enoyl-CoA isomerase**) makes sure the double bond is at the correct position.
Then the cycle continues.

#### Polyunsaturated Fatty Acids

Doesn't fit in the enzymes.

2,4-dienoyl-CoA reductase converts a 2,4-dienoyl into 3-enoyl.
Then, see [[#Monounsaturated Fatty Acids]].

#### Odd-numbered Fatty Acids

Propionyl-CoA left after $\beta$ oxidation.
**Propionyl-CoA carboxylase** - adds a carboxyl group to propionyl-CoA, extending it by 1 $\ce{C}$.
Then the groups are rearranged.

Resulting compound is **succinyl-CoA**, which goes to [[Metabolic Pathways/Citric Acid Cycle (TCA Cycle)|TCA cycle]].

**Biotin** - coenzyme for carboxylation reactions.
**Vitamin B12** - coenzyme for intramolecular rearrangement; has $\ce{Co^{3+}}$.
Cobalt bond is susceptible to homolytic cleavage.

## Anabolism

Entirely different pathway compared to catabolism.
**In the cytoplasm**.

**FA synthase** - single polypeptide that does almost all of lipid anabolism on mammals.
Multiple active sites, uses substrate channeling to move the intermediates between them.

**ACP** - acyl-carrier protein; intermediates stay attached to it.

$\ce{NADP+}$ is used.

**Acetyl-CoA carboxylase** - makes malonyl-CoA (biotin coenzyme)

## Regulation

**Acetyl-CoA carboxylase** is regulated in anabolism.
Phosphorylated enzyme is inactive.
Deactivation - AMP stimulates, ATP inhibits
Activation - insulin stimulates, glucagon and epinephrine inhibit

| Regulator                 | Effect on acetyl-CoA carboxylase (anabolism) |
| ------------------------- | -------------------------------------------- |
| AMP                       | ↓                                            |
| ATP                       | ↑                                            |
| Insulin                   | ↑                                            |
| Glucagon &<br>epinephrine | ↓                                            |

