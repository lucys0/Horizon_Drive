# ----------------------------------------------------------
# Magnetisation.py
# Voice coil-permanent magnet electromagnetic interaction force calculation
# End of study internship 2020
# SLT ROUDET
# January-June 2020
#
# The whole program below helps to calculate the electromagnetic
# force between a permanent magnet (Rm,lm,Nm,Br,Nm) and a voice
# coil (rc,Rc,lc,Nr,Nz) as a function of the distance z between
# their two centres and the input current. The calculation is
# based on the filament method explained by J. M. Camacho and
# V. Sosa in "Alternative method to calculate the magnetic
# field of permanent magnets with azimuthal symmetry".
#
# -----------------------------------------------------------

import scipy.special
from math import *
import matplotlib.pyplot as plt
import time


rc = 1.25E-02  # inner voice coil radius
Rc = 1.29E-02  # outside voice coil radius
Rm = 0.0045  # magnet radius
lm = 0.003  # magnet length
lc = 0.013  # coil length
h = 0   # distance between edge of the voice coil and the magnet surface
z = (lm + lc) / 2 + h  # distance between the centers
Nr = 2  # voice coil number of layers
Nz = 55  # number of turn in the coil
Nm = 2000  # number of turns used to model the ferrite magnet
Br = 0.2  # magnet remanence
u0 = 1.25664E-06  # vacuum permeability
I2 = (Br*lm)/(u0*Nm)


def Ff(r1, r2, z, I):
    """
    This program calculate the interaction force between two
     circular coaxial loops.
    The current in the second loop however isn't specified as
    it is supposed to be the permanent magnet.
    :param r1: First loop's radius (m)
    :param r2: Second loop's radius (m)
    :param z: Distance between their center (m)
    :param I: Current in the first loop (A)
    :return: Resulting EM force (N)
    """
    m = 4*r1*r2/((r1+r2)**2 + z**2)
    K = scipy.special.ellipk(m)
    E = scipy.special.ellipe(m)
    F = u0*I*I2*z*sqrt(m/(4*r1*r2))*(K-(((m/2)-1)/(m-1))*E)
    return(F)


def force(I, z):
    """
    This program uses the filament method to calculate the
     electromagnetic force between a permanent magnet and a
      voice coil. It first approaches the voice coil and the
       magnet as discretized single coaxial current loops.
    The total force between them then results from the
     superposition of every interaction forces summed.
    :param I: Current carried by the voice coil
    :param z: Distance between the center of the voice coil and
     the center of the magnet
    :return: Resulting EM force (uN)
    """
    F = []
    for nm in range(1, Nm):
        for nr in range(1, Nr):
            for nz in range(1, Nz):
                x = Rc + ((nr-1)/(Nr-1))*(Rc-rc)
                y = -0.5*(lm+lc) + ((nz-1)/(Nz-1))*lc + ((nm-1)/(Nm-1))*lm
                f = Ff(x, Rm, z+y, I)
                F += [f]
    return(sum(F)*1000000)


def graphe_Nm(z):
    """
    graphe_Nm() calculate the EM force for various current
     carried by the voice coil.
    The extreme forces value are printed as well as the
     approached linear equation and the execution time.
    :param z: Distance between their center (see above)
    :return: The program returns two lists: one with the
     discretized current, the other with the associated EM force.
     Both the values and the approached linear equation are plotted.
    """
    start_time = time.time()  # Time count starts
    f = []
    C = []
    for i in range(40):  # Current's discretization
        c = i/100
        f += [-force(c, z)]
        C += [c]

    if not graphe_h():
        print("Minimum value : " + str(f[1]) + " uN")
        print("Maximum value : " + str(f[-1]) + " uN")
        print("Linear equation : y = " +
              str((f[-1] - f[0]) / (C[-1] - C[0])) + "x")

        plt.plot(C, f, '.', ms=8, label="discretized value")
        plt.plot(C, f, 'r-', ms=2, label="associated linear equation")
        plt.title('EM force as a function of the voice coil carried current')
        plt.xlabel('Current (A)')
        plt.ylabel('Force (uN)')
        plt.legend()
        plt.show()

    print("Execution time : %s secondes" % (time.time() - start_time))

    return(f, C)


def graphe_h():
    """
    This program shows the previous proportionality coefficient
     depending on the distance h between the magnet surface and
      the voice coil's edge.
    :return: The EM force coefficient is plotted as a function
     of the height.
     The linear equation's coefficient list is printed as for
      the execution time.
    """
    start_time = time.time()  # Time count starts
    H = []
    F = []
    for h in range(0, 30):
        z = (lm + lc) / 2 + h/6000
        f, C = graphe_Nm(z)
        F += [(f[-1] - f[0]) / (C[-1] - C[0])]
        H += [h]

    plt.plot(H, F, '.', ms=8)
    plt.title('EM force variations as a function of the coil-magnet distance')
    plt.xlabel('Height (mm)')
    plt.ylabel('Force (uN)')
    plt.legend()
    plt.show()
    print("Execution time : %s secondes" % (time.time() - start_time))
    print(F)

# graphe_Nm(z)
# graphe_h()
