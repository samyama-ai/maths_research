---
id: 01-number-theory/effective-schmidt-subspace-theorem
title: "Schmidt's Subspace Conjecture Effectivity Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Schmidt's Subspace Conjecture Effectivity Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/effective-schmidt-subspace-theorem` · **Status:** open

## 1. Problem Statement / Conjecture

Schmidt's Subspace Theorem (1972) says that the solutions of a system of Diophantine inequalities in $n$ variables lie in finitely many proper rational linear subspaces of $\mathbb{Q}^n$. The proof — a descendant of Thue–Siegel–Roth — is **ineffective**: it shows the exceptional subspaces exist and (after later work) bounds their *number*, but supplies no algorithm to *find* them, and no bound on the height of solutions outside them.

**The problem.** Produce an effective form of the Subspace Theorem. Concretely:

- **(E1) Effective subspaces.** Give an algorithm that, on input the linear forms $L_1,\dots,L_n$ and $\varepsilon>0$, outputs an explicit finite list of proper subspaces $T_1,\dots,T_t\subsetneq\mathbb{Q}^n$ containing all solutions.
- **(E2) Effective height bound.** Equivalently in most applications: bound $H(\mathbf{x})$ effectively for all solutions $\mathbf{x}$ not lying in a *degenerate* locus that is itself explicitly described.

A complete solution to (E1) for all $n\ge 3$ would be a proof or a construction; a disproof is not expected (no one conjectures ineffectivity is intrinsic), so the problem is one of method. Already $n=2$ — an effective Roth theorem — is open.

## 2. Mathematical Foundations

Let $K$ be a number field, $M_K$ its places, normalized so the product formula $\prod_{v\in M_K}|x|_v=1$ holds for $x\in K^\times$. For $\mathbf{x}=(x_1,\dots,x_n)\in K^n\setminus\{0\}$ the absolute multiplicative height is
$$H(\mathbf{x})=\prod_{v\in M_K}\max_{1\le i\le n}|x_i|_v^{\,d_v/[K:\mathbb{Q}]},\qquad d_v=[K_v:\mathbb{Q}_v].$$

**Subspace Theorem (Schmidt 1972; Schlickewei 1977, $S$-adic form).** Let $S\subset M_K$ be finite, and for each $v\in S$ let $L_{1,v},\dots,L_{n,v}$ be linearly independent linear forms in $n$ variables with algebraic coefficients. For every $\varepsilon>0$ the set of solutions $\mathbf{x}\in \mathcal{O}_S^n$ (or $K^n$, with the normalized double product) of
$$\prod_{v\in S}\prod_{i=1}^{n}\frac{|L_{i,v}(\mathbf{x})|_v}{\|\mathbf{x}\|_v}\;<\;H(\mathbf{x})^{-n-\varepsilon}$$
is contained in a finite union of proper linear subspaces of $K^n$.

For $n=2$ with $L_1=\alpha x_1 - x_2$, $L_2=x_1$ this reduces to **Roth's Theorem** (1955): for algebraic irrational $\alpha$ and $\varepsilon>0$,
$$\left|\alpha-\frac{p}{q}\right|>\frac{c(\alpha,\varepsilon)}{q^{2+\varepsilon}}\quad\text{for all }p/q\in\mathbb{Q},$$
with $c(\alpha,\varepsilon)>0$ **not effectively computable** by the proof.

**Source of ineffectivity.** The Thue–Siegel–Roth–Schmidt machine constructs an auxiliary polynomial $P$ of controlled height vanishing to high order, and derives a contradiction from *two or more* hypothetical solutions $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(m)}$ whose heights grow rapidly:
$$\log H(\mathbf{x}^{(1)})\ \gg_{\varepsilon}\ 1,\qquad \log H(\mathbf{x}^{(j+1)})\ \ge\ \omega\,\log H(\mathbf{x}^{(j)}),\ \ \omega=\omega(n,\varepsilon)\ \text{large}.$$
The contradiction shows no such *chain* exists; it does not exclude one "first" solution of unknown size. Hence the argument bounds the **number** of solutions/subspaces but not their **height**. This "one exceptional solution" gap is the technical heart of the problem.

**Effective counterpoint.** Baker's theory of linear forms in logarithms gives, for algebraic $\alpha_1,\dots,\alpha_m$ and integers $b_i$,
$$\left|b_1\log\alpha_1+\cdots+b_m\log\alpha_m\right|>\exp\!\big(-C(m,d,h(\alpha_i))\log B\big),\qquad B=\max|b_i|,$$
with $C$ explicit. This yields effective bounds for Thue, Thue–Mahler, and two-variable $S$-unit equations, but its reach stops at $\mathbb{G}_m^n$-type problems and does not cover general subspace configurations.

