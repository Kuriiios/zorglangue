from app.components.zorglangue_translator import zorglangue_translator 

def test_zorglangue_translator():
    assert zorglangue_translator('Vive Zorglub !') == 'eviV bulgroZ !'