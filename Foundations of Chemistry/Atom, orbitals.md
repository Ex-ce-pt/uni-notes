
## Dalton model

First scientific model of the atom by **John Dalton** (1803).
Atomos (anc. greek.) - "indivisible"

Theory:
- Hard sphere
- Very small
- Indivisible
- Combining in integer ratios
- Elements - atoms of one element are identical, atoms of different elements differ
- Reactions involve combining different atoms

![[atomic-model/dalton-model.png]]

## Thomson model

Model by **JJ Thompson** (1904).
"Plum pudding".
Investigated cathode ray tubes.
Applied magnetic field to the cathode ray.
Saw the beam move.
Discovered electrons.

Theory:
- Dalton model
- The atom's continuum is positively charged
- Negatively charged electrons are spread inside

![[atomic-model/thomson-model.png]]

## Rutherford model

Model by **Rutherford** (1911).
Studied radiation.
Put gold foil in the way of $\alpha$ radiation.
Expected: $\alpha$-particle penetrating /w some dispersion.
Observed: random repulsion from the foil.
Conclusion: the positive charge is very concentrated.
Discovered the atomic nucleus.

Theory (planetarium):
- The nucleus is small and positively charged
- Negatively charged electrons orbit it like planets orbit stars

![[atomic-model/rutherford-model.png]]

## Bohr-Rutherford model

Combined work of **Rutherford** and **Niels Bohr** (1913)
Insight: the atoms absorb and emit specific frequencies of the EM spectrum.

Theory:
- Rutherford model
- Electrons orbit the nucleus on discrete shells/orbits

![[atomic-model/bohr-model.png]]

> Not a physical representation, but an energy diagram.

In practice, only works for hydrogen.

## Quantum mechanics

1920s
Physicists are puzzled by light - a wave or a particle?

| Wave                    | Particle         |
| ----------------------- | ---------------- |
| Frequency               | Location & Mass  |
| Travel through a medium | Travel in vacuum |

**Wave-particles** - the lighter, the more similar to a wave, the heavier, the more similar to a particle.

Electrons are light - behave more like waves.
Nuclei are heavier - behave more like particles.

Theory:
- The orbitals are not discrete in location, but smeared out
- The waves are the probability density of finding an electron at a particular distance (radius) from the nucleus

![[atomic-model/schroedinger-model.png]]

Schrödinger equation:

$\hat H \Psi = E \Psi$
$\Psi$ - wavefunction.
$E$ - energy scalar (eigenvalue).
$\hat H$ - Hamiltonian, function that extracts info about potential ($e^-$-$e^-$ repulsion, $e^-$-$p^+$ attraction) & kinetic energy.

$\hat H = \hat V + \hat T$
$\hat V$ - potential energy
$\hat T$ - kinetic energy

