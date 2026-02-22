from src.main import main


def test_main_prints_message(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from python-project!" in captured.out
