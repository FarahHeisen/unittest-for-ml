import pytest
from os import path

from typer.testing import CliRunner

from main import app

runner = CliRunner()


def test_app_return_exit_code_0():
    path_file_input = path.dirname(__file__)
    result = runner.invoke(app, [path_file_input + "/test_file.csv"])
    assert result.exit_code == 0
    assert path.exists(path_file_input + "/test_file.csv")
    assert ("processed" in result.stdout)


if __name__ == '__main__':
    pytest.main()
