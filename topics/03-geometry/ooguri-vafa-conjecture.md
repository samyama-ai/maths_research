---
id: 03-geometry/ooguri-vafa-conjecture
title: "Ooguri-Vafa Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ooguri-Vafa Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/ooguri-vafa-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Ooguri and Vafa (1999) conjectured that the colored HOMFLY-PT invariants of a link $\mathcal{L}\subset S^3$ are the open topological-string partition function of a Lagrangian brane in the resolved conifold. The conjecture has two coupled halves.

**(A) Geometric (large $N$ duality with branes).** Let $\mathcal{L}$ have $L$ components and let $C_{\mathcal{L}}\subset T^*S^3$ be its conormal Lagrangian. Under the conifold transition $T^*S^3 \rightsquigarrow X = \mathcal{O}(-1)^{\oplus 2}\to\mathbb{P}^1$, $C_{\mathcal{L}}$ deforms to a Lagrangian $L_{\mathcal{L}}\subset X$, and the $U(N)$ Chern–Simons generating function of $\mathcal{L}$ at level $k$ equals the all-genus open Gromov–Witten partition function of $(X,L_{\mathcal{L}})$ under
$$q=e^{g_s},\qquad \lambda=q^{N}=e^{Ng_s},\qquad g_s=\frac{2\pi i}{k+N}.$$

**(B) Integrality (BPS / LMOV form).** The reformulated free energies $\hat f_{\vec\mu}(q,\lambda)$ of the colored HOMFLY-PT invariants satisfy
$$\hat f_{\vec\mu}(q,\lambda)=\frac{1}{q-q^{-1}}\sum_{g\ge 0}\ \sum_{Q\in\tfrac12\mathbb{Z}} N_{\vec\mu,g,Q}\,(q-q^{-1})^{2g}\,\lambda^{Q},$$
with **all $N_{\vec\mu,g,Q}\in\mathbb{Z}$** and only finitely many nonzero. The $N_{\vec\mu,g,Q}$ are to be the (signed) degeneracies of M2-branes ending on $L_{\mathcal{L}}$, of genus $g$, boundary winding $\vec\mu$ and D2-charge $Q$.

A complete proof must (i) construct $L_{\mathcal{L}}$ and a well-defined all-genus open GW theory for it, and (ii) identify its invariants with the Chern–Simons side, thereby giving the integers $N_{\vec\mu,g,Q}$ an enumerative meaning. A disproof would exhibit a link whose $\hat f_{\vec\mu}$ has a non-integral coefficient, a pole of order $>1$ at $q=1$, or infinitely many nonzero $N$.

## 2. Mathematical Foundations

**Chern–Simons side.** For $\mathcal{L}=\bigsqcup_{\alpha=1}^{L}\mathcal{K}_\alpha$ and partitions $\vec\lambda=(\lambda^1,\dots,\lambda^L)$, let $W_{\vec\lambda}(\mathcal{L};q,\lambda)$ be the quantum $\mathfrak{gl}_N$ invariant with component $\alpha$ colored by the irreducible representation $\lambda^\alpha$ (unnormalized colored HOMFLY-PT). Form
$$Z(\mathcal{L};\vec x)=\sum_{\vec\lambda}W_{\vec\lambda}(\mathcal{L})\prod_{\alpha=1}^{L}s_{\lambda^\alpha}(x^\alpha),\qquad F=\log Z=\sum_{\vec\mu\neq\vec 0}f_{\vec\mu}(q,\lambda)\prod_\alpha p_{\mu^\alpha}(x^\alpha),$$
where $s_\lambda$ are Schur and $p_\mu$ power-sum functions, $x^\alpha$ the eigenvalues of the $\alpha$-th brane holonomy. The **reformulated free energy** is the Möbius transform
$$\hat f_{\vec\mu}(q,\lambda)=\sum_{d\,\mid\,\vec\mu}\frac{\mu(d)}{d}\,f_{\vec\mu/d}\!\left(q^{d},\lambda^{d}\right),$$
$\mu(\cdot)$ the number-theoretic Möbius function, the sum over $d$ dividing every part of every $\mu^\alpha$.

