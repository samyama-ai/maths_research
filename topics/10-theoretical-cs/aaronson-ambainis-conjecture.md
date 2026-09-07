---
id: 10-theoretical-cs/aaronson-ambainis-conjecture
title: "Aaronson-Ambainis Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Aaronson-Ambainis Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/aaronson-ambainis-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Every bounded low-degree real polynomial on the Boolean cube should have an *influential* variable — one whose flipping changes the value noticeably — with influence polynomially large in the polynomial's variance and polynomially small in its degree.

**Conjecture (Aaronson–Ambainis, 2011/2014).** There is an absolute constant $c > 0$ such that for every $n$, every $d$, and every multilinear polynomial $p : \{-1,1\}^n \to [-1,1]$ of degree at most $d$,
$$\max_{i \in [n]} \mathrm{Inf}_i(p) \;\ge\; \left(\frac{\mathrm{Var}(p)}{d}\right)^{c}.$$

The two hypotheses that matter are (i) *boundedness on the cube*, $|p(x)| \le 1$ for all $x \in \{-1,1\}^n$ (not merely $\|p\|_2 \le 1$), and (ii) *low degree*. The bound must be **independent of $n$**. A proof means establishing the inequality for some explicit $c$; a disproof means an infinite family $p_{n,d}$ with $\mathrm{Var}(p_{n,d}) = \Omega(1)$ and $\max_i \mathrm{Inf}_i(p_{n,d}) = d^{-\omega(1)}$.

**Why it matters.** Aaronson and Ambainis proved that the conjecture implies: every bounded-error quantum algorithm making $T$ queries to a Boolean string can be simulated by a classical randomized algorithm making $\mathrm{poly}(T,1/\varepsilon,1/\delta)$ queries that agrees with it, to within $\varepsilon$, on a $1-\delta$ fraction of inputs. Consequence: **quantum speedups need structure** — no exponential quantum advantage relative to a random oracle, i.e. $\mathsf{BQP}^A = \mathsf{BPP}^A$ with probability $1$ over a uniformly random $A$.

## 2. Mathematical Foundations

Every $f : \{-1,1\}^n \to \mathbb{R}$ has a unique multilinear Fourier expansion
$$f(x) \;=\; \sum_{S \subseteq [n]} \hat f(S)\, \chi_S(x), \qquad \chi_S(x) = \prod_{i \in S} x_i, \qquad \hat f(S) = \mathop{\mathbb{E}}_{x \sim \{-1,1\}^n}[f(x)\chi_S(x)].$$
The **degree** is $\deg(f) = \max\{|S| : \hat f(S) \neq 0\}$, and by Parseval $\mathbb{E}[f^2] = \sum_S \hat f(S)^2$.

**Variance and influence.**
$$\mathrm{Var}(f) = \sum_{S \neq \emptyset} \hat f(S)^2, \qquad \mathrm{Inf}_i(f) = \mathbb{E}\big[(\partial_i f)^2\big] = \sum_{S \ni i} \hat f(S)^2, \qquad \partial_i f(x) = \tfrac{1}{2}\big(f(x^{i \to 1}) - f(x^{i \to -1})\big).$$
Total influence $\mathbf{I}[f] = \sum_i \mathrm{Inf}_i(f) = \sum_S |S|\,\hat f(S)^2$. For Boolean-valued $f$, $\mathrm{Inf}_i(f) = \Pr_x[f(x) \ne f(x^{\oplus i})]$.

Two elementary facts frame the conjecture. Poincaré: $\mathrm{Var}(f) \le \mathbf{I}[f]$. Degree bound: $\mathbf{I}[f] \le d \cdot \mathbb{E}[f^2] \le d$ for bounded $p$ of degree $d$. Together these give only $\max_i \mathrm{Inf}_i \ge \mathrm{Var}(p)/n$ — useless, since the conjecture demands $n$-independence.

