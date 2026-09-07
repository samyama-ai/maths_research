---
id: 09-probability/aldous-spectral-gap-conjecture
title: "Aldous Spectral Gap Conjecture"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Aldous Spectral Gap Conjecture

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/aldous-spectral-gap-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be a finite connected graph with $|V|=n$ and positive edge weights (conductances) $c_{xy}>0$ for $\{x,y\}\in E$. Two continuous-time Markov processes are built from the same data:

- the **random walk** (RW): a single particle at $x$ jumps to $y$ at rate $c_{xy}$;
- the **interchange process** (IP): $n$ distinguishable particles occupy the $n$ vertices bijectively, and for each edge $\{x,y\}$ the contents of $x$ and $y$ are swapped at rate $c_{xy}$. This is a random walk on the symmetric group $S_n$ driven by the transpositions $\tau_{xy}$.

Both generators are self-adjoint and negative semidefinite; write $\lambda(G)$ and $\lambda_{\mathrm{IP}}(G)$ for their spectral gaps (smallest nonzero eigenvalue of the negated generator).

**Conjecture (Aldous, c. 1992).** For every finite connected weighted graph,
$$\lambda_{\mathrm{IP}}(G)=\lambda(G).$$

The inequality $\lambda_{\mathrm{IP}}\le\lambda$ is elementary (one-particle functions embed into the IP), so the content is $\lambda_{\mathrm{IP}}\ge\lambda$: adding $n-1$ extra interacting particles cannot slow relaxation. An equivalent formulation: for every $k$, the $k$-particle **symmetric exclusion process** (SEP) on $G$ has spectral gap exactly $\lambda(G)$, independent of $k$. A complete resolution requires a proof valid for all graphs and all positive conductances, or a single counterexample weighted graph.

The conjecture was **proved by Caputo, Liggett and Richthammer** (*J. Amer. Math. Soc.* 23, 2010). The page is retained because the surrounding program — sharper spectral statements, non-transposition generators, quantum analogues — remains open.

## 2. Mathematical Foundations

**Random walk generator.** On $\ell^2(V)$,
$$(\mathcal{L}f)(x)=\sum_{y\sim x}c_{xy}\bigl(f(y)-f(x)\bigr),\qquad
\mathcal{E}(f,f)=\tfrac12\sum_{x,y}c_{xy}\bigl(f(y)-f(x)\bigr)^2 .$$
With the counting measure reversible, $\lambda(G)=\min\{\mathcal{E}(f,f)/\|f\|^2:\ \textstyle\sum_x f(x)=0\}$. For $c\equiv1$ this is the algebraic connectivity, the second-smallest eigenvalue of the graph Laplacian.

**Interchange generator.** Identify configurations with permutations $\sigma\in S_n$. In the group algebra $\mathbb{R}[S_n]$ (equivalently, on $\ell^2(S_n)$ by right multiplication),
$$\mathcal{L}_{\mathrm{IP}}=\sum_{\{x,y\}\in E}c_{xy}\bigl(\mathbb{1}-\tau_{xy}\bigr),$$
where $\tau_{xy}$ acts by $(\tau_{xy}f)(\sigma)=f(\sigma\tau_{xy})$. Since $\mathcal{L}_{\mathrm{IP}}$ lies in $\mathbb{R}[S_n]$ and commutes with left translation, its spectrum decomposes over the irreducible representations $\rho^\mu$ indexed by partitions $\mu\vdash n$:
$$\operatorname{spec}\mathcal{L}_{\mathrm{IP}}=\bigcup_{\mu\vdash n}\operatorname{spec}\Bigl(\sum_{\{x,y\}}c_{xy}\bigl(I-\rho^\mu(\tau_{xy})\bigr)\Bigr),$$
each eigenvalue carrying multiplicity $\dim\rho^\mu$. The partition $\mu=(n)$ gives $0$; the partition $\mu=(n-1,1)$ gives exactly the nonzero RW spectrum. So the conjecture says the *minimum over all $\mu\ne(n)$ is attained at $\mu=(n-1,1)$* — a purely representation-theoretic statement.

**Reduction to exclusion.** The $k$-particle SEP is the projection of the IP onto functions invariant under $S_k\times S_{n-k}$; the SEP spectrum is the union over $\mu$ with at most two rows and second row $\le k$. Hence $\lambda_{\mathrm{IP}}=\min_k\lambda_{\mathrm{SEP}(k)}$ and the two formulations agree.

