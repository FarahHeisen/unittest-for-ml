import unittest
from os import path

from typer.testing import CliRunner

from main import app

runner = CliRunner()


class TestCli(unittest.TestCase):

    def test_app_return_exit_code_0(self):
        path_file_input = path.dirname(__file__)
        result = runner.invoke(app, [path_file_input + "/test_file.csv"])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(path.exists(path_file_input + "/test_file.csv"))
        self.assertTrue("processed" in result.stdout)


if __name__ == '__main__':
    unittest.main()
