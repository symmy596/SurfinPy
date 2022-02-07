Bulk Theory
===========

Bulk phase diagrams enable the comparison of the thermodynamic stability of various different bulk phases under different chemical potentials giving valuable insight in to the synthesis of solid phases.
This theory example will consider a series of bulk phases which can be defined through a reaction scheme across all phases,
thus for this example including MgO, :math:`H_2O` and :math:`CO_2` as reactions and A as a generic product.

.. math::
    x\text{MgO} + y\text{H}_2\text{O} + z\text{CO}_2 \rightarrow \text{A}

The system is in equilibrium when the chemical potentials of the reactants and product are equal; i.e. the change in Gibbs free energy is :math:`$\delta G_{T,p} = 0$`.

.. math::
	\delta G_{T,p} = \mu_A - x\mu_{\text{MgO}} - y\mu_{\text{H}_2\text{O}} - z\mu_{\text{CO}_2} = 0

Assuming that :math:`H_2O` and :math:`CO_2` are gaseous species, :math:`$\mu_{CO_2}$` and :math:`$\mu_{H_2O}$` can be written as

.. math::
	\mu_{\text{H}_2\text{O}} = \mu^0_{\text{H}_2\text{O}} + \Delta\mu_{\text{H}_2\text{O}}

and

.. math::
	\mu_{\text{CO}_2} = \mu^0_{\text{CO}_2} + \Delta\mu_{\text{CO}_2}

The chemical potential :math:`$\mu^0_x$` is the partial molar free energy of any reactants or products (x) in their standard states,
in this example we assume all solid components can be expressed as

.. math::
    \mu_{\text{component}} = \mu^0_{\text{component}}

Hence, we can now rearrange the equations to produce;

.. math::
	\mu^0_A - x\mu^0_{\text{MgO}} - y\mu^0_{\text{H}_2\text{O}} - z\mu^0_{CO_2} = y\Delta\mu_{H_2O} + z\Delta\mu_{CO_2}

As :math:`$\mu^0_A$` corresponds to the partial molar free energy of product A, we can replace the left side with the Gibbs free energy (:math:`$\Delta G_{\text{f}}^0$`).

.. math::
	\delta G_{T,p} = \Delta G_{\text{f}}^0 - y\Delta\mu_{\text{H}_2\text{O}} - z\Delta\mu_{\text{CO}_2}

At equilibrium :math:`$\delta G_{T,p} = 0$`, and hence

.. math::
	\Delta G_{\text{f}}^0 = y\Delta\mu_{\text{H}_2\text{O}} + z\Delta\mu_{\text{CO}_2}

Thus, we can find the values of :math:`$\Delta\mu_{H_2O}$` and :math:`$\Delta\mu_{CO_2}$` (or :math:`$(p_{H_2O})^y$` and :math:`$p_{CO_2}^z$` when Mg-rich phases are in thermodynamic equilibrium; i.e.
they are more or less stable than MgO.
This procedure can then be applied to all phases to identify which is the most stable, provided that the free energy :math:`$\Delta G_f^0$` is known for each Mg-rich phase.

The free energy can be calculated using

.. math::
    \Delta G^{0}_{f} = \sum\Delta G_{f}^{0,\text{products}} - \sum\Delta G_{f}^{0,\text{reactants}}

Where for this example the free energy (G) is equal to the calculated DFT energy (:math:`U_0`).

Temperature
~~~~~~~~~~~

The previous method will generate a phase diagram at 0 K. This is not representative of normal conditions.
Temperature is an important consideration for materials chemistry and we may wish to evaluate the phase thermodynamic stability at various synthesis conditions.

As before the free energy can be calculated using;

.. math::
    \Delta G^{0}_{f} = \sum\Delta G_{f}^{0,\text{products}} - \sum\Delta G_{f}^{0,\text{reactants}}

Where for this example the free energy (G) for solid phases is equal to is equal to the calculated DFT energy :math:`(U_0)`.
For gaseous species, the standard free energy varies significantly with temperature, and as DFT simulations are designed for condensed phase systems,
we use experimental data to determine the temperature dependent free energy term for gaseous species, where :math:`$S_{expt}(T)$` is specific entropy value for a given T and  :math:`$H-H^0(T)$` is the,
both can be obtained from the NIST database and can be calculated as;

.. math::
    G =  U_0 + (H-H^0(T) - T S_{\text{expt}}(T))

Pressure
--------

In the previous tutorials we went through the process of generating a simple phase diagram for bulk phases and introducing temperature dependence for gaseous species.
This useful however, sometimes it can be more beneficial to convert the chemical potentials (eVs) to partial pressure (bar).

Chemical potential can be converted to pressure values using

.. math::
    P & = \frac{\mu_O}{k_B T} ,

where P is the pressure, :math:`$\mu$` is the chemical potential of oxygen, $k_B$ is the Boltzmann constant and T is the temperature.
