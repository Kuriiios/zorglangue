import os
import sys
from app.components.zorglangue_translator import zorglangue_translator 

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    ) ))

def test_zorglangue_translator():
    assert zorglangue_translator('Vive Zorglub !') == 'eviV bulgroZ !'