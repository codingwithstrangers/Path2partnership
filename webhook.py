def as_uri(self):
        """
        Converts the Topic into the URI which can be used to create a Webhook subscription.

        Returns
        -------
        str
            The Topic as an URI.
        """

        params = '&'.join(f'{name}={getattr(self, name)}' for name in self._parameters)
        return f'{self.URL}?{params}'


