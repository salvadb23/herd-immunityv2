class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        dividors = "==========================="
        data = "{}\nVirus name: {}\nReproduction number: {}\nVaccination percentage: {}\nMortality rate: {}\nPopulation number: {}\n{}\n".format(
            dividors,                                                                                           virus_name, basic_repro_num, vacc_percentage, mortality_rate, pop_size, dividors)
        self.add_to_file(data, "w")
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        if did_infect:
            self.add_to_file("Person {} infected Person {}!\n".format(
                person._id, random_person._id), "a")
        else:
            self.add_to_file("Person {} did not infect Person{}!\n".format(
                person._id, random_person._id), "a")
            if random_person_vacc:
                self.add_to_file(" This person was vaccinated!\n", "a")
            elif random_person_sick:
                self.add_to_file(" This person was already sick!\n", "a")
            self.add_to_file("\n", "a")

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .did_survive_infection() method
        '''
        if did_die_from_infection:
            self.add_to_file(
                "Person {} died from infection\n".format(person._id), "a")
        else:
            self.add_to_file(
                "Person {} survived infection\n".format(person._id), "a")

    def log_time_step(self, time_step_number):
        # Fix this in simulation
        self.add_to_file("Time step {} ended, beginning {}\n".format(
            time_step_number, time_step_number + 1), "a")

    def add_to_file(self, data, mode):
        with open(self.file_name, mode) as file:
            file.writelines(list(data))
