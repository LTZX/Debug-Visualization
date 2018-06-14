class Config:
    SECRET_KEY = 'samplekey'
    GOOGLE = {
        'consumer_key': os.getenv('GOOGLE_ID', 'fake'),
        'secret': os.getenv('GOOGLE_SECRET', 'fake')
    }