**Block-multilinear forms.** A degree-$d$ block-multilinear form on blocks $x^{(1)},\dots,x^{(d)} \in \mathbb{R}^{n}$ is
$$f(x^{(1)},\dots,x^{(d)}) = \sum_{i_1,\dots,i_d} c_{i_1 \cdots i_d}\, x^{(1)}_{i_1} \cdots x^{(d)}_{i_d},$$
homogeneous and linear in each block. It is **bounded** if $|f| \le 1$ on $(\{-1,1\}^n)^d$; it is **completely bounded** if the same holds when the $x^{(j)}_i$ are replaced by unitary (or contraction) matrices and the value is measured in operator norm. Completely bounded forms are exactly the amplitudes computed by $d$-query quantum algorithms (Arunachalam–Briët–Palazuelos, 2019), which is why this class is the right restriction for the quantum application.

**Quantum bridge.** By Beals–Buhrman–Cleve–Mosca–de Wolf, the acceptance probability of a $T$-query quantum algorithm on input $x \in \{0,1\}^n$ is a real polynomial $p(x) \in [0,1]$ of degree $\le 2T$. The AA conjecture applied to $p$, then recursively to restrictions of $p$ (which stay bounded and of no larger degree), yields a shallow classical decision tree approximating $p$ on most inputs.

## 3. History & State of the Art (SOTA)

- **2011.** Aaronson and Ambainis state the conjecture in *The Need for Structure in Quantum Speedups* (ICS 2011; journal version *Theory of Computing* 10 (2014), 133–166), motivated by the question of whether a random oracle separates $\mathsf{BQP}$ from $\mathsf{BPP}$. They prove the implication conjecture $\Rightarrow$ classical simulation on most inputs, and observe the Boolean-valued case is already a theorem.
- **2006–07.** Dinur, Friedgut, Kindler and O'Donnell prove that any $p:\{-1,1\}^n\to[-1,1]$ of degree $d$ has $\max_i \mathrm{Inf}_i(p) \ge \mathrm{Var}(p)\cdot 2^{-O(d)}$ — the best general bound known, and exponentially weaker in $d$ than required.
- **2014.** Backurs and Bavarian bound the sum of $L^1$-influences of bounded degree-$d$ polynomials by $2^{O(d)}$ (and by $O(d^3)$ for $d=2$), a close relative of the conjecture with the same exponential barrier.
- **2016.** Aaronson, Ambainis, Iraids, Kokainis and Smotrovs settle the **degree-2 block-multilinear** case using Grothendieck's inequality, and map the landscape of bounded-vs-completely-bounded forms.
- **2019.** Keller and Klein circulate a claimed proof (*Quantum speedups need structure*, arXiv); it is **withdrawn** after an error is found. The conjecture returns to open status.
- **2022.** Bansal, Sinha and de Wolf prove the conjecture for **completely bounded** block-multilinear forms of any degree, with polynomial dependence on both $\mathrm{Var}$ and $d$. Combined with Arunachalam–Briët–Palazuelos, this delivers the *quantum consequence* — classical simulation of quantum query algorithms on most inputs — **unconditionally**, while leaving the analytic conjecture for general bounded polynomials open.

State of the art: exponential-in-$d$ in general; polynomial-in-$d$ for Boolean-valued functions and for completely bounded forms.

## 4. Partial Results / Verified Cases

| Class | Best known influence bound | Source |
|---|---|---|
| Boolean-valued $f:\{-1,1\}^n\to\{-1,1\}$, degree $d$ | $\max_i \mathrm{Inf}_i \ge \mathrm{Var}(f)/O(d^3)$ | OSSS (2005) + Midrijānis (2004) |
| General bounded $p$, degree $d$ | $\max_i \mathrm{Inf}_i \ge \mathrm{Var}(p)\,2^{-O(d)}$ | Dinur–Friedgut–Kindler–O'Donnell (2007) |
| Degree $d = 1$ | $\max_i \mathrm{Inf}_i \ge \mathrm{Var}(p)^2$, tight | Elementary (Section 10) |
| Degree $d = 2$, block-multilinear, bounded | $\mathrm{poly}(\mathrm{Var})$, constant $d$-factor via Grothendieck | Aaronson–Ambainis–Iraids–Kokainis–Smotrovs (2016) |
| Any $d$, **completely bounded** block-multilinear | $\mathrm{poly}(\mathrm{Var}(f)/d)$ — conjecture holds | Bansal–Sinha–de Wolf (2022) |
| Quantum acceptance polynomials ($T$ queries) | simulation on $1-\delta$ of inputs with $\mathrm{poly}(T,1/\varepsilon,1/\delta)$ classical queries | BSdW (2022) + ABP (2019) |