**Geometric side.** $X=\mathcal{O}_{\mathbb{P}^1}(-1)\oplus\mathcal{O}_{\mathbb{P}^1}(-1)$ is the resolved conifold, Kähler parameter $t$ with $\lambda=e^{-t}$. For a Lagrangian $L\subset X$ with $H_1(L)\cong\mathbb{Z}^L$, open GW invariants $K_{g,\vec\mu,\beta}$ count stable maps from bordered genus-$g$ Riemann surfaces with $\partial$-classes $\vec\mu\in H_1(L)$ and relative class $\beta$. The conjectural equality is
$$\sum_{g,\vec\mu,\beta}K_{g,\vec\mu,\beta}\,g_s^{2g-2+\ell(\vec\mu)}e^{-\beta\cdot t}\prod p_{\mu^\alpha}(x^\alpha)\;=\;F(\mathcal{L};q=e^{g_s},\lambda=e^{-t},\vec x).$$

**Multiple-cover kernel.** The integrality ansatz is equivalent to resumming BPS states with the Ooguri–Vafa multiple-cover factor: a single primitive disc of area $t$ contributes
$$\sum_{d\ge1}\frac{1}{d}\,\frac{e^{-dt}}{q^{d}-q^{-d}}\,p_d(x),$$
whose genus-$0$ part is $\sum_d d^{-2}e^{-dt}p_d(x)/(2g_s)$ — the $1/d^{2}$ disc multiple-cover rule.

**Input theorems relied on.** Witten's identification of Chern–Simons theory with open strings on $T^*S^3$ (1995); the Gopakumar–Vafa closed-string integrality for $X$; the conifold geometric transition; the Chern–Simons/skein presentation of $W_{\vec\lambda}$ (HOMFLY-PT skein theory of the annulus).

## 3. History & State of the Art (SOTA)

- **1995.** Witten: Chern–Simons theory on $S^3$ = open A-model on $T^*S^3$ with $N$ branes on the zero section.
- **1998.** Gopakumar–Vafa: closed-string large $N$ duality $T^*S^3\rightsquigarrow X$; free energy of $SU(N)$ CS on $S^3$ = closed topological string on the resolved conifold.
- **1999–2000.** Ooguri–Vafa, *Knot invariants and topological strings* (Nucl. Phys. B 577, 419–438; hep-th/9912123), add the conormal brane and state (A)+(B) for knots.
- **2000–2002.** Labastida–Mariño and Labastida–Mariño–Vafa give the precise generating-function algebra for links, fixing $\hat f_{\vec\mu}$ and the sign/framing conventions — the statement now usually called the **LMOV conjecture**.
- **2001.** Katz–Liu define open GW invariants for the conormal of the unknot by localization with Lagrangian boundary condition and prove the $1/d^2$ disc multiple-cover formula.
- **2003.** Liu–Liu–Zhou prove the Mariño–Vafa Hodge-integral formula (framed unknot), the first full-strength check of (A).
- **2010.** Liu–Peng prove the LMOV integrality/pole statement (B) for all links, by symmetry-function and cabling arguments — a purely combinatorial proof, without producing the geometry.
- **2012–2016.** Diaconescu–Shende–Vafa, Oblomkov–Shende and Maulik establish the algebraic-knot case of the geometric side via stable pairs.
- **2019–.** Ekholm–Shende develop skein-valued curve counting, making $L_{\mathcal{L}}$-side counts well-defined as HOMFLY-skein classes.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| Unknot, all windings $d\ge1$, genus 0 | Disc multiple-cover contribution $=1/d^{2}$; $N_{(1),0,\pm1}=\pm1$, all other $N=0$ | Katz–Liu (2001) |
| Framed unknot, all genera, all framings $\tau\in\mathbb{Z}$ | Mariño–Vafa formula for triple Hodge integrals proved | Liu–Liu–Zhou (2003); Okounkov–Pandharipande |
| **All links, statement (B)** | $N_{\vec\mu,g,Q}\in\mathbb{Z}$; only a simple pole at $q=\pm1$; finiteness in $g$ | Liu–Peng, *J. Diff. Geom.* 85 (2010) |
| Torus links $T(m,n)$ | Explicit closed-form $N_{\vec\mu,g,Q}$ from skein-theoretic colored HOMFLY | Zhu (2013) |
| Algebraic knots (links of plane-curve singularities) | HOMFLY = stable-pair/Hilbert-scheme count; geometric side (A) established | Oblomkov–Shende (2012), Diaconescu–Shende–Vafa (2013), Maulik (2016) |
| Unknot conormal, all colors | Skein-valued count of holomorphic curves reproduces colored HOMFLY-PT | Ekholm–Shende (2019+) |
| Knot-contact-homology augmentation variety | $Q$-deformed $A$-polynomial matches the recursion of colored HOMFLY-PT for $4_1$, $5_2$, twist knots | Aganagic–Ekholm–Ng–Vafa (2014); Ekholm–Ng (2020) |
| Numerical checks | $N_{\vec\mu,g,Q}$ integral for all knots up to 10 crossings, symmetric colors $\lambda=(n)$, $n\le 5$ | LMOV-era and later tabulations |

