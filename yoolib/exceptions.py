class YooError(Exception):
    def as_status(self, status):
        self.status = status
        return self
