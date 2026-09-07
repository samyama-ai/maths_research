---
id: 04-topology/chromatic-convergence-theorem
title: "Chromatic Convergence Theorem"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chromatic Convergence Theorem

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/chromatic-convergence-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Fix a prime $p$ and work in the $p$-local stable homotopy category. Let $E(n)$ be the $n$-th Johnson–Wilson theory and $L_n = L_{E(n)}$ the associated Bousfield localization. The localizations assemble into the **chromatic tower**

$$X \longrightarrow \cdots \longrightarrow L_n X \longrightarrow L_{n-1} X \longrightarrow \cdots \longrightarrow L_1 X \longrightarrow L_0 X .$$

**Chromatic Convergence Theorem (Hopkins–Ravenel, 1992).** If $X$ is a $p$-local *finite* spectrum, the canonical map

$$X \;\xrightarrow{\ \simeq\ }\; \operatorname*{holim}_{n} L_n X$$

is an equivalence.

Ravenel stated this as a conjecture in 1984; Hopkins and Ravenel proved it, and the proof appears as Theorem 7.5.7 of Ravenel's *Nilpotence and Periodicity*. The statement is sharp in a strong sense: finiteness cannot be dropped. The page is catalogued as `solved-recently` because the core theorem is settled while its natural extensions — which classes of infinite spectra converge, the rate of convergence, and the motivic/equivariant/$K(n)$-local analogues — remain open, and the 2023 disproof of the telescope conjecture reopened the surrounding picture.

A complete resolution of the *remaining* problem means: characterize the full subcategory of $p$-local spectra $X$ for which $X \to \operatorname{holim}_n L_n X$ is an equivalence.

## 2. Mathematical Foundations

**Brown–Peterson theory.** $BP$ is the $p$-local summand of complex cobordism with
$$\pi_* BP = \mathbb{Z}_{(p)}[v_1, v_2, \dots], \qquad |v_i| = 2(p^i - 1).$$

**Johnson–Wilson theory.** $E(n)$ is the Landweber-exact $BP$-algebra with
$$\pi_* E(n) = \mathbb{Z}_{(p)}[v_1,\dots,v_{n-1}, v_n^{\pm 1}], \qquad E(0) = H\mathbb{Q}.$$

**Morava $K$-theory.** $K(n)$ has $\pi_* K(n) = \mathbb{F}_p[v_n^{\pm 1}]$, with $K(0) = H\mathbb{Q}$ and $K(\infty) = H\mathbb{F}_p$. Bousfield classes satisfy
$$\langle E(n)\rangle = \bigvee_{i=0}^{n} \langle K(i)\rangle .$$

**Bousfield localization.** $L_E X$ is terminal among $E_*$-equivalences out of $X$; $L_E X$ is $E$-local, i.e. $[W, L_E X] = 0$ whenever $E_* W = 0$.

**Type and periodicity.** A finite $p$-local spectrum $X$ has *type* $n$ if $K(i)_* X = 0$ for $i < n$ and $K(n)_* X \neq 0$. By Hopkins–Smith, such $X$ admits a $v_n$-self map
$$v \colon \Sigma^{d} X \to X, \qquad K(n)_*(v) = v_n^{k}\ \text{(iso)},\quad K(i)_*(v)=0 \ (i \neq n).$$

**Smash product theorem** (Ravenel, Thm. 7.5.6): $L_n$ is *smashing*,
$$L_n X \simeq X \wedge L_n S^0 \quad\text{for all }X.$$

**Chromatic fracture square.** For every $X$ there is a homotopy pullback
$$\begin{array}{ccc} L_n X & \longrightarrow & L_{K(n)} X \\ \downarrow & & \downarrow \\ L_{n-1} X & \longrightarrow & L_{n-1} L_{K(n)} X \end{array}$$
so the tower is built from $K(n)$-local pieces, the "monochromatic layers" $M_n X = \operatorname{fib}(L_n X \to L_{n-1}X)$.

**Milnor sequence.** Convergence yields, for each $k$,
$$0 \to {\textstyle\lim^1_n}\, \pi_{k+1} L_n X \to \pi_k X \to \lim_n \pi_k L_n X \to 0 .$$

**Harmonic / dissonant.** $X$ is *harmonic* if it is local with respect to $\bigvee_{n \ge 0} K(n)$, and *dissonant* if $K(n)_* X = 0$ for all $n$. Dissonant spectra have trivial chromatic tower.

## 3. History & State of the Art (SOTA)

