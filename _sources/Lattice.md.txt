# Lattice

In this file, we will talk about lattices.

XYZ is defined as

$$
\mathbf{b}_i^\star = \pi_i(\mathbf{b}_i) 
= \mathbf{b}_i - \sum_{j=0}^{i-1} \frac{\mathbf{b}_i \cdot \mathbf{b}_j^\star}{\lVert \mathbf{b}_j^\star \rVert^2} \, \mathbf{b}_j^\star,
$$

where $\pi_i$ is the projection on the space orthogonal to the span of 
$\{\mathbf{b}_0, \mathbf{b}_1, \ldots, \mathbf{b}_{i-1}\}$.
