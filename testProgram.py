from random import randint
import hello


def test_payCalculator_prints_correct_result(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"Chuck")
    hello.hello()

    out, err = capfd.readouterr()
    print(out)
    assert out == 'Howdy Chuck\n'