- **1970s.** Quillen's identification of $MU_*$ with the Lazard ring, and Morava's stratification of the moduli of formal groups by height, produce the "chromatic" organizing principle. Johnson–Wilson (1975) construct $E(n)$.
- **1979.** Bousfield's localization machinery (*Topology* 18) makes $L_n$ available.
- **1984.** Ravenel, *Localization with respect to certain periodic homology theories* (Amer. J. Math. 106), states the chromatic convergence conjecture along with the telescope, smashing and nilpotence conjectures, and computes $\pi_* L_1 S^0$.
- **1988.** Devinatz–Hopkins–Smith prove the nilpotence theorem ($MU$ detects nilpotence).
- **1992.** Hopkins–Ravenel prove the smash product theorem, and from it chromatic convergence for finite $p$-local spectra (Ravenel, *Nilpotence and Periodicity*, Thm. 7.5.7). In the same year Hopkins–Ravenel prove *suspension spectra are harmonic*, extending the reach of the tower beyond finite complexes.
- **1998.** Hopkins–Smith classify thick subcategories, giving the type-$n$ filtration used throughout.
- **1999.** Hovey–Strickland's memoir systematizes the $K(n)$-local category; Hovey formulates the (still open) chromatic splitting conjecture governing how $L_n S^0$ is reassembled from layers.
- **2016.** Barthel isolates *chromatic completion* $X \to \operatorname{holim}_n L_n X$ as a functor and gives non-convergence examples among infinite spectra.
- **2023.** Burklund–Hahn–Levy–Schlank disprove the telescope conjecture ($L_n^f \neq L_n$ for $n \ge 2$), separating the finite-localization tower $\{L_n^f X\}$ from $\{L_n X\}$. Chromatic convergence for the *telescopic* tower becomes a genuinely distinct question.

## 4. Partial Results / Verified Cases

- **Finite $p$-local spectra, all $n$, all $p$:** theorem, unconditional (Hopkins–Ravenel 1992). Includes $S^0_{(p)}$, Moore spectra $S/p^k$, $S/(p, v_1^j)$, and all type-$n$ finite complexes.
- **$n = 0$:** trivial; $L_0 X = X_{\mathbb{Q}}$.
- **$n = 1$:** accessible by hand. $\pi_* L_1 S^0$ is completely known (Ravenel 1984; Mahowald at $p=2$ via the image-of-$J$ spectrum), and convergence of the two-stage tower $L_1 \to L_0$ can be checked directly against $\pi_*S^0$ in low stems.
- **$n = 2$:** $\pi_* L_2 S^0$ computed at $p \ge 5$ (Shimomura–Yabe) and largely at $p = 3$ (Shimomura–Wang); consistent with convergence.
- **Suspension spectra:** $\Sigma^\infty Y$ is harmonic for any space $Y$ (Hopkins–Ravenel 1992) — a necessary condition for convergence, though not sufficient.
- **Failure cases (sharpness):** $H\mathbb{F}_p$ is dissonant, $L_n H\mathbb{F}_p = 0$ for all $n \ge 0$, so $\operatorname{holim}_n L_n H\mathbb{F}_p = 0 \neq H\mathbb{F}_p$. Infinite wedges/colimits of finite spectra of unbounded type also fail: convergence is not preserved under arbitrary homotopy colimits (Barthel 2016).

## 5. Principal Obstacles

The obstacles now sit in the *extensions*, not the finite case.

- **No structural criterion for convergence.** Harmonicity is necessary but demonstrably not sufficient; there is no known intrinsic homological characterization of chromatically complete spectra. The class is not closed under colimits, so it is not the local objects of any obvious localization.
- **$\lim^1$ is uncontrolled.** For non-finite $X$ the derived limit of $\{\pi_* L_n X\}$ can be huge and is not computed by any spectral sequence with a vanishing line; the Milnor sequence gives no leverage.
- **The smash product theorem is the whole engine.** Ravenel's proof of convergence uses $L_n X \simeq X \wedge L_n S^0$ plus a vanishing-line estimate in the localized Adams–Novikov $E_2$-term, itself resting on Landweber exactness of $E(n)$. In motivic, equivariant, or $\mathbb{Z}$-graded-ring settings there is often no Landweber-exact $E(n)$ and no proof that $L_n$ is smashing, so the argument does not transport.
- **Telescopic tower is now different.** With $L_n^f \neq L_n$ for $n \ge 2$ (Burklund–Hahn–Levy–Schlank 2023), $X \to \operatorname{holim}_n L_n^f X$ is a separate assertion; the $T(n)$-local layers are not understood well enough to run the same vanishing-line argument.
- **Quantitative failure.** No effective bound is known for how large $n$ must be, as a function of the stem $k$, for $\pi_k X \to \pi_k L_n X$ to be injective or surjective. The proof is a limit statement with no rate.

