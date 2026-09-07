---
id: 09-probability/boolean-satisfiability-phase-transition
title: "Boolean Satisfiability Phase Transition"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boolean Satisfiability Phase Transition

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/boolean-satisfiability-phase-transition` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fix $k \ge 2$ and let $\Phi_k(n,m)$ be a random $k$-CNF formula on $n$ Boolean variables obtained by drawing $m$ clauses independently and uniformly from the $2^k\binom{n}{k}$ possible $k$-clauses. Write $m = \lfloor rn \rfloor$, where $r$ is the **clause density**.

**Satisfiability Threshold Conjecture.** For every $k \ge 2$ there is a constant $r_k \in (0,\infty)$ such that for all $\varepsilon > 0$,
$$
\lim_{n\to\infty}\Pr\bigl[\Phi_k(n,\lfloor rn\rfloor)\ \text{is satisfiable}\bigr]=
\begin{cases}
1, & r < r_k - \varepsilon,\\[2pt]
0, & r > r_k + \varepsilon .
\end{cases}
$$

A complete resolution requires: (i) existence of the limit for each fixed $k$; (ii) identification of $r_k$ with the value predicted by the one-step replica-symmetry-breaking (1RSB) cavity method; and (iii) description of the **scaling window** — the width $\delta(n)$ over which the probability drops from $1-\varepsilon$ to $\varepsilon$ — together with the critical exponents.

The case $k=3$ is the emblematic open instance: numerically $r_3 \approx 4.26675$, but existence of $r_3$ is not proved.

## 2. Mathematical Foundations

**Probability space.** $\Phi \sim \Phi_k(n,m)$, clauses $C_1,\dots,C_m$ i.i.d. uniform. Let
$$
Z(\Phi) \;=\; \bigl|\{\sigma \in \{0,1\}^n : \sigma \models \Phi\}\bigr|
$$
be the number of satisfying assignments. Satisfiability is the event $\{Z \ge 1\}$.

**First moment.** A fixed $\sigma$ satisfies a uniform random clause with probability $1-2^{-k}$, so
$$
\mathbb{E}[Z] \;=\; 2^n\bigl(1-2^{-k}\bigr)^{m}\;=\;\exp\Bigl\{n\bigl(\ln 2 + r\ln(1-2^{-k})\bigr)+o(n)\Bigr\}.
$$
Markov's inequality gives the **first-moment upper bound**
$$
r_k \;\le\; r_k^{\mathrm{fm}} := -\frac{\ln 2}{\ln(1-2^{-k})} \;=\; 2^k\ln 2 - \tfrac{\ln 2}{2} + O(2^{-k}).
$$

**Second moment.** With $\mathbb{E}[Z^2] = 2^n\sum_{z} \binom{n}{zn}\bigl(1 - 2^{1-k} + 2^{-k}\,\alpha(z)\bigr)^m$ where $\alpha(z)=z^k+(1-z)^k$ and $zn$ is the overlap, Laplace analysis of $\phi(z)$ yields lower bounds; the plain second moment fails because $\phi$ is maximized off the symmetric point $z=1/2$. Achlioptas–Moore's NAE-SAT trick and Achlioptas–Peres's weighted moment $Z_\lambda=\sum_\sigma \prod_{i}\lambda^{\,\\#\text{true literals in }C_i}$ repair this.

**Sharpness (Friedgut).** Satisfiability is a monotone decreasing property invariant under a transitive symmetry group. Friedgut's sharp-threshold criterion gives a sequence $r_k(n)$ with
$$
\Pr[\Phi_k(n,\lfloor (1\pm\varepsilon) r_k(n)\, n\rfloor)\ \text{sat}] \to 1 \text{ resp. } 0 ,
$$
i.e. the threshold is *sharp* but not known to *converge*.

**1RSB prediction.** The cavity method models the solution space as a union of clusters; the Survey Propagation / Belief Propagation fixed point is a distribution $Q$ over cavity fields $\eta\in[0,1]$ satisfying a recursive distributional equation. The **complexity** $\Sigma(r)$ (exponential growth rate of the number of clusters) is given by a Bethe free-entropy functional $\mathcal{F}[Q]$; the predicted threshold is
$$
r_k \;=\; \sup\{r : \Sigma(r) > 0\},
$$
with intermediate transitions at the clustering (dynamical) density $r_{\mathrm d}(k)$ and the condensation density $r_{\mathrm c}(k)$, so that $r_{\mathrm d} < r_{\mathrm c} < r_k$.

## 3. History & State of the Art (SOTA)

- **1992.** Cheeseman, Kanefsky and Taylor observe experimentally that hard instances concentrate at a critical clause density; Mitchell, Selman and Levesque report the "easy–hard–easy" pattern for random 3-SAT near $r\approx 4.3$.
- **1992–96.** $k=2$ resolved: Chvátal–Reed, Goerdt, and Fernandez de la Vega prove $r_2 = 1$.
- **1994.** Chvátal–Reed also prove $r_k = \Theta(2^k)$: satisfiable for $r \le c\,2^k/k$, unsatisfiable for $r \ge 2^k\ln 2$.
- **1999.** Friedgut proves the threshold is sharp for every $k$ (up to the non-convergence caveat).
- **1999–2002.** Physics: Monasson–Zecchina replica computation; Mézard–Parisi–Zecchina's 1RSB solution gives $r_3 = 4.267$ and the Survey Propagation algorithm solving $n=10^6$ instances at $r=4.25$.
- **2001–2004.** Rigorous second-moment work: Achlioptas–Moore ($r_k \ge 2^k\ln 2 - O(k)$ via NAE-SAT), Achlioptas–Peres ($r_k \ge 2^k \ln 2 - \tfrac{k+1}{2}\ln 2 - 1 - o_k(1)$).
- **2011–2016.** Coja-Oghlan–Panagiotou pin the asymptotics: $r_k = 2^k\ln 2 - \tfrac{1+\ln 2}{2} + o_k(1)$.
- **2015/2022.** **Ding–Sly–Sun** prove the Satisfiability Conjecture for all $k \ge k_0$: the limit exists and equals the 1RSB prediction.

Current numeric bracket for $k=3$: $3.52 \le \liminf r_3(n)$ (Kaporis–Kirousis–Lalas; Hajiaghayi–Sorkin) and $\limsup r_3(n) \le 4.4898$ (Díaz–Kirousis–Mitsche–Pérez-Giménez), against the conjectured $4.26675$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $k=2$ | $r_2 = 1$ exactly; scaling window $m = n + \Theta(n^{2/3})$ | Chvátal–Reed 1992; Goerdt 1996; Bollobás–Borgs–Chayes–Kim–Wilson 2001 |
| $k \ge k_0$ (large, non-explicit) | Full conjecture: limit exists, equals 1RSB value | Ding–Sly–Sun 2015/2022 |
| All $k$ | Sharpness of the (possibly $n$-dependent) threshold | Friedgut 1999 |
| All $k$ | $2^k\ln2 - \tfrac{k+1}{2}\ln2 - 1 \le r_k \le 2^k\ln 2 - \tfrac{\ln 2}{2}$ | Achlioptas–Peres 2004 |
| $k \to \infty$ | $r_k = 2^k\ln 2 - \tfrac{1+\ln 2}{2}+o_k(1)$ | Coja-Oghlan–Panagiotou 2016 |
| Clustering, large $k$ | $r_{\mathrm d}(k) = \tfrac{2^k}{k}(\ln k + O(1))$ | Achlioptas–Coja-Oghlan 2008 |
| Condensation, large $k$ | $r_{\mathrm c}(k)$ identified to $o_k(1)$ | Coja-Oghlan–Panagiotou 2016; Bapst et al. 2016 |
| Regular NAE-SAT | Exact threshold and cluster free energy | Ding–Sly–Sun 2016 |
| $k=3$ | $3.52 \le r_3 \le 4.4898$ | Kaporis et al. 2006; Díaz et al. 2009 |
| $k=4$ | $\approx 7.91 \le r_4 \le 10.22$ (predicted $9.93$) | Kaporis et al.; Dubois–Boufkhad–Mandler |

## 5. Principal Obstacles

- **Non-convergence gap in Friedgut's theorem.** Sharpness gives a threshold *sequence* $r_k(n)$; ruling out oscillation requires a monotonicity or interpolation argument. Sub-additivity via Guerra–Toninelli interpolation works for the free energy of *soft* models but the hard constraint $Z \ge 1$ is not an average of a smooth Hamiltonian, so the standard super-additivity route does not close.
- **Second-moment breakdown.** For $k = 3$ the overlap functional $\phi(z)$ has its maximum at $z \ne 1/2$ throughout most of the satisfiable regime, so $\mathbb{E}[Z^2]/\mathbb{E}[Z]^2$ is exponentially large. Weighting ($Z_\lambda$) fixes this only for $k \ge 4$ (Achlioptas–Peres); at $k=3$ no admissible weighting is known.
- **Condensation.** Above $r_{\mathrm c}$ the solution measure is dominated by $O(1)$ clusters of comparable weight, so $Z$ is not concentrated: $\ln Z$ has non-vanishing fluctuations and second-moment methods are structurally inapplicable in $[r_{\mathrm c}, r_k]$ — precisely where the threshold sits.
- **Small $k$ has no expansion parameter.** All rigorous 1RSB verifications use $2^{-k}$ as a small parameter to control the distributional recursion; at $k=3$ the corrections are $O(1)$ and the fixed-point equation must be handled exactly, which no rigorous method does.
- **Algorithmic barrier.** Every known polynomial algorithm stalls at $O(2^k \ln k / k)$, a factor $\Theta(k/\ln k)$ below $r_k$; overlap-gap-property arguments (Gamarnik–Sudan) show local/stable algorithms provably cannot cross, so algorithmic certificates cannot supply lower bounds near $r_k$.

## 6. The Gap

Three separated statements remain:

1. **Existence for small $k$.** For $3 \le k < k_0$, prove $\lim_n r_k(n)$ exists. This is the missing convergence step in Friedgut's theorem — an interpolation/sub-additivity inequality for $\Pr[\text{SAT}]$ or for $\frac1n\mathbb{E}\ln(Z+1)$.
2. **Effective $k_0$.** Ding–Sly–Sun's $k_0$ is not explicit and the arguments are asymptotic in $2^{-k}$; bringing $k_0$ down to $3$ requires replacing asymptotic contraction estimates with exact control of the 1RSB recursion.
3. **Identification at $k=3$.** Even granting existence, showing $r_3$ equals the numerical Bethe value $4.26675\ldots$ needs a rigorous evaluation of the complexity functional $\Sigma(r)$ and a proof that the 1RSB ansatz (rather than full RSB) is exact for $k$-SAT at $k=3$.

## 7. Current Research (as of June 2026)

- **Cluster-based moment methods.** Extensions of the Ding–Sly–Sun "one-step replica-symmetry-breaking moment" technique to smaller $k$ and to regular/planted ensembles, with groups at Stanford (Sly), Princeton, MIT and Berkeley. *(frontier — verify)* Reports of improved explicit bounds on $k_0$ remain unconfirmed in refereed form.
- **Coja-Oghlan school (Frankfurt/TU Dortmund).** Rigorous "Belief Propagation guided decimation" analyses, condensation phase transitions, and the general theory of the Bethe prediction via the *Nishimori identity* and *contiguity* arguments.
- **Interpolation and Gaussian comparison.** Attempts to extract sub-additivity from Panchenko-type ultrametricity results for diluted models; the Panchenko–Talagrand framework confirms 1RSB structure for some diluted spin glasses but not for hard constraints.
- **Overlap gap property (Gamarnik and coauthors).** Sharp algorithmic-hardness lower bounds in $[c 2^k\ln k/k,\ r_k]$; this now anchors the "statistical–computational gap" narrative for random CSPs.
- **Numerics.** Population-dynamics estimates of $r_3$ stable at $4.26675 \pm 10^{-5}$ (Mertens–Mézard–Zecchina); finite-size scaling exponent $\nu \approx 1.5$ measured, unproved.

## 8. Future Work

- Prove an **interpolation inequality** making $n\mapsto \mathbb{E}\ln(Z(\Phi_k(n,\lfloor rn\rfloor))+1)$ super-additive, which would immediately give convergence of $r_k(n)$ for all $k$.
- Devise a weighting scheme $Z_w$ for $k=3$ whose second moment is tight at $r$ close to $4.267$, or replace the moment method by a **spatial-coupling** argument transferring the (provable) coupled-ensemble threshold to the uncoupled one.
- Establish rigorously the full **phase diagram** for $k=3$: $r_{\mathrm d}(3)\approx 3.86$, $r_{\mathrm c}(3)\approx 4.267$ (these nearly coincide, unlike large $k$), and the associated freezing transition.
- Determine the **scaling window** for $k \ge 3$: is $r_k(n) - r_k = \Theta(n^{-1/\nu})$ with $\nu = 3/2$? For $k=2$ the window is $\Theta(n^{-1/3})$, proved.
- Extend results to related CSPs (random graph $q$-colouring, hypergraph 2-colouring, XORSAT — where the threshold is known exactly by linear algebra) to test the universality of the 1RSB picture.

## 9. Key References

- **[Foundational]** V. Chvátal and B. Reed. *Mick gets some (the odds are on his side).* Proc. 33rd IEEE FOCS, 1992, pp. 620–627.
- **[Foundational]** E. Friedgut (with an appendix by J. Bourgain). *Sharp thresholds of graph properties, and the $k$-SAT problem.* Journal of the American Mathematical Society 12(4), 1999, 1017–1054.
- **[Foundational]** D. Mitchell, B. Selman, H. Levesque. *Hard and easy distributions of SAT problems.* Proc. AAAI-92, 1992, 459–465.
- **[Foundational]** M. Mézard, G. Parisi, R. Zecchina. *Analytic and algorithmic solution of random satisfiability problems.* Science 297(5582), 2002, 812–815.
- **[SOTA / Recent]** J. Ding, A. Sly, N. Sun. *Proof of the satisfiability conjecture for large $k$.* Proc. 47th ACM STOC, 2015, 59–68; Annals of Mathematics 196(1), 2022, 1–388.
- **[SOTA / Recent]** A. Coja-Oghlan and K. Panagiotou. *The asymptotic $k$-SAT threshold.* Advances in Mathematics 288, 2016, 985–1068.
- **[SOTA / Recent]** D. Achlioptas and Y. Peres. *The threshold for random $k$-SAT is $2^k\log 2 - O(k)$.* Journal of the AMS 17(4), 2004, 947–973.
- **[SOTA / Recent]** D. Achlioptas and A. Coja-Oghlan. *Algorithmic barriers from phase transitions.* Proc. 49th IEEE FOCS, 2008, 793–802.
- **[SOTA / Recent]** J. Díaz, L. Kirousis, D. Mitsche, X. Pérez-Giménez. *On the satisfiability threshold of formulas with three literals per clause.* Theoretical Computer Science 410(30–32), 2009, 2920–2934.
- **[SOTA / Recent]** B. Bollobás, C. Borgs, J. T. Chayes, J. H. Kim, D. B. Wilson. *The scaling window of the 2-SAT transition.* Random Structures & Algorithms 18(3), 2001, 201–256.
- **[SOTA / Recent]** D. Gamarnik and M. Sudan. *Limits of local algorithms over sparse random graphs.* Annals of Probability 45(4), 2017, 2353–2376.
- **[Survey]** M. Mézard and A. Montanari. *Information, Physics, and Computation.* Oxford University Press, 2009.
- **[Survey]** A. Coja-Oghlan. *Phase transitions in discrete structures.* Proc. 7th European Congress of Mathematics, EMS Press, 2018.
- **[Survey]** S. Mertens, M. Mézard, R. Zecchina. *Threshold values of random K-SAT from the cavity method.* Random Structures & Algorithms 28(3), 2006, 340–373.

## 10. Worked Example / Concrete Special Case

**(a) The first-moment upper bound for $k = 3$, computed.**

Each clause forbids exactly one of the $2^3 = 8$ truth patterns on its three variables, so $\Pr[\sigma \models C] = 7/8$ for any fixed $\sigma$. With $m = rn$ clauses drawn independently,
$$
\mathbb{E}[Z] = 2^n \left(\tfrac78\right)^{rn} = \exp\bigl\{ n\left(\ln 2 + r\ln\tfrac78\right)\bigr\}.
$$
This decays iff $\ln 2 + r\ln(7/8) < 0$, i.e.
$$
r > \frac{\ln 2}{\ln(8/7)} = \frac{0.693147}{0.133531} = 5.19089\ldots
$$
So $\Pr[\text{SAT}] \le \mathbb{E}[Z] \to 0$ for $r > 5.191$: a rigorous, one-line upper bound on $r_3$. It overshoots the true value $4.267$ by $22\%$ because $\mathbb{E}[Z]$ is dominated by rare formulas with exponentially many solutions.

**(b) Why the second moment fails here.** With overlap $z$, one computes for $k=3$
$$
\frac{1}{n}\ln \mathbb{E}[Z^2] \approx \max_{z\in[0,1]} \Bigl[ H(z) + \ln 2 + r \ln\bigl(1 - \tfrac{2}{8} + \tfrac{1}{8}(z^3 + (1-z)^3)\bigr)\Bigr],
$$
$H(z) = -z\ln z-(1-z)\ln(1-z)$. At $z = 1/2$ the bracket equals $2(\ln 2 + r\ln\frac78)$, i.e. exactly $\frac2n\ln\mathbb{E}[Z]$. But for $r \gtrsim 2.8$ the maximum moves to $z^\ast > 1/2$, giving $\mathbb{E}[Z^2] \ge e^{cn}\,\mathbb{E}[Z]^2$ with $c>0$. Paley–Zygmund then yields only $\Pr[Z>0] \ge e^{-cn}$ — exponentially weak, hence useless. This single inequality is the technical heart of Section 5.

**(c) The solved case $k = 2$.** A random 2-CNF at density $r$ maps to the implication digraph $D$ on $2n$ literals: clause $(x \vee y)$ gives arcs $\bar x \to y$ and $\bar y \to x$. The formula is unsatisfiable iff some variable $x$ has $x$ and $\bar x$ in the same strongly connected component (Aspvall–Plass–Tarjan). The digraph has out-degree mean $2r \cdot \frac{2}{2n}\cdot n = r\cdot$const; the branching process of implications is subcritical for $r<1$ and supercritical for $r>1$. Hence $r_2 = 1$, with the critical window $m = n + \lambda n^{2/3}$ mirroring the Erdős–Rényi giant-component window — the exact rigorous picture that is still missing for $k \ge 3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*