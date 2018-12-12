

# Done
class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    # TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("MRSA", 0.2, 0.2)
    assert virus.name == "MRSA"
    assert virus.repro_rate == 0.2
    assert virus.mortality_rate == 0.2


def test_virus_instantiation1():
    virus = Virus("Snapple", 0.2, 0.5)
    assert virus.name == "Snapple"
    assert virus.repro_rate == 0.2
    assert virus.mortality_rate == 0.5


def test_virus_instantiation2():
    virus = Virus("Apple", 0.5, 0.1)
    assert virus.name == "Apple"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.1
