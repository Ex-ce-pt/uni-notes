#Metabolism
aka. TCA Cycle (Tricarboxylic Acid Cycle), Krebs Cycle

Uses the pyruvate from the [[Glycolysis]].
**Aerobic** - needs $\ce{O2}$.
Inside the mitochondrial matrix.

## Pyruvate Dehydrogenase (PDH) Complex

In the mitochondrial matrix.
Turns pyruvate into Acetyl-CoA to prepare it for the Citric Acid Cycle.
$\ce{\text{pyruvate} + CoA + NAD+ -> Ac-CoA + CO2 + NADH}$

Uses many cofactors: TPP, Lipoamide, $\ce{FAD}$, CoA, $\ce{NAD+}$.
Series of reactions close together to improve efficiency.
**Substrate channeling** - passage of intermediates from one enzyme directly to another without release.

Acetyl-CoA - $\ce{Ac-S-CoA}$
High energy of hydrolysis.
High transfer potential of acetyl group.

> Coenzyme A has adenine and ribose in its structure.
> Cells like to reuse compounds as much as possible!

In the complex:

| Step | Enzyme                       | Prosthetic group (cofactor) | Kind of reaction                |
| ---- | ---------------------------- | --------------------------- | ------------------------------- |
| E1   | Pyruvate dehydrogenase       | $\ce{TPP}$                  | Decarboxylation of pyruvate     |
| E2   | Dihydrolipoyl Transacetylase | Lipoamide                   | Oxidation to a carbocation      |
| E3   | Dihydrolipoyl Dehydrogenase  | $\ce{FAD}$                  | Restoration & transfer of $e^-$ |

#### E1

Cofactor: $\ce{TPP}$ (derived from Vitamin B1) - catalyses decarboxylation almost always.
Thiazolium ring can easily lose a proton and act as a nucleophile.

![[_media/Metabolic Pathways/Citric Acid Cycle/TPP-H-loss.png|310]]

![[_media/Metabolic Pathways/Citric Acid Cycle/PDH-E1.png]]

#### E2

Cofactor: **Lipoic acid**
Has a disulfide bond, can receive $e^-$ by breaking it.

![[_media/Metabolic Pathways/Citric Acid Cycle/lipoic-acid.png]]

![[_media/Metabolic Pathways/Citric Acid Cycle/PDH-E2-1.png]]
![[_media/Metabolic Pathways/Citric Acid Cycle/PDH-E2-2.png]]

#### E3

Dihydrolipoamide gives the $\ce{2 H+}$ back to $\ce{FAD}$, forming $\ce{FADH2}$.
Then, $\ce{FADH2}$ transfers them to $\ce{NAD+}$, forming $\ce{NADH}$.
$\ce{FAD}$ is there, because it's covalently bonded to E3, making sure that the hydrogens get transferred quickly and efficiently, then $\ce{NAD+}$ takes them and escapes.

![[_media/Metabolic Pathways/Citric Acid Cycle/PDH-E3.png]]

## TCA cycle

Cyclic pathway.
**Amphibolic pathway** - involved in both catabolism and anabolism.
Reactions are either oxidation/decarboxylation or preparation for those.
9 steps.

Summary:
	$\ce{Acetyl -> 2 CO2 + 3 NADH + FADH2 + GTP (ATP)}$

The cycle is driven by the **generation of citrate** (very exergonic) and decarboxylations ($\ce{CO2}$ constantly escapes).

Decarboxylations are very energetically favourable:
$\ce{CO2}$ is very inert and stable → generating it yields a lot of energy

Intermediates can be withdrawn to synthesise other molecules:
- nucleotides
- amino acids
- glucose

#### Step 1 - synthesis of citrate

$\ce{Acetyl-S-CoA + Oxaloacetate + H2O -> Citrate + HS-CoA}$

![[_media/Metabolic Pathways/Citric Acid Cycle/TCA-1.png]]

Enzyme: **Citrate synthase**

The acetyl group is attached to oxaloacetate and the sulfur bond of CoA is hydrolysed.

#### Step 2 - dehydration

$\ce{Citrate \rightleftharpoons cis-Aconitate + H2O}$

Enzyme: **Aconitase**

Introduces a double bond.

#### Step 3 - hydration

$\ce{cis-Aconitate + H2O \rightleftharpoons Isocitrate}$

Enzyme: **Aconitase**

The $\ce{OH}$ group is added back, but now at a different position.

#### Step 4 - dehydrogenation

$\ce{Isocitrate -> \alpha-Ketoglutarate + NADH + CO2}$

Enzyme: **Isocitrate dehydrogenase**

1st carbon cleaved, 1st $\ce{NADH}$ produced.

#### Step 5 - dehydrogenation

$\ce{\alpha-Ketoglutarate + CoA -> Succinyl-CoA + NADH + CO2}$

Enzyme: **$\alpha$-ketoglutarate dehydrogenase complex**

2nd carbon cleaved, 2nd $\ce{NADH}$ produced.
The enzyme complex is almost identical to Pyruvate dehydrogenase.
The substrate is added onto CoA again.

#### Step 6 - phosphorylation/oxidation

$\ce{Succinyl-CoA + Pi \rightleftharpoons Succinate + CoA + GTP}$

Enzyme: **Succinyl-CoA synthetase**

#### Step 7 - dehydrogenation

$\ce{Succinate \rightleftharpoons Fumarate + FADH2}$

Enzyme: **Succinate dehydrogenase**

#### Step 8 - hydration

$\ce{Fumarate + H2O \rightleftharpoons Malate}$

Enzyme: **Fumarase**

Makes the substrate more reactive.

#### Step 9 - dehydrogenation

$\ce{Malate \rightleftharpoons Oxaloacetate + NADH}$

Enzyme: **Malate dehydrogenase**

Regenerates oxaloacetate.

## Regulation

Points:
- PDH complex
- citrate synthase
- isocitrate dehydrogenase complex
- $\alpha$-ketoglutarate dehydrogenase complex

TCA cycle intermediates, $\ce{ATP}$, $\ce{NADH}$, fatty acids - deactivate.
$\ce{AMP}$, $\ce{ADP}$, $\ce{NAD+}$, $\ce{Ca^{2+}}$ - activate.

$\ce{Ca^{2+}}$ contracts muscle, signals metabolism to produce energy because the body is doing work.

PDH can be phosphorylated to disactivate it, and dephosphorylated to activate it again.

