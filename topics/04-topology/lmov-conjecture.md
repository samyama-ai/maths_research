---
id: 04-topology/lmov-conjecture
title: "LMOV Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# LMOV Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/lmov-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Labastida–Mariño–Ooguri–Vafa (LMOV) conjecture asserts that the colored HOMFLY-PT invariants of a link, after a universal change of generating function dictated by large-$N$ duality, are governed by a finite table of **integers** — the counts of BPS states (M2-branes) ending on a Lagrangian brane in the resolved conifold.

Concretely: let $\mathcal{L}$ be an oriented framed link with $L$ components. Assemble its colored HOMFLY-PT invariants into a partition function $Z(\mathcal{L})$, take $F = \log Z$, and expand $F$ in "reformulated invariants" $f_{\vec\mu}(q,a)$ (Section 2). The conjecture is that

$$f_{\vec\mu}(q,a) \;=\; \sum_{g\ge 0}\ \sum_{Q\in\frac12\mathbb{Z}} N_{\vec\mu;\,g,\,Q}\,\bigl(q^{1/2}-q^{-1/2}\bigr)^{2g-2+L}\,a^{Q}$$

with **$N_{\vec\mu;g,Q}\in\mathbb{Z}$** and only **finitely many** nonzero for each $\vec\mu$. Three claims are packaged here:

1. **Pole structure:** $f_{\vec\mu}$ has a pole of order at most $2-L$ at $q=1$, i.e. the expansion starts at $g=0$.
2. **Symmetry:** $f_{\vec\mu}(q^{-1},a) = (-1)^{L-1} f_{\vec\mu}(q,a)$, forcing only even/odd powers of $z=q^{1/2}-q^{-1/2}$ of the right parity.
3. **Integrality:** the coefficients $N_{\vec\mu;g,Q}$ are integers.

A complete proof requires all three for every framed link and every coloring $\vec\mu=(\mu^1,\dots,\mu^L)$ by partitions. A disproof requires one link, one $\vec\mu$, and one coefficient with nonzero denominator (or infinitely many nonzero $N$).

## 2. Mathematical Foundations

**Colored HOMFLY-PT.** For a partition $\lambda$, let $W_\lambda(\mathcal{L};q,a)$ denote the unnormalized HOMFLY-PT invariant of $\mathcal{L}$ colored by the irreducible $U(N)$ representation $R_\lambda$, with $a=q^N$ and $q=e^{g_s}$. These arise as $SU(N)$ Chern–Simons expectation values of Wilson loops at level $k$, $q = e^{2\pi i/(k+N)}$, analytically continued in $N$. Set $z = q^{1/2}-q^{-1/2}$.

**Chern–Simons partition function.** Introduce $L$ sets of auxiliary variables $x^\alpha=(x^\alpha_1,x^\alpha_2,\dots)$ and put

$$Z(\mathcal{L}) \;=\; \sum_{\vec\lambda} W_{\vec\lambda}(\mathcal{L})\ \prod_{\alpha=1}^{L} s_{\lambda^\alpha}(x^\alpha),\qquad F \;=\; \log Z,$$

$s_\lambda$ the Schur function. In the Chern–Simons/topological-string dictionary $x^\alpha$ are holonomy eigenvalues on the $\alpha$-th brane.

**Reformulation.** The LMOV ansatz is the plethystic (Adams-operation) rewriting

$$F \;=\; \sum_{d=1}^{\infty}\ \sum_{\vec\mu\ne \vec\emptyset} \frac{1}{d}\, f_{\vec\mu}\bigl(q^{d},a^{d}\bigr)\ \prod_{\alpha=1}^{L} s_{\mu^\alpha}\bigl((x^\alpha)^{d}\bigr),$$

where $(x)^d=(x_1^d,x_2^d,\dots)$. Möbius inversion over $d$ determines $f_{\vec\mu}$ uniquely from the $W_{\vec\lambda}$; a priori $f_{\vec\mu}\in\mathbb{Q}(q^{1/2},a^{1/2})$. Equivalently, in power-sum coordinates,

