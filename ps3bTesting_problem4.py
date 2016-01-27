from ps3b_precompiled_27 import *

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    unTreatTimeSteps = 150
    timesteps = 300

    virusPopulation = []
    resistantVirusPopulation = []

    for step in range(timesteps):
        virusPopulation.append([])
        resistantVirusPopulation.append([])

    for trial in range(numTrials):
        # instance of Viruses
        viruses = []
        for num in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        # instance of Patient
        patient = TreatedPatient(viruses, maxPop)

        # First part of simulation
        for step in range(unTreatTimeSteps):
            virusPopulation[step].append(patient.update())
            resistantVirusPopulation[step].append(patient.getResistPop(['guttagonol']))

        patient.addPrescription('guttagonol')

        #Second part of simulation
        for step in range(unTreatTimeSteps, timesteps):
            virusPopulation[step].append(patient.update())
            resistantVirusPopulation[step].append(patient.getResistPop(['guttagonol']))

    # calculate the average size of the virus population
    avgVirusPopulation = [];
    avgResistantVirusPopulation = [];

    for step in range(timesteps):
        avgVirusPopulation.append(sum(virusPopulation[step]) / float(numTrials));
        avgResistantVirusPopulation.append(sum(resistantVirusPopulation[step]) / float(numTrials));

    pylab.plot(range(timesteps), avgVirusPopulation, label="Virus")
    pylab.plot(range(timesteps), avgResistantVirusPopulation, label="ResistantVirus")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Timestep")
    pylab.ylabel("Average size of the virus Population")
    pylab.legend(loc='upper right')
    #pylab.savefig('resistantVirus-simulation.png')
    pylab.show()

simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)