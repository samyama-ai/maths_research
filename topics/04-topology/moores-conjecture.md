---
id: 04-topology/moores-conjecture
title: "Moore's Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Moore's Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/moores-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a simply connected finite CW complex and $p$ a prime. Say $X$ **has a homotopy exponent at $p$** if there is an integer $e \ge 0$ such that $p^{e}$ annihilates the $p$-torsion of $\pi_*(X)$:
$$p^{e}\cdot \big({}_{p\text{-torsion}}\,\pi_n(X)\big)=0 \quad\text{for all } n .$$
Say $X$ is **rationally elliptic** if $\dim_{\mathbb Q}\pi_*(X)\otimes\mathbb Q<\infty$, and **rationally hyperbolic** otherwise.

**Moore's Conjecture (J. C. Moore, c. 1979).** The following are equivalent:

1. $X$ has a homotopy exponent at some prime $p$;
2. $X$ has a homotopy exponent at every prime $p$;
3. $X$ is rationally elliptic.

Equivalently in contrapositive form: $X$ is rationally hyperbolic $\iff$ for every prime $p$ the orders of $p$-torsion elements in $\pi_*(X)$ are unbounded.

A complete proof must supply both implications for all simply connected finite complexes. A disproof requires one explicit finite complex that is elliptic yet has $p$-torsion of unbounded order at some prime, or hyperbolic yet has bounded $p$-torsion. The conjecture is remarkable because it asserts that a *rational* (torsion-free, characteristic-zero) invariant controls *torsion* behaviour at every prime.

Note: this is the homotopy-exponent conjecture, distinct from the **normal Moore space conjecture** of set-theoretic topology (settled as independent of ZFC).

## 2. Mathematical Foundations

**Homotopy Lie algebra.** For $X$ simply connected, set
$$L_X \;=\; \pi_*(\Omega X)\otimes\mathbb Q,$$
a graded Lie algebra under the Samelson bracket, with $L_X^{\,n}\cong \pi_{n+1}(X)\otimes\mathbb Q$. By the Milnor–Moore theorem,
$$H_*(\Omega X;\mathbb Q)\;\cong\; U(L_X),$$
the universal enveloping algebra. Ellipticity says $\dim L_X<\infty$.

**The dichotomy theorem (Félix–Halperin).** For $X$ a simply connected finite complex, exactly one of:
- $\dim L_X<\infty$ (elliptic), in which case $\dim L_X\le \dim X$, $L_X^{\,n}=0$ for $n\ge 2\dim X$, and the Euler characteristic satisfies $\chi(X)\ge 0$;
- $\dim L_X=\infty$ (hyperbolic), in which case the ranks grow exponentially: there is $C>1$ with
$$\sum_{i=n+1}^{n+\dim X}\dim L_X^{\,i}\;\ge\; C^{\,n}\quad\text{for all large }n .$$
Refined asymptotics (Félix–Halperin–Thomas, 2009): $\displaystyle\log\Big(\sum_{i\le n}\dim L_X^{\,i}\Big)\sim \alpha n$ for some $\alpha>0$.

**Exponents.** Write $\exp_p(X)=\min\{e: p^e \text{ annihilates } p\text{-torsion of }\pi_*(X)\}$ when finite. Basic facts:
- $\exp_p(-)$ is inherited by retracts: if $Y$ is a homotopy retract of $X$ then $\exp_p(Y)\le\exp_p(X)$.
- For a fibration $F\to E\to B$ with all three spaces having exponents, $\exp_p(E)\le \exp_p(F)+\exp_p(B)$ (long exact sequence).
- Serre: for $X$ simply connected finite with $H^*(X;\mathbb Q)\ne H^*(\mathrm{pt})$, $\pi_*(X)$ contains $p$-torsion in infinitely many degrees.

**Known sphere exponents.**
$$\text{(Cohen–Moore–Neisendorfer, } p \text{ odd)}\qquad p^{\,n}\cdot{}_{p}\pi_*(S^{2n+1})=0,$$
and this is sharp by Gray's construction of elements of order exactly $p^{n}$; hence $\exp_p(S^{2n+1})=n$ for odd $p$. At $p=2$, James gives $2^{2n}$ for $S^{2n+1}$; $\exp_2(S^3)=2$ (order-$4$ elements exist since $\pi_6(S^3)=\mathbb Z/12$). Even spheres reduce via the fibration $S^{2n-1}\to S^{2n}\to \Omega S^{4n-1}$ (localized at odd $p$), giving $\exp_p(S^{2n})\le \exp_p(S^{2n-1})+\exp_p(S^{4n-1})$.