$$f_{\vec\mu}(q,a) \;=\; \sum_{d\ge 1}\frac{\mu(d)}{d}\sum_{\vec\nu}\ \chi \text{-weighted }\log Z\bigl(q^{d},a^{d}\bigr),$$

using the characters $\chi_{\lambda}(\nu)$ of the symmetric group to pass between Schur and power-sum bases.

**Physical origin.** Under Gopakumar–Vafa large-$N$ duality, $SU(N)$ Chern–Simons on $S^3$ equals the topological A-model on the resolved conifold $\mathcal{O}(-1)^{\oplus2}\to\mathbb{P}^1$, with $\mathcal{L}\subset S^3$ lifting to a Lagrangian brane $\mathcal{C}_\mathcal{L}$. Then $N_{\vec\mu;g,Q}$ is (conjecturally) an Euler characteristic of a moduli space of M2-branes with boundary winding $\vec\mu$, genus $g$, and Kähler charge $Q$; integrality is the statement that a BPS index counts objects.

## 3. History & State of the Art (SOTA)

- **1998–1999.** Gopakumar–Vafa propose the closed-string integrality structure and the conifold transition (*Adv. Theor. Math. Phys.* 3, 1999).
- **1999–2000.** Ooguri–Vafa extend the duality to knots, producing the first version of the conjecture for the fundamental representation (*Nucl. Phys. B* 577, 2000).
- **2000–2002.** Labastida–Mariño–Vafa and Labastida–Mariño give the full multi-component, all-colorings formulation, the group-theoretic reformulation via Adams operations, and extensive checks on torus knots.
- **2003.** Liu–Liu–Zhou prove the Mariño–Vafa Hodge-integral formula, which is the framed-unknot instance of the whole framework (*J. Differential Geom.* 65).
- **2010.** Liu–Peng prove the pole structure, the $q\mapsto q^{-1}$ symmetry, and integrality of the reformulated invariants for framed links, using the cut-and-join equation together with a $p$-adic/congruence argument (*J. Differential Geom.* 85).
- **2013–2016.** Diaconescu–Shende–Vafa and Maulik supply the *geometric* side for algebraic knots: stable-pair invariants of the conifold with Lagrangian boundary reproduce HOMFLY-PT (Maulik's proof of the Oblomkov–Shende conjecture, *Invent. Math.* 204, 2016).
- **2017–2021.** Kucharski–Reineke–Stošić–Sułkowski's knots–quivers correspondence recasts LMOV integrality as Donaldson–Thomas integrality for symmetric quivers (Efimov's theorem), and Stošić–Wedrich prove the correspondence for all rational (2-bridge) links.

**SOTA summary.** The *arithmetic* statement is theorem-level for framed links (Liu–Peng); the *geometric/enumerative* statement — that the $N_{\vec\mu;g,Q}$ count actual BPS states with a moduli-theoretic definition — is proven only in restricted classes, and the $SO/Sp$–Kauffman analogue remains open.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Unknot, all colorings $\lambda$ | $f_{(1)} = \dfrac{a^{1/2}-a^{-1/2}}{q^{1/2}-q^{-1/2}}$, $f_\lambda=0$ for $|\lambda|\ge2$ | Ooguri–Vafa 2000 |
| Framed unknot, all $\lambda$ | Equivalent to Mariño–Vafa Hodge-integral formula; proved | Liu–Liu–Zhou 2003 |
| Torus knots $T(m,n)$, colorings up to $|\lambda|\le 4$–$6$ | Verified by explicit Rosso–Jones computation | Labastida–Mariño 2001 |
| Links up to 8 crossings, fundamental and small colorings | Verified numerically | Ramadevi–Sarkar 2001 |
| All framed links, all $\vec\mu$: pole structure + symmetry + integrality of $f_{\vec\mu}$ | Proved | Liu–Peng 2010 |
| Algebraic knots (links of plane-curve singularities) | BPS numbers realized as stable-pair/Hilbert-scheme invariants | Diaconescu–Shende–Vafa 2013; Maulik 2016 |
| Rational (2-bridge) links | Knots–quivers correspondence proved ⇒ DT integrality ⇒ LMOV integrality | Stošić–Wedrich 2021 |
| Torus knots, $(2,2p+1)$ and $(3,q)$ families | Explicit quivers found; LMOV integers computed | Kucharski–Reineke–Stošić–Sułkowski 2019 |