**The octopus inequality (Caputo–Liggett–Richthammer).** Let the star with centre $0$ and legs $1,\dots,m$ carry weights $c_1,\dots,c_m>0$, $c=\sum_j c_j$. Then, as elements of $\mathbb{R}[S_{m+1}]$ acting on $\ell^2(S_{m+1})$,
$$\sum_{j=1}^m c_j\bigl(\mathbb{1}-\tau_{0j}\bigr)\ \succeq\ \sum_{1\le i<j\le m}\frac{c_ic_j}{c}\bigl(\mathbb{1}-\tau_{ij}\bigr).$$
The right side is the **star–mesh (star–delta) transform** of the left, the network reduction that eliminates vertex $0$ while preserving all effective resistances between the legs, hence preserving the one-particle Dirichlet form on $V\setminus\{0\}$. The octopus inequality lifts this classical electrical identity to an operator inequality on the full permutation space. Combined with induction on $n$, it yields $\lambda_{\mathrm{IP}}\ge\lambda$.

## 3. History & State of the Art (SOTA)

- **1981.** Diaconis and Shahshahani compute the full spectrum of the random-transposition walk (the complete graph $K_n$) by character theory, obtaining $\Theta(n\log n)$ mixing.
- **1985.** Flatto, Odlyzko and Wales analyse random shuffles and group representations, giving the complete-graph gap.
- **c. 1992.** Aldous states the conjecture, circulating it on his open-problem list and in the Aldous–Fill monograph *Reversible Markov Chains and Random Walks on Graphs*.
- **1996.** Handjani and Jungreis prove the conjecture for **trees** with arbitrary weights.
- **1997.** Koma and Nachtergaele obtain the gap of the ferromagnetic XXZ chain, giving the $q\to1$ interval case.
- **1998.** Lee and Yau prove log-Sobolev constants of order $(\log n)^{-1}$ for the exclusion and interchange processes on boxes — stronger than a gap bound but with non-sharp constants.
- **2008.** Morris proves the gap for the SEP on $d$-dimensional boxes up to a $1+o(1)$ factor, then exactly for the discrete torus and boxes.
- **2010.** **Caputo, Liggett and Richthammer** prove the conjecture in full generality via the octopus inequality plus a recursive network reduction.
- **2010–2016.** Cesi gives alternative and simplified routes: an explicit spectral analysis for complete multipartite transposition sets (2010) and a streamlined proof of the octopus inequality (2016). Dieker establishes interlacing relations between IP and RW spectra.
- **2013.** Alon and Kozma use the CLR theorem, plus a character-theoretic identity, to bound the probability of long cycles in the interchange process.

## 4. Partial Results / Verified Cases

Cases settled *before* the general theorem, each still the model example in its regime:

| Class | Result | Source |
|---|---|---|
| Complete graph $K_n$, uniform rates | $\lambda_{\mathrm{IP}}=\lambda=n$; full spectrum known | Diaconis–Shahshahani 1981; Flatto–Odlyzko–Wales 1985 |
| Trees, arbitrary positive weights | $\lambda_{\mathrm{IP}}=\lambda$ | Handjani–Jungreis 1996 |
| Star $K_{1,m}$, arbitrary weights | $\lambda_{\mathrm{IP}}=\lambda$; base case of octopus | Handjani–Jungreis 1996 |
| Path / interval $\{1,\dots,n\}$ | equivalent to XXZ chain gap at $\Delta=1$ | Koma–Nachtergaele 1997 |
| Boxes $\{1,\dots,L\}^d$, tori $\mathbb{Z}_L^d$ | exact gap for SEP at all densities | Morris 2008 |
| Complete multipartite transposition sets | full eigenvalue description | Cesi 2010 |
| $n\le 6$ (and weighted variants) | exhaustive computer diagonalisation of $\mathbb{R}[S_n]$ | folklore verification |

Post-2010 the statement holds for **all** finite connected weighted graphs, all $n$, all conductances. What remains open are the strengthenings in §6.

## 5. Principal Obstacles

Why the problem resisted for eighteen years, and why the surviving questions still resist:

- **No comparison argument works.** The standard route to a gap bound — a path/comparison inequality between Dirichlet forms — always loses a factor depending on $n$ or on the graph geometry. Aldous' identity is *exact*, so any lossy comparison is structurally the wrong tool.
- **Coupling fails.** Particles in the IP are not independent; the natural couplings between the IP and $n$ independent walkers are not monotone, and no coupling reproduces an equality of gaps.
- **Character theory does not localise.** Diaconis–Shahshahani works because on $K_n$ the generator is a central element of $\mathbb{R}[S_n]$, so it acts as a scalar on each irrep. For any non-complete graph the generator is non-central; its restriction to $\rho^\mu$ is a genuine matrix and there is no closed formula for its smallest eigenvalue.
- **Induction needs a graph operation that preserves the statement.** Deleting a vertex changes the RW gap unpredictably. The star–mesh transform is the unique reduction that keeps the one-particle spectrum controlled; recognising that it also dominates at the group-algebra level (the octopus inequality) was the missing idea.
- **The octopus inequality itself is delicate.** It is not implied by any general positivity principle on $\mathbb{R}[S_n]$; CLR's proof is a combinatorial induction over subsets of legs with a careful choice of test vectors, and there is still no representation-theoretic "reason" for it.

