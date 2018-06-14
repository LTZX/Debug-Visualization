    def __init__(self):
        APISchema.__init__(self)
        self.parser.add_argument('assignment', type=str, required=True,
                                 help='Name of Assignment')
        self.parser.add_argument('messages', type=json_field, required=True,
                                 help='Backup Contents as JSON')

        # Optional - probably not needed now that there are two endpoints
        self.parser.add_argument('submit', type=bool,
                                 help='Flagged as a submission')
        self.parser.add_argument('submitter', help='Name of Assignment')

