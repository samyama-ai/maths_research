---
id: 02-algebra-group-theory/gelfand-kirillov-conjecture
title: "Gelfand-Kirillov Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gelfand-Kirillov Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/gelfand-kirillov-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $k$ be a field of characteristic $0$ and $\mathfrak{g}$ a finite-dimensional **algebraic** Lie algebra over $k$ (the Lie algebra of an algebraic group). Its universal enveloping algebra $U(\mathfrak{g})$ is a Noetherian domain, hence has a skew field of fractions $D(\mathfrak{g}) = \operatorname{Frac} U(\mathfrak{g})$.

**Conjecture (Gelfand–Kirillov, 1966).** There exist integers $n, m \ge 0$ with $2n + m = \dim \mathfrak{g}$ such that
$$D(\mathfrak{g}) \;\cong\; D_{n,m}(k) \;:=\; \operatorname{Frac}\big(A_n(k[y_1,\dots,y_m])\big),$$
where $A_n$ is the $n$-th Weyl algebra. Equivalently, $D(\mathfrak{g})$ is a **Weyl skew field**: generated over its centre $k(y_1,\dots,y_m)$ by $2n$ elements $p_i,q_i$ with $[p_i,q_j]=\delta_{ij}$, $[p_i,p_j]=[q_i,q_j]=0$.

A complete proof must produce such an isomorphism for every algebraic $\mathfrak{g}$; a disproof must exhibit one $\mathfrak{g}$ with $D(\mathfrak{g}) \not\cong D_{n,m}(k)$ for all admissible $(n,m)$. The conjecture is **false in general** (Alev–Ooms–Van den Bergh 1996; Premet 2010), so the live problem is: *for which classes does it hold?* The flagship open case is $\mathfrak{g} = \mathfrak{sp}_{2n}(\mathbb{C})$, $n \ge 2$.

## 2. Mathematical Foundations

**Enveloping algebra.** $U(\mathfrak{g}) = T(\mathfrak{g}) / \langle x\otimes y - y\otimes x - [x,y]\rangle$. By PBW, $\operatorname{gr} U(\mathfrak{g}) \cong S(\mathfrak{g})$, so $U(\mathfrak{g})$ is a Noetherian domain and Ore's condition holds, giving $D(\mathfrak{g})$.

**Weyl algebra.** $A_n(R) = R\langle p_1,\dots,p_n,q_1,\dots,q_n\rangle$ with $[p_i,q_j] = \delta_{ij}$. Then $D_{n,m}(k) = \operatorname{Frac} A_n(k[y_1,\dots,y_m])$ has centre $k(y_1,\dots,y_m)$ and transcendence degree $2n+m$ over $k$ (in the sense of Gelfand–Kirillov transcendence degree).

**Index.** The index of $\mathfrak{g}$ is
$$\operatorname{ind}\mathfrak{g} \;=\; \min_{\xi\in\mathfrak{g}^*} \dim \mathfrak{g}^\xi, \qquad \mathfrak{g}^\xi = \{x : \xi([x,\mathfrak{g}])=0\},$$
the dimension of a generic coadjoint stabiliser. The Kirillov form $\xi([\cdot,\cdot])$ on $\mathfrak{g}/\mathfrak{g}^\xi$ is symplectic, so $\dim\mathfrak{g} - \operatorname{ind}\mathfrak{g}$ is even.

**Forced parameters.** If the conjecture holds then $(n,m)$ is determined:
$$m = \operatorname{ind}\mathfrak{g}, \qquad n = \tfrac{1}{2}\big(\dim\mathfrak{g} - \operatorname{ind}\mathfrak{g}\big).$$
Reason: $Z(D(\mathfrak{g})) = \operatorname{Frac} Z(U(\mathfrak{g}))$ has transcendence degree $\operatorname{ind}\mathfrak{g}$ (Dixmier), and $Z(D_{n,m}) = k(y_1,\dots,y_m)$. For $\mathfrak{g}$ reductive, $\operatorname{ind}\mathfrak{g} = \operatorname{rk}\mathfrak{g}$, so the prediction is
$$D(\mathfrak{g}) \;\cong\; D_{N,\,\ell}(k), \qquad N = \tfrac{1}{2}(\dim\mathfrak{g}-\ell)=|\Delta^+|,\ \ \ell=\operatorname{rk}\mathfrak{g}.$$

