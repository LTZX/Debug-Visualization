class AssignmentForm(BaseForm):
    display_name = StringField(u'Display Name',
                               validators=[validators.required()]),
    name = StringField(u'Offering', validators=[validators.required()])
    due_date = DateTimeField(u'Due Date (Pacific Time)',
                             default=dt.datetime.now,
                             validators=[validators.required()])
    lock_date = DateTimeField(u'Lock Date (UTC)',
                              default=dt.datetime.now,
                              validators=[validators.required()])
    max_group_size = IntegerField(u'Max Group Size', default=1,
                                  validators=[validators.required()])
    url = StringField(u'URL',
                      validators=[validators.optional(), validators.url()])
    revisions = BooleanField(u'Enable Revisions', default=False,
                             validators=[validators.optional()])
    autograding_key = StringField(u'Autograder Key', [validators.optional()])