## 6. The Gap

Proven: $X$ finite $p$-local $\Rightarrow$ $X \simeq \operatorname{holim}_n L_n X$. Known false: $X = H\mathbb{F}_p$ and various infinite complexes.

The gap is the region between. Precisely, the missing step is a criterion $C$ on a $p$-local spectrum $X$ such that

$$C(X) \iff \bigl(X \to \operatorname{holim}_n L_n X\ \text{is an equivalence}\bigr),$$

together with a proof that $C$ holds for the natural test classes: $\Sigma^\infty Y$ for $Y$ a finite-dimensional space, $K(R)$ for a nice ring spectrum $R$, and $\operatorname{holim}$-type objects such as $BP$ and $ko$. Secondarily: replace $L_n$ by $L_n^f$ and decide the same statement. Bridging requires either a smash-product-type theorem valid beyond finite objects, or a genuinely new handle on $\lim^1$ across monochromatic layers.

## 7. Current Research (as of June 2026)

- **Post-telescope program.** Burklund, Hahn, Levy and Schlank's counterexamples (via algebraic $K$-theory of Lubin–Tate-type inputs and redshift) have made $T(n)$-local homotopy the active frontier; the status of convergence for the telescopic tower is open. *(frontier — verify)*
- **Chromatic Nullstellensatz.** Burklund–Schlank–Yuan give a "Nullstellensatz" for $\mathbb{E}_\infty$-rings, showing Lubin–Tate theories are algebraically closed points of $K(n)$-local ring spectra; being exploited to detect chromatic completeness of ring spectra. Groups at Copenhagen, Jerusalem, Harvard, MIT, Bonn (MPIM).
- **Chromatic splitting.** Hovey's conjecture governs the fracture squares assembling $\operatorname{holim}_n L_n S^0$; Beaudry's work at $n=2$, $p=2$ shows the strong form fails, refining what a convergence proof can assume. *(frontier — verify)*
- **Equivariant and motivic analogues.** Balmer-spectrum computations for compact Lie groups (Barthel–Greenlees–Hausmann and successors) and $\mathbb{C}$-/$\mathbb{R}$-motivic chromatic towers are the main testing grounds for a Landweber-free proof. *(frontier — verify)*
- **Ambidexterity and higher semiadditivity** (Hopkins–Lurie; Carmeli–Schlank–Yanovski) supply new structural tools for $K(n)$-local categories that may control the inverse limit directly.

## 8. Future Work

1. Find a criterion for chromatic completeness stable under the operations of interest, or prove no reasonable one exists.
2. Decide $X \simeq \operatorname{holim}_n L_n^f X$ for finite $X$ in light of the telescope disproof.
3. Extract an effective rate: bound $n(k)$ such that $\pi_k S^0 \to \pi_k L_{n} S^0$ is injective for $n \ge n(k)$.
4. Prove or disprove convergence for $K(R)$ with $R$ a chromatically complete ring — the redshift-side question.
5. Establish a smashing theorem in the $C_2$-equivariant and $\mathbb{C}$-motivic settings, which would transport the Hopkins–Ravenel argument verbatim.

## 9. Key References

