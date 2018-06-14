    def validate(self):
        check_validate = super(BatchEnrollmentForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False
        try:
            rows = self.csv.data.splitlines()
            self.csv.parsed = list(csv.reader(rows))
        except csv.error as e:
            logging.error(e)
            self.csv.errors.append(['The CSV could not be parsed'])
            return False

        for row in self.csv.parsed:
            if len(row) != 5:
                err = "{} did not have 5 columns".format(row)
                self.csv.errors.append(err)
                return False
            if not row[0]:
                err = "{} did not have an email".format(row)
                self.csv.errors.append(err)
                return False
            elif "@" not in row[0]:
                # TODO : Better email check.
                err = "{} is not a valid email".format(row[0])
                self.csv.errors.append(err)
                return False
