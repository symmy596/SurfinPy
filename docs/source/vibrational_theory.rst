Vibrational Theory
==================

The vibrational entropy allows for a more accurate calculation of phase diagrams without the need to include experimental corrections for solid phases.

The standard free energy varies significantly with temperature, and as DFT simulations are designed for condensed phase systems, 
we use experimental data to determine the temperature dependent free energy term for gaseous species obtained from the NIST database.  
In addition we also calculate the vibrational properties for the solid phases modifying the free energy (G) for solid phases to be;

.. math::
    \Delta G_f = U_0 + U_{\text{ZPE}} + A_{\text{vib}}

:math:`$U_0$` is the calculated internal energy from a DFT calculation, :math:`$U_{ZPE}$` is the zero point energy and :math:`$S_{vib}$` is the vibrational entropy.

.. math::
	U_{\text{ZPE}} = \sum_i^{3n} \frac{R \theta_i}{2}

where :math:`$A_{vib}$` is the vibrational Helmholtz free energy and defined as;

.. math::
	A_{\text{vib}} = \sum_i^{3n} RT \ln{(1-e^{-\theta_i/T})}

3n is the total number of vibrational modes, n is the number of species and :math:`$\theta_i$` is the characteristic vibrational temperature (frequency of the vibrational mode in Kelvin).

.. math::
	\theta_i = \frac{h\nu_i}{k_B}
