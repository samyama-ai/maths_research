---
id: 01-number-theory/langlands-program
title: "Langlands Program"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Langlands Program

> **Topic:** Number Theory · **ID:** `01-number-theory/langlands-program` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Langlands Program is a vast, unifying network of conjectures that propose deep theoretical correspondences between algebraic number theory (specifically, Galois representations) and harmonic analysis (automorphic forms and representations). 

The central conjecture, known as the **Global Langlands Correspondence**, posits that for any connected reductive algebraic group $G$ defined over a global field $F$, there exists a natural, essentially bijective mapping between certain global Galois representations (called $L$-parameters) taking values in the Langlands dual group ${}^L G$, and the automorphic representations of $G(\mathbb{A}_F)$, where $\mathbb{A}_F$ is the adele ring of $F$. This correspondence must preserve critical analytic invariants, specifically ensuring the equality of local and global $L$-functions and $\varepsilon$-factors on both sides of the correspondence. 

A complete proof would provide a grand unified theory of mathematics, allowing the profound theorems of harmonic analysis to solve long-standing problems in number theory, and vice versa.

## 2. Mathematical Foundations

Let $F$ be a global field (either a number field like $\mathbb{Q}$, or the function field of a curve over a finite field). 
Let $\mathbb{A}_F$ be the adele ring of $F$, a restricted topological product $\mathbb{A}_F = \prod_{v}' F_v$ over all places $v$ of $F$. 
Let $\Gamma_F = \text{Gal}(\overline{F}/F)$ be the absolute Galois group of $F$, and $W_F$ its Weil group.

Let $G$ be a connected reductive algebraic group over $F$. We associate to $G$ its Langlands dual group (or L-group), denoted ${}^L G$. The L-group is defined as the semidirect product:
$$ {}^L G = \hat{G}(\mathbb{C}) \rtimes W_F $$
where $\hat{G}(\mathbb{C})$ is the complex reductive group whose root datum is dual to that of $G$ (e.g., if $G = \text{Sp}_{2n}$, then $\hat{G} = \text{SO}_{2n+1}$).

**Automorphic Side:** 
An automorphic representation $\pi$ is an irreducible representation of the adele group $G(\mathbb{A}_F)$ that appears in the decomposition of the right regular representation of $G(\mathbb{A}_F)$ on the Hilbert space $L^2(G(F) \backslash G(\mathbb{A}_F))$. By Flath's theorem, $\pi$ decomposes as a restricted tensor product of local representations: $\pi \cong \bigotimes_{v}' \pi_v$.

**Galois Side:** 
A global $L$-parameter is a continuous homomorphism $\phi : W_F \times \text{SU}(2, \mathbb{R}) \to {}^L G$, satisfying certain boundedness and semisimplicity conditions. It restricts to local parameters $\phi_v : W_{F_v} \times \text{SU}(2, \mathbb{R}) \to {}^L G$.

**The Correspondence:**
For any finite-dimensional algebraic representation $r$ of ${}^L G$, one can define a Galois $L$-function $L(s, \phi, r)$ and an automorphic $L$-function $L(s, \pi, r)$. The Langlands Correspondence asserts that there exists a surjective mapping from automorphic representations to $L$-parameters such that:
$$ L(s, \pi, r) = L(s, \phi, r) $$
and local epsilon factors $\varepsilon(s, \pi, r) = \varepsilon(s, \phi, r)$ match for all $r$ and at all places $v$.

## 3. History & State of the Art (SOTA)

The program originated in a handwritten letter from Robert Langlands to André Weil in 1967, introducing the general notion of $L$-groups and functoriality.

- **1970s:** The Jacquet-Langlands correspondence established the theory for $G = \text{GL}(2)$, generalizing classical modular forms.
- **1990s:** The proof of Fermat's Last Theorem by Andrew Wiles (1994) was achieved by proving the Modularity Theorem for semistable elliptic curves, which is essentially the Langlands correspondence for $G = \text{GL}(2)$ over $\mathbb{Q}$ with specific weights.
- **1998-1999:** Michael Harris and Richard Taylor, and independently Guy Henniart, proved the Local Langlands Correspondence for $\text{GL}(n)$ over $p$-adic fields.
- **2002:** Laurent Lafforgue proved the Global Langlands Correspondence for $\text{GL}(n)$ over function fields, using the geometry of Drinfeld shtukas, earning the Fields Medal.
- **2009:** Ngô Bảo Châu proved the Fundamental Lemma for Lie algebras (a vital component of the Arthur-Selberg trace formula), utilizing the geometry of Hitchin fibrations.
- **2018:** Vincent Lafforgue established the global correspondence (from automorphic forms to Galois representations) for arbitrary reductive groups over function fields.
- **2021+:** Laurent Fargues and Peter Scholze introduced a geometrization of the Local Langlands correspondence over $p$-adic fields using perfectoid spaces and the Fargues-Fontaine curve.

