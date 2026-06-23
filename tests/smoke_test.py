from unittest import TestCase

import fl_cmd


class SmokeTest(TestCase):
    def test_import(self) -> None:
        assert fl_cmd.FileClose == 57602