## 5. Principal Obstacles

- **Open GW theory is not intrinsically defined.** Moduli of stable maps with Lagrangian boundary have real codimension-one boundary strata; there is no canonical virtual fundamental class without extra input (torus action, as in Katz–Liu; or skein-valued coefficients, as in Ekholm–Shende). For a general $L_{\mathcal{L}}$ with no $S^1$-symmetry, localization is unavailable, so the geometric side of (A) has no definition to compare against.
- **Boundary bubbling / framing ambiguity.** Disc bubbling makes the count depend on the choice of framing and of the deformation class of $L_{\mathcal{L}}$; the Chern–Simons side has a matching $\mathbb{Z}$ ambiguity, but no proof matches the two ambiguities canonically for general knots.
- **The transition is not a smooth family.** The conormal $C_{\mathcal{L}}$ must be pushed through the singular conifold; the resulting $L_{\mathcal{L}}$ is only constructed explicitly for the unknot, algebraic knots (via $\mathbb{C}^*$-invariant curves) and a handful of examples.
- **Integrality proof is blind to geometry.** Liu–Peng's argument runs through infinite-dimensional symmetries of symmetric functions and a cabling induction; it produces integers but no cycles, so it cannot yield positivity, finiteness in $Q$ with geometric bounds, or the refined (Gukov–Schwarz–Vafa) homological statement.
- **No positivity.** Unlike Gopakumar–Vafa closed invariants in low genus, the $N_{\vec\mu,g,Q}$ have signs; there is no known cohomological model whose Euler characteristic they compute for a general knot.

## 6. The Gap

Statement (B) is a theorem (Liu–Peng). Statement (A) is a theorem only for the unknot, its framings, and algebraic knots. The gap is exactly:

> Produce, for an arbitrary link $\mathcal{L}$, the Lagrangian $L_{\mathcal{L}}\subset X$ together with a deformation-invariant all-genus open GW count $K_{g,\vec\mu,\beta}(X,L_{\mathcal{L}})\in\mathbb{Q}$, and prove that the resulting free energy equals $F(\mathcal{L})$ — hence that Liu–Peng's integers count curves.

Concretely: bridge from "the numbers are integers" to "the integers are dimensions of BPS Hilbert spaces / counts of embedded curves". The skein-valued theory of Ekholm–Shende is the leading candidate to close it, but transporting a skein-valued count back to a numerical BPS degeneracy with the OV multiple-cover kernel is not yet done for a general knot.

## 7. Current Research (as of June 2026)