**Semiclassical shadow.** $\operatorname{gr} D(\mathfrak{g})$ relates to $k(\mathfrak{g}^*)$ with its Kirillov–Kostant Poisson bracket. The commutative analogue of the conjecture asks that $k(\mathfrak{g}^*)$ be Poisson-isomorphic to a field of rational functions on $\mathbb{A}^{2n}\times\mathbb{A}^m$ with the standard symplectic bracket — a "Poisson Noether problem". Failure of rationality of $k(\mathfrak{g}^*)^{\mathfrak{g}}$ would already refute the conjecture, though known counterexamples do not proceed that way.

## 3. History & State of the Art (SOTA)

- **1966.** I. M. Gelfand and A. A. Kirillov, in *Sur les corps liés aux algèbres enveloppantes des algèbres de Lie* (Publ. Math. IHÉS 31), introduce $D(\mathfrak{g})$ as a birational invariant, prove the conjecture for **nilpotent** $\mathfrak{g}$ and for $\mathfrak{gl}_n$, $\mathfrak{sl}_n$, and pose the general statement.
- **1973–74.** Borho–Gabriel–Rentschler (LNM 357), A. Joseph (*Proof of the Gelfand–Kirillov conjecture for solvable Lie algebras*, Proc. AMS 45, 1974) and J. C. McConnell (Proc. LMS 29, 1974) settle the **solvable algebraic** case; Nghiêm Xuân Hai gives an induction-theoretic proof.
- **1980s.** Ooms, Joseph and others study $D(\mathfrak{g})$ for semidirect products; the conjecture becomes a standard test question in enveloping-algebra theory (Dixmier's book, ch. 4, 10).
- **1994–95.** Quantum analogue: Alev–Dumas compute fraction fields of quantum algebras; Joseph proves the **quantum Gelfand–Kirillov conjecture** for $U_q(\mathfrak{g})$ (Springer, 1995), showing the quantised problem is strictly easier than the classical one.
- **1996.** Alev–Ooms–Van den Bergh produce the **first counterexamples**, of dimension $9$ (Trans. AMS 348).
- **2000.** The same authors verify the conjecture for **all algebraic Lie algebras of dimension $\le 8$** over an algebraically closed field of characteristic $0$ (J. Algebra 227), pinning the counterexample threshold at exactly $9$.
- **2010.** A. Premet (Invent. Math. 181) refutes the conjecture for simple Lie algebras of types $B_n\,(n\ge 3)$, $D_n\,(n\ge 4)$, $E_6, E_7, E_8, F_4, G_2$ by reduction modulo $p$. Types $A$ (true) and $C$ (open) survive.

**SOTA summary:** true for nilpotent, solvable algebraic, $\mathfrak{gl}_n$, $\mathfrak{sl}_n$, all algebraic $\mathfrak{g}$ with $\dim\mathfrak{g}\le 8$; false for dimension $\ge 9$ in general and for all simple types except $A_n$ and $C_n$; **open for $\mathfrak{sp}_{2n}$, $n\ge 2$**.

## 4. Partial Results / Verified Cases

| Class | Verdict | Source |
|---|---|---|
| $\mathfrak{g}$ nilpotent (any $\dim$) | **True**, $D(\mathfrak{g})\cong D_{n,m}$ with $m=\operatorname{ind}\mathfrak{g}$ | Gelfand–Kirillov 1966 |
| $\mathfrak{g}$ solvable algebraic | **True** | Joseph 1974; McConnell 1974; Borho–Gabriel–Rentschler 1973 |
| $\mathfrak{gl}_n$, $\mathfrak{sl}_n$ (all $n$) | **True**; $D(\mathfrak{sl}_n)\cong D_{n(n-1)/2,\,n-1}$ | Gelfand–Kirillov 1966 |
| Algebraic $\mathfrak{g}$, $\dim \mathfrak{g}\le 8$, $k=\bar k$, $\operatorname{char}k=0$ | **True** (exhaustive classification-based check) | Alev–Ooms–Van den Bergh 2000 |
| Certain $\mathfrak{g}=\mathfrak{s}\ltimes\mathfrak{n}$ of $\dim = 9$ | **False** | Alev–Ooms–Van den Bergh 1996 |
| Simple types $B_{n\ge3}, D_{n\ge4}, E_6, E_7, E_8, F_4, G_2$ | **False** | Premet 2010 |
| $\mathfrak{sp}_{2n}$, $n\ge2$ (type $C$) | **Open** | — |
| Quantised $U_q(\mathfrak{g})$, $q$ generic | **True** (quantum analogue) | Joseph 1995; Alev–Dumas 1994 |
| Finite $W$-algebras of type $A$ | **True** (analogue for $\operatorname{Frac}$) | Futorny–Molev–Ovsienko 2010 |

## 5. Principal Obstacles

- **No characteristic-zero invariant separates skew fields.** Over $k$ of characteristic $0$, $D(\mathfrak{g})$ and $D_{n,m}(k)$ agree in every classical invariant: centre, GK-transcendence degree, global dimension, Brauer group of the centre (trivial). Standard division-algebra techniques therefore cannot distinguish them, and *all* known refutations must pass to characteristic $p$.
- **The mod-$p$ obstruction is delicate.** Premet's method reduces $\mathfrak{g}$ mod $p$, where $U(\mathfrak{g}_{\mathbb{F}_p})$ acquires a large $p$-centre $Z_p$ generated by $x^p - x^{[p]}$; $\operatorname{Frac}U$ becomes a division algebra of PI degree $p^{(\dim\mathfrak{g}-\operatorname{ind}\mathfrak{g})/2}$ over its centre. If the conjecture held, this class in the Brauer group would be split by a purely transcendental extension in a very rigid way. Premet shows, using his proof of the Kac–Weisfeiler conjecture and finite $W$-algebras attached to minimal/rigid nilpotent orbits, that this fails outside types $A$ and $C$. The argument consumes structural facts (existence of suitable nilpotent orbits with prescribed component groups) that are simply *absent* in types $A$ and $C$ — so the obstruction vanishes there without supplying a proof.
- **No construction method scales.** The positive proofs are all by explicit "Weyl coordinates": for nilpotent and solvable $\mathfrak{g}$, polarisations $\mathfrak{h}\subset\mathfrak{g}$ (Vergne) give an induction realising $U(\mathfrak{g})$ inside a differential-operator ring. For semisimple $\mathfrak{g}$, no polarisation exists; the $\mathfrak{gl}_n$ proof uses the Gelfand–Tsetlin chain $\mathfrak{gl}_1\subset\cdots\subset\mathfrak{gl}_n$, which has no analogue for $\mathfrak{sp}_{2n}$ with the required multiplicity-one and rationality properties.
- **Rationality is itself hard.** Even the semiclassical statement — that $k(\mathfrak{g}^*)^G$ is a rational field — is an unsolved Noether-type problem for many $\mathfrak{g}$, and cannot be checked directly.

## 6. The Gap

The gap is now sharply localised. Everything of dimension $\le 8$ and every solvable/nilpotent case is settled affirmatively; every simple type except $A$ and $C$ is settled negatively. What remains:

> **Is $D(\mathfrak{sp}_{2n}(\mathbb{C})) \cong D_{n^2,\,n}(\mathbb{C})$ for $n\ge 2$?** (Here $\dim\mathfrak{sp}_{2n}=2n^2+n$, $\operatorname{rk}=n$, so the forced parameters are $2n^2$ Weyl generators over a centre of transcendence degree $n$.)

Crossing it requires either (i) an explicit chain of subalgebras of $\mathfrak{sp}_{2n}$ producing commuting Weyl pairs, mimicking Gelfand–Tsetlin for $\mathfrak{gl}_n$ but overcoming the failure of multiplicity-one for the branching $\mathfrak{sp}_{2n}\downarrow\mathfrak{sp}_{2n-2}$; or (ii) a new characteristic-$p$ invariant, sensitive in type $C$ where Premet's orbit-theoretic input degenerates. A third possibility — an invariant valid in characteristic $0$, e.g. a birational Poisson invariant of $\mathfrak{sp}_{2n}^*$ — is currently without any candidate.

## 7. Current Research (as of June 2026)

- **Type $C$ attack via Galois algebras.** The Futorny–Ovsienko framework of *Galois orders* (a noncommutative Galois-descent picture for algebras with a Harish-Chandra subalgebra) is the main positive machine; it delivers type-$A$ results and $W$-algebra analogues, and groups in São Paulo, Kyiv and Sydney continue to test whether a symplectic Gelfand–Tsetlin-type subalgebra of $U(\mathfrak{sp}_{2n})$ can be made to work. Partial constructions exist for $\mathfrak{sp}_4$ *(frontier — verify)*.
- **Modular methods.** Continuations of Premet's programme (Manchester; Bielefeld) study division algebras of reduced enveloping algebras and Azumaya loci, seeking a type-$C$-sensitive Brauer-theoretic invariant.
- **Quantum and super analogues.** The quantum conjecture is largely settled (Joseph; Cauchon's deleting-derivations algorithm); current work concerns quantum cluster algebras, and the superalgebra version for $\mathfrak{gl}(m|n)$ and $\mathfrak{osp}$ (Musson's school), where the correct target is a Weyl–Clifford skew field.
- **Poisson rationality.** Ongoing computations of $\mathbb{C}(\mathfrak{g}^*)^G$ for non-reductive $\mathfrak{g}$ (Ooms, Yakimova, Panyushev) probe the semiclassical necessary condition and generate new candidate counterexamples in dimensions $9$–$12$.

## 8. Future Work

1. **Settle $\mathfrak{sp}_4$ ($\dim 10$) by direct computation.** The predicted answer is $D_{4,2}(\mathbb{C})$. This is the smallest untouched simple case and is within reach of computer algebra (Gröbner bases in Ore algebras).
2. **Build a symplectic analogue of the Gelfand–Tsetlin chain** with rational, multiplicity-controlled branching; this is the strategy most often named by Futorny and collaborators.
3. **Find a characteristic-$0$ birational invariant** of $D(\mathfrak{g})$ — e.g. from cyclic homology or from the Poisson geometry of $\mathfrak{g}^*$ — that reproduces Premet's negative answers without reduction mod $p$; this would likely also decide type $C$.
4. **Classify the counterexample locus in dimension $9$–$12$**, extending Alev–Ooms–Van den Bergh's dimension-$\le 8$ census, to see whether failure is generic or exceptional.
5. **Weaken the conjecture:** ask only that $D(\mathfrak{g})$ and $D_{n,m}$ become isomorphic after a finite extension of centres, or that they have the same "Weyl degree" — versions that may be true universally.

## 9. Key References

- **[Foundational]** I. M. Gelfand, A. A. Kirillov. *Sur les corps liés aux algèbres enveloppantes des algèbres de Lie.* Publications Mathématiques de l'IHÉS, no. 31, 5–19, 1966.
- **[Foundational]** J. Dixmier. *Enveloping Algebras.* North-Holland, 1977; reprinted AMS Graduate Studies in Mathematics 11, 1996.
- **[Foundational]** W. Borho, P. Gabriel, R. Rentschler. *Primideale in Einhüllenden auflösbarer Lie-Algebren.* Lecture Notes in Mathematics 357, Springer, 1973.
- **[Foundational]** A. Joseph. *Proof of the Gelfand–Kirillov conjecture for solvable Lie algebras.* Proceedings of the American Mathematical Society 45, 1–10, 1974.
- **[Foundational]** J. C. McConnell. *Representations of solvable Lie algebras and the Gelfand–Kirillov conjecture.* Proceedings of the London Mathematical Society (3) 29, 453–484, 1974.
- **[Counterexamples]** J. Alev, A. Ooms, M. Van den Bergh. *A class of counterexamples to the Gel'fand–Kirillov conjecture.* Transactions of the American Mathematical Society 348, 1709–1716, 1996.
- **[Verified cases]** J. Alev, A. Ooms, M. Van den Bergh. *The Gelfand–Kirillov conjecture for Lie algebras of dimension at most eight.* Journal of Algebra 227, 549–581, 2000.
- **[SOTA]** A. Premet. *Modular Lie algebras and the Gelfand–Kirillov conjecture.* Inventiones Mathematicae 181, 395–420, 2010.
- **[SOTA]** V. Futorny, A. Molev, S. Ovsienko. *The Gelfand–Kirillov conjecture and Gelfand–Tsetlin modules for finite W-algebras.* Advances in Mathematics 223, 773–796, 2010.
- **[Quantum]** A. Joseph. *Quantum Groups and Their Primitive Ideals.* Ergebnisse der Mathematik 29, Springer, 1995.
- **[Quantum]** J. Alev, F. Dumas. *Sur le corps des fractions de certaines algèbres quantiques.* Journal of Algebra 170, 229–265, 1994.
- **[Survey / background]** J. C. McConnell, J. C. Robson. *Noncommutative Noetherian Rings.* Revised edition, AMS Graduate Studies in Mathematics 30, 2001.

## 10. Worked Example / Concrete Special Case

**(a) Heisenberg algebra $\mathfrak{h}_3$.** Basis $x,y,z$ with $[x,y]=z$, $z$ central. Then $\dim\mathfrak{h}_3=3$; a generic $\xi$ has $\dim\mathfrak{h}_3^\xi=1$, so $\operatorname{ind}=1$ and the prediction is $D(\mathfrak{h}_3)\cong D_{1,1}(k)$.

In $D(\mathfrak{h}_3)$ set $p := z^{-1}x$, $q := y$. Since $z$ is central and invertible in the fraction field,
$$[p,q] = z^{-1}[x,y] = z^{-1}z = 1 .$$
Also $x = zp$, $y=q$, so $k(z)\langle p,q\rangle$ contains all of $\mathfrak{h}_3$ and hence generates $D(\mathfrak{h}_3)$; conversely $p,q,z$ lie in $D(\mathfrak{h}_3)$. So $D(\mathfrak{h}_3)=\operatorname{Frac}A_1(k[z]) = D_{1,1}(k)$. ✔

**(b) $\mathfrak{sl}_2$, the smallest simple case.** Basis $e,f,h$: $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$. Here $\dim=3$, $\operatorname{rk}=1$, so the prediction is $D(\mathfrak{sl}_2)\cong D_{1,1}(k)$.

Set $v := \tfrac12\,h e^{-1}$ in $D(\mathfrak{sl}_2)$. Since $e^{-1}$ commutes with $e$,
$$[v,e] = \tfrac12[h,e]\,e^{-1} = \tfrac12(2e)e^{-1} = 1 .$$
So $k\langle e,v\rangle \cong A_1(k)$. Now use the Casimir
$$\Omega = ef+fe+\tfrac12 h^2 = 2fe + h + \tfrac12 h^2 \quad(\text{using } ef=fe+h),$$
which is central and generates $Z(U(\mathfrak{sl}_2))$. Solving,
$$f = \tfrac12\big(\Omega - h - \tfrac12 h^2\big)e^{-1}, \qquad h = 2ve .$$
Hence $f \in k(\Omega)\langle e^{\pm1}, v\rangle$, so $D(\mathfrak{sl}_2) = \operatorname{Frac}A_1(k[\Omega]) = D_{1,1}(k)$. ✔

**(c) Where the pattern breaks.** For $\mathfrak{g}$ of type $G_2$ ($\dim 14$, $\operatorname{rk}2$) the same bookkeeping predicts $D(\mathfrak{g})\cong D_{6,2}(k)$ — the numerology is unobstructed. Yet Premet (2010) shows no isomorphism exists: reducing mod $p\gg0$, $\operatorname{Frac}U(\mathfrak{g}_{\mathbb{F}_p})$ is a division algebra of degree $p^{6}$ over its centre whose Brauer class is not the class of a Weyl field over any rational subfield. The example shows the conjecture cannot be decided by counting: the invariants $(n,m)$ match exactly, and only a finer, characteristic-$p$ invariant sees the failure. The absence of such an invariant in type $C$ is precisely why $\mathfrak{sp}_{2n}$ remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*