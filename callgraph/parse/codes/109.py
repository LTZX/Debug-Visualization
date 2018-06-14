    def is_complete(self):
        return self.kind in [s.tag for s in self.backup.scores]


