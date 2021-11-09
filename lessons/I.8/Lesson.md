To sum up the last couple nodes, here are all the single-qubit gates we've met
so far, shown with their matrix representations, circuit elements, and their
actions on the basis states. Feel free to come back to this node any time and
use it as a reference.

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> Gate </th>
  <th> Matrix </th>
  <th> Circuit element(s) </th>
  <th> Basis state action </th>
 </tr>
 <tr>
  <td style="text-align:center"> $X$  </td>
  <td style="text-align:center"> $\begin{pmatrix} 0 & 1 \\1 & 0 \\ \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/x.svg" width="180x"> </td>
  <td style="text-align:center"> $$\begin{align*} X\vert 0 \rangle &= \vert 1 \rangle \\ X\vert 1 \rangle &= \vert 0 \rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $H$ </td>
  <td style="text-align:center"> $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/h.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} H\vert 0 \rangle &= \frac{1}{\sqrt{2}} (\vert 0 \rangle + \vert 1 \rangle) \\ H\vert 1 \rangle &= \frac{1}{\sqrt{2}} (\vert 0 \rangle - \vert 1 \rangle) \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $Z$ </td>
  <td style="text-align:center"> $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/z.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} Z\vert 0 \rangle &= \vert 0 \rangle \\ Z\vert 1 \rangle &= -\vert 1 \rangle \end{align*}$$ </td>
 </tr>
 <tr>
   <td style="text-align:center"> $S$ </td>
   <td style="text-align:center"> $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$ </td>
   <td style="text-align:center"> <img src="pics/s.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} S\vert 0 \rangle &= \vert 0 \rangle \\ S\vert 1 \rangle &= i\vert 1 \rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $T$ </td>
  <td style="text-align:center"> $\begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/t.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} T\vert 0 \rangle &= \vert 0 \rangle \\ T\vert 1 \rangle &= e^{i\pi/4}\vert 1 \rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $Y$ </td>
  <td style="text-align:center"> $\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/y.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} Y\vert 0 \rangle &= i \vert 1 \rangle \\ Y\vert 1 \rangle &= -i\vert 0 \rangle \end{align*}$$ </td>
 </tr> 
 <tr>
  <td style="text-align:center"> $RZ$ </td>
  <td style="text-align:center"> $\begin{pmatrix} e^{-i \frac{\theta}{2}} & 0 \\ 0 & e^{i \frac{\theta}{2}} \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/rz.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} RZ(\theta)\vert 0 \rangle &= e^{-i \frac{\theta}{2}} \vert 0 \rangle \\ RZ(\theta)\vert 1 \rangle &= e^{i \frac{\theta}{2}} \vert 1 \rangle \end{align*}$$ </td>
 </tr>     
 <tr>
  <td style="text-align:center"> $RX$ </td>
  <td style="text-align:center"> $\begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\ -i\sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right) \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/rx.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} RX(\theta)\vert 0 \rangle &= \cos \frac{\theta}{2} \vert 0 \rangle - i \sin \frac{\theta}{2} \vert 1\rangle \\ RX(\theta) \vert 1 \rangle &=  - i \sin \frac{\theta}{2} \vert 0 \rangle +  \cos \frac{\theta}{2}  \vert 1\rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $RY$ </td>
  <td style="text-align:center"> $ \begin{pmatrix} \cos \left(\frac{\theta}{2} \right) & - \sin \left(\frac{\theta}{2} \right) \\ \sin \left(\frac{\theta}{2} \right)& \cos \left(\frac{\theta}{2} \right)   \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/ry.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} RY(\theta)\vert 0 \rangle &= \cos \frac{\theta}{2} \vert 0 \rangle + \sin \frac{\theta}{2} \vert 1 \rangle \\ RY(\theta) \vert 1 \rangle &=  - \sin \frac{\theta}{2} \vert 0 \rangle +  \cos \frac{\theta}{2}  \vert 1 \rangle \end{align*}$$ </td>
 </tr>
</table>
