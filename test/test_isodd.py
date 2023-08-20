from main import is_odd


def test_isodd(capsys):
    is_odd(3)

    captured = capsys.readouterr()

    output_lines: list = captured.out.split('\n')
    output_lines.pop(1)

    assert output_lines[0] == 'Weird'

def test_iseven(capsys):
    is_odd(4)

    captured = capsys.readouterr()

    output_lines: list = captured.out.split('\n')
    output_lines.pop(1)

    assert output_lines[0] == 'Not Weird'