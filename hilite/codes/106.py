    @staticmethod
    def statistics(self):
        db.session.query(Backup).from_statement(
            db.text("""SELECT date_trunc('hour', backup.created), count(backup.id)  FROM backup
            WHERE backup.created >= NOW() - '1 day'::INTERVAL
            GROUP BY date_trunc('hour', backup.created)
            ORDER BY date_trunc('hour', backup.created)""")).all()