Not covered: the Kauffman/$SO(N)$ version (Bouchard–Florea–Mariño, Mariño 2010) is verified only in low degree; the knots–quivers correspondence is unproven for general hyperbolic knots.

## 5. Principal Obstacles

- **Möbius inversion destroys positivity control.** $f_{\vec\mu}$ is an alternating sum over divisors $d$ of $|\vec\mu|$ of terms $\log Z(q^d,a^d)$ weighted by $\mu(d)/d$. Denominators of size $d$ appear at every step; showing they cancel is a congruence problem, not a skein-theoretic one. Ordinary skein relations, Kauffman-bracket state sums, and quantum-group $R$-matrix formulas give no handle on $p$-divisibility.
- **No cohomology theory to count.** Integrality proofs of Gopakumar–Vafa type usually come from an Euler characteristic of a moduli space. For open strings with Lagrangian boundary there is no general, rigorously constructed moduli space of holomorphic curves with boundary on $\mathcal{C}_\mathcal{L}$ (transversality and boundary-bubbling obstructions), so the *conceptual* proof is unavailable outside algebraic knots.
- **$\mathfrak{sl}_N$ representation theory grows too fast.** Verifying a coloring $\lambda$ with $|\lambda|=n$ needs cabling by $n$ strands; the Hecke-algebra dimension grows like $n!$, so brute-force checks stall around $|\lambda|\le 6$ for non-torus knots.
- **The quiver route needs an existence theorem.** The knots–quivers correspondence *implies* integrality, but proving a symmetric quiver exists for a given knot is itself an open combinatorial problem; existing proofs are constructive and class-specific (rational links, arborescent partial cases).
- **Orientifold sector.** For the Kauffman polynomial the reformulation involves composite representations and an unoriented worldsheet contribution; the Adams-operation structure is more intricate and the cut-and-join machinery of Liu–Peng does not directly apply.

## 6. The Gap

The gap is now less arithmetic than geometric. Liu–Peng close the integrality statement as an assertion about rational functions; what is *not* proved in general is that

$$N_{\vec\mu;g,Q} \;=\; \chi\bigl(\mathcal{M}_{\vec\mu,g,Q}\bigr)\quad\text{(up to sign)}$$

for an honest moduli space $\mathcal{M}$ of BPS states — the statement that gives the integers meaning, predicts signs and vanishing, and would explain the observed positivity after a sign twist. Concretely, three steps remain:

1. Construct $\mathcal{M}_{\vec\mu,g,Q}$ (or a substitute: a quiver, a skein module, a HOMFLY-PT homology) for **arbitrary** links, not just algebraic knots and rational links.
2. Prove the knots–quivers correspondence in general, or produce a counterexample.
3. Prove pole structure + symmetry + integrality in the $SO/Sp$–Kauffman setting, where no analogue of Liu–Peng exists.

## 7. Current Research (as of June 2026)

- **Skeins on branes.** Ekholm–Shende's program constructs the open topological string partition function from the HOMFLY-PT skein module of a Lagrangian filling, giving a first-principles derivation of the reformulation. *(frontier — verify)* Extensions to arbitrary Legendrian conormals and to the $\mathbb{Z}$-graded/refined setting are active at IHES, Uppsala, and Harvard.
- **Knots–quivers.** Groups at IST Lisbon (Stošić), Warsaw (Sułkowski, Panfil), and Bonn (Reineke, Wedrich) push the correspondence toward arborescent and general hyperbolic knots, and toward multi-component links where the quiver has several "knot" nodes.
- **Refined/categorified LMOV.** Superpolynomials and HOMFLY-PT homology (Gorsky, Nawata, Oblomkov, Rasmussen) suggest $N_{\vec\mu;g,Q}$ are Euler characteristics of a triply-graded homology; a refined LMOV with positivity is conjectured but only checked in families. *(frontier — verify)*
- **Chinese school (Liu, Peng, Zhu, Chen).** Congruence skein relations for colored HOMFLY-PT, and extensions of the cut-and-join method to Kauffman-type invariants.