> $E = \frac{Q_1Q_2}{4 \pi \epsilon_0 r}$, [[Cheat Sheet#Constants]]
> $Q_1 > 0, Q_2 < 0$ or vice versa, $E < 0$ and as $r \rightarrow 0, \space E \rightarrow -\infty$
> The more negative the total $E$ is, the more electrostatic attraction, the more stable the system.
> At the same time, as $r \rightarrow infty, \space E \rightarrow 0$ - free electron.
> The energy of an electron in the atom is lower than the energy of a free electron.

Copenhagen interpretation of the wavefunction:
$\Psi$ - the **state** of the system. The information about all the electrons and their own state is all contained in the wavefunction.

Born interpretation:
$\Psi^2 = \Psi \Psi^*$ - **probability density** (probability per unit volume) of finding an electron in a specific region in space around the nucleus.

#### Radial distribution

Want to know: total probability of finding an electron at a specific distance $r$ away from the nucleus (in any direction).
Know: $\Psi^2$ - probability density, probability per unit volume.
Consider an infinitesimal shell around $r$. Its volume would be: $V = \frac{4}{3} \pi r^3 \Rightarrow \frac{dV}{dr} = 4 \pi r^2$
Since the shell is infinitesimal, $\frac{dV}{dr} \cdot \Psi^2$ should approach the probability we're after.
**Conclusion**: $\frac{dV}{dr} \cdot \Psi^2 = 4 \pi r^2 \cdot \Psi^2$ - probability of finding an electron $r$ away from the nucleus (**electron density**).

| ![[atomic-model/psi-graph-simple.png]] | ![[atomic-model/psi-sq-graph-simple.png]] | ![[atomic-model/prob-graph-simple.png]] |
| -------------------------------------- | ----------------------------------------- | --------------------------------------- |

$\int_{0}^{\infty} \frac{dV}{dr}\cdot \Psi^2 dr = (\text{\# of electrons})$ - all of the electrons in the atom must exist *somewhere*.

#### Quantum numbers

Full form on the wavefunction: $\Psi(n, l, m_l, m_s)$ - extracts info about a specific electron.
$n, l, m_l, m_s$ - quantum numbers, first 3 describe electron's position is space.

| Letter | Values                                                                 | Name                                                  | Tells (about the electron)                                                         |
| ------ | ---------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------- |
| $n$    | $\mathbb{N} \setminus \{0\}$                                           | principal quantum number                              | electron shell;<br>orbital size;<br>orbital energy;<br>\# of nodes                 |
| $l$    | $[0 ; n-1]$                                                            | azimuthal quantum number/<br>orbital angular momentum | subshell;<br>orbital shape;<br>\# of nodal planes;<br>ang. mom. around the nucleus |
| $m_l$  | $[-l ; +l]$                                                            | magnetic quantum number                               | orbital;<br>orientation in space;<br>ang. mom. around the axis                     |
| $m_s$  | $\{+\frac{1}{2} (\upharpoonleft) ; -\frac{1}{2} (\downharpoonright)\}$ | magnetic spin                                         |                                                                                    |

**Pauli exclusion principle** - every electron in a single atom has a different combination of the quantum numbers.

#### Orbitals

| Orbitals | $n$ | $l$ | $m_l$               | $m_s$             |
| -------- | --- | --- | ------------------- | ----------------- |
| $1s$     | $1$ | $0$ | $0$                 | $\pm \frac{1}{2}$ |
| $2s$     | $2$ | $0$ | $0$                 | $\pm \frac{1}{2}$ |
| $2p$     | $2$ | $1$ | $-1, 0, +1$         | $\pm \frac{1}{2}$ |
| $3s$     | $3$ | $0$ | $0$                 | $\pm \frac{1}{2}$ |
| $3p$     | $3$ | $1$ | $-1, 0, +1$         | $\pm \frac{1}{2}$ |
| $3d$     | $3$ | $2$ | $-2, -1, 0, +1, +2$ | $\pm \frac{1}{2}$ |

#### Subshell naming

| $l$ | Subshell |
| --- | -------- |
| $0$ | $s$      |
| $1$ | $p$      |
| $2$ | $d$      |
| $3$ | $f$      |

#### Orbital shapes

- $l = 0$, $s$-orbital, shape: sphere

![[atomic-model/s-orbital.png]]

- $l = 1$, $p$-orbital, shape: dumbbells

![[atomic-model/p-orbital.png]]

- $l = 2$, $d$-orbital, shape: clover

![[atomic-model/d-orbitals.png]]

**Nodal plane** - a plane where there's no electron density; goes between the lobes of the orbital through the nucleus.
$l = \# \text{ of nodal planes of the orbital}$.

#### Orbitals on different shells

As $n$ increases, we add nodes.
The first instance of an orbital ($1s, \space 2p, \space 3d, \space 4f$) has no nodes.
**Node** - a point where the electron density is 0.
$\text{\# of nodes} = n - (l + 1)$

| ![[atomic-model/1s-wavefn-graph.png]]    | ![[atomic-model/2s-wavefn-graph.png]]    | ![[atomic-model/3s-wavefn-graph.png]]    |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| ![[atomic-model/1s-elec-dens-graph.png]] | ![[atomic-model/2s-elec-dens-graph.png]] | ![[atomic-model/3s-elec-dens-graph.png]] |
| ![[atomic-model/2p-wavefn-graph.png]]    | ![[atomic-model/3p-wavefn-graph.png]]    |                                          |
| ![[atomic-model/2p-elec-dens-graph.png]] | ![[atomic-model/3p-elec-dens-graph.png]] |                                          |
Different subshells on different shells, 3D (slice):
![[atomic-model/1s-2s-2p-3p.png]]
The shaded areas are the cusps on the graphs and the gaps are the nodes.

Note: the electrons on the subshells of the same shell (same $n$) are located at approximately the same distance from the nucleus. Though the "lower" subshells (lower $l$) also have additional cusps closer to the nucleus, that makes them slightly lower in energy. In this case, $2s$ is slightly lower in energy than $2p$, even though they are at a similar distance, because $2s$ also has a cusp where $1s$ would have it.
![[atomic-model/2s-vs-2p-elec-dens.png]]

#### Energy levels

Orbitals have different energies.
- Greater $n$ → higher energy (because of the distance)
- Greater $l$ → higher energy (usually, because electrons can't get as close to the nucleus, see $2s$ vs $2p$)
- Lower effective nuclear charge → higher energy

**Degenerate orbitals** - orbitals that have the same energy.
In isolated atoms, $p$, $d$, and $f$ orbitals are degenerate.
That is because without a reference point, there's no difference between the possible orientations of an orbital.

Energy diagram:
![[atomic-model/energy-levels.png]]

> In hydrogen atoms, whole shells are degenerate, meaning $2s$ and $2p$ all have the same energies, as do $3s$, $3p$, $3d$ etc.

#### Aufbau
(ger. Build-Up)

Rules:
1. **Fill lowest energy orbital first.**
	The atom wants to be as stable as possible (having the lowest energy possible), so if an electron is added and there's a lower energy orbital available, why not stick the electron there?
2. **Pair up as long as the energy diff between orbitals is greater than the electron repulsion**
	![[atomic-model/pairing-electrons.png]]
3. **Hund's rule** - (for degenerate orbitals) maximize the spin.
	First, one electron with a particular spin is placed into every orbital, then they start pairing up.
	This is because if 2 electrons were in the same orbital, they would repel each other, so why not occupy the empty orbital instead?
	![[atomic-model/hunds-rule.png]]
4. **Madelung's rule (rule of diagonals)** - fill orbitals in a diagonal pattern.
	Just a mnemonic to memorize the filling order.
	![[atomic-model/madelung-rule.png]]


Alternate way to write energy diagrams, electron configuration:

| Element   | Electron configuration                                                                       | Noble gas notation                                                        |
| --------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| $\ce{H}$  | $\textcolor{yellow}{1s^1}$                                                                   | $\textcolor{yellow}{1s^1}$                                                |
| $\ce{He}$ | $\textcolor{yellow}{1s^2}$                                                                   | $\textcolor{yellow}{1s^2}$                                                |
| $\ce{Li}$ | $\textcolor{cyan}{1s^2} \space \textcolor{yellow}{2s^1}$                                     | $\textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^1}$             |
| $\ce{B}$  | $\textcolor{cyan}{1s^2} \space \textcolor{yellow}{2s^2 \space 2p^1}$                         | $\textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^2 \space 2p^1}$ |
| $\ce{N}$  | $\textcolor{cyan}{1s^2} \space \textcolor{yellow}{2s^2 \space 2p^3}$                         | $\textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^2 \space 2p^3}$ |
| $\ce{F}$  | $\textcolor{cyan}{1s^2} \space \textcolor{yellow}{2s^2 \space 2p^5}$                         | $\textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^2 \space 2p^5}$ |
| $\ce{Ne}$ | $\textcolor{cyan}{1s^2} \space \textcolor{yellow}{2s^2 \space 2p^6}$                         | $\textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^2 \space 2p^6}$ |
| $\ce{Na}$ | $\textcolor{cyan}{1s^2 \space 2s^2 \space 2p^6} \space \textcolor{yellow}{3s^1}$             | $\textcolor{cyan}{\ce{[Ne]}} \space \textcolor{yellow}{3s^1}$             |
| $\ce{P}$  | $\textcolor{cyan}{1s^2 \space 2s^2 \space 2p^6} \space \textcolor{yellow}{3s^2 \space 3p^3}$ | $\textcolor{cyan}{\ce{[Ne]}} \space \textcolor{yellow}{3s^2 \space 3p^3}$ |
| $\ce{K}$  | ...                                                                                          | $\textcolor{cyan}{\ce{[Ar]}} \space  \textcolor{yellow}{4s^1}$            |
| $\ce{Ca}$ | ...                                                                                          | $\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2}$             |
| $\ce{Sc}$ | ...                                                                                          | $\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2 \space 3d^1}$ |
| $\ce{V}$  | ...                                                                                          | $\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2 \space 3d^2}$ |
| $\ce{Cr}$ | ...                                                                                          | $\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{red}{4s^1 \space 3d^5}$    |

