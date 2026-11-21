
from helper_objects import Escuela

class test_Escuela_methods:
    def test_Escuela_is_empty():
        esc = Escuela("", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        assert esc.is_sender_empty() == False


    def test_Escuela_is_not_empty():
        esc = Escuela("FCA", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        assert esc.is_sender_empty() == True


    def test_Escuela_is_empty_calls_mod_sender():
        esc = Escuela("", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        esc.__mod_sender()