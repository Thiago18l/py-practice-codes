from main import output

def test_lines(capsys):
    output(2, 3)
    captured = capsys.readouterr()

    output_lines: list = captured.out.split('\n')
    
    output_lines.pop(3)
    
    for line in output_lines:
        linha = str(line)
        if linha is not None:
            expected = None
            if '5' in line:
                expected = str(2 + 3)
            elif '-1' in line:
                expected = str(2 - 3)
            elif '6' in line:
                expected =  str(2 * 3)
            
            assert linha == expected