**Valence shell/orbitals** $\textcolor{yellow}{\square}$ - the outermost shell/orbitals.
**Core orbital** $\textcolor{cyan}{\square}$ - orbital that is not valence.

Core orbitals have significantly lower energy than valence orbitals.
Valence orbitals tend to have comparable energies (not at all equal!).

We start filling up $4s$ orbital before $3d$. $3d$ **is lower in energy** than $4s$, but the repulsion from the $3s$ and $3p$ electrons is strong enough to make $4s$ a better option for an electron. Starting from $\ce{Sc}$, the nuclear charge is strong enough to start adding electrons to the $3d$ orbital.

When we get to $\ce{Cr}$, we get a jump from $(\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2 \space 3d^3})$ to $(\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{red}{4s^1 \space 3d^5})$ instead of $(\textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2 \space 3d^4})$. One of the reasons: Hund's rule - having 6 unpaired electrons means less repulsion. Same jump happens for $\ce{Cu}$.

#### Effective nuclear charge

**Shielding/screening** - surrounding electrons partially cancel the charge of the nucleus.
We are mostly interested in the valence electrons, so we can reformulate:
**Shielding/screening** - core electrons partially cancel the charge of the nucleus the valence electrons experience.

$Z_{\text{eff}}$ - effective nuclear charge, the charge that would result in the same interaction that an electron is experiencing, relevant because of shielding.