The Boolean-valued proof is worth stating: by the OSSS inequality, for any decision tree $\mathcal{T}$ computing $f$, $\mathrm{Var}(f) \le \sum_i \delta_i(\mathcal{T})\,\mathrm{Inf}_i(f)$ where $\delta_i$ is the probability that $\mathcal{T}$ queries $x_i$; hence $\mathrm{Var}(f) \le D(f)\cdot\max_i \mathrm{Inf}_i(f)$, and $D(f) = O(\deg(f)^3)$.

## 5. Principal Obstacles

- **Loss of the Boolean handle.** Every polynomial-in-$d$ result for Boolean-valued functions routes through decision trees ($D(f) \le O(\deg^3)$, OSSS). A real-valued bounded $p$ has no decision tree, no sensitivity, no certificate complexity. The entire $\{-1,1\}$-valued toolkit — Nisan–Szegedy, Huang's sensitivity theorem, random restrictions that "kill" a Boolean function — is unavailable.
- **Hypercontractivity gives $2^{-\Theta(d)}$, not $d^{-O(1)}$.** The DFKO proof uses the Bonami–Beckner $(2,q)$-hypercontractive inequality, whose constant is $\sqrt{q-1}^{\,d}$. Any argument that bounds high-degree Fourier mass by comparing $L^2$ and $L^q$ norms pays this exponential factor. This is not a slack in the write-up: the exponential loss is intrinsic to norm-comparison, so a proof must exploit boundedness on the *whole cube* in a way no $L^q$ norm sees.
- **Boundedness is a global, non-convex constraint.** $|p(x)|\le 1$ at $2^n$ points is not captured by any finite set of Fourier moment inequalities; the set of bounded degree-$d$ polynomials has no known tractable semidefinite description. Complete boundedness *does* have one (an operator-space / factorization characterization), which is exactly why Bansal–Sinha–de Wolf could succeed there and why their proof does not transfer.
- **The bounded/completely bounded gap is real.** For $d \ge 3$ there are bounded block-multilinear forms whose completely bounded norm is $\omega(1)$ (a Grothendieck-type phenomenon: no analogue of Grothendieck's inequality holds for $d\ge 3$ tensors). So the 2022 theorem provably does not cover the general case.
- **No candidate counterexample.** Extremal examples (products of normalized linear forms, Grover-like acceptance polynomials, symmetric polynomials such as $T_d$ composed with averages) all obey influence $\ge \mathrm{Var}^{O(1)}/d^{O(1)}$, so the search for a disproof has produced no near-miss to guide theory.

## 6. The Gap

Proven: $\max_i \mathrm{Inf}_i(p) \ge \mathrm{Var}(p) \cdot 2^{-O(d)}$ for all bounded degree-$d$ $p$.
Conjectured: $\max_i \mathrm{Inf}_i(p) \ge (\mathrm{Var}(p)/d)^{O(1)}$.

The whole content of the gap is the **substitution of $d^{-O(1)}$ for $2^{-O(d)}$** — for $d = \Theta(\log n)$ this is precisely the difference between polynomial and quasi-polynomial simulation, and the reason the random-oracle question is untouched by DFKO. Equivalently: prove that a bounded degree-$d$ polynomial of constant variance has a variable of influence $\ge 1/\mathrm{poly}(d)$.

The second, structural gap: extend the Bansal–Sinha–de Wolf argument from *completely bounded* to merely *bounded* forms, and from homogeneous block-multilinear forms to arbitrary multilinear $p$. Block-multilinearization is known to be lossy in the cb-norm for $d \ge 3$, so this is not a bookkeeping step.

## 7. Current Research (as of June 2026)

- **Operator-space methods.** The line from Arunachalam–Briët–Palazuelos through Bansal–Sinha–de Wolf treats polynomials as multilinear maps between operator spaces. Follow-up work by Escudero Gutiérrez extends the influence theorem to *Fourier completely bounded* polynomials, a class strictly larger than cb block-multilinear forms, and derives corresponding classical simulations. *(frontier — verify current scope of the class covered.)*
- **Quantifying the bounded/cb gap.** Determining the maximal ratio $\|f\|_{cb}/\|f\|_\infty$ for degree-$d$ block-multilinear forms; the conjecture would follow from a $\mathrm{poly}(d)$ bound on this ratio. Current constructions give growth in $d$, so this route likely needs a variance-sensitive refinement. *(frontier — verify.)*
- **Groups.** CWI/QuSoft (de Wolf, Sinha, Briët and collaborators), UT Austin (Aaronson), University of Latvia (Ambainis, Kokainis), Bar-Ilan/Weizmann (Keller, Klein), and the analysis-of-Boolean-functions community around O'Donnell (CMU) and Filmus.
- **Adjacent problems being used as testbeds:** the sum-of-$L^1$-influences conjecture (Backurs–Bavarian), $\mathrm{poly}(d)$ Fourier-tail bounds for bounded polynomials, and the degree-3 Grothendieck-type inequality.

## 8. Future Work

- Prove the case $d = 3$ for general bounded (not completely bounded) block-multilinear forms — the first point where Grothendieck's inequality fails and the smallest open instance with genuine content.
- Establish a $\mathrm{poly}(d)$ bound on the sum of $L^1$-influences of bounded degree-$d$ polynomials, which Backurs and Bavarian identify as essentially equivalent in strength.
- Develop a "restriction-robust" invariant: a quantity that decreases under random restrictions, controls variance, and is defined for real-valued bounded $p$ (a surrogate for decision-tree depth).
- Look for a counterexample among polynomials arising from quantum algorithms with *non-unitary* or *noisy* structure, where the cb norm blows up but the sup norm does not.
- Aaronson's stated program: settle whether $\mathsf{BQP}^A \neq \mathsf{BPP}^A$ for random $A$ directly; the 2022 results already rule out a separation via *query* algorithms, so any separation must come from a non-query mechanism.

## 9. Key References

- **[Foundational]** Scott Aaronson, Andris Ambainis. *The Need for Structure in Quantum Speedups.* Theory of Computing, vol. 10, article 6, pp. 133–166, 2014 (earlier: Innovations in Computer Science, 2011).
- **[Foundational]** Irit Dinur, Ehud Friedgut, Guy Kindler, Ryan O'Donnell. *On the Fourier tails of bounded functions over the discrete cube.* Israel Journal of Mathematics, vol. 160, pp. 389–412, 2007 (earlier: STOC 2006).
- **[Foundational]** Ryan O'Donnell, Michael Saks, Oded Schramm, Rocco A. Servedio. *Every decision tree has an influential variable.* Proc. 46th IEEE Symposium on Foundations of Computer Science (FOCS), pp. 31–39, 2005.
- **[Foundational]** Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca, Ronald de Wolf. *Quantum lower bounds by polynomials.* Journal of the ACM, vol. 48(4), pp. 778–797, 2001.
- **[SOTA / Recent]** Nikhil Bansal, Makrand Sinha, Ronald de Wolf. *Influence in Completely Bounded Block-Multilinear Forms and Classical Simulation of Quantum Algorithms.* Proc. 37th Computational Complexity Conference (CCC), 2022.
- **[SOTA / Recent]** Srinivasan Arunachalam, Jop Briët, Carlos Palazuelos. *Quantum query algorithms are completely bounded forms.* SIAM Journal on Computing, vol. 48(3), pp. 903–925, 2019 (earlier: ITCS 2018).
- **[SOTA / Recent]** Scott Aaronson, Andris Ambainis, Jānis Iraids, Martins Kokainis, Juris Smotrovs. *Polynomials, Quantum Query Complexity, and Grothendieck's Inequality.* Proc. 31st Computational Complexity Conference (CCC), 2016.
- **[SOTA / Recent]** Arturs Backurs, Mohammad Bavarian. *On the sum of $L_1$ influences.* Proc. 29th IEEE Conference on Computational Complexity (CCC), pp. 132–143, 2014.
- **[Related]** Gatis Midrijānis. *Exact quantum query complexity for total Boolean functions.* arXiv:quant-ph/0403168, 2004. (Gives $D(f) = O(\deg(f)^3)$.)
- **[Survey]** Ryan O'Donnell. *Analysis of Boolean Functions.* Cambridge University Press, 2014.
- **[Survey]** Scott Aaronson. *Open Problems Related to Quantum Query Complexity.* ACM Transactions on Quantum Computing, vol. 2(4), 2021.

## 10. Worked Example / Concrete Special Case

**The degree-1 case, solved exactly — and why the exponent $c$ cannot be $1$ in the variance.**

Let $p(x) = a_0 + \sum_{i=1}^n a_i x_i$ on $\{-1,1\}^n$ with $|p(x)| \le 1$ everywhere. Then $\mathrm{Var}(p) = \sum_i a_i^2$ and $\mathrm{Inf}_i(p) = a_i^2$.

*Step 1 (boundedness $\Rightarrow$ $\ell^1$ bound).* Choose $x_i = \mathrm{sgn}(a_i)$ and $x_i = -\mathrm{sgn}(a_i)$. Then $p$ takes the values $a_0 \pm \sum_i |a_i|$, both in $[-1,1]$, so
$$\sum_{i=1}^n |a_i| \;\le\; 1.$$

*Step 2 (Hölder).* $\displaystyle \mathrm{Var}(p) = \sum_i a_i^2 \le \Big(\max_i |a_i|\Big)\sum_i |a_i| \le \max_i |a_i|.$

*Step 3.* Squaring, $\max_i \mathrm{Inf}_i(p) = \max_i a_i^2 \ge \mathrm{Var}(p)^2$. The conjecture holds for $d=1$ with $c=2$.

*Tightness.* Take $a_0 = 0$, $a_i = 1/n$: $p(x) = \frac{1}{n}\sum_i x_i$, so $|p| \le 1$, $\mathrm{Var}(p) = n \cdot n^{-2} = 1/n$, and every influence equals $1/n^2 = \mathrm{Var}(p)^2$. So the quadratic loss in $\mathrm{Var}$ is unavoidable — the conjecture is correctly stated with an exponent, not as $\max_i \mathrm{Inf}_i \ge \mathrm{Var}/\mathrm{poly}(d)$ for real-valued $p$.

**Where the difficulty starts ($d \ge 2$).** Split $[n]$ into $d$ blocks of size $m = n/d$ and set
$$q(x) \;=\; \prod_{j=1}^{d} \left( \frac{1}{\sqrt m}\sum_{i \in B_j} x_i \right)\cdot \frac{1}{M},$$
with $M$ chosen so $|q| \le 1$. Each factor is a normalized linear form of variance $1$; the product is degree $d$, and $\mathrm{Inf}_i(q) = \Theta(\mathrm{Var}(q)/m)$ — still fine, because $\mathrm{Var}(q)$ is itself small once $M$ is large enough. To break the conjecture one needs a bounded degree-$d$ polynomial with $\mathrm{Var} = \Omega(1)$ *and* all influences $d^{-\omega(1)}$; every natural construction that keeps $\mathrm{Var}$ constant forces the Fourier mass onto few levels and produces an influential variable. What is missing is a proof that this is necessary — DFKO shows it with a loss of $2^{-O(d)}$, and closing that to $d^{-O(1)}$ is the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*