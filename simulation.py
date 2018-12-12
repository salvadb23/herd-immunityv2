import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    def __init__(self, pop_size, vacc_percentage, initial_infected=1, virus=None):
        self.logger = Logger("interactions.txt")
        self.pop_size = pop_size  # Int
        self.next_person_id = 0
        self.virus = virus
        self.initial_infected = initial_infected  # Int
        # FIXME: Use the variables below
        self.total_infected = 0
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.current_infected = 0
        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        id = 0

        for _ in range(initial_infected):
            person = Person(id, False, self.virus)
            population.append(person)
            id += 1
            self.current_infected += 1
        for _ in range(self.pop_size - len(population)):
            # We need to randomize our people getting vaccinated
            person = Person(id, False)
            population.append(person)
            id += 1
        return population

    # def _simulation_should_continue(self):
    #     return self.pop_size > 0 and self.total_dead < self.pop_size

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # should_continue = self._simulation_should_continue()
        # time_step_counter = 0
        self.time_step()

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper

        # while should_continue:
        #     self.time_step()
        #     self.logger.log_time_step(time_step_counter)
        #     time_step_counter += 1
        # self.logger.add_to_file(
        #     "'The simulation has ended after {time_step_counter} turns.'.format(time_step_counter)", "a")

    def choose_infected(self):
        return random.choice(self.newly_infected)

    # Test later today in an index.py file
    def time_step(self):
        healthy_people = []
        infected_people = []
        for person in self.population:
            if person.infection:
                infected_people.append(person)
            else:
                healthy_people.append(person)

        for person in infected_people:
            for _ in range(101):
                self.interaction(
                    person, random_person=random.choice(healthy_people))

        for person in self.population:
            if person.did_survive_infection():
                self.logger.log_infection_survival(
                    person, did_die_from_infection=False)
            else:
                self.logger.log_infection_survival(
                    person, did_die_from_infection=True)

        self._infect_newly_infected()

    def append_newly_infected(self, random_person):
        if random_person.is_vaccinated() == False:
            num = random.randint(0, 1)
            if num < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                random_person.infection = virus

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True
        if random_person.is_vaccinated:
            self.logger.log_interaction(
                person, random_person, did_infect=False, random_person_vacc=True)
        elif random_person.infection:
            self.logger.log_interaction(
                person, random_person, random_person_sick=True, random_person_vacc=False)
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # for person in self.population:
        #     for id in self.newly_infected:
        #         if person._id == id:
        #             person.infection = self.virus
        # self.newly_infected = []


if __name__ == "__main__":

    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
