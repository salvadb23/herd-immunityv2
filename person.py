import random
random.seed(42)
from virus import Virus

# Person is done


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_alive = True
        self.is_vaccinated = is_vaccinated
        self.infection = infection

    def did_survive_infection(self):
        if self.infection != None:
            if random.random() < self.infection.mortality_rate:
                return False
            else:
                return True


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''

person = Person(1, False, Virus("Snapple", 0.2, 0.4))
print(person.infection)


def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id is 2
    assert person.is_alive == True
    assert person.is_vaccinated == False
    assert person.infection is None


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_alive == True
    assert person.is_vaccinated == False
    assert person.infection is virus


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert True
    else:
        assert person.is_alive is False
