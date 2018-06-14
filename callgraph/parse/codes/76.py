    @property
    def message(self):
        return ("Incorrect client version. Supplied version was {}. " +
                "Correct version is {}.".format(
                    self.supplied_version,
                    self.correct_version.current_version))