- **Skein-valued curve counting** (Ekholm, Shende, and collaborators; Uppsala/Berkeley–Harvard orbit): counts of holomorphic curves with boundary valued in the HOMFLY skein module of $L$, avoiding wall-crossing by absorbing bubbling into skein relations. Extensions to toric branes, the resolved conifold with several branes, and to the recursion/quantum-$A$-polynomial picture. *(frontier — verify)* recent work claims a skein-valued proof of the geometric half for conormals of general knots via SFT stretching.
- **Stable pairs and Hilbert schemes of singular curves** (Diaconescu, Shende, Maulik, Oblomkov, Rasmussen): pushing the algebraic-knot proof toward all knots by degenerating to singular Lagrangian cycles.
- **Refined/categorified OV** (Gukov, Nawata, Aganagic): $N_{\vec\mu,g,Q}$ as Poincaré characteristics of HOMFLY-PT homology; the refined LMOV integrality with a second grading is checked but unproven in general. *(frontier — verify)*
- **Knot contact homology / augmentation varieties** (Ng, Ekholm, Aganagic, Vafa): $Q$-deformed $A$-polynomials as the classical limit of the recursion satisfied by $\{W_{(n)}\}_{n\ge0}$.
- **Quiver correspondence** (Kucharski, Reineke, Stošić, Sułkowski): knots-quivers correspondence expressing $\hat f_{\vec\mu}$ via motivic Donaldson–Thomas invariants of a symmetric quiver, giving an independent route to integrality and, for many knots, to positivity of the BPS counts.

## 8. Future Work

- Define open GW invariants for $(X,L_{\mathcal{L}})$ without torus symmetry — via bounding cochains / obstruction theory (Fukaya–Oh–Ohta–Ono) or via skein coefficients — and prove deformation invariance.
- Prove that the knots-quivers correspondence holds for all knots; this would upgrade integrality to *positivity* after a change of variables, which is the strongest available structural prediction.
- Establish finiteness bounds: show $N_{\vec\mu,g,Q}=0$ for $g>g_{\max}(\vec\mu)$ with $g_{\max}$ given by a Seifert-genus or Euler-characteristic bound, matching the geometric expectation.
- Extend the DSV/Maulik stable-pair proof from algebraic knots to all knots by resolving the Lagrangian cycle in families.
- Categorify: build a knot homology whose graded Euler characteristic is $\sum N_{\vec\mu,g,Q}$, realizing the Gukov–Schwarz–Vafa proposal.

## 9. Key References

- **[Foundational]** H. Ooguri, C. Vafa. *Knot invariants and topological strings.* Nuclear Physics B **577** (2000), 419–438. arXiv:hep-th/9912123.
- **[Foundational]** R. Gopakumar, C. Vafa. *On the gauge theory/geometry correspondence.* Advances in Theoretical and Mathematical Physics **3** (1999), 1415–1443.
- **[Foundational]** J. M. F. Labastida, M. Mariño, C. Vafa. *Knots, links and branes at large $N$.* Journal of High Energy Physics **11** (2000), 007.
- **[Foundational]** J. M. F. Labastida, M. Mariño. *A new point of view in the theory of knot and link invariants.* Journal of Knot Theory and Its Ramifications **11** (2002), 173–197.
- **[Partial result]** S. Katz, C.-C. M. Liu. *Enumerative geometry of stable maps with Lagrangian boundary conditions and multiple covers of the disc.* Advances in Theoretical and Mathematical Physics **5** (2001), 1–49. arXiv:math/0103074.
- **[Partial result]** C.-C. M. Liu, K. Liu, J. Zhou. *A proof of a conjecture of Mariño–Vafa on Hodge integrals.* Journal of Differential Geometry **65** (2003), 289–340.
- **[SOTA]** K. Liu, P. Peng. *Proof of the Labastida–Mariño–Ooguri–Vafa conjecture.* Journal of Differential Geometry **85** (2010), 479–525. arXiv:0704.1526.
- **[SOTA]** D.-E. Diaconescu, V. Shende, C. Vafa. *Large $N$ duality, Lagrangian cycles, and algebraic knots.* Communications in Mathematical Physics **319** (2013), 813–863. arXiv:1111.6533.
- **[SOTA]** D. Maulik. *Stable pairs and the HOMFLY polynomial.* Inventiones Mathematicae **204** (2016), 787–831. arXiv:1210.6323.
- **[SOTA]** A. Oblomkov, V. Shende. *The Hilbert scheme of a plane curve singularity and the HOMFLY polynomial of its link.* Duke Mathematical Journal **161** (2012), 1277–1303.
- **[SOTA]** T. Ekholm, V. Shende. *Skeins on branes.* arXiv:1901.08027 (2019).
- **[SOTA]** M. Aganagic, T. Ekholm, L. Ng, C. Vafa. *Topological strings, D-model, and knot contact homology.* Advances in Theoretical and Mathematical Physics **18** (2014), 827–956.
- **[Survey]** M. Mariño. *Chern–Simons Theory, Matrix Models, and Topological Strings.* International Series of Monographs on Physics 131, Oxford University Press, 2005.
- **[Survey]** P. Kucharski, M. Reineke, M. Stošić, P. Sułkowski. *BPS states, knots and quivers.* Physical Review D **96** (2017), 121902.

