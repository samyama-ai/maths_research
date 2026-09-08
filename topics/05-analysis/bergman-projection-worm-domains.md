---
id: 05-analysis/bergman-projection-worm-domains
title: "Regularity of the Bergman Projection on Worm Domains"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Regularity of the Bergman Projection on Worm Domains

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bergman-projection-worm-domains` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Omega\subset\mathbb{C}^n$ be a bounded domain and let
$$P_\Omega : L^2(\Omega)\longrightarrow A^2(\Omega)=L^2(\Omega)\cap\mathcal{O}(\Omega)$$
be the Bergman projection, the orthogonal projection onto square-integrable holomorphic functions. Say $\Omega$ satisfies **Condition R** if $P_\Omega(C^\infty(\overline\Omega))\subseteq C^\infty(\overline\Omega)$.

The **worm domains** of Diederich–Fornæss are smooth bounded pseudoconvex domains in $\mathbb{C}^2$ that fail Condition R. The open problem is to determine the *exact* regularity of $P_\Omega$ on them:

1. **(Sharp Sobolev threshold.)** For the smooth worm $\Omega_\beta$ with winding parameter $\beta>\pi/2$, determine the supremum
$$s_\beta^\ast := \sup\{s\ge 0:\ P_{\Omega_\beta}:W^s(\Omega_\beta)\to W^s(\Omega_\beta)\ \text{is bounded}\}.$$
The conjecture, extrapolated from Barrett's model computation, is
$$s_\beta^\ast=\frac{\pi}{2\beta-\pi}.$$
2. **(Sharp $L^p$ range.)** Determine $\{p\in(1,\infty): P_{\Omega_\beta}$ is bounded on $L^p(\Omega_\beta)\}$, conjecturally an open interval about $p=2$ shrinking to $\{2\}$ as $\beta\to\infty$.
3. **(Mechanism.)** Decide whether the failure is *quantitatively governed* by the Diederich–Fornæss index $\eta(\Omega_\beta)$, i.e. whether $s^\ast_\beta$ is a function of $\eta$ alone across a wider class of domains.

A complete solution requires two-sided estimates on the smooth (not merely model) worm: matching upper bounds for $s<s^\ast_\beta$ and unboundedness for $s>s^\ast_\beta$.

## 2. Mathematical Foundations

**The Diederich–Fornæss worm.** For $\beta>\pi/2$ set
$$\Omega_\beta=\Big\{(z_1,z_2)\in\mathbb{C}^2:\ \big|z_1-e^{i\log|z_2|^2}\big|^2<1-\phi\big(\log|z_2|^2\big)\Big\},$$
where $\phi\ge 0$ is smooth, even, convex, $\phi^{-1}(0)=[-\beta+\tfrac\pi2,\ \beta-\tfrac\pi2]$, and $\phi'(x)\ne 0$ when $\phi(x)=1$. Then $\Omega_\beta$ is smooth, bounded, pseudoconvex; its boundary contains the annulus
$$A=\{(0,z_2):\ |\log|z_2|^2|\le \beta-\tfrac\pi2\},$$
whose Levi-flat structure carries a nontrivial normal-bundle winding of total angle $2\beta-\pi$.

The **non-smooth model worm** (where all sharp computations are made) is
$$D_\beta'=\Big\{(z_1,z_2):\ \big|z_1-e^{i\log|z_2|^2}\big|^2<1,\ \ \big|\log|z_2|^2\big|<\beta-\tfrac\pi2\Big\}.$$

**Bergman kernel.** $K_\Omega(z,w)=\sum_k \varphi_k(z)\overline{\varphi_k(w)}$ for any orthonormal basis of $A^2$, and $P_\Omega f(z)=\int_\Omega K_\Omega(z,w)f(w)\,dV(w)$.

**Link to $\bar\partial$-Neumann.** With $N$ the $\bar\partial$-Neumann operator on $(0,1)$-forms, Kohn's formula gives
$$P=I-\bar\partial^{\,\ast}N\bar\partial .$$
Boas–Straube (1990) proved that exact $W^s$-regularity of $N$ and of $P$ are equivalent on smooth bounded pseudoconvex domains, so the problem is equally a statement about $N$.

**Diederich–Fornæss index.**
$$\eta(\Omega)=\sup\{\eta\in(0,1]:\ -(-\rho)^{\eta}\ \text{is strictly psh on }\Omega\ \text{for some defining function}\ \rho\}.$$
Every smooth bounded pseudoconvex domain has $\eta>0$ (Diederich–Fornæss 1977). Boas–Straube: if $\eta(\Omega)=1$ (equivalently, a defining function psh on $b\Omega$ exists) then $P$ is $W^s$-bounded for all $s$. The worm has $\eta(\Omega_\beta)<1$, computed exactly in terms of $\beta$ by B. Liu.

**Bell's transformation rule.** If $F:\Omega_1\to\Omega_2$ is biholomorphic,
$$P_{\Omega_1}\big(\det J_F\cdot (u\circ F)\big)=\det J_F\cdot \big(P_{\Omega_2}u\big)\circ F,$$
which is why Condition R implies smooth extension of biholomorphisms (Bell 1981). The worm therefore removes the only general tool for boundary regularity of mappings.

## 3. History & State of the Art (SOTA)

- **1977.** Diederich and Fornæss construct $\Omega_\beta$ to exhibit a smooth bounded pseudoconvex domain with nontrivial Nebenhülle (no Stein neighbourhood basis).
- **1984.** Barrett shows the worm's boundary annulus obstructs the existence of a plurisubharmonic defining function, and that $\Omega_\beta$ fails the Bell–Ligocka machinery.
- **1991.** Kiselman analyses the Bergman projection on Hartogs domains modelled on the worm and finds smoothness is not preserved for the non-smooth model.
- **1992.** **Barrett (Acta Math.)**: for the model worm $D'_\beta$, $P$ does not map $W^s\to W^s$ once $s\ge \pi/(2\beta-\pi)$. Sharp, and the first quantitative irregularity result.
- **1996.** **Christ (JAMS)**: the *smooth* worm $\Omega_\beta$ fails Condition R — $N$ and $P$ do not preserve $C^\infty(\overline\Omega)$. Proof uses a microlocal/Fourier-integral analysis of the winding together with a Mergelyan-type approximation and a contradiction with hypoellipticity.
- **2008.** Krantz–Peloso compute the Bergman kernel of $D'_\beta$ by Fourier decomposition, obtain its boundary asymptotics, and derive positive $W^s$ and $L^p$ estimates in explicit ranges.
- **2012.** Barrett–Şahutoğlu extend irregularity to worm-like domains in $\mathbb{C}^n$, $n\ge 2$.
- **2016.** Krantz–Peloso–Stoppato treat the unbounded worm $D_\infty$ and obtain an explicit kernel/projection description.
- **2019.** B. Liu computes the Diederich–Fornæss index of the worm exactly, tying the geometric invariant to the winding angle.

**SOTA summary.** Sharp thresholds are known only for the *non-smooth* model $D'_\beta$; on the smooth worm only qualitative failure ($C^\infty$) is known, with no matching positive Sobolev range.

## 4. Partial Results / Verified Cases

| Domain | Result | Source |
|---|---|---|
| Model worm $D'_\beta$, $\beta>\pi/2$ | $P$ unbounded on $W^s$ for $s\ge \pi/(2\beta-\pi)$ | Barrett 1992 |
| Model worm $D'_\beta$ | $P$ bounded on $W^s$ for $0\le s<\pi/(2\beta-\pi)$; explicit kernel asymptotics | Krantz–Peloso 2008 |
| Model worm $D'_\beta$ | $P$ unbounded on $L^p$ for $p$ outside an explicit interval about $2$ contracting as $\beta\to\infty$ | Krantz–Peloso 2008 |
| Smooth worm $\Omega_\beta\subset\mathbb{C}^2$ | Condition R fails; $N$, $P$ do not preserve $C^\infty(\overline\Omega)$ | Christ 1996 |
| Worm-type domains in $\mathbb{C}^n$, $n\ge2$ | Irregularity of $P$ persists | Barrett–Şahutoğlu 2012 |
| $\eta(\Omega)=1$ (psh defining function on $b\Omega$) | $P$ bounded on $W^s$ for all $s\ge0$ — worms excluded | Boas–Straube 1991 |
| Any smooth bounded pseudoconvex $\Omega$ | $P$ bounded on $W^s$ for $0\le s<\eta(\Omega)/2$ (Sobolev gain from DF index) | Harrington-type estimates |
| Unbounded worm $D_\infty$ | Kernel and projection computed in closed Fourier form | Krantz–Peloso–Stoppato 2016 |
| $\beta\le\pi/2$ | No winding: domain is (biholomorphic to) a smoothly bounded strictly-pseudoconvex-like piece; $P$ fully regular | classical |

## 5. Principal Obstacles

- **Loss of the model's symmetry.** All sharp results exploit the $S^1$-action $z_2\mapsto e^{i\theta}z_2$ on $D'_\beta$, which diagonalises $P$ into a $\mathbb{Z}$-indexed family of one-variable weighted projections. The smooth worm $\Omega_\beta$ retains this symmetry but the smoothing cap $\phi$ destroys the exact solvability of each Fourier piece; no explicit kernel is known.
- **Non-elliptic, non-subelliptic regime.** $\bar\partial$-Neumann on $\Omega_\beta$ is not subelliptic (the boundary contains an analytic annulus, so finite type fails) and not even *globally regular*. Standard tools — pseudodifferential calculus with subelliptic multipliers, Kohn's ideal algorithm, Catlin's finite-type property (P) — all require conditions the worm violates by design.
- **Compactness fails.** $N$ is not compact on $\Omega_\beta$ (the annulus is an analytic disc family in the boundary), removing the compactness ⇒ global regularity route.
- **Vector-field method breaks at a computable angle.** Boas–Straube's global-regularity criterion needs a family of vector fields whose commutators with $\bar\partial$ are controlled; on the worm the obstruction is the *winding* of the normal bundle over the annulus, a topological monodromy $e^{i(2\beta-\pi)}$ that no choice of vector field can unwind once $2\beta-\pi>\pi$.
- **Upper bounds are qualitative.** Christ's proof is a contradiction argument: it shows $C^\infty$ regularity is impossible, but produces no quantitative Sobolev exponent, and does not yield the positive half of a sharp statement.
- **Interpolation is unavailable.** $W^s$-boundedness is not known to be an interval-in-$s$ property for $P$ on non-regular domains, so partial positive results at isolated $s$ do not propagate.

## 6. The Gap

Proven: (a) a sharp two-sided threshold $s_\beta = \pi/(2\beta-\pi)$ for the **non-smooth model** $D'_\beta$; (b) failure of $C^\infty$ regularity for the **smooth** worm $\Omega_\beta$.

Missing: any *positive* Sobolev estimate for $\Omega_\beta$ beyond the generic $s<\eta(\Omega_\beta)/2$ gain, and any *quantitative* irregularity exponent for $\Omega_\beta$. The exact step to cross is a transfer principle: show that the smoothing cap $\phi$ perturbs the $j$-th Fourier component's operator norm by a factor uniformly bounded in $j$, so that the model's threshold survives. Currently the cap changes the slice geometry from a disc of fixed radius to a shrinking family, and the $j$-uniformity of the resulting weighted projections is unproved. Equivalently: is
$$s^\ast_\beta = \frac{\pi}{2\beta-\pi}\quad\text{and is }s^\ast_\beta\text{ a function of }\eta(\Omega_\beta)\text{ alone?}$$

## 7. Current Research (as of June 2026)

- **Kernel asymptotics school (Krantz, Peloso, Stoppato; Washington Univ. St. Louis, Milano, Firenze).** Push the explicit Fourier–Bessel representation of $K_{D'_\beta}$ toward the capped domain; also the Müntz–Szász-type completeness questions for $A^2$ of the worm.
- **Diederich–Fornæss index programme (B. Liu, Harrington, Fornæss–Herbig).** Establish inequalities of the form $s^\ast(\Omega)\ge c\,\eta(\Omega)$ and, conversely, index-driven irregularity. Whether $\eta$ *determines* $s^\ast$ is the sharpest open sub-question. *(frontier — verify)*
- **$L^p$ theory (Zeytuncu, L. Chen, Şahutoğlu and collaborators).** Sharp $L^p$ intervals for worm and worm-like Hartogs domains; weighted-projection reductions. Reports of a sharp $L^p$ range for $D'_\beta$ matching the Sobolev threshold circulate as preprints. *(frontier — verify)*
- **Higher-dimensional and Levi-flat generalisations (Barrett, Şahutoğlu; Univ. of Michigan, Univ. of Toledo).** Worms built over Levi-flat hypersurfaces with prescribed monodromy, to see which winding invariants control regularity.
- **Consequences for mapping theory.** Whether biholomorphisms between smooth bounded pseudoconvex domains extend smoothly remains open; the worm is the canonical test case since Bell's route is blocked.

## 8. Future Work

- Prove a *quantitative* version of Christ's theorem: exhibit $f\in C^\infty(\overline{\Omega_\beta})$ with $P f\notin W^s$ for an explicit $s=s(\beta)$.
- Establish uniform-in-$j$ bounds for the Fourier-decomposed projections on the capped worm, the missing transfer step of §6.
- Test the conjecture $s^\ast=\pi/(2\beta-\pi)$ numerically by computing $\|P_j\|$ on truncated Fourier blocks for $\beta=\pi,\,3\pi/2,\,2\pi$.
- Decide whether the *weighted* Bergman projection with weight $(-\rho)^{a}$ regains full Sobolev regularity on the worm for $a$ large (Kohn's weighted estimates suggest yes; sharp $a=a(\beta)$ unknown).
- Determine whether $L^p$- and $W^s$-thresholds are related by the expected duality $\tfrac1p-\tfrac12 \leftrightarrow s$.

## 9. Key References

- **[Foundational]** K. Diederich, J. E. Fornæss. *Pseudoconvex domains: an example with nontrivial Nebenhülle.* Math. Ann. 225 (1977), 275–292.
- **[Foundational]** S. Bell. *Biholomorphic mappings and the $\bar\partial$-problem.* Ann. of Math. 114 (1981), 103–113.
- **[Foundational]** D. Barrett. *Behavior of the Bergman projection on the Diederich–Fornæss worm.* Acta Math. 168 (1992), 1–10.
- **[Foundational]** M. Christ. *Global $C^\infty$ irregularity of the $\bar\partial$-Neumann problem for worm domains.* J. Amer. Math. Soc. 9 (1996), 1171–1185.
- **[Foundational]** C. O. Kiselman. *A study of the Bergman projection in certain Hartogs domains.* Proc. Sympos. Pure Math. 52, Part 3, Amer. Math. Soc., 1991, 219–231.
- **[Structural]** H. Boas, E. Straube. *Equivalence of regularity for the Bergman projection and the $\bar\partial$-Neumann operator.* Manuscripta Math. 67 (1990), 25–33.
- **[Structural]** H. Boas, E. Straube. *Sobolev estimates for the $\bar\partial$-Neumann operator on domains in $\mathbb{C}^n$ admitting a defining function that is plurisubharmonic on the boundary.* Math. Z. 206 (1991), 81–88.
- **[SOTA / Recent]** S. G. Krantz, M. M. Peloso. *The Bergman kernel and projection on non-smooth worm domains.* Houston J. Math. 34 (2008), 873–950.
- **[SOTA / Recent]** S. G. Krantz, M. M. Peloso. *Analysis and geometry on worm domains.* J. Geom. Anal. 18 (2008), 478–510.
- **[SOTA / Recent]** D. Barrett, S. Şahutoğlu. *Irregularity of the Bergman projection on worm domains in $\mathbb{C}^n$.* Michigan Math. J. 61 (2012), 187–198.
- **[SOTA / Recent]** S. G. Krantz, M. M. Peloso, C. Stoppato. *Bergman kernel and projection on the unbounded Diederich–Fornæss worm domain.* Ann. Sc. Norm. Super. Pisa Cl. Sci. 16 (2016), 1153–1183.
- **[SOTA / Recent]** B. Liu. *The Diederich–Fornæss index I: for domains of non-trivial index.* Adv. Math. 353 (2019), 776–801.
- **[Survey]** E. J. Straube. *Lectures on the $L^2$-Sobolev Theory of the $\bar\partial$-Neumann Problem.* ESI Lectures in Mathematics and Physics, EMS, 2010.
- **[Related]** Y. E. Zeytuncu. *$L^p$ regularity of weighted Bergman projections.* Trans. Amer. Math. Soc. 365 (2013), 2959–2976.

## 10. Worked Example / Concrete Special Case

**Fourier decomposition of $A^2(D'_\beta)$.** Set $b=\beta-\pi/2>0$, so the total winding of the slice centres is $2b=2\beta-\pi$. The model worm is
$$D'_\beta=\{(z_1,z_2):\ |z_1-e^{it}|<1,\ t=\log|z_2|^2,\ |t|<b\}.$$

$D'_\beta$ is invariant under $z_2\mapsto e^{i\theta}z_2$ and omits $z_2=0$, so every $f\in A^2$ has a Laurent expansion $f(z_1,z_2)=\sum_{j\in\mathbb{Z}} f_j(z_1)z_2^{\,j}$, orthogonal in $L^2$.

**Norm computation.** Write $z_2=re^{i\varphi}$, $t=2\log r$, so $r\,dr=\tfrac12 e^{t}dt$ and $|z_2|^{2j}=e^{jt}$. Integrating in $z_2$ first:
$$\|f\|_{L^2(D'_\beta)}^2=\pi\sum_{j\in\mathbb{Z}}\int_{-b}^{b} e^{(j+1)t}\,\big\|f_j\big\|^2_{L^2(D(e^{it},1))}\,dt .$$
So $P$ splits as $P=\bigoplus_j P_j$, where $P_j$ is the orthogonal projection onto holomorphic $f_j$ in the weighted space with weight $e^{(j+1)t}$ over the **winding family of unit discs** $D(e^{it},1)$, $|t|<b$.

**Where the threshold comes from.** For $|j|$ large, $e^{(j+1)t}$ concentrates the mass at $t=\pm b$ (sign of $j+1$), i.e. on the discs $D(e^{\pm ib},1)$. The union $\bigcup_{|t|<b} D(e^{it},1)$ covers the origin with multiplicity governed by the angle $2b$: if $2b\le\pi$, no two extreme discs overlap in a way that forces a phase mismatch, and $P$ is fully regular. If $2b>\pi$, extremal Bergman-type functions on $D(e^{it},1)$ pick up the phase factor $e^{i j t}$ and cannot be matched consistently across the whole winding; the resulting $P_j$ have operator norms on the $|j|^{s}$-weighted (Sobolev) scale growing like
$$\|P_j\|_{W^s}\ \asymp\ |j|^{\,s-\pi/(2b)}\quad(|j|\to\infty).$$
Summability over $j$ therefore holds exactly when $s<\pi/(2b)=\pi/(2\beta-\pi)$ — Barrett's exponent — and fails at and above it.

**Numerical instance.** Take $\beta=\pi$, so $b=\pi/2$ and total winding $2b=\pi$: threshold $s_\pi=\pi/(2\pi-\pi)=1$. Then $P_{D'_\pi}$ is bounded on $W^s$ for $s<1$ and unbounded on $W^1$. For $\beta=3\pi/2$: $s=\pi/(3\pi-\pi)=1/2$. Letting $\beta\to\infty$ drives $s^\ast_\beta\to0$: arbitrarily little Sobolev regularity survives. On the *smooth* worm $\Omega_\beta$ the same decomposition exists, but the cap $\phi$ replaces $D(e^{it},1)$ by $D(e^{it},\sqrt{1-\phi(t)})$, and the uniform asymptotics of $\|P_j\|$ in $j$ are exactly what nobody has proved.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*