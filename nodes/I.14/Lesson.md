As we near the end of this module, here is an updated reference of all the
gates you've learned about so far, both single- and multi-qubit.

## Multi-qubit gate reference

<table style="align:center" cellspacing="20" cellpadding="15">
 <tr>
  <th> Gate </th>
  <th> Matrix </th>
  <th> Circuit element(s) </th>
  <th> Basis state action </th>
 </tr>
 <tr>
  <td style="text-align:center"> $CNOT$  </td>
  <td style="text-align:center"> $\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 1 & 0
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/cnot.svg" width="250x"> </td>
  <td style="text-align:center"> $$\begin{align*} CNOT\vert 00 \rangle &= \vert 00 \rangle \\ CNOT\vert 01 \rangle &= \vert 01 \rangle \\ CNOT\vert 10 \rangle &= \vert 11 \rangle \\ CNOT\vert 11 \rangle &= \vert 10 \rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $CZ$ </td>
  <td style="text-align:center"> $
    \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & -1
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/cz.svg" width="250px"> </td>
  <td style="text-align:center"> $$\begin{align*} CZ\vert 00 \rangle &= \vert 00 \rangle \\ CZ\vert 01 \rangle &= \vert 01 \rangle \\ CZ\vert 10 \rangle &= \vert 10 \rangle \\ CZ\vert 11 \rangle &= -\vert 11 \rangle \end{align*}$$ </td>  
 </tr>
 <tr>
  <td style="text-align:center"> $CRZ$ </td>
  <td style="text-align:center"> $
    \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & e^{-i \frac{\theta}{2}} & 0 \\
    0 & 0 & 0 & e^{i \frac{\theta}{2}}
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/crz.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*}
  CZ\vert 00 \rangle &= \vert 00 \rangle \\
  CZ\vert 01 \rangle &= \vert 01 \rangle \\
  CZ\vert 10 \rangle &= e^{-i \frac{\theta}{2}} \vert 10 \rangle \\
  CZ\vert 11 \rangle &= e^{i \frac{\theta}{2}} \vert 11 \rangle \end{align*}$$ </td>  
 </tr> 
 <tr>
  <td style="text-align:center"> $CRX$ </td>
  <td style="text-align:center"> $
    \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & \cos \left(\frac{\theta}{2} \right) & -i \sin \left(\frac{\theta}{2} \right) \\
    0 & 0 &  -i \sin \left(\frac{\theta}{2} \right) &  \cos \left(\frac{\theta}{2} \right)
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/crx.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*}
  CRX(\theta)\vert 00 \rangle &= \vert 00 \rangle \\
  CRX(\theta)\vert 01 \rangle &= \vert 01 \rangle \\
  CRX(\theta)\vert 10 \rangle &= \cos \frac{\theta}{2} \vert 10 \rangle - i \sin \frac{\theta}{2} \vert 11\rangle \\
  CRX(\theta)\vert 11 \rangle &= - i \sin \frac{\theta}{2} \vert 10 \rangle +  \cos \frac{\theta}{2}  \vert 11\rangle \end{align*}$$ </td>
 </tr>
 <tr>
  <td style="text-align:center"> $CRY$ </td>
  <td style="text-align:center"> $
    \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & \cos \left(\frac{\theta}{2} \right) & - \sin \left(\frac{\theta}{2} \right) \\
    0 & 0 &  \sin \left(\frac{\theta}{2} \right) &  \cos \left(\frac{\theta}{2} \right)
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/cry.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*}
  CRY(\theta)\vert 00 \rangle &= \vert 00 \rangle \\
  CRY(\theta)\vert 01 \rangle &= \vert 01 \rangle \\
  CRY(\theta)\vert 10 \rangle &= \cos \frac{\theta}{2} \vert 10 \rangle + \sin \frac{\theta}{2} \vert 11\rangle \\
  CRY(\theta)\vert 11 \rangle &= -\sin \frac{\theta}{2} \vert 10 \rangle +  \cos \frac{\theta}{2}  \vert 11\rangle \end{align*}$$ </td>
 </tr>  
 <tr>
  <td style="text-align:center"> $CU$ </td>
  <td style="text-align:center"> $\begin{pmatrix} I_2 & 0 \\ 0 & U \\ \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/cu.svg" width="100px"> </td>
  <td style="text-align:center"> $$\begin{align*} CU\vert 00 \rangle &= \vert 00 \rangle \\ CU\vert 01 \rangle &= \vert 01 \rangle \\ CU\vert 10 \rangle &= \vert 1 \rangle \otimes U\vert 0 \rangle \\ CU\vert 11 \rangle &= \vert 1 \rangle \otimes U \vert 1 \rangle \end{align*}$$ </td>    
 </tr>
 <tr>
  <td style="text-align:center"> $SWAP$  </td>
  <td style="text-align:center"> $\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0\\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/swap.svg" width="100px"> </td>
   <td style="text-align:center"> $$\begin{align*} SWAP\vert 00 \rangle &= \vert 00 \rangle \\ SWAP\vert 01 \rangle &= \vert 10 \rangle \\ SWAP\vert 10 \rangle &= \vert 01 \rangle \\ SWAP\vert 11 \rangle &= \vert 11 \rangle \end{align*}$$ </td> 
 </tr>
 <tr>
  <td style="text-align:center"> $TOF$  </td>
  <td style="text-align:center"> $\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/toffoli.svg" width="100px"> </td>
   <td style="text-align:center"> $$\begin{align*} TOF\vert 000 \rangle &= \vert 000 \rangle \\ TOF\vert 001 \rangle &= \vert 001 \rangle \\ \vdots &= \vdots \\ TOF \vert 101 \rangle &= \vert 101 \rangle  \\ TOF \vert 110 \rangle &= \vert 111 \rangle  \\ TOF \vert 111 \rangle &= \vert 110 \rangle \end{align*}$$ </td>   
 </tr>
 <tr>
  <td style="text-align:center"> $CCZ$  </td>
  <td style="text-align:center"> $\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & -1\\
    \end{pmatrix}$ </td>
  <td style="text-align:center"> <img src="pics/ccz.svg" width="250px"> </td>
   <td style="text-align:center"> $$\begin{align*} CCZ\vert 000 \rangle &= \vert 000 \rangle \\ \vdots &= \vdots \\ CCZ \vert 110 \rangle &= \vert 110 \rangle  \\ CCZ \vert 111 \rangle &= -\vert 111 \rangle \end{align*}$$ </td>     
 </tr>  
</table>


## Single-qubit gate reference

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