## 10. Worked Example / Concrete Special Case

**The unknot.** Use variables $a=\lambda$, $q$, with the unnormalized colored HOMFLY-PT of the unknot given by the quantum dimension
$$W_\lambda=\prod_{(i,j)\in\lambda}\frac{a\,q^{\,j-i}-a^{-1}q^{\,i-j}}{q^{h(i,j)}-q^{-h(i,j)}},\qquad h(i,j)=\text{hook length}.$$
For the fundamental representation $W_{\square}=\dfrac{a-a^{-1}}{q-q^{-1}}$, and for the two two-box colors
$$W_{(2)}=\frac{(a-a^{-1})(aq-a^{-1}q^{-1})}{(q^{2}-q^{-2})(q-q^{-1})},\qquad
W_{(1,1)}=\frac{(a-a^{-1})(aq^{-1}-a^{-1}q)}{(q^{2}-q^{-2})(q-q^{-1})}.$$

Since $W_\lambda=s_\lambda(y)$ for the specialization with power sums $p_d(y)=\dfrac{a^{d}-a^{-d}}{q^{d}-q^{-d}}$, the Cauchy identity $\sum_\lambda s_\lambda(y)s_\lambda(x)=\exp\big(\sum_{d\ge1}\tfrac1d p_d(x)p_d(y)\big)$ gives the **exact** free energy
$$F=\sum_{d\ge1}\frac{1}{d}\,\frac{a^{d}-a^{-d}}{q^{d}-q^{-d}}\;p_d(x)\quad\Longrightarrow\quad f_{(d)}=\frac1d\,\frac{a^{d}-a^{-d}}{q^{d}-q^{-d}},\ \ f_\mu=0 \text{ for } \ell(\mu)\ge2 .$$

Now apply the Möbius transform of Section 2.

*Winding 1:* $\ \hat f_{(1)}=f_{(1)}=\dfrac{a-a^{-1}}{q-q^{-1}}$. Hence $(q-q^{-1})\hat f_{(1)}=a-a^{-1}$, so
$$N_{(1),0,+1}=1,\qquad N_{(1),0,-1}=-1,\qquad N_{(1),g,Q}=0 \text{ otherwise.}$$
One BPS state (with its conjugate), genus $0$: exactly the single primitive holomorphic disc that $L_{\text{unknot}}$ bounds in $X$.

*Winding 2:* $\ \hat f_{(2)}=f_{(2)}+\dfrac{\mu(2)}{2}f_{(1)}(q^{2},a^{2})=\dfrac12\dfrac{a^{2}-a^{-2}}{q^{2}-q^{-2}}-\dfrac12\dfrac{a^{2}-a^{-2}}{q^{2}-q^{-2}}=0.$

The same cancellation holds for every $d\ge2$, so the unknot has **no** BPS states beyond winding 1 — all higher-winding data is multiple covers of the one disc. Reading off the genus-$0$ part of the $d$-th term of $F$ with $q=e^{g_s/2}$, $a^{2}=e^{-t}$:
$$\frac1d\,\frac{e^{-dt/2}\text{-terms}}{q^{d}-q^{-d}}\;\sim\;\frac{1}{d^{2}g_s}\,e^{-dt/2},$$
the $1/d^{2}$ disc multiple-cover formula proved by Katz–Liu. This is the complete verification of both (A) and (B) in the simplest case; for the trefoil, the analogous computation already requires $W_{(2)},W_{(1,1)}$ at framing $\pm1$ and yields $N_{(1),0,Q}\in\{1,-1,-1,1\}$ at $Q=2,4$ and their conjugates — integral, as the conjecture demands, but with no known Lagrangian producing them.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*