## 6. The Gap

The original conjecture is closed. The boundary now runs between the *gap* and everything finer:

1. **Full spectrum.** Aldous' stronger guess — that every IP eigenvalue is a sum of RW eigenvalues — is **false**; it holds for $K_n$ and stars but already fails on cycles. No description of $\operatorname{spec}\mathcal{L}_{\mathrm{IP}}$ for general $G$ exists.
2. **Non-transposition generators.** Replace transpositions by another conjugacy class or an arbitrary generating set of $S_n$: the analogous "gap attained at $\mu=(n-1,1)$" statement is false in general, and no criterion separates the true instances.
3. **Ferromagnetic ordering of energy levels (FOEL).** The spin-$\tfrac12$ Heisenberg ferromagnet on an arbitrary graph is exactly the IP, and CLR settles it. For spin $S>\tfrac12$, or $U_q(\mathfrak{sl}_2)$-deformed chains, the Nachtergaele–Starr FOEL conjecture — that the minimum energy in each total-spin sector decreases in the spin — is open beyond one-dimensional chains.
4. **Beyond the gap: mixing.** $\lambda_{\mathrm{IP}}=\lambda$ does not determine the mixing time; the Aldous–Diaconis cutoff picture for the IP on general graphs remains largely conjectural.
5. **Other conservative dynamics.** Hermon and Salez proved an Aldous-type gap identity for the zero-range process under a monotonicity hypothesis on the rates; without it the statement is open.

## 7. Current Research (as of June 2026)

- **Simplifying the octopus.** Cesi's shortened derivation is the reference proof; groups in Rome (Caputo, Cesi), UCLA/Munich (Liggett's and Richthammer's schools) continue to look for a representation-theoretic or positivity-certificate proof. A sum-of-squares certificate for the octopus inequality in $\mathbb{R}[S_n]$, uniform in $n$, is the stated target *(frontier — verify)*.
- **Cycle structure.** Following Alon–Kozma, work continues on Tóth's conjecture that the IP on high-dimensional tori develops macroscopic cycles; the gap identity supplies one of the few exact inputs.
- **Mathematical physics.** FOEL for higher spin and for $q$-deformed chains is pursued by Nachtergaele, Starr and collaborators (UC Davis, Virginia).
- **Non-reversible and infinite-volume extensions.** Gap identities for exclusion with reservoirs, and for asymmetric variants where the generator is non-self-adjoint, are being probed with hydrodynamic and Bethe-ansatz methods *(frontier — verify)*.

## 8. Future Work

- Find a *structural* proof: exhibit the octopus inequality as an instance of a general positivity theorem for Coxeter groups, which would immediately suggest the correct analogue for other Weyl groups.
- Determine exactly which generating sets of $S_n$ (or which conjugacy classes) satisfy "gap at $\mu=(n-1,1)$"; a classification would subsume both the true and known-false cases.
- Prove FOEL for spin-$S$ ferromagnets on trees, the natural first step past chains.
- Convert the exact gap into sharp mixing bounds — e.g. cutoff for the IP on expanders and on $\mathbb{Z}_L^d$.
- Extend the identity to other conservative particle systems (zero-range without monotone rates, misanthrope processes).

## 9. Key References