## 8. Future Work

- Prove the knots–quivers correspondence for all knots, or identify the obstruction; this would give a uniform, DT-theoretic proof of LMOV integrality with signs.
- Extend Maulik-type stable-pair geometry from algebraic knots to satellite and cable knots, where the Lagrangian conormal is still algebraically accessible.
- Develop a cut-and-join / congruence proof in the $SO/Sp$ setting to settle the Kauffman LMOV conjecture of Bouchard–Florea–Mariño and Mariño.
- Give an intrinsic topological definition of $N_{\vec\mu;g,Q}$ (skein module rank, or homology dimension), turning the integers into a link invariant defined without passing through $\log Z$.
- Push explicit verification to $|\lambda|\ge 8$ for hyperbolic knots using Hecke-algebra and evaluation-at-roots-of-unity techniques.

## 9. Key References

- **[Foundational]** R. Gopakumar, C. Vafa. *On the gauge theory/geometry correspondence.* Adv. Theor. Math. Phys. **3** (1999), 1415–1443.
- **[Foundational]** H. Ooguri, C. Vafa. *Knot invariants and topological strings.* Nuclear Physics B **577** (2000), 419–438.
- **[Foundational]** J. M. F. Labastida, M. Mariño, C. Vafa. *Knots, links and branes at large $N$.* JHEP **11** (2000), 007.
- **[Foundational]** J. M. F. Labastida, M. Mariño. *Polynomial invariants for torus knots and topological strings.* Comm. Math. Phys. **217** (2001), 423–449.
- **[Foundational]** J. M. F. Labastida, M. Mariño. *A new point of view in the theory of knot and link invariants.* J. Knot Theory Ramifications **11** (2002), 173–197.
- **[SOTA]** K. Liu, P. Peng. *Proof of the Labastida–Mariño–Ooguri–Vafa conjecture.* J. Differential Geom. **85** (2010), 479–525.
- **[SOTA]** D.-E. Diaconescu, V. Shende, C. Vafa. *Large $N$ duality, Lagrangian cycles, and algebraic knots.* Comm. Math. Phys. **319** (2013), 813–863.
- **[SOTA]** D. Maulik. *Stable pairs and the HOMFLY polynomial.* Invent. Math. **204** (2016), 787–831.
- **[SOTA]** P. Kucharski, M. Reineke, M. Stošić, P. Sułkowski. *BPS states, knots and quivers.* Phys. Rev. D **96** (2017), 121902(R).
- **[SOTA]** P. Kucharski, M. Reineke, M. Stošić, P. Sułkowski. *Knots–quivers correspondence.* Adv. Theor. Math. Phys. **23** (2019), 1849–1902.
- **[SOTA]** M. Stošić, P. Wedrich. *Rational links and DT invariants of quivers.* Int. Math. Res. Not. IMRN (2021), no. 6, 4169–4210.
- **[Supporting]** A. I. Efimov. *Cohomological Hall algebra of a symmetric quiver.* Compositio Math. **148** (2012), 1133–1146.
- **[Supporting]** C.-C. M. Liu, K. Liu, J. Zhou. *A proof of a conjecture of Mariño–Vafa on Hodge integrals.* J. Differential Geom. **65** (2003), 289–340.
- **[Supporting]** P. Ramadevi, T. Sarkar. *On link invariants and topological string amplitudes.* Nuclear Physics B **600** (2001), 487–511.
- **[Orientifold]** M. Mariño. *String theory and the Kauffman polynomial.* Comm. Math. Phys. **298** (2010), 613–643.
- **[Survey / Book]** M. Mariño. *Chern–Simons Theory, Matrix Models, and Topological Strings.* Oxford University Press, 2005.

## 10. Worked Example / Concrete Special Case