## 4. Partial Results / Verified Cases

The conjecture has been proven rigorously in several pivotal settings:
- **$G = \text{GL}(1)$:** Fully solved. This is precisely Abelian Class Field Theory (Artin reciprocity), where the correspondence is between Dirichlet characters (automorphic) and 1-dimensional Galois representations.
- **$G = \text{GL}(2)$ over $\mathbb{Q}$:** Verified for representations corresponding to elliptic curves (Modularity Theorem; Wiles, Taylor, Breuil, Conrad, Diamond).
- **$G = \text{GL}(n)$ over Function Fields:** Solved completely by Laurent Lafforgue (2002) for curves over finite fields $\mathbb{F}_q$.
- **Arbitrary $G$ over Function Fields:** The automorphic-to-Galois direction was proven by Vincent Lafforgue (2018).
- **Local Langlands for $\text{GL}(n)$:** Solved over both characteristic zero $p$-adic fields (Harris-Taylor, Henniart) and local function fields (Laumon-Rapoport-Stuhler). 
- **Symplectic and Orthogonal Groups:** James Arthur (2013) classified automorphic representations for classical groups using the trace formula, establishing functorial lifts to $\text{GL}(n)$.

## 5. Principal Obstacles

For arbitrary reductive groups over number fields (like $\mathbb{Q}$), the problem faces monumental barriers:
1. **Lack of Geometric Analogues over $\mathbb{Z}$:** In the function field case, the correspondence is proven using the moduli stack of shtukas. Over number fields, no analogous geometric object exists because $\text{Spec}(\mathbb{Z})$ has no product over $\mathbb{F}_q$. Without an "arithmetic surface," the geometric methods of V. Lafforgue cannot be translated to number fields.
2. **Trace Formula Complexities:** The standard analytic approach involves the Arthur-Selberg Trace Formula. Comparing trace formulas between groups is overwhelmingly complex. While the Fundamental Lemma was proven, stable trace formulas for non-classical reductive groups involve combinatorial and analytic nightmares that currently defy resolution.
3. **Non-Tempered Representations:** Arthur's conjectures show that for general $G$, multiple automorphic representations map to the same $L$-parameter (forming an "$L$-packet"). Furthermore, non-tempered representations require extending the parameters to include the $\text{SU}(2)$ factor, creating intricate representation-theoretic obstructions.

## 6. The Gap

The precise mathematical barrier lies in traversing from the global function field case to the global number field case for $n > 2$ or non-$\text{GL}$ groups. We currently have no methodology to systematically attach a global Galois representation to a general automorphic representation of an arbitrary group $G$ over a number field unless the group gives rise to a Shimura variety (like $\text{GL}(2)$ and modular curves). 

Because Shimura varieties only exist for specific groups (those with Hermitian symmetric spaces), most reductive groups fall into a "dark space" where neither algebraic geometry (Shimura varieties) nor the trace formula (too computationally explosive) can cross the bridge to Galois representations.

## 7. Current Research (as of June 2026)

- **The Fargues-Scholze Program:** There is intense activity in using the Fargues-Fontaine curve to bridge $p$-adic Hodge theory and the Local Langlands correspondence via derived categories of sheaves on perfectoid spaces.
- **Categorical Langlands:** Formulating the correspondence not as a bijection of sets, but as an equivalence of categories (specifically, D-modules on the moduli stack of principal $G$-bundles versus quasi-coherent sheaves on the stack of $L$-parameters).
- **Liquid Tensor Experiment / Condensed Mathematics:** Clausen and Scholze’s framework of condensed mathematics is being utilized to handle the topology of infinite-dimensional topological vector spaces that arise in automorphic representations over archimedean fields.
- *(frontier — verify)* Attempts to define "absolute shtukas" or algebraic frameworks over the mythical field with one element ($\mathbb{F}_1$) in hopes of constructing the missing geometric background for number fields.

## 8. Future Work