## 3. History & State of the Art (SOTA)

- **1953.** Serre proves $\pi_*(S^n)$ has $p$-torsion in infinitely many degrees — the setting in which "bounded order" becomes a meaningful question.
- **1957.** James: $2^{2n}$ annihilates the $2$-torsion of $\pi_*(S^{2n+1})$. **1965–66.** Toda: $p^{2n}$ at odd primes.
- **1969.** Gray constructs $p$-torsion of order $p^{n}$ in $\pi_*(S^{2n+1})$, fixing the lower bound.
- **1978.** Selick: $p$ annihilates the $p$-torsion of $\pi_*(S^3)$ for $p$ odd — the first sharp exponent, and the direct stimulus for Moore's question.
- **1979.** Cohen–Moore–Neisendorfer prove $\exp_p(S^{2n+1})=n$ for $p$ odd, via the loop space decomposition of $\Omega^2 S^{2n+1}$ and mod-$p^r$ Moore space technology. Moore formulates the conjecture in this period; it circulated informally and appears in print in Selick's survey (LNM 1318, 1988) and in Félix–Halperin–Thomas, *Rational Homotopy Theory* (2001).
- **1986.** McGibbon–Wilkerson: an elliptic finite complex has an exponent at all but finitely many primes — the "easy" direction of $(3)\Rightarrow(2)$ modulo finitely many primes.
- **2001–2009.** Rational side hardens: dichotomy theorem and exponential-growth asymptotics.
- **2020–2024.** Huang–Wu, Boyde, Theriault and collaborators produce **$p$-hyperbolicity** theorems (exponential growth of the number of $\mathbb Z/p^k$ summands) for large families of suspensions, Moore spaces, and Poincaré duality complexes.

## 4. Partial Results / Verified Cases

**Elliptic $\Rightarrow$ exponent.**
- Odd-dimensional spheres $S^{2n+1}$: $\exp_p=n$ ($p$ odd, CMN + Gray); even spheres bounded by the fibration argument.
- All simply connected finite complexes that are elliptic: exponent exists at every prime $p>\dim X$ (McGibbon–Wilkerson, 1986); at $p$ large the $p$-localized loop space splits as a product of spheres and sphere-like factors.
- Compact simple Lie groups: odd-primary exponents computed or bounded in essentially all cases by Davis–Theriault (2008); e.g. $SU(n)$, $Sp(n)$, $G_2$ at $p$ odd. Finite $H$-spaces are elliptic (rationally products of odd spheres) and fall under this.
- Mod-$p^r$ Moore spaces $P^{n}(p^r)=S^{n-1}\cup_{p^r}e^{n}$: $\exp_p=r+1$ for $p\ge 5$ (Cohen–Moore–Neisendorfer, 1979); $p=2$, $r\ge 6$ handled by Theriault (2008). These are *hyperbolic* in the sense of having infinite-dimensional $\pi_*\otimes\mathbb Q$ but they are not simply connected finite complexes with the required $\mathbb Q$-behaviour — they are the tool, and they are the boundary case that shows how delicate the statement is (they have a $p$-exponent at $p$ only, not at other primes, consistent with the conjecture applying to a single fixed $p$ only through condition (1)–(2) for *finite simply connected* $X$; $P^n(p^r)$ is $\mathbb Q$-acyclic).

**Hyperbolic $\Rightarrow$ no exponent.**
- Wedges of at least two simply connected spheres, and more generally any $X$ retracting off such a wedge: unbounded orders via Hilton's theorem (Section 10).
- Suspensions $\Sigma Y$ with $H_*(Y;\mathbb Z/p)$ of rank $\ge 2$: $p$-hyperbolic (Huang–Wu, 2020), i.e. $\sum_{i\le n}\dim_{\mathbb F_p}\big(\pi_i(X)\otimes\mathbb Z/p\big)$ grows exponentially.
- Boyde (2022): $p$-hyperbolicity from $K$-theoretic/James-construction input for large classes including many Poincaré duality complexes and $(p-1)$-cell complexes.
- Products/connected sums: $\exp_p$ additivity gives the conjecture for $X\times Y$ once known for $X,Y$.