- **[Foundational]** D. C. Ravenel. *Localization with respect to certain periodic homology theories.* American Journal of Mathematics 106 (1984), 351–414.
- **[Foundational]** A. K. Bousfield. *The localization of spectra with respect to homology.* Topology 18 (1979), 257–281.
- **[Foundational]** D. C. Johnson, W. S. Wilson. *BP operations and Morava's extraordinary K-theories.* Mathematische Zeitschrift 144 (1975), 55–75.
- **[Proof]** D. C. Ravenel. *Nilpotence and Periodicity in Stable Homotopy Theory.* Annals of Mathematics Studies 128, Princeton University Press, 1992. (Chromatic convergence: Theorem 7.5.7; smash product theorem: Theorem 7.5.6.)
- **[Foundational]** E. S. Devinatz, M. J. Hopkins, J. H. Smith. *Nilpotence and stable homotopy theory I.* Annals of Mathematics 128 (1988), 207–241.
- **[Foundational]** M. J. Hopkins, J. H. Smith. *Nilpotence and stable homotopy theory II.* Annals of Mathematics 148 (1998), 1–49.
- **[Related]** M. J. Hopkins, D. C. Ravenel. *Suspension spectra are harmonic.* Boletín de la Sociedad Matemática Mexicana (2) 37 (1992), 271–279.
- **[Structural]** M. Hovey, N. P. Strickland. *Morava K-theories and localisation.* Memoirs of the American Mathematical Society 139, no. 666, 1999.
- **[SOTA]** T. Barthel. *Chromatic completion.* Proceedings of the American Mathematical Society 144 (2016), 2263–2274.
- **[SOTA / Recent]** R. Burklund, J. Hahn, I. Levy, T. M. Schlank. *K-theoretic counterexamples to Ravenel's telescope conjecture.* arXiv:2310.17459, 2023.
- **[SOTA / Recent]** R. Burklund, T. M. Schlank, A. Yuan. *The chromatic Nullstellensatz.* arXiv:2207.09929, 2022.
- **[Survey]** T. Barthel, A. Beaudry. *Chromatic structures in stable homotopy theory.* In *Handbook of Homotopy Theory* (H. Miller, ed.), CRC Press, 2020.

## 10. Worked Example / Concrete Special Case

Take $X = S^0_{(p)}$ with $p$ odd, and truncate the tower at $n = 1$. Write $q = 2p-2$.

**Step 1 — the bottom two stages.** $L_0 S^0 = S^0_{\mathbb{Q}} = H\mathbb{Q}$, so $\pi_* L_0 S^0 = \mathbb{Q}$ concentrated in degree $0$. Ravenel (1984) computed
$$\pi_i L_1 S^0 = \begin{cases} \mathbb{Z}_{(p)} & i = 0,\\[2pt] \mathbb{Q}_p/\mathbb{Z}_{(p)} & i = -2,\\[2pt] \mathbb{Z}/p^{\,\nu_p(j)+1} & i = qj - 1,\ j \neq 0,\\[2pt] 0 & \text{otherwise,}\end{cases}$$
where $\nu_p$ is the $p$-adic valuation. Concretely $L_1 S^0$ is the fiber of $\psi^g - 1$ on the $p$-completed Adams summand, glued to $H\mathbb{Q}$ along the fracture square of Section 2.

**Step 2 — comparison with $\pi_* S^0$.** In stem $i = q - 1 = 2p-3$ the formula gives $\mathbb{Z}/p$, generated by the image of $\alpha_1 \in \pi_{2p-3} S^0$. So
$$\pi_{2p-3} S^0_{(p)} \supseteq \mathbb{Z}/p \xrightarrow{\ \cong\ } \pi_{2p-3} L_1 S^0 .$$
At $p = 5$: $\pi_7 S^0_{(5)} = \mathbb{Z}/5\{\alpha_1\}$ and $\pi_7 L_1 S^0 = \mathbb{Z}/5$ — the tower already sees all of it at height $1$. The class $\beta_1 \in \pi_{2(p^2-1)(p-1)-2}S^0$ ($\pi_{38}$ at $p=5$) is $v_2$-periodic: it dies in $L_1 S^0$ and is first detected at $n = 2$. This is exactly the mechanism convergence formalizes — each element of $\pi_* S^0$ appears at some finite height.

**Step 3 — the limit.** Convergence says $S^0_{(p)} \simeq \operatorname{holim}_n L_n S^0$, hence
$$0 \to {\textstyle\lim^1_n}\, \pi_{k+1} L_n S^0 \to \pi_k S^0_{(p)} \to \lim_n \pi_k L_n S^0 \to 0 .$$
Since $\pi_k S^0_{(p)}$ is finite for $k > 0$ and each $\pi_k L_n S^0 \to \pi_k L_{n-1} S^0$ is eventually an isomorphism in a fixed stem, the $\lim^1$ term vanishes and $\pi_k S^0_{(p)} \cong \lim_n \pi_k L_n S^0$.

**Step 4 — sharpness.** Replace $S^0$ by $H\mathbb{F}_p$. Then $K(n)_* H\mathbb{F}_p = 0$ for all $n \ge 0$, so every $L_n H\mathbb{F}_p = 0$ and $\operatorname{holim}_n L_n H\mathbb{F}_p = 0$, while $H\mathbb{F}_p \neq 0$. Finiteness in Section 1 is not a convenience of the proof — it is necessary.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*