Leading mathematicians suggest that proving the Global Langlands Correspondence over number fields will require an entirely new foundation of arithmetic geometry that does not rely on classical Shimura varieties. 

Key open pathways include:
- Establishing a full Geometrization of the Global Langlands Correspondence by finding global arithmetic counterparts to the local Fargues-Fontaine curve.
- Proving the generalized Ramanujan-Petersson conjectures, which govern the temperedness of automorphic representations, to simplify the classification of $L$-packets.
- Developing higher categorical trace formulas that can seamlessly compare derived categories of representations rather than point-wise character traces.

## 9. Key References

- **[Foundational]** Langlands, R. P. *Problems in the Theory of Automorphic Forms.* Lectures in Modern Analysis and Applications III, Springer, 1970.
- **[SOTA / Recent]** Fargues, L., and Scholze, P. *Geometrization of the Local Langlands Correspondence.* Annals of Mathematics, 2021 (Preprint/Astérisque).
- **[SOTA / Recent]** Lafforgue, V. *Chtoucas pour les groupes réductifs et paramétrisation de Langlands globale.* Journal of the American Mathematical Society (JAMS), 2018.
- **[Survey]** Arthur, J. *The Principle of Functoriality.* Bulletin of the American Mathematical Society, 2002.
- **[Survey]** Gelbart, S. *An Elementary Introduction to the Langlands Program.* Bulletin of the American Mathematical Society, 1984.

## 10. Worked Example / Concrete Special Case

The simplest concrete instance of the Langlands Correspondence occurs for the group $G = \text{GL}(1)$ over the rational numbers $F = \mathbb{Q}$, which recovers the classical **Kronecker-Weber Theorem** and **Abelian Class Field Theory**.

1. **Automorphic Side ($G = \text{GL}(1)$):**
   The adele group is $\mathbb{A}_{\mathbb{Q}}^{\times}$, and an automorphic representation is simply a continuous, unitary character of the idele class group: 
   $$ \chi : \mathbb{Q}^{\times} \backslash \mathbb{A}_{\mathbb{Q}}^{\times} \to \mathbb{C}^{\times} $$
   By the structure of ideles, $\mathbb{Q}^{\times} \backslash \mathbb{A}_{\mathbb{Q}}^{\times} \cong \mathbb{R}_{>0} \times \hat{\mathbb{Z}}^{\times}$, where $\hat{\mathbb{Z}}^{\times}$ is the profinite completion of the integers. Therefore, finite-order automorphic characters correspond to Dirichlet characters modulo $N$.

2. **Galois Side (${}^L G = \mathbb{C}^{\times}$):**
   The dual group of $\text{GL}(1)$ is $\widehat{\text{GL}(1)} = \mathbb{C}^{\times}$. An $L$-parameter is a continuous homomorphism from the absolute Galois group $\Gamma_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ to $\mathbb{C}^{\times}$:
   $$ \phi : \Gamma_{\mathbb{Q}} \to \mathbb{C}^{\times} $$
   Because $\mathbb{C}^{\times}$ is abelian, $\phi$ must factor through the abelianization of the Galois group, $\text{Gal}(\mathbb{Q}^{\text{ab}}/\mathbb{Q})$.

3. **The Correspondence (Artin Reciprocity):**
   The Langlands correspondence asserts a natural bijection $\chi \leftrightarrow \phi$. The Kronecker-Weber theorem states that $\mathbb{Q}^{\text{ab}}$ is generated by the roots of unity, meaning $\text{Gal}(\mathbb{Q}^{\text{ab}}/\mathbb{Q}) \cong \hat{\mathbb{Z}}^{\times}$.
   
   The global Artin map provides the exact isomorphism:
   $$ \text{Art}_{\mathbb{Q}} : \mathbb{Q}^{\times} \backslash \mathbb{A}_{\mathbb{Q}}^{\times} / \mathbb{R}_{>0} \xrightarrow{\sim} \text{Gal}(\mathbb{Q}^{\text{ab}}/\mathbb{Q}) $$
   Through this isomorphism, the automorphic character $\chi$ and the Galois character $\phi$ become identical. Furthermore, their $L$-functions match perfectly: the automorphic $L$-function $L(s, \chi)$ (a Hecke $L$-function) equals the Galois $L$-function $L(s, \phi)$ (an Artin $L$-function), both of which simplify to the classical Dirichlet $L$-function $L(s, \chi_D)$ for some Dirichlet character $\chi_D$.