---
id: 09-probability/optimal-mixing-time-of-the-riffle-shuffle
title: "Optimal Mixing Time of the Riffle Shuffle"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Mixing Time of the Riffle Shuffle

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/optimal-mixing-time-of-the-riffle-shuffle` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

How many riffle (dovetail) shuffles are needed to mix a deck of $n$ cards?

Formally: let $Q$ be the Gilbert–Shannon–Reeds (GSR) measure on the symmetric group $S_n$, let $Q^{*k}$ be its $k$-fold convolution, and let $U$ be uniform on $S_n$. Define
$$d(k) = \|Q^{*k} - U\|_{\mathrm{TV}} = \tfrac12 \sum_{w \in S_n} \left| Q^{*k}(w) - \tfrac{1}{n!} \right|,\qquad t_{\mathrm{mix}}(\varepsilon)=\min\{k: d(k)\le\varepsilon\}.$$
Determine $t_{\mathrm{mix}}$ exactly and asymptotically, and determine whether the convergence exhibits **cutoff** — an abrupt drop of $d(k)$ from near $1$ to near $0$ over a window of lower order than $t_{\mathrm{mix}}$ itself.

The core question is **resolved**. Bayer and Diaconis (1992) gave a closed form for $Q^{*k}$, proved cutoff at
$$k_n = \tfrac{3}{2}\log_2 n,$$
and computed the limit profile: for $k = \frac32\log_2 n + c$ with $c$ fixed,
$$d(k) \;=\; 1 - 2\Phi\!\left(\frac{-2^{-c}}{4\sqrt{3}}\right) + O\!\left(n^{-1/4}\right),$$
where $\Phi$ is the standard normal CDF. For $n = 52$ this yields the famous answer: **seven shuffles**.

What remains genuinely open, and is the live content of this entry: (i) the sharp cutoff *window* and the true order of the error term; (ii) the mixing time under metrics other than total variation ($L^\infty$, relative entropy, separation) where the constant differs; (iii) the mixing time of *physically realistic* shuffles (biased cuts, clumpy riffles, "smooshing"); and (iv) how few shuffles suffice when only part of the deck's randomness is used.

## 2. Mathematical Foundations

**GSR model.** Cut the deck into two packets of sizes $j$ and $n-j$ with $j \sim \mathrm{Bin}(n,1/2)$; then interleave, dropping the next card from the left packet with probability proportional to its remaining size. Equivalently (inverse description): assign each card an i.i.d. uniform bit, then move all $0$-cards to the top preserving relative order.

**$a$-shuffles.** Generalize: cut into $a$ packets with multinomial sizes $(j_1,\dots,j_a)$ having probability $\binom{n}{j_1,\dots,j_a}/a^n$, then riffle all $a$ packets together uniformly at random among all interleavings. The resulting measure is
$$Q_a(w) \;=\; \frac{\binom{a+n-r(w)}{n}}{a^n},\qquad r(w) = \mathrm{des}(w^{-1}) + 1,$$
where $\mathrm{des}$ counts descents and $r(w)$ is the number of **rising sequences** of the arrangement.

**Convolution identity (the key structural fact).** An $a$-shuffle followed by a $b$-shuffle is exactly an $ab$-shuffle:
$$Q_a * Q_b = Q_{ab} \quad\Longrightarrow\quad Q^{*k} = Q_{2^k}.$$
This collapses a $k$-step random walk into a one-parameter family — the reason this chain is solvable while nearly all others are not.

**Exact distance.** Since $Q_a(w)$ depends on $w$ only through $r(w)$, and the number of $w$ with $r(w)=r$ is the Eulerian number $A_{n,r}$,
$$\|Q_{2^k} - U\|_{\mathrm{TV}} \;=\; \frac12\sum_{r=1}^{n} A_{n,r}\left|\frac{\binom{2^k+n-r}{n}}{2^{kn}} - \frac{1}{n!}\right|.$$
The asymptotics follow from the central limit theorem for descents, $\mathrm{des} \approx \mathcal N(n/2,\,n/12)$, combined with the smoothness of $x\mapsto\binom{a+n-x}{n}$.

**Separation distance.** $\mathrm{sep}(k) = \max_w\left(1 - n!\,Q^{*k}(w)\right)$ satisfies the exact identity
$$\mathrm{sep}(k) \;=\; 1 - \prod_{i=1}^{n-1}\left(1 - \frac{i}{2^k}\right),$$
a birthday-problem expression giving cutoff at $2\log_2 n$ — strictly larger than the TV constant $\tfrac32$. The strong uniform time realizing this is the inverse-shuffle bit-assignment: the deck is exactly uniform once all $n$ binary strings are distinct (Aldous–Diaconis, 1986).

**Algebraic structure.** The $Q_a$ generate a commutative subalgebra of $\mathbb{C}[S_n]$; the eigenvalues of the $a$-shuffle transition matrix are $a^{-j}$ with multiplicity the number of permutations with $n-j$ cycles (Stirling numbers of the first kind), a fact due to Hanlon and to Diaconis–McGrath–Pitman. Bidigare–Hanlon–Rockmore embed this in random walks on the chambers of the braid hyperplane arrangement $\{x_i = x_j\}$, where the eigenvalues are read off from the intersection lattice.

## 3. History & State of the Art (SOTA)

- **1955.** Gilbert and Claude Shannon formulate the GSR model in a Bell Labs technical report; Jim Reeds rediscovers it independently in 1981 unpublished notes.
- **1983.** Aldous proves the first $O(\log n)$ bound, identifying $\tfrac32\log_2 n$ as the correct order and establishing cutoff qualitatively.
- **1986.** Aldous and Diaconis introduce strong uniform times, giving the exact separation formula and the clean upper bound $2\log_2 n$.
- **1992.** Bayer and Diaconis prove the closed form $Q_a(w) = \binom{a+n-r}{n}/a^n$, derive the exact TV sum, and produce the table for $n=52$:

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $d(k)$ | 1.000 | 1.000 | 1.000 | 1.000 | 0.924 | 0.614 | 0.334 | 0.167 | 0.085 | 0.043 |

- **1994–2000.** Mann's expository analysis, and Trefethen–Trefethen's argument that under an entropy/$L^\infty$-flavoured criterion the answer for $n=52$ is closer to $\log_2 n \approx 11.7$ shuffles, showing the "7" is metric-dependent.
- **1995–2002.** Structural theory: Diaconis–McGrath–Pitman connect shuffles to cycle structure and Poisson–Dirichlet limits; Lalley links riffles to dynamical systems; Fulman develops the symmetric-function and Lie-theoretic picture; Stark–Ganesh–O'Connell compute relative-entropy loss.
- **2011.** Assaf, Diaconis and Soundararajan prove a "rule of thumb": if only a limited feature of the deck is used, far fewer shuffles suffice — quantitatively, mixing a designated subset of $k$ cards needs a $k$-dependent number of shuffles far below $\tfrac32\log_2 n$ when $k \ll n$.
- **2023.** Diaconis and Fulman's book *The Mathematics of Shuffling Cards* consolidates the field and lists the remaining open problems.

## 4. Partial Results / Verified Cases

- **Exactly solved:** every $n$, every $k$, for the idealized GSR model in TV and separation, via the Eulerian-number formula. Numerically exact for $n = 52$ (7 shuffles for $d < 1/2$; 11 for $d < 0.01$).
- **Cutoff constants confirmed:** TV at $\tfrac32\log_2 n$; separation at $2\log_2 n$; $L^\infty$/relative-entropy at $2\log_2 n$ (Stark–Ganesh–O'Connell show entropy decays with the larger constant).
- **Eigenvalue spectrum:** complete for all $n$ and all $a$-shuffles.
- **Cycle and fixed-point statistics:** exact after any $k$; number of fixed points after a $2^k$-shuffle has an explicit distribution, converging to Poisson$(1)$ once $2^k \gg n$.
- **Biased shuffles:** for the $a$-shuffle with unequal packet probabilities $p_1,\dots,p_a$, Fulman and others give closed forms and mixing bounds in the "$p$-shuffle" family.
- **Card-guessing benchmarks:** Ciucu (1998) determines the optimal no-feedback guessing strategy and its success probability after riffle shuffles; Diaconis–Graham–He–Xu (2022) extend to partial feedback.
- **Small $n$:** brute-force verification for $n \le 10$ agrees with the closed form to machine precision.

## 5. Principal Obstacles

- **The solvability is an accident.** The whole analysis rests on $Q_a * Q_b = Q_{ab}$ and on $Q_a$ being a function of descents alone. Perturb the model — bias the cut, allow clumps, allow dependence between drops — and both properties fail immediately. There is no perturbative theory around GSR.
- **Fourier analysis on $S_n$ is not the tool.** The GSR measure is not a class function; its Fourier transform at a representation $\rho$ does not diagonalize in a usable basis, and the standard upper-bound lemma $4d(k)^2 \le \sum_{\rho\ne 1} d_\rho \operatorname{tr}(\hat Q(\rho)^k \hat Q(\rho)^{*k})$ is intractable because the $d_\rho$ are enormous and the singular values are not known representation-by-representation.
- **Metric dependence is real, not cosmetic.** TV, separation, $\chi^2$ and relative entropy give constants $\tfrac32$, $2$, $2$, $2$. Deciding which is "optimal" requires specifying the adversary — a modelling question, not a theorem. The seven-shuffle claim is only correct against an adversary who can compute an arbitrary function of the full arrangement.
- **The window and error term.** Bayer–Diaconis's $O(n^{-1/4})$ error is almost certainly not sharp, but improving it requires uniform Edgeworth-type control on Eulerian numbers against a binomial-coefficient weight, in a regime where the two profiles nearly cancel.
- **Physical shuffles are not GSR.** Empirical studies of human riffles show packet sizes and drop patterns deviating substantially from the binomial/greedy model, and no tractable model matching the data has closed-form convolution structure.

## 6. The Gap

Precisely: the GSR chain is fully solved, but three boundaries remain uncrossed.

1. **From constant to window.** Proven: $d\big(\tfrac32\log_2 n + c\big) \to 1 - 2\Phi(-2^{-c}/(4\sqrt3))$ with $O(n^{-1/4})$ error. Not proven: the true rate, conjecturally $O(n^{-1/2})$ or better, and whether the window has width $\Theta(1)$ uniformly in $\varepsilon$.
2. **From idealized to physical.** Proven: mixing for GSR and for the parametric $p$-shuffle family. Not proven: any sharp mixing statement for a shuffle with dependence between successive drops, or for smooshing (spreading cards face-down on a table and swirling them), where even the order of the mixing time in seconds is undetermined.
3. **From worst-case to used-case.** Proven: a rule-of-thumb bound for $k$ tracked cards (Assaf–Diaconis–Soundararajan). Not proven: matching lower bounds for the specific statistics that real games actually read (dealt hands, bridge distributions), where the relevant $\sigma$-algebra is coarse and the exact threshold is unknown.

## 7. Current Research (as of June 2026)

- **Limit profiles.** The Teyssier (2020) framework for random transpositions and its extension by Nestoridi and Olesker-Taylor (2022) to reversible chains has renewed interest in obtaining the riffle-shuffle profile by representation-theoretic rather than combinatorial means, with the hope of sharper error terms. *(frontier — verify)*
- **Hyperplane-arrangement walks.** The Bidigare–Hanlon–Rockmore / Brown–Diaconis theory continues to be extended to other Coxeter types and to buildings, where the "riffle shuffle" analogue is a walk on chambers with $q$-analogue eigenvalues. Active at Stanford, Michigan, USC.
- **Card guessing.** Following Diaconis–Graham–He–Xu, sharp asymptotics for the expected number of correct guesses after $k$ riffles under various feedback regimes is an active line; this gives a *statistical* mixing criterion that is arguably closer to the practical question than TV. *(frontier — verify)*
- **Smooshing.** Diaconis's empirical program — timing physical smooshing against statistical tests — remains without a theorem. Diffusion-on-$S_n$ models have been proposed but not analyzed to cutoff precision. *(frontier — verify)*
- **Casino-realistic protocols.** Analysis of shuffle machines and of riffle-plus-cut-plus-strip composites, where the composite measure is no longer in any closed family.

## 8. Future Work

- Prove a sharp limit-profile theorem with error $O(n^{-1/2})$ or identify the true rate; this likely needs an Edgeworth expansion for descents with explicit uniformity.
- Develop a robustness theory: a general theorem showing that a shuffle within $\delta$ of GSR (in a suitable model-space metric) mixes in $\tfrac32\log_2 n + f(\delta)$ steps.
- Establish matching lower bounds for game-relevant $\sigma$-algebras, closing the Assaf–Diaconis–Soundararajan rule of thumb into a theorem with two-sided constants.
- Analyze smooshing rigorously, even at the level of the exponent.
- Extend the exact theory to $q$-analogues and to shuffles on other Coxeter groups, where the descent algebra structure survives.

## 9. Key References

- **[Foundational]** D. Bayer and P. Diaconis. *Trailing the dovetail shuffle to its lair.* Annals of Applied Probability 2(2):294–313, 1992.
- **[Foundational]** D. Aldous and P. Diaconis. *Shuffling cards and stopping times.* American Mathematical Monthly 93(5):333–348, 1986.
- **[Foundational]** D. Aldous. *Random walks on finite groups and rapidly mixing Markov chains.* Séminaire de Probabilités XVII, Lecture Notes in Mathematics 986, Springer, 243–297, 1983.
- **[Structural]** P. Diaconis, M. McGrath and J. Pitman. *Riffle shuffles, cycles, and descents.* Combinatorica 15(1):11–29, 1995.
- **[Structural]** T. P. Bidigare, P. Hanlon and D. Rockmore. *A combinatorial description of the spectrum for the Tsetlin library and its generalization to hyperplane arrangements.* Duke Mathematical Journal 99(1):135–174, 1999.
- **[Structural]** S. P. Lalley. *Cycle structure of riffle shuffles.* Annals of Probability 24(1):49–73, 1996.
- **[SOTA / Recent]** S. Assaf, P. Diaconis and K. Soundararajan. *A rule of thumb for riffle shuffling.* Annals of Applied Probability 21(3):843–875, 2011.
- **[SOTA / Recent]** P. Diaconis, R. Graham, X. He and S. Xu. *Card guessing with partial feedback.* Combinatorics, Probability and Computing 31(1):1–20, 2022.
- **[SOTA / Recent]** L. Teyssier. *Limit profile for random transpositions.* Annals of Probability 48(5):2323–2343, 2020.
- **[SOTA / Recent]** E. Nestoridi and S. Olesker-Taylor. *Limit profiles for reversible Markov chains.* Probability Theory and Related Fields 182:157–188, 2022.
- **[Related]** D. Stark, A. Ganesh and N. O'Connell. *Information loss in riffle shuffling.* Combinatorics, Probability and Computing 11(1):79–95, 2002.
- **[Related]** L. N. Trefethen and L. M. Trefethen. *How many shuffles to randomize a deck of cards?* Proceedings of the Royal Society of London A 456:2561–2568, 2000.
- **[Related]** M. Ciucu. *No-feedback card guessing for dovetail shuffles.* Annals of Applied Probability 8(4):1251–1269, 1998.
- **[Survey / Book]** P. Diaconis and J. Fulman. *The Mathematics of Shuffling Cards.* American Mathematical Society, 2023.
- **[Survey]** P. Diaconis. *Mathematical developments from the analysis of riffle shuffling.* In *Groups, Combinatorics and Geometry* (Durham, 2001), World Scientific, 73–97, 2003.

## 10. Worked Example / Concrete Special Case

Take $n = 3$. The Eulerian numbers are $A_{3,1}=1$, $A_{3,2}=4$, $A_{3,3}=1$ (permutations with $1$, $2$, $3$ rising sequences).

**One shuffle ($a = 2$).** $Q_2(w) = \binom{5-r}{3}/8$:

| $r$ | count | $\binom{5-r}{3}$ | $Q_2(w)$ | mass |
|---|---|---|---|---|
| 1 | 1 | 4 | $1/2$ | $1/2$ |
| 2 | 4 | 1 | $1/8$ | $1/2$ |
| 3 | 1 | 0 | $0$ | $0$ |

Total mass $=1$. Note $321$, which has three rising sequences, is unreachable in one riffle — correct, since a single riffle cannot reverse a deck. Then
$$d(1)=\tfrac12\left[\left|\tfrac12-\tfrac16\right| + 4\left|\tfrac18-\tfrac16\right| + \left|0-\tfrac16\right|\right] = \tfrac12\left[\tfrac13+\tfrac16+\tfrac16\right]=\tfrac13.$$

**Two shuffles ($a=4$).** $Q_4(w)=\binom{7-r}{3}/64$, giving $20/64$, $10/64$, $4/64$ for $r=1,2,3$ (check: $20+4\cdot10+4=64$). With $1/6 = 10.667/64$,
$$d(2)=\frac{1}{2\cdot 64}\big[9.333 + 4(0.667) + 6.667\big] = \frac{18.667}{128} = \frac{7}{48}\approx 0.1458.$$

**Three shuffles ($a=8$).** $\binom{11-r}{3}/512 = 120/512,\,84/512,\,56/512$; $1/6 = 85.33/512$, so
$$d(3)=\frac{34.67 + 4(1.33) + 29.33}{1024}\approx 0.0677.$$

The distance roughly halves each shuffle — the fixed-$n$ geometric tail governed by the second eigenvalue $2^{-k}$.

**Separation, same deck.** $\mathrm{sep}(k)=1-\prod_{i=1}^{2}(1-i/2^k)$ gives $\mathrm{sep}(1)=1$, $\mathrm{sep}(2)=5/8$, $\mathrm{sep}(3)=11/32\approx0.344$. Separation is uniformly larger than TV, and the gap is exactly the $\tfrac32$-versus-$2$ constant discrepancy in miniature: the metric you choose changes the answer, which is why "optimal mixing time" is a family of questions rather than one.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*