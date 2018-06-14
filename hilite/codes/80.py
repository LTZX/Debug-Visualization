class EnrollmentForm(BaseForm):
    name = StringField(u'Name', validators=[validators.optional()])
    email = EmailField(u'Email',
                       validators=[validators.required(), validators.email()])
    sid = StringField(u'SID', validators=[validators.optional()])
    secondary = StringField(u'Secondary Auth (e.g Username)',
                            validators=[validators.optional()])
    role = SelectField(u'Role',
                       choices=[(r, r.capitalize()) for r in VALID_ROLES])

