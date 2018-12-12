import pytest
from simulation import Simulation
from virus import Virus
from person import Person
import random


# Works
def test_interaction():
    simulation = Simulation(1000, 0.2, Virus("Snapple", 0.2, 0.4))
    simulation.logger.file_name = 'test_interaction.txt'
    vacc_options = random.choice([True, False])
    virus_options = random.choice([None, Virus])
    person = Person(1, False, simulation.virus)
    rand_person = Person(2, vacc_options, simulation.virus)
    simulation.interaction(person, rand_person)
