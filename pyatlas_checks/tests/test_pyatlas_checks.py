import unittest
from click.testing import CliRunner
from pyatlas_checks.cli import cli


class TestLogCounter(unittest.TestCase):

    def test_log_counter(self):
        runner = CliRunner()
        resource_path = '/Users/matthewmanley/Documents/github/atlas-checks/pyatlas_checks/tests/data/1595568193641-2527.log'
        result = runner.invoke(cli=cli, args=['log-counter', resource_path])
        print(result)
        self.assertEqual(0, result.exit_code)

