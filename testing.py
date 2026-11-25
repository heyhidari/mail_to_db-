from unittest import mock
from helper_objects import Escuela

class Test_Escuela_methods:
    def test_Escuela_is_empty(self):
        esc = Escuela("", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        assert esc.is_sender_empty() == True


    def test_Escuela_is_not_empty(self):
        esc = Escuela("FCA", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        assert esc.is_sender_empty() == False


    def test_Escuela_is_empty_calls_mod_sender(self):
        esc = Escuela("", "Maestria", "Fiscal", "20-11-2026", 10, "Edgard Huerta")
        
        with mock.patch("builtins.input", lambda *args, **kwargs:"FCA"):
            result = esc._Escuela__mod_sender("_siglas")
            assert result == "Se modificó _siglas con el valor: FCA"
            assert esc._siglas == "FCA"