**Claim.** For the unknot $U$ ($L=1$), $f_{(2)}(q,a)=0$ — an exact cancellation of the $1/2$-denominators, the simplest nontrivial instance of LMOV integrality.

Write $z=q^{1/2}-q^{-1/2}$, $u=q^{1/2}+q^{-1/2}$, $A=a^{1/2}-a^{-1/2}$, $B=a^{1/2}+a^{-1/2}$, and $[n]=\frac{q^{n/2}-q^{-n/2}}{z}$ with $a=q^N$. Quantum dimensions give the unnormalized HOMFLY-PT of $U$:

$$W_{(1)}=[N]=\frac{A}{z},\qquad W_{(2)}=\frac{[N][N+1]}{[2]},\qquad W_{(1,1)}=\frac{[N][N-1]}{[2]},$$

so that, with $[N+1]=\frac{a^{1/2}q^{1/2}-a^{-1/2}q^{-1/2}}{z}$ and $[2]=u$,

$$W_{(2)}=\frac{A\,\bigl(a^{1/2}q^{1/2}-a^{-1/2}q^{-1/2}\bigr)}{z^{2}u}.$$

**Extracting $f_{(2)}$.** Expand $F=\log Z$ to degree 2 in $x$. Using $s_{(1)}^2=s_{(2)}+s_{(1,1)}$ and $s_{(1)}(x^2)=p_2=s_{(2)}-s_{(1,1)}$, the LMOV ansatz at $d=1,2$ gives

$$f_{(2)}=W_{(2)}-\tfrac12 W_{(1)}^{2}-\tfrac12 f_{(1)}(q^{2},a^{2}),\qquad f_{(1,1)}=W_{(1,1)}-\tfrac12 W_{(1)}^{2}+\tfrac12 f_{(1)}(q^{2},a^{2}).$$

Since $f_{(1)}=W_{(1)}=A/z$, we have $f_{(1)}(q^2,a^2)=\dfrac{a-a^{-1}}{q-q^{-1}}=\dfrac{AB}{zu}$. Therefore

$$f_{(2)}=\frac{A\bigl(a^{1/2}q^{1/2}-a^{-1/2}q^{-1/2}\bigr)}{z^{2}u}-\frac{A^{2}}{2z^{2}}-\frac{AB}{2zu}.$$

Multiplying by $2z^{2}u/A$ reduces the claim to

$$2\bigl(a^{1/2}q^{1/2}-a^{-1/2}q^{-1/2}\bigr) \;\overset{?}{=}\; Au+Bz.$$

Expanding: $Au=a^{1/2}q^{1/2}+a^{1/2}q^{-1/2}-a^{-1/2}q^{1/2}-a^{-1/2}q^{-1/2}$ and $Bz=a^{1/2}q^{1/2}-a^{1/2}q^{-1/2}+a^{-1/2}q^{1/2}-a^{-1/2}q^{-1/2}$. The cross terms cancel and the sum is $2a^{1/2}q^{1/2}-2a^{-1/2}q^{-1/2}$. Hence $f_{(2)}=0$, and symmetrically $f_{(1,1)}=0$.

**Reading off the BPS numbers.** Only $\vec\mu=(1)$ survives, with

$$f_{(1)}=\frac{a^{1/2}-a^{-1/2}}{q^{1/2}-q^{-1/2}}=z^{2\cdot 0-2+1}\bigl(a^{1/2}-a^{-1/2}\bigr),$$

i.e. $N_{(1);0,\,1/2}=1$, $N_{(1);0,\,-1/2}=-1$, all other $N_{\vec\mu;g,Q}=0$. This matches the string prediction: a single primitive M2-brane disc ending on the conifold Lagrangian, genus $0$, in two charge sectors. The general conjecture asserts that the same $1/d$-denominator cancellation seen here occurs for every link and every $\vec\mu$ — for the trefoil, for instance, the degree-2 cancellation involves the full colored HOMFLY-PT $W_{(2)}$ of $T(2,3)$ and produces $f_{(2)}\ne 0$ but with integer coefficients $N_{(2);g,Q}\in\{\pm1,\pm2,\dots\}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*