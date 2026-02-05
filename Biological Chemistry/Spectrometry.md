
**Spectroscopy** - interaction between energy (light/electrons) & material (atoms/molecules).

Different types.
Used to determine structures of molecules.
Produces spectra that you need to interpret.

## Infrared Spectroscopy (IR)

Gives: functional groups (chemical bonds).

Uses infrared light.
Chemical bonds absorb the light and vibrate.
Each bond absorbs a specific wavelength (depends on atom mass, bond type).

![[IR ex. 1.png]]
$\text{x-axis}$ - wavenumber, wavelength in $cm^{-1}$, **axis goes from high to low**.
$\text{y-axis}$ - transmittance, how much light passed through the material.
$x < 1500$ - "fingerprint region", always some absorption, doesn't give much info, but unique for a molecule.

![[IR ex. 2.png]]
Same type of bonds ($\ce{C-H, C-C}$) → similar spectra.


Absorbance in important functional groups (units omitted for clarity):
- **Alcohols ($\ce{OH}$)** - broad and strong absorbance at  $3000-3400$
- **Amines** ($\ce{NH2}$) - $\textasciitilde 3200-3300$
- **Alkenes** - just above $3000$
- **Alkanes** - just below $3000$
- **Nitriles** ($\ce{C#N}$) - $2200$
- **Carbonyls** ($\ce{C=O}$) - strong absorbance $\textasciitilde 1700$

- **Carboxylic acids ($\ce{COOH}$)** = carbonyl + alcohol = $3000-3400$ & $\textasciitilde 1700$
- **Esters** = carbonyl = $\textasciitilde 1700$
- **Aromatics** = alkenes = just above $3000$

> Everything above 3000 is a double bond.

![[IR ex. 3.png]]

Summary for different functional groups:
![[IR ex. 4.png]]

## Nuclear Magnetic Resonance Spectroscopy (NMR)

Gives: chemical environment of certain atoms.

Based on nuclei spin that behave like rotating magnets and their frequency.
The nuclei align themselves with the magnetic field of the machine.
$\alpha$-state - aligned with the field. $\beta$-state - aligned opposed to the field.
The states are *almost* 50-50, but not quite and the sum magnetic field is nonzero.
Radio wave is used to manipulate the magnetization and a frequency is acquired.
Common spin nuclei: $\ce{^1H, ^{13}C, ^{15}N, ^{31}P}$.

Focusing on $\ce{^1H}$ from now on, but same applies to other atoms.

Info we get:
1. [\# of peaks](#Number%20of%20peaks)
2. [[#Size of peaks]]
3. [[#Splitting pattern]]
4. [Peak position/chemical shift](#Chemical%20shift) ($ppm$)

Graph:
![[NMR graph.png]]
$\text{x-axis}$ - $ppm$, shows chemical shift, , **axis goes from high to low**.
$\text{y-axis}$ - intensity.

> Tables are not always accurate, values depend on solvents, temperature, pH.

Peak at $0$ is generally the calibrating signal.

#### Number of peaks

Equal to **\# of unique proton environments**.
**Proton environment** - position & interaction of the $\ce{^1H}$ relative to the other atoms.

![[NMR proton environment.png]]

#### Size of peaks

Integrated area under the peaks is **proportional** to the \# of $\ce{^1H}$ in each environment.
The horizontal lines on the graph is integration: going left to right, the curve accumulates the area under the graph.

> If there's a fractional \# of $\ce{^1H}$, multiply the values by a factor.

![[NMR size of peaks.png]]

#### Splitting pattern

Peaks split into multiple subpeaks because of the interaction between neighboring hydrogens.
$\text{\# of subpeaks} = (\text{\# of neighbors}) + 1$
*Neighbors* are other $\ce{^1H}$ within 3 bonds (multiple bonds count as 1).
In practice: count $\ce{^1H}$ of the neighboring carbon.
$\ce{H-C-CH2}$ - the hydrogen on the left has 2 neighbors.

> The $\ce{^1H}$ that are identical to the one we're focusing on **are not counted** as neighbors!

![[NMR splitting pattern.png]]

#### Chemical shift

How much each peak is shifted relative to the standard.
Tables are used to determine how big the shift generally is.
Add up chemical shift values from the table, if multiple conditions apply.

If the $\ce{^1H}$ is close to electronegative atoms → shifted more to the left.
If the $\ce{^1H}$ is near a lot of electrons → shifted more to the right.
This shift explains why sometimes the peaks are shifted more than the table says they should be.

$\ce{OH}$ & $\ce{NH2}$ have broad peaks and produce singlets.

**Aromatics** commonly around $8.0-7.0$: (rtl) peak, peak, pause, peak.

## Mass Spectrometry

Gives: molecular mass, molecular fragments. 

Molecules turned into ions (electron bombardment) and separated according to their mass.
Usually coupled to other techniques to separate the compound first:
- **LC/MS** - liquid chromatography/mass spectrometry
- **GC/MS**  - gas chromatography/mass spectrometry

Graph:
![[MS fragmentation.png]]
$\text{x-axis}$ - mass-to-charge ratio.
$\text{y-axis}$ - intensity (%), \# of counted ions.

#### Common fragments

> Fragments of the molecule are also seen on the graph - there's never a single peak!
> There are also isotopes. $\ce{Cl}$ & $\ce{Br}$ leave 2 peaks.

91 - benzene ring
```smiles
C-c1ccccc1
```
29 - ethyl ion
$\ce{CH3CH2+}$

#### Nitrogen rule

Atoms have either even **nominal mass & even valence** OR **odd nominal mass & odd valence**.
**Nominal mass** - integer value of atomic mass.

The exception is $\ce{N}$: mass = 14, valence = 3

For neutral molecules in MS:
- odd mass → odd \# of $\ce{N}$
- even mass → even \# of $\ce{N}$ (0 counts as even)

