        def bind_field(self, form, unbound_field, options):
            filters = unbound_field.kwargs.get('filters', [])
            field_type = type(unbound_field)
            if field_type == StringField:
                filters.append(strip_whitespace)
            elif field_type == DateTimeField:
                filters.append(convert_to_utc)
            return unbound_field.bind(form=form, filters=filters, **options)


