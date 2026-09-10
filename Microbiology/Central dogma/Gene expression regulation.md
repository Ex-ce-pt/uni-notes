
Regulation helps to adapt to changing environment.
In multicellular organisms, all cells have the same genes, but perform different functions.

## Replication

Replication is regulated by binding a protein (e.g. SeqA) to oriC to block DnaA from binding.
==more details?==

## Transcription

**Operon** - regulatory region + coding genes; "header + content".
Allows to regulate multiple proteins at once.
**Regulon** - set of multiple operons of similar function that are all regulated by same/similar molecules.

DNA regulatory region:
	**Promoter** $(+)$ - used to start transcription of the operon; typically in the beginning.
	**Operator** $(-)$ - used to block transcription of the operon; typically between promoters & genes.

Transcription factors (regulatory proteins that bind to the regulatory region):
	**Activator** $(+)$ - binds to promoters to start transcription.
	**Repressor** $(-)$ - binds to operators to block transcription.

**Inducer** - small molecule that binds to and disables repressors or enhances activators.

![[operon.png]]

**Structural genes** - encode enzymes & structural proteins.
**Regulatory genes** - encode proteins that regulate gene expression.

For regulatory genes:
	**Auto-regulation** - regulation of own production.
	**Co-regulation** - 2 genes regulated together.
	**Cis-acting** - regulating genes on the same DNA molecule.
	**Trans-acting** - regulating genes on a different DNA molecule.

**Modulon** - regulons regulated in response to **general** metabolic/environmental factors.
**Stimulon** - regulons regulated in response to **specific** environmental factors (stimuli).

---

**Constructive operon** - always on; housekeeping genes: DNA replication, repair, metabolism.
**Repressible operon** - default on, can be turned off.
**Inducible operon** - default off, can be turned on.

#### trp operon

Example of a **repressible operon**: default on, can be turned off.
Encodes enzymes that produce tryphophan.

- Little tryptophan → operon transcribed.
- Much tryptophan → tryptophan binds to a repressor, which allows it to bind to the operator and block transcription.

#### lac operon

Example of an **inducible operon**: default off, can be turned on.
Encodes enzymes that metabolise lactose.
The cell insists on using glucose as much as it can.
**Enzyme IIA** - produces $\text{cAMP}$ in response to glucose levels dropping.
$\text{cAMP}$ binds to **catabolite activator protein (CAP)**.
Lactose binds to the repressor, removing it from the operator.

| Transcription | Glucose ↑ | Glucose ↓ |
| ------------- | --------- | --------- |
| **Lactose ↑** | Slow      | Steady    |
| **Lactose ↓** | Blocked   | Blocked   |

#### Global and local

**Local regulation** - regulation of a set of several genes. ==check==
**Global regulation** - regulation of a set of lots of genes.

**Alarmones** - small nucleotide derivatives prokaryotes produce to globally regulate genes in response to stress (e.g. $\text{cAMP}$).

**(p)ppGpp** - guanosine penta/tetra prosphate - alarmone produced in response to low amino acid levels.
**ReIA** - (p)ppGpp synthase - senses uncharged tRNA and produces pppGpp.
$\ce{ATP + GTP -> AMP + pppGpp}$

**Spot T** - degrades ReIA.
$\ce{pppGpp -> GTP + PPi, ppGpp -> GDP + PPi}$

**Stringent response** - global response to low amino acid levels; ribosomes get stalled.

#### Attenuation

Only in prokaryotes.

==???==
==attenuation - concentration of trp influences the speed of translation, which influences the mRNA conformation==

#### Riboswitches

Only in prokaryotes.
**Riboswitch** - noncoding RNA at the 5' end of some mRNA transcripts.

During transcription:
	Downstream of the riboswitch → stem loop (terminator/antiterminator).
	A small regulatory molecule can bind to the riboswitch → riboswitch changes conformation → mRNA changes conformation → stem loop downstream changes to the opposite of what it was by default.
	So, initially - antiterminator stem loop (RNA Polymerase continued transcription), a small molecule binds to the riboswitch - antiterminator stem loop changed to terminator stem loop. RNA Polymerase would then detect the change and stop transcription.

During translation:
	Downstream of the riboswitch → RBS (ribosome binding site).
	Molecule binding or not to the riboswitch could make the RBS accessible for the ribosome or not.

![[riboswitch.png]]

#### Other

**DNA supercoiling**:
Supercoiled → lots of strain, easier to unwrap.
log phase → supercoiling, stationary phase → less supercoiling.

**NAPs**:
Shield different genes from transcription at different points in growth.

**Histone acetylation** - enhanced transcription.
**Histone methylation** - position dependent effect.

Alternative $\sigma$ factors for different environmental needs.
$\sigma^{70}$ - housekeeping genes
$\sigma^{32}$ - heat shock
$\sigma^{38}$ - starvation/stationary phase

## Translation

The speed of translation is influenced by:
- The specific codons used.
- Secondary structures of mRNA
- Multiple of charged amino acids together or proline

## Growth

Resource scarcity regulates growth by itself.

To grow, cell needs more proteins, more ribosomes, more rRNA.
rRNA genes are close to oriC and in the direction of the replication fork.

## Prokaryotes vs eukaryotes


|                      | Prokaryotes                                                  | Eukaryotes                                                  |
| -------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| mRNA content         | **Polycistronic transcript**<br>1 operon → multiple proteins | **Monocistronic transcript**<br>1 operon → 1 protein        |
| mRNA processing      | mRNA ready to use                                            | mRNA processed                                              |
| Gene expr regulation | @ transcription (incl. attenuation & riboswitches)           | transcription & translation are separated in time and space |
