---
id: 02-algebra-group-theory/gap-conjecture-on-group-growth
title: "Gap Conjecture on Group Growth"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gap Conjecture on Group Growth

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/gap-conjecture-on-group-growth` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finitely generated group with finite generating set $S = S^{-1}$, and let
$$\gamma_{G,S}(n) = \\#\{g \in G : |g|_S \le n\}$$
be its growth function, where $|g|_S$ is the word length of $g$.

**Gap Conjecture (Grigorchuk).** If $\gamma_{G,S}(n) \prec e^{\sqrt{n}}$, then $\gamma_{G,S}(n)$ is polynomially bounded — equivalently, by Gromov's theorem, $G$ is virtually nilpotent.

Here $f \prec g$ means $f(n) \le g(Cn)$ fails to hold in the reverse direction: precisely, $f \preccurlyeq g$ iff $f(n) \le C g(Cn)$ for some $C>0$ and all $n$, and $f \prec g$ means $f \preccurlyeq g$ but not $g \preccurlyeq f$. The conjecture asserts that no group has growth type strictly between polynomial and $e^{\sqrt n}$: the interval of growth types
$$\big(\text{polynomial},\ e^{\sqrt n}\big)$$
is empty.

A **disproof** is a single finitely generated group of intermediate growth with $\gamma(n) \prec e^{\sqrt n}$. A **proof** must handle all finitely generated groups, including non-residually-finite and infinite simple ones. The parametrised version, $\mathrm{GC}_\beta$, replaces $e^{\sqrt n}$ by $e^{n^\beta}$ for $\beta \in (0,1)$; $\mathrm{GC}_{1/2}$ is the conjecture proper, and $\mathrm{GC}_\beta$ for $\beta<1/2$ is weaker. Growth type is independent of $S$, so the statement is a group invariant.

## 2. Mathematical Foundations

**Growth types.** For generating sets $S,T$ there is $C$ with $\gamma_{G,S}(n) \le \gamma_{G,T}(Cn)$; equivalence classes under $\preccurlyeq$-mutual domination are *growth degrees*. $G$ has **polynomial growth** if $\gamma(n) \le Cn^d$, **exponential growth** if $\lim_n \gamma(n)^{1/n} > 1$, and **intermediate growth** otherwise. Submultiplicativity $\gamma(m+n)\le\gamma(m)\gamma(n)$ gives the existence of $\lambda = \lim \gamma(n)^{1/n} \ge 1$ (Fekete), so no group has growth type strictly between subexponential and exponential.

**Gromov's theorem (1981).** $\gamma_G(n) \le Cn^d$ for all $n$ $\iff$ $G$ is virtually nilpotent. Bass–Guivarc'h then gives the exact degree: for nilpotent $G$ with lower central series $\gamma_1 = G \supseteq \gamma_2 \supseteq \cdots$,
$$\gamma_G(n) \asymp n^{d}, \qquad d = \sum_{i\ge 1} i \cdot \operatorname{rank}(\gamma_i/\gamma_{i+1}).$$
Hence "polynomially bounded", "virtually nilpotent", and "$\gamma(n)\preccurlyeq n^{d}$ for some $d$" are interchangeable in §1.

**Where $\sqrt{n}$ comes from.** Let $G$ be residually-$p$ and let $\{D_n(G)\}$ be the Zassenhaus–Jennings–Lazard dimension series, $D_n(G) = G \cap (1 + \Delta^n)$ for the augmentation ideal $\Delta \subset \mathbb{F}_p[G]$. The graded Lie algebra $L(G) = \bigoplus_{n\ge1} D_n/D_{n+1}$ and the Hilbert–Poincaré series of $\operatorname{gr}\mathbb{F}_p[G]$ control $\gamma_G$ from below: if $L(G)$ has superlinear dimension growth, one obtains
$$\gamma_G(n) \succcurlyeq e^{c\sqrt{n}} .$$
The exponent $1/2$ is exactly the threshold produced by a graded algebra of *linear* dimension growth, via the partition-function estimate $\log p(n) \sim \pi\sqrt{2n/3}$. This is the structural reason $e^{\sqrt n}$, and not some other function, is conjectured to be the edge of the gap.

**Branch/self-similar side.** For a self-similar group $G \le \operatorname{Aut}(T_2)$ with $\psi: \operatorname{St}_G(1) \hookrightarrow G\times G$, $g \mapsto (g_0,g_1)$, a *contraction* inequality
$$|g_0| + |g_1| \le \eta\,|g| + C, \qquad \eta < 1,$$
forces subexponential growth with $\gamma(n) \le \exp(C n^{\alpha})$, $\alpha = \dfrac{\log 2}{\log(2/\eta)}$. Note $\alpha = 1/2$ requires $\eta = 1/2$, the exact critical contraction.

## 3. History & State of the Art (SOTA)

- **1968.** Milnor asks whether every finitely generated group has growth either polynomial or exponential (Amer. Math. Monthly Problem 5603). Milnor and Wolf settle the solvable case: a finitely generated solvable group is either virtually nilpotent (polynomial) or of exponential growth.
- **1972.** Tits alternative: finitely generated linear groups over a field are virtually solvable or contain $F_2$ — so linear groups have no intermediate growth.
- **1981.** Gromov proves the polynomial growth theorem, fixing the lower end of the scale.
- **1983–84.** Grigorchuk answers Milnor negatively: the first Grigorchuk group $\mathcal{G}$ has intermediate growth, and the family $G_\omega$ realises uncountably many pairwise incomparable growth degrees. Crucially, every constructed example satisfies $\gamma(n) \succcurlyeq e^{\sqrt n}$ — the empirical origin of the conjecture.
- **1989.** Grigorchuk proves the $e^{\sqrt n}$ gap for residually nilpotent (in particular residually-$p$) groups, via Hilbert–Poincaré series of associated graded algebras.
- **1998–2001.** Bartholdi: $\gamma_{\mathcal G}(n) \le \exp(n^{\alpha_0})$, $\alpha_0 = \log 2/\log(2/\rho) \approx 0.7674$, $\rho$ the real root of $x^3+x^2+x=2$; Leonov and Bartholdi push the lower bound to $\exp(n^{0.5157})$.
- **2010.** Shalom–Tao give a finitary Gromov theorem: if $\gamma(n_0) \le n_0^{c(\log\log n_0)^c}$ at a *single* scale $n_0 \ge \exp(\exp(c))$, then $G$ is virtually nilpotent. This is a genuine gap theorem, but at the scale $n^{(\log\log n)^{c}}$, far below $e^{\sqrt n}$.
- **2012–2013.** Bartholdi–Erschler realise $\exp(n^\alpha)$ for every $\alpha \in [\alpha_0,1)$; Kassabov–Pak build groups of oscillating intermediate growth, whose lower oscillation envelope in known constructions does not go below $e^{\sqrt n}$.
- **2014.** Grigorchuk formalises and names the Gap Conjecture (Bull. Math. Sci. 4), proving it for residually solvable and left-orderable groups and reducing the general case to just-infinite groups.
- **2020.** Erschler–Zheng determine the growth of $\mathcal{G}$ exactly: $\gamma_{\mathcal G}(n) = \exp(n^{\alpha_0+o(1)})$, $\alpha_0 \approx 0.7674$. The slowest known intermediate growth is therefore still $\exp(n^{0.7674})$, well above $e^{\sqrt n}$.

## 4. Partial Results / Verified Cases

The conjecture is a theorem in the following classes.

| Class | Result | Source |
|---|---|---|
| Residually nilpotent (incl. residually-$p$) | $\gamma \prec e^{\sqrt n} \Rightarrow$ virtually nilpotent; exponent $1/2$ sharp for the method | Grigorchuk 1989 |
| Residually solvable | Same conclusion, by reduction to the residually nilpotent case | Grigorchuk 2014 |
| Elementary amenable | Subexponential $\Rightarrow$ virtually nilpotent (no intermediate growth at all) | Chou 1980 |
| Finitely generated linear over any field | Polynomial or exponential | Tits 1972 + Milnor–Wolf |
| Solvable, polycyclic | Polynomial or exponential | Milnor 1968, Wolf 1968 |
| Word-hyperbolic | Virtually cyclic or exponential | Gromov 1987 |
| Left-orderable | Gap holds (amenable left-orderable $\Rightarrow$ locally indicable, D. W. Morris 2006) | Grigorchuk 2014 |
| Groups with a single scale bound $\gamma(n_0)\le n_0^{c(\log\log n_0)^c}$ | Virtually nilpotent | Shalom–Tao 2010 |
| All known intermediate-growth groups: $G_\omega$, Grigorchuk–Gupta–Sidki type, Bartholdi–Erschler, Kassabov–Pak, Nekrashevych's simple groups of intermediate growth | Every one verified to satisfy $\gamma \succcurlyeq e^{\sqrt n}$; minimum realised exponent $\alpha_0\approx 0.7674$ | Bartholdi 1998; Erschler–Zheng 2020 |

**Reduction.** Grigorchuk proved the Gap Conjecture holds in general iff it holds for just-infinite groups. By Wilson's trichotomy, a just-infinite group is branch, hereditarily just-infinite, or virtually a direct power of a simple group; so it suffices to prove $\mathrm{GC}_{1/2}$ for (i) residually finite branch groups, (ii) hereditarily just-infinite groups, (iii) finitely generated infinite simple groups.

## 5. Principal Obstacles

- **No general lower-bound machinery.** Every proven case obtains its $e^{\sqrt n}$ bound from a *linear structure*: a graded Lie algebra (residually nilpotent), a solvable quotient, or an order. For a group with no nontrivial finite-dimensional linear representation and no normal subgroup structure — Nekrashevych's simple groups of intermediate growth, say — no such algebra exists, and there is no known substitute invariant that converts "infinite" into a growth lower bound.
- **The Shalom–Tao ceiling.** Ultrafilter/Gleason–Yamabe methods and their finitary versions detect virtual nilpotence only under bounds of type $n^{(\log\log n)^c}$. Pushing the threshold to $e^{\sqrt n}$ would require the entire Hilbert-fifth-problem apparatus to run at exponential-type scale, where the escape and non-degeneracy estimates on the limit Lie group collapse.
- **Upper-bound constructions are one-sided.** Self-similar contraction gives $\alpha = \log 2/\log(2/\eta)$; to reach $\alpha < 1/2$ one needs $\eta < 1/2$ on a binary tree, which forces the group to be finite or to lose the branching that produced infiniteness. Larger alphabets or permutational wreath extensions raise $\alpha$, not lower it.
- **Non-uniformity of growth.** Kassabov–Pak's oscillating groups show growth need not have a well-defined exponent, so any proof must control $\gamma$ at *all* scales simultaneously; single-scale arguments and subsequence arguments are both inadequate.
- **Amenability is not enough.** All subexponential-growth groups are amenable (Følner), but amenability supplies no quantitative lower bound on $\gamma$.

## 6. The Gap

Proven: $\gamma \prec e^{\sqrt n}$ forces virtual nilpotence *when $G$ has a faithful approximation by nilpotent, solvable, linear, or ordered structure*. Unproven: the same for groups with none of these — concretely, for (i) residually finite branch groups that are not residually nilpotent (a branch group is typically residually finite but its lower central series may fail to separate points), (ii) hereditarily just-infinite groups, (iii) finitely generated infinite simple groups of subexponential growth, of which Nekrashevych (2018) constructed the first examples.

The precise missing step: **a growth lower bound $\gamma_G(n) \succcurlyeq e^{c\sqrt n}$ for infinite finitely generated groups derived from a non-linear invariant.** Equivalently, one wants an analogue of the Hilbert–Poincaré series argument in which the role of $\bigoplus D_n/D_{n+1}$ is played by a filtration surviving in the absence of nilpotent quotients — e.g. a filtration by rigid stabilisers, by the germ/portrait complexity of tree automorphisms, or by the Følner-set entropy profile. The numerical gap on the constructive side is equally stark: known intermediate growth exponents occupy $[0.7674, 1)$, and nothing is known in $(1/2, 0.7674)$ either.

## 7. Current Research (as of June 2026)

- **Branch and self-similar groups.** Groups around Grigorchuk (Texas A&M), Bartholdi (Saarbrücken), Nekrashevych (Texas A&M), and Erschler (ENS Paris) continue to compute growth of fragmented/periodic Grigorchuk-type groups and of simple groups built from étale groupoids, testing whether any construction can dip below $\exp(n^{0.7674})$. No candidate below $e^{\sqrt n}$ has been produced. *(frontier — verify)*
- **Random walk entropy route.** Erschler–Zheng's method — bounding growth via return probability and Følner function of the Grigorchuk group — is being extended to broader classes; a general inequality relating the Følner function $\mathrm{Føl}(\varepsilon)$ to $\gamma$ would give lower bounds independent of linearity. *(frontier — verify)*
- **Quantitative Gromov.** Continued attempts, following Shalom–Tao and Breuillard–Green–Tao's structure theory of approximate groups, to raise the single-scale threshold; the current barrier remains quasi-polynomial in $n$.
- **Just-infinite reduction programme.** Work classifying hereditarily just-infinite groups and verifying $\mathrm{GC}_\beta$ for restricted $\beta$ within Wilson's trichotomy; Grigorchuk has emphasised that even $\mathrm{GC}_\beta$ for some fixed $\beta>0$ in full generality would be a major advance.

## 8. Future Work

1. **Prove $\mathrm{GC}_\beta$ for some $\beta > 0$ unconditionally.** Grigorchuk's stated intermediate target: any uniform gap above polynomial growth, however small the exponent.
2. **Branch groups first.** Establish $e^{\sqrt n}$ for all finitely generated residually finite branch groups using rigid stabiliser filtrations; combined with the just-infinite reduction this leaves only hereditarily just-infinite and simple groups.
3. **Non-commutative Hilbert series.** Find a graded object attached to an arbitrary infinite finitely generated group whose Hilbert series must have infinitely many nonzero coefficients, then transfer the $\log p(n) \asymp \sqrt n$ partition bound.
4. **Search below $\alpha_0$.** Construct any group with $\alpha \in (1/2, 0.7674)$; either it exists, giving evidence that the gap is a genuine boundary, or the obstruction found in the attempt is itself the mechanism of the proof.
5. **Growth of simple subexponential groups.** Compute the growth exponent of Nekrashevych's simple groups of intermediate growth explicitly, the most direct test of case (iii).

## 9. Key References

- **[Foundational]** J. Milnor. *Growth of finitely generated solvable groups.* Journal of Differential Geometry 2 (1968), 447–449.
- **[Foundational]** J. A. Wolf. *Growth of finitely generated solvable groups and curvature of Riemannian manifolds.* Journal of Differential Geometry 2 (1968), 421–446.
- **[Foundational]** M. Gromov. *Groups of polynomial growth and expanding maps.* Publications Mathématiques de l'IHÉS 53 (1981), 53–73.
- **[Foundational]** R. I. Grigorchuk. *Degrees of growth of finitely generated groups and the theory of invariant means.* Izvestiya Akademii Nauk SSSR, Ser. Mat. 48 (1984), 939–985.
- **[Foundational]** R. I. Grigorchuk. *On the Hilbert–Poincaré series of graded algebras associated with groups.* Matematicheskii Sbornik 180 (1989), 207–225.
- **[SOTA / Recent]** R. I. Grigorchuk. *On the gap conjecture concerning group growth.* Bulletin of Mathematical Sciences 4 (2014), 79–100.
- **[SOTA / Recent]** A. Erschler, T. Zheng. *Growth of periodic Grigorchuk groups.* Inventiones Mathematicae 219 (2020), 1069–1155.
- **[SOTA / Recent]** L. Bartholdi, A. Erschler. *Growth of permutational extensions.* Inventiones Mathematicae 189 (2012), 431–455.
- **[SOTA / Recent]** Y. Shalom, T. Tao. *A finitary version of Gromov's polynomial growth theorem.* Geometric and Functional Analysis 20 (2010), 1502–1547.
- **[SOTA / Recent]** M. Kassabov, I. Pak. *Groups of oscillating intermediate growth.* Annals of Mathematics 177 (2013), 1113–1145.
- **[Related]** L. Bartholdi. *The growth of Grigorchuk's torsion group.* International Mathematics Research Notices 1998, no. 20, 1049–1054.
- **[Related]** C. Chou. *Elementary amenable groups.* Illinois Journal of Mathematics 24 (1980), 396–407.
- **[Related]** J. S. Wilson. *Groups with every proper quotient finite.* Proceedings of the Cambridge Philosophical Society 69 (1971), 373–391.
- **[Related]** D. W. Morris. *Amenable groups that act on the line.* Algebraic & Geometric Topology 6 (2006), 2509–2518.
- **[Survey]** R. I. Grigorchuk. *Milnor's problem on the growth of groups and its consequences.* In *Frontiers in Complex Dynamics*, Princeton University Press, 2014, 705–773.
- **[Survey]** R. Grigorchuk, I. Pak. *Groups of intermediate growth: an introduction.* L'Enseignement Mathématique 54 (2008), 251–272.
- **[Survey]** A. Mann. *How Groups Grow.* LMS Lecture Note Series 395, Cambridge University Press, 2012.

## 10. Worked Example / Concrete Special Case

**The first Grigorchuk group and why its exponent cannot reach $1/2$.**

$\mathcal{G} = \langle a,b,c,d\rangle \le \operatorname{Aut}(T_2)$ acts on the binary rooted tree: $a$ swaps the two subtrees, and on the stabiliser of level 1,
$$\psi(b) = (a,c), \quad \psi(c) = (a,d), \quad \psi(d) = (1,b), \qquad a^2=b^2=c^2=d^2=bcd=1 .$$
$\operatorname{St}_{\mathcal G}(1)$ has index 2, and $\psi : \operatorname{St}_{\mathcal G}(1) \hookrightarrow \mathcal{G}\times\mathcal{G}$ is injective.

*Step 1 — contraction.* In a suitable weighted word metric (Bartholdi 1998) there is $\eta<1$ with
$$|g_0| + |g_1| \le \eta\,|g| + C \qquad \text{for all } g \in \operatorname{St}_{\mathcal G}(1).$$
The optimal weighting yields $\eta = \rho \approx 0.8114$, the real root of $x^3+x^2+x = 2$.

*Step 2 — counting.* Each $g$ with $|g|\le n$ is determined by a coset representative (boundedly many choices, $\le K$) plus the pair $(g_0,g_1)$, so
$$\gamma(n) \;\le\; K\,(n+1)\!\!\max_{m_0+m_1 \le \eta n + C}\!\! \gamma(m_0)\,\gamma(m_1).$$

*Step 3 — solving.* Try $\gamma(m) \le e^{Am^{\alpha}}$. Under the constraint $m_0+m_1 \le \eta n$, concavity of $t\mapsto t^\alpha$ makes $m_0^\alpha+m_1^\alpha$ maximal at $m_0=m_1=\eta n/2$, giving exponent
$$2A\left(\tfrac{\eta n}{2}\right)^{\alpha} = A n^{\alpha}\cdot 2\left(\tfrac{\eta}{2}\right)^{\alpha}.$$
The recursion closes iff $2(\eta/2)^{\alpha} \le 1$, i.e.
$$\alpha \;\ge\; \frac{\log 2}{\log(2/\eta)} .$$
With $\eta = \rho \approx 0.8114$: $\alpha_0 = \log 2/\log(2.4649) \approx 0.7674$. So $\gamma_{\mathcal G}(n) \le \exp(Cn^{0.7674})$, and Erschler–Zheng (2020) proved this is sharp: $\gamma_{\mathcal G}(n) = \exp(n^{\alpha_0 + o(1)})$.

*Step 4 — the gap read off the formula.* Setting $\alpha = 1/2$ in $\alpha = \log 2/\log(2/\eta)$ gives $\log(2/\eta) = 2\log 2$, i.e. $\eta = 1/2$. A binary self-similar group with contraction coefficient $1/2$ splits a word of length $n$ into two sections of total length $n/2$ with no loss — the sections carry all the information at half the cost, iterating to sections of length $n/2^k$ across $2^k$ coordinates with total length $n/2^k \to 0$. Such a group has trivial sections at bounded depth and is finite. Every infinite branch group therefore has $\eta > 1/2$ and $\alpha > 1/2$.

This is the conjecture in miniature: within the self-similar world, $e^{\sqrt n}$ is precisely the growth of the critical, unattainable contraction $\eta = 1/2$. The Gap Conjecture asserts the same threshold holds for *all* finitely generated groups — including those with no tree action, no nilpotent quotients, and no linear representation, where the argument above has no counterpart.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*