- **[Foundational]** D. Aldous and J. Fill. *Reversible Markov Chains and Random Walks on Graphs.* Unfinished monograph, 2002 (recompiled 2014). — original statement of the conjecture.
- **[Foundational]** P. Diaconis and M. Shahshahani. *Generating a random permutation with random transpositions.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981), 159–179.
- **[Foundational]** L. Flatto, A. M. Odlyzko, D. B. Wales. *Random shuffles and group representations.* Annals of Probability 13 (1985), 154–178.
- **[Partial]** S. Handjani and D. Jungreis. *Rate of convergence for shuffling cards by transpositions.* Journal of Theoretical Probability 9 (1996), 983–993.
- **[Partial]** T. Koma and B. Nachtergaele. *The spectral gap of the ferromagnetic XXZ chain.* Letters in Mathematical Physics 40 (1997), 1–16.
- **[Partial]** T.-Y. Lee and H.-T. Yau. *Logarithmic Sobolev inequality for some models of random walks.* Annals of Probability 26 (1998), 1855–1873.
- **[Partial]** B. Morris. *Spectral gap for the interchange process in a box.* Electronic Communications in Probability 13 (2008), 311–318.
- **[SOTA]** P. Caputo, T. M. Liggett, T. Richthammer. *Proof of Aldous' spectral gap conjecture.* Journal of the American Mathematical Society 23 (2010), 831–851.
- **[SOTA]** F. Cesi. *On the eigenvalues of Cayley graphs on the symmetric group generated by a complete multipartite set of transpositions.* Journal of Algebraic Combinatorics 32 (2010), 155–185.
- **[SOTA]** F. Cesi. *A few remarks on the octopus inequality and Aldous' spectral gap conjecture.* Communications in Algebra 44 (2016), 279–302.
- **[SOTA]** A. B. Dieker. *Interlacings for random walks on weighted graphs and the interchange process.* SIAM Journal on Discrete Mathematics 24 (2010), 191–206.
- **[SOTA]** N. Alon and G. Kozma. *The probability of long cycles in interchange processes.* Duke Mathematical Journal 162 (2013), 1567–1585.
- **[Related]** B. Nachtergaele and S. Starr. *Ferromagnetic Lieb–Mattis theorem.* Physical Review Letters 94 (2005), 057206.
- **[Related]** B. Nachtergaele, W. Spitzer, S. Starr. *Ferromagnetic ordering of energy levels.* Journal of Statistical Physics 124 (2006), 1–46.
- **[Related]** J. Hermon and J. Salez. *A version of Aldous' spectral-gap conjecture for the zero range process.* Annals of Applied Probability 29 (2019), 2217–2229.
- **[Survey]** D. A. Levin and Y. Peres. *Markov Chains and Mixing Times*, 2nd ed. American Mathematical Society, 2017.

## 10. Worked Example / Concrete Special Case

Take the **path on three vertices** $0-1$, $0-2$ with unit conductances (the star $K_{1,2}$), so $n=3$.

**Random walk.** The Laplacian is
$$L=\begin{pmatrix}2&-1&-1\\-1&1&0\\-1&0&1\end{pmatrix},\qquad \operatorname{spec}L=\{0,1,3\},\qquad \lambda(G)=1.$$

**Interchange process.** $\mathcal{L}_{\mathrm{IP}}=2\cdot\mathbb{1}-\tau_{01}-\tau_{02}\in\mathbb{R}[S_3]$, acting on the $6$-dimensional space $\ell^2(S_3)$. Decompose:

- *Trivial* $\rho^{(3)}$: $\tau\mapsto1$, eigenvalue $2-1-1=0$ (multiplicity $1$).
- *Sign* $\rho^{(1,1,1)}$: $\tau\mapsto-1$, eigenvalue $2+1+1=4$ (multiplicity $1$).
- *Standard* $\rho^{(2,1)}$ (dim $2$): set $A=\rho(\tau_{01})+\rho(\tau_{02})$. The character at a transposition is $0$, so $\operatorname{tr}A=0$. Also $A^2=2I+\rho(c)+\rho(c^{-1})$ where $c=\tau_{01}\tau_{02}$ is a $3$-cycle; since $I+\rho(c)+\rho(c^2)=0$ on the standard representation, $A^2=2I-I=I$. Hence $A$ has eigenvalues $+1,-1$ and $\mathcal{L}_{\mathrm{IP}}$ contributes $2-1=1$ and $2+1=3$, each with multiplicity $\dim\rho^{(2,1)}=2$.

So
$$\operatorname{spec}\mathcal{L}_{\mathrm{IP}}=\{0,\;1,1,\;3,3,\;4\},\qquad \lambda_{\mathrm{IP}}=1=\lambda(G).\ \checkmark$$
Note the standard representation reproduces the RW spectrum $\{1,3\}$ exactly, and here $4=1+3$ is a sum of RW eigenvalues — a coincidence of stars that fails on cycles.

**Checking the octopus inequality** for this star: $c_1=c_2=1$, $c=2$, so the claim is
$$2\cdot\mathbb{1}-\tau_{01}-\tau_{02}\ \succeq\ \tfrac12\bigl(\mathbb{1}-\tau_{12}\bigr).$$
Irrep by irrep: trivial gives $0\ge0$; sign gives $4\ge1$; on the standard representation the left side has eigenvalues $\{1,3\}$ so it dominates $I$, while the right side has eigenvalues $\{0,1\}$ so it is dominated by $I$. The inequality holds in every block, hence in $\ell^2(S_3)$. The right-hand side is precisely the star–mesh reduction of the star to the single edge $\{1,2\}$ with conductance $c_1c_2/c=\tfrac12$ — the electrical transform that CLR lift to the permutation group and iterate to prove the general theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*