## 5. Principal Obstacles

- **No mechanism converts rational infinitude into torsion of unbounded order.** $p$-hyperbolicity theorems produce *many* torsion summands but say nothing about their *orders*. A space could conceivably have $\dim_{\mathbb F_p}\pi_n\otimes\mathbb Z/p$ growing like $C^n$ while every element has order $\le p^5$. Closing that gap is the core difficulty.
- **Exponent proofs are construction-specific.** All sharp upper bounds (CMN, Selick, Theriault) come from explicit loop space decompositions, e.g. the odd-primary splitting
$$\Omega^2 S^{2n+1}\langle 3\rangle \;\simeq\; \text{(product involving } S^{2n-1}\text{ and Anick's space } T^{2n+1}(p)\text{)},$$
and from constructing a power map $\pi\colon \Omega^{2}S^{2n+1}\to S^{2n-1}$ with controlled composite. Such decompositions are known only for spheres, Moore spaces, and a handful of Lie groups. There is no functorial machine producing them from ellipticity alone.
- **Unstable $v_1$-periodicity is only an approximation.** Localized/telescopic methods (Mahowald, Davis) compute $v_1$-periodic homotopy $v_1^{-1}\pi_*(X)$, which detects exponents *from below* well but never bounds full torsion above.
- **Rational models are torsion-blind.** Sullivan minimal models and the homotopy Lie algebra $L_X$ compute $\pi_*\otimes\mathbb Q$ exactly and give no information at any prime; conversely $\mathbb F_p$-homology of $\Omega X$ (an enveloping-algebra-like object over $\mathbb F_p$ by Halperin–Levin theory) loses the extension data recording element orders.
- **Finiteness of the complex is essential but hard to exploit.** The conjecture is false without finiteness ($\mathbb{CP}^\infty=K(\mathbb Z,2)$ has $\pi_*$ trivial above degree 2); yet no current technique uses "finitely many cells" quantitatively beyond McGibbon–Wilkerson's large-prime regime.

## 6. The Gap

Proven: (a) elliptic $\Rightarrow$ exponent at $p>\dim X$; (b) hyperbolic $\Rightarrow$ exponentially many $\mathbb Z/p$ summands, for broad families of suspensions and Poincaré complexes.

Missing, precisely:

1. **Small primes in the elliptic case.** For elliptic $X$ and a prime $p\le \dim X$, no general bound on $\exp_p(X)$ is known. The $p$-local loop space need not split as a product, and torsion in $H_*(\Omega X;\mathbb Z)$ can be unbounded a priori.
2. **From cardinality to order in the hyperbolic case.** One needs: if $\dim L_X=\infty$, then for every $e$ there exists $n$ and $x\in\pi_n(X)$ of order $>p^{e}$. Even for $X=S^3\cup e^5\cup e^7$ style small hyperbolic complexes this is open in general. The natural route — find spheres $S^{2m+1}$ of arbitrarily large $m$ as $p$-local retracts of $\Omega X$, then invoke $\exp_p(S^{2m+1})=m$ — is exactly what fails: hyperbolic loop spaces need not retract off high-dimensional spheres, and the retract must be compatible with Gray's order-$p^m$ elements surviving.
3. **Prime-independence.** Even granting (1) at one prime, the implication "exponent at $p$ $\Rightarrow$ exponent at $q$" has no known direct proof avoiding rational homotopy.

## 7. Current Research (as of June 2026)

- **$p$-hyperbolicity programme** (Ruizhi Huang, Jie Wu, Stephen Theriault, Guy Boyde; AMSS Beijing, Southampton, Utrecht/Bonn). Extends exponential-growth results from suspensions to polyhedral products, moment-angle complexes, and closed simply connected manifolds with prescribed cohomology rank. *(frontier — verify)* Several 2024–2026 preprints claim $p$-hyperbolicity for all simply connected closed manifolds of dimension $\le 7$ with $b_2\ge 2$.
- **Anick space technology.** Theriault and collaborators refine the fibration $S^{2n-1}\to T^{2n+1}(p^r)\to \Omega S^{2n+1}$ and its $2$-primary analogues, pushing sharp exponents to new classes (gauge groups, quasi-$p$-regular Lie groups).
- **Chromatic/telescopic attacks.** Use of $v_1$- and $v_2$-periodic unstable homotopy (Behrens–Heuts–Meier circle) to detect unbounded orders; the Bousfield–Kuhn functor gives an obstruction-theoretic reformulation of bounded exponent as a vanishing statement for periodic Goodwillie layers. *(frontier — verify)*
- **Rational-to-mod-$p$ transfer.** Attempts to lift Félix–Halperin–Thomas exponential growth to $\mathbb F_p$ via Halperin–Levin depth theory and the radical of $L_X$.

## 8. Future Work

- Prove the "single hard implication": hyperbolic $\Rightarrow$ unbounded torsion orders, first for two-cone complexes $X=(\bigvee S^{n_i})\cup(\text{cells})$ where $H_*(\Omega X;\mathbb F_p)$ is a free algebra modulo one relation.
- Establish a **retraction criterion**: find checkable conditions on $H_*(X;\mathbb F_p)$ guaranteeing that $\Omega X_{(p)}$ retracts off $S^{2m+1}_{(p)}$ for arbitrarily large $m$ (Selick's suggested route).
- Remove the large-prime hypothesis in McGibbon–Wilkerson by finding an exponent bound depending only on $\dim X$ and $\dim L_X$, not on $p$.
- Formulate and test a **quantitative Moore conjecture**: for elliptic $X$, is $\exp_p(X)\le \dim X$ for all $p$? Verified for spheres and Lie groups; no counterexample known.
- Systematic machine search over small CW complexes (few cells, dimension $\le 12$) computing $\pi_*$ ranges with computer algebra (e.g. Kenzo/HAP) to look for anomalous bounded torsion.

## 9. Key References

- **[Foundational]** J.-P. Serre. *Groupes d'homotopie et classes de groupes abéliens.* Annals of Mathematics 58 (1953), 258–294.
- **[Foundational]** I. M. James. *On the suspension sequence.* Annals of Mathematics 65 (1957), 74–107. [DOI](https://doi.org/10.2307/1969666)
- **[Foundational]** B. Gray. *On the sphere of origin of infinite families in the homotopy groups of spheres.* Topology 8 (1969), 219–232. [DOI](https://doi.org/10.1016/0040-9383(69)90012-3)
- **[Foundational]** P. Selick. *Odd primary torsion in $\pi_k(S^3)$.* Topology 17 (1978), 407–412.
- **[Foundational]** F. R. Cohen, J. C. Moore, J. A. Neisendorfer. *Torsion in homotopy groups.* Annals of Mathematics 109 (1979), 121–168.
- **[Foundational]** F. R. Cohen, J. C. Moore, J. A. Neisendorfer. *Exponents in homotopy theory.* In *Algebraic Topology and Algebraic K-Theory*, Annals of Mathematics Studies 113, Princeton University Press, 1987.
- **[Survey]** P. Selick. *Moore conjectures.* In *Algebraic Topology — Rational Homotopy* (Louvain-la-Neuve, 1986), Lecture Notes in Mathematics 1318, Springer, 1988, 219–227.
- **[Foundational]** C. A. McGibbon, C. W. Wilkerson. *Loop spaces of finite complexes at large primes.* Proceedings of the American Mathematical Society 96 (1986), 698–702. [DOI](https://doi.org/10.1090/s0002-9939-1986-0826505-x)
- **[Survey]** Y. Félix, S. Halperin, J.-C. Thomas. *Rational Homotopy Theory.* Graduate Texts in Mathematics 205, Springer, 2001.
- **[SOTA]** Y. Félix, S. Halperin, J.-C. Thomas. *Exponential growth and an asymptotic formula for the ranks of homotopy groups of a finite 1-connected complex.* Annals of Mathematics 170 (2009), 443–464. [DOI](https://doi.org/10.4007/annals.2009.170.443)
- **[SOTA]** D. M. Davis, S. Theriault. *Odd-primary homotopy exponents of compact simple Lie groups.* Geometry & Topology Monographs 13 (2008), 195–201. [DOI](https://doi.org/10.2140/gtm.2008.13.195)
- **[SOTA]** S. Theriault. *Homotopy exponents of mod $2^r$ Moore spaces.* Topology 47 (2008), 369–398.
- **[Survey]** J. A. Neisendorfer. *Algebraic Methods in Unstable Homotopy Theory.* New Mathematical Monographs 12, Cambridge University Press, 2010. [DOI](https://doi.org/10.1017/cbo9780511691638)
- **[SOTA]** R. Huang, J. Wu. *Exponential growth of homotopy groups of suspended finite complexes.* Mathematische Zeitschrift 295 (2020), 1301–1321. [DOI](https://doi.org/10.1007/s00209-019-02383-w)
- **[SOTA]** G. Boyde. *$p$-hyperbolicity of homotopy groups via $K$-theory.* Mathematische Zeitschrift 301 (2022), 977–1009. [DOI](https://doi.org/10.1007/s00209-021-02917-1)

## 10. Worked Example / Concrete Special Case

**Claim.** Moore's conjecture holds for $X=S^3\vee S^3$, at every odd prime $p$.

*Step 1: $X$ is hyperbolic.* The rational homotopy Lie algebra $L_X=\pi_*(\Omega X)\otimes\mathbb Q$ is the free graded Lie algebra $\mathbb{L}(x_1,x_2)$ on two generators of degree $2$. Its dimensions are given by the necklace/Witt formula: the number of basic products of weight $k$ is
$$W(k)=\frac1k\sum_{d\mid k}\mu(d)\,2^{k/d}.$$
So $W(1)=2$, $W(2)=1$, $W(3)=2$, $W(4)=3$, $W(5)=6$, $W(6)=9$, $W(7)=18$, $W(8)=30$. Since $\sum_k W(k)=\infty$ and $W(k)\sim 2^k/k$, $X$ is hyperbolic with growth rate $C=2$.

*Step 2: Hilton's theorem.* There is a homotopy equivalence
$$\Omega(S^3\vee S^3)\;\simeq\;\prod_{w}\Omega S^{\,n_w},$$
the product taken over basic products $w$, where a basic product of weight $k$ contributes a sphere of dimension $n_w=2k+1$. Concretely the factors are
$$S^3,S^3;\;S^5;\;S^7,S^7;\;S^9,S^9,S^9;\;S^{11}\ (\times 6);\ \dots$$
Hence for every $k\ge 1$, $S^{2k+1}$ is a retract of $\Omega(S^3\vee S^3)$ (indeed $\Sigma$-desuspending, $\pi_n(S^{2k+1})$ is a direct summand of $\pi_n(S^3\vee S^3)$ for all $n$).

*Step 3: apply Gray's lower bound.* For odd $p$ and each $k\ge 1$, Gray produces an element of order exactly $p^{k}$ in $\pi_*(S^{2k+1})$. Take $p=3$, $k=4$: there is $\alpha\in\pi_N(S^{9})$ of order $3^{4}=81$, and by Step 2 it injects as a summand into $\pi_N(S^3\vee S^3)$.

*Step 4: conclude.* Given any putative exponent $3^{e}$, choose $k=e+1$. The wedge contains $S^{2k+1}=S^{2e+3}$ as a retract and thus contains an element of order $3^{\,e+1}>3^{e}$. So no exponent exists at $p=3$; the same argument runs at every odd $p$. Therefore $X$ is hyperbolic **and** has unbounded $p$-torsion — exactly as Moore predicts.

**Contrast (elliptic side).** $X=S^3$ itself: $L_X=\mathbb Q\langle x\rangle$ is $1$-dimensional, so $X$ is elliptic, and Selick's theorem gives $\exp_p(S^3)=1$ for odd $p$ (and $\exp_2(S^3)=2$). Bounded torsion, finite rational homotopy — again consistent.

**Where the argument breaks in general.** Step 2 is the whole proof, and it is available only because Hilton's theorem splits the loop space of a wedge into spheres. For a hyperbolic complex with cells attached — say $X=(S^3\vee S^3)\cup_f e^{7}$ with $f$ a nontrivial Whitehead-type attaching map — $\Omega X$ has no such decomposition, no high-dimensional sphere retracts are known, and whether $\pi_*(X)$ has unbounded $p$-torsion is open. That is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*