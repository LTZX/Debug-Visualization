    @hybrid_property
    def active(self):
        return dt.utcnow() < self.lock_date  # TODO : Ensure all times are UTC


