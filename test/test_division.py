from main import division

def test_division_int(capsys):
    division(3, 5)

    captured = capsys.readouterr()
    output_lines: list = captured.out.split('\n')
    output_lines.pop(1)

    assert output_lines[0] == '0'


def test_division_float(capsys):
    division(3, 5)
    captured = capsys.readouterr()
    output_lines: list = captured.out.split('\n')
    output_lines.pop(0)

    assert output_lines[0] == '0.6'

