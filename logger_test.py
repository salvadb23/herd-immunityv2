import pytest
from logger import Logger
import random


def test_init_logger():
    logger = Logger("test.txt")
    assert logger.file_name == "test.txt"


def test_add_to_file():
    logger = Logger("test.txt")
    logger.add_to_file("test worked", "w")


def test_write_metadeta():
    logger = Logger('test_meta.txt')
    logger.write_metadata(100, 0.2, "Snapple", 0.3, 0.4)


def test_log_time_step():
    logger = Logger("time_step.txt")
    logger.log_time_step(1)


def test_log_infection_survival():
    from person import Person
    from virus import Virus
    logger = Logger("infection_survival.txt")
    virus = Virus("Bookworm", 0.3, 0.4)
    person = Person(1, False, virus)
    still_alive = person.did_survive_infection()
    logger.log_infection_survival(person, did_die_from_infection=still_alive)


def test_log_interaction():
    from person import Person
    from virus import Virus
    virus = Virus("Bookworm", 0.3, 0.4)
    vacc_options = random.choice([True, False])
    virus_options = random.choice([None, virus])
    person = Person(1, False, virus)
    rand_person = Person(2, vacc_options, virus_options)
    logger = Logger("test_interactions")
    logger.log_interaction(person, rand_person,
                           did_infect=True, random_person_sick=False)
