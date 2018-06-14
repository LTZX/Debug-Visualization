    @property
    def data(self):
        return {
            'supplied': self.supplied_version,
            'correct': self.correct_version.current_version,
            'download_link': self.correct_version.download_link