## 3. History & State of the Art (SOTA)

- **1909–1955.** Thue, Siegel, Dyson, Gelfond, Roth: the exponent $2+\varepsilon$ for rational approximation, ineffective from the start (Thue's method already compared two large solutions).
- **1970–71.** Feldman: an effective improvement on Liouville, $|\alpha-p/q|>c(\alpha)q^{-d+\kappa}$ with $c,\kappa>0$ effective but $\kappa$ minuscule — the only effective general improvement known, and far from $2+\varepsilon$.
- **1972.** Schmidt proves the Subspace Theorem, applying it to norm-form equations (*Ann. of Math.* 96).
- **1977.** Schlickewei's $p$-adic/$S$-adic extension.
- **1982–1993.** Bombieri's effective Thue–Siegel–Dyson theorem and "effective Diophantine approximation on $\mathbb{G}_m$" (with Cohen) — effective in restricted settings via Dyson's lemma plus an auxiliary "starting" approximation.
- **1989–2002.** Quantitative subspace theorems: Schmidt (*Compositio* 69, 1989), Evertse (*Compositio* 101, 1996), Evertse–Schlickewei absolute version (*J. reine angew. Math.* 548, 2002). Explicit bounds on the *number* of subspaces of shape
$$t\ \le\ 2^{2^{c n^2}}\varepsilon^{-7n}\log(4D)\log\log(4D),$$
$D$ the degree of the coefficient field. Heights remain unbounded.
- **1994.** Faltings–Wüstholz give a new proof via a product-theorem/geometric induction; still ineffective.
- **2002–2020.** Evertse–Schlickewei–Schmidt bound the number of non-degenerate solutions of $a_1u_1+\dots+a_nu_n=1$ in a multiplicative group (*Ann. of Math.* 155, 2002); Evertse–Ferretti extend the theorem to hypersurfaces of higher degree; Corvaja–Zannier and Levin build the integral-points program on it — all inheriting ineffectivity.

**SOTA in one line:** the number of exceptional subspaces is explicit; the height of solutions is effective only in cases reachable by Baker's method or Bombieri's $\mathbb{G}_m$ technique.

## 4. Partial Results / Verified Cases

Effective results are known in these concrete regimes:

1. **$n=2$, specific algebraic numbers by the hypergeometric method.** Baker (1964): $|2^{1/3}-p/q|>10^{-6}q^{-2.955}$ for all $p/q$. Similar explicit exponents $<d$ exist for $\sqrt[n]{a}$ with $a$ close to a perfect power (Baker, Chudnovsky, Bennett). Bennett (1997) obtained $|\sqrt[3]{a}-p/q|>q^{-2.5}/4$ for all integers $a\ge 3$ outside an explicit list.
2. **Thue and Thue–Mahler equations.** $F(x,y)=m$ with $F$ irreducible binary of degree $\ge 3$: effective bounds $\max(|x|,|y|)<\exp\big(c\,H^{c'}\,\log m\big)$ via Baker (Baker 1968; Győry–Yu 2006 give sharp explicit $S$-versions). Complete solution lists are computed routinely (Tzanakis–de Weger algorithm).
3. **$S$-unit equations in two variables.** $u_1+u_2=1$, $u_i\in\mathcal{O}_S^\times$: heights effectively bounded (Győry, Evertse–Győry, *Unit Equations in Diophantine Number Theory*, CUP 2015), including over finitely generated domains (Evertse–Győry 2022).
4. **Decomposable-form and norm-form equations of "$\mathbb{G}_m$ type".** Effective when the associated module has rank giving a two-term unit equation; ineffective as soon as three independent units appear.
5. **Counting, all $n$.** Fully explicit bounds on the number of subspaces and on the number of non-degenerate solutions of $\sum a_iu_i=1$ — e.g. at most $(2^{35}n^2)^{n^3 r}$ solutions with $r$ the rank of the group (Evertse–Schlickewei–Schmidt 2002).
6. **Approximation to $\alpha$ with an unusually good starting approximation.** Bombieri–Cohen: given one explicit very good approximation, effective exponent improvements follow — the "effective from effective" phenomenon.

## 5. Principal Obstacles

- **The two-solution architecture.** Roth's index/Roth lemma argument, Dyson's lemma, and the Faltings–Wüstholz product theorem all derive a contradiction only from a *gap sequence* of solutions. A single solution of arbitrary height is invisible to the method. Removing this requires an entirely different source of contradiction.
- **Non-constructive pigeonholing.** The auxiliary polynomial is produced by Siegel's lemma; its zero locus is not controlled, so the exceptional subspaces arise as "the span of whichever solutions the argument failed on", not as computable objects.
- **No class-number/height-zero anchor.** Baker's method works because logarithms of algebraic numbers admit a lower bound in terms of *heights of fixed data*; Roth-type approximation has no analogous archimedean invariant to lower-bound.
- **Baker's method does not scale.** Linear forms in logarithms handle $\mathbb{G}_m^n$ but the general subspace configuration involves several linear forms per place whose vanishing loci are not multiplicative; there is no known linear-forms-in-logarithms statement whose specialization gives Roth.
- **Equivalence to hard conjectures.** An effective Roth theorem with the full exponent $2+\varepsilon$ is at least as strong as effective versions of $abc$-type statements; conversely, an effective $abc$ conjecture would give an effective Roth. Both remain open.

## 6. The Gap

Section 4 gives effective bounds exactly where the problem can be reduced to **at most two multiplicatively independent quantities** (Thue, two-term $S$-unit equations, $\mathbb{G}_m$ approximation). Section 1 asks for the same in $n\ge 3$ variables with arbitrary linear forms.

The precise crossing point:

> Given the Subspace Theorem's hypothetical solution set, produce a bound $H(\mathbf{x})\le B(n,\varepsilon,L_{i,v})$ for solutions outside an explicitly listed union of subspaces.

The cleanest test case is the **three-term $S$-unit equation** $u_1+u_2+u_3=1$: the number of non-degenerate solutions is bounded explicitly, but no effective bound on $\max_i h(u_i)$ is known for any $S$ with $|S|\ge 3$. Any technique effective there would very likely break the general barrier.

## 7. Current Research (as of June 2026)

- **Nevanlinna–Diophantine dictionary.** Ru–Vojta's birational Nevanlinna constant $\mathrm{Nev}(D)$ and its arithmetic counterpart (Ru–Vojta, *Amer. J. Math.* 2020; Ru–Wang) reorganize subspace-type statements around Seshadri-like constants. These are computable in examples, which raises the possibility of computable exceptional loci — height effectivity still absent. *(frontier — verify)*
- **Effective results via Baker + geometry.** Continuing work of Győry, Bugeaud, Evertse and collaborators pushes explicit constants in decomposable-form and unit equations, and in equations over finitely generated domains.
- **Arakelov/Bost-style approaches.** Slope inequalities and Bost's arithmetic Bogomolov-type methods have produced alternative proofs of Roth-type statements with more geometric constants; effectivity has not followed. *(frontier — verify)*
- **Effective $abc$ via modularity or via inter-universal methods.** Any effective $abc$ would yield effective Roth in the number-field case; the status of claimed proofs remains contested. *(frontier — verify)*
- **Groups:** Leiden (Evertse), Rényi Institute/Debrecen (Győry, Bérczes), Padova/Udine (Corvaja, Zannier), Brown (Levin), Houston (Ru).

## 8. Future Work

1. **Attack $u_1+u_2+u_3=1$ effectively.** Even a bound depending on an unspecified but *finite* list of explicitly-tested small solutions would be a breakthrough.
2. **Effectivize the Faltings–Wüstholz proof.** Its product theorem is more geometric than Roth's lemma; making the exceptional subvariety explicit is a concrete target.
3. **Find a second archimedean invariant.** Bombieri's programme — extract effectivity from one good explicit approximation — suggests searching for constructions of such approximations (e.g. from Padé/hypergeometric families, or from special points on modular curves).
4. **Quantitative → effective transfer.** Determine whether an explicit bound on the *number* of solutions plus a bound on the *gap ratio* $\omega$ can ever be converted into a height bound; currently believed impossible without new input, but no theorem forbids it.
5. **Effective $abc$ over function fields as a model.** The function-field analogue (Mason–Stothers) is fully effective; understanding what makes the number-field case fail is a guiding question.

## 9. Key References

- **[Foundational]** K. F. Roth. *Rational approximations to algebraic numbers.* Mathematika 2 (1955), 1–20.
- **[Foundational]** W. M. Schmidt. *Norm form equations.* Annals of Mathematics 96 (1972), 526–551.
- **[Foundational]** W. M. Schmidt. *Diophantine Approximation.* Lecture Notes in Mathematics 785, Springer, 1980.
- **[Foundational]** H. P. Schlickewei. *The p-adic Thue–Siegel–Roth–Schmidt theorem.* Archiv der Mathematik 29 (1977), 267–270.
- **[Foundational]** A. Baker. *Rational approximations to certain algebraic numbers.* Proc. London Math. Soc. (3) 14 (1964), 385–398.
- **[SOTA]** J.-H. Evertse, H. P. Schlickewei. *A quantitative version of the absolute subspace theorem.* J. reine angew. Math. 548 (2002), 21–127.
- **[SOTA]** J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt. *Linear equations in variables which lie in a multiplicative group.* Annals of Mathematics 155 (2002), 807–836.
- **[SOTA]** G. Faltings, G. Wüstholz. *Diophantine approximations on projective spaces.* Inventiones Mathematicae 116 (1994), 109–138.
- **[SOTA]** M. Ru, P. Vojta. *A birational Nevanlinna constant and its consequences.* American Journal of Mathematics 142 (2020), 957–991.
- **[SOTA]** E. Bombieri. *On the Thue–Siegel–Dyson theorem.* Acta Mathematica 148 (1982), 255–296.
- **[Survey / Book]** J.-H. Evertse, K. Győry. *Unit Equations in Diophantine Number Theory.* Cambridge University Press, 2015.
- **[Survey / Book]** J.-H. Evertse, K. Győry. *Effective Results and Methods for Diophantine Equations over Finitely Generated Domains.* Cambridge University Press, 2022.
- **[Survey]** Y. Bugeaud. *Approximation by Algebraic Numbers.* Cambridge University Press, 2004.
- **[Survey]** P. Corvaja, U. Zannier. *Applications of the Subspace Theorem to Certain Diophantine Problems*, Springer Lecture Notes in Mathematics 2298, 2022.

## 10. Worked Example / Concrete Special Case

**The effective side ($n=2$, one algebraic number).** Take $\alpha=2^{1/3}$ and the Thue equation
$$x^3-2y^3=m,\qquad |m|\le 100,\ x,y\in\mathbb{Z},\ y\ge 1.$$
Factor over $\mathbb{R}$:
$$|x^3-2y^3|=|x-\alpha y|\cdot\big|x^2+\alpha xy+\alpha^2y^2\big| .$$
If $|x-\alpha y|$ is small then $x/y\approx\alpha$, so $|x^2+\alpha xy+\alpha^2 y^2|\ge 3\alpha^2y^2/2\ge 2.3\,y^2$ for $y$ large. Baker's explicit bound gives $|x-\alpha y| = y\,|\alpha - x/y| > 10^{-6}y^{-1.955}$. Hence
$$100\ \ge\ |m|\ >\ 10^{-6}y^{-1.955}\cdot 2.3\,y^{2}\ =\ 2.3\times 10^{-6}\,y^{0.045},$$
so $y^{0.045}<4.35\times10^{7}$, i.e. $y< \exp(0.045^{-1}\log(4.35\times10^7))\approx e^{391}$. Crude, but **explicit**: a finite search (in practice reduced to a few hundred steps by lattice reduction) settles the equation. Roth's theorem alone gives $|x-\alpha y|>c(\varepsilon)y^{-1-\varepsilon}$ with $c$ unknown, hence *no* bound at all on $y$.

**The ineffective side ($n=3$).** Let $S=\{\infty,2,3,5\}$ and consider
$$u_1+u_2+u_3=1,\qquad u_i\in\mathbb{Z}[1/30]^\times=\{\pm2^{a}3^{b}5^{c}\}.$$
Applying the Subspace Theorem to the forms $L_1=x_1,L_2=x_2,L_3=x_1+x_2+x_3$ at each $v\in S$ shows: all but finitely many solutions satisfy a vanishing subsum ($u_i+u_j=0$ or $u_i=1$), and the number of non-degenerate ones is bounded by the Evertse–Schlickewei–Schmidt estimate. Small non-degenerate solutions are easy to list by search, e.g.
$$\tfrac{1}{2}+\tfrac{1}{3}+\tfrac{1}{6}=1,\qquad \tfrac{3}{5}+\tfrac{1}{3}+\tfrac{1}{15}=1,\qquad \tfrac{9}{10}+\tfrac{1}{15}+\tfrac{1}{30}=1 .$$
**What is not known:** any effective $B$ with $\max_i h(u_i)\le B$. Nothing in the proof rules out a further solution with $a,b,c$ of size $10^{100}$; the argument only says a *second* such large solution cannot exist beyond the counted total. That single un-bounded solution — for this four-place, three-term instance — is the whole problem in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*