$Z_{\text{eff}} \approx Z - (\text{\# of core electrons})$ (gross estimation)

For valence electrons, $Z_{\text{eff}}$ increases going to the right in the periodic table (same core electrons, $Z$ increases), and decreases going down (more shells, more core electrons).

Greater $Z$ → greater $Z_{\text{eff}}$ → lower energy in all orbitals, because the electrons are drawn closer to the nucleus.

![[atomic-model/z-eff-inc.png]]
Even though $\ce{Li}$'s $2s$ orbital is still higher in energy than $\ce{H}$'s $1s$, they're still comparable, as valence orbitals.
Since $2s$ orbital has a cusp closer to the nucleus, its energy decreases faster than that of $2p$ when going through the periodic table.

![[atomic-model/2s-elec-dens-Li-vs-F.png]]


#### Blocks

Elements in the periodic table are organized in blocks. The block the element is in shows to which orbital an electron has been added last.
![[atomic-model/ptable-blocks.jpg]]


## Cations

**Ionization energy ($E_I$)** - energy that it takes to take away an electron from an atom.
$E_I > 0$.

$E_I \approx -E_{\text{orbital}}$, because we need to compensate the energy it took to make the electron "free" (0 potential energy).

![[atomic-model/ionization-energy.png]]

$\ce{Li}: \space \textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^1} \space | \space \ce{Li^+}: \space \textcolor{cyan}{\ce{[He]}} \space \textcolor{yellow}{2s^\textcolor{red}{0}}$
$\ce{Ti}: \space \textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^2 \space 3d^2} \space | \space \ce{Ti^+}: \space \textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^\textcolor{red}{1} \space 3d^2} \space | \space \ce{Ti^{2+}}: \space \textcolor{cyan}{\ce{[Ar]}} \space \textcolor{yellow}{4s^\textcolor{red}{0} \space 3d^2}$

Size of a cation is just a big smaller that the size of the neutral atom, except when losing a whole shell.

## Anions

**Electron affinity ($E_a$)** - energy released because electrons were added.

Electron affinities are smaller than ionization energies.

Generally, $E_a >0$.
When the electron added should either **go to the next orbital** or be the **first to pair**, $E_a < 0$.

| Element | $\ce{Li}$ | $\ce{Be}$ | $\ce{B}$ | $\ce{C}$ | $\ce{N}$ | $\ce{O}$ | $\ce{F}$ | $\ce{Ne}$ |
| ------- | --------- | --------- | -------- | -------- | -------- | -------- | -------- | --------- |
| $E_a$   | $60$      | $< 0$     | $27$     | $122$    | $<0$     | $141$    | $328$    | $<0$      |

Anions are a lot larger than the neutral atoms.
