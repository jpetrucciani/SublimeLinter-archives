"""
@author jacobi petrucciani
@desc the linter for archives inside sublime text
"""
import logging
from SublimeLinter.lint import PythonLinter  # type: ignore
from typing import List


logger = logging.getLogger("SublimeLinter.plugins.archives")


class Archives(PythonLinter):
    """
    @desc archives linter plugin
    """

    cmd = ("archives", "--ignore-exceptions", "-")
    defaults = {
        "selector": "source.python",
        # Ignore codes Sublime can auto-fix
        "ignore_fixables": True,
    }

    regex = (
        r"^.+?:(?P<line>\d+):(?P<col>\d+): "
        r"(?:(?P<error>(?:F(?:40[24]|8(?:12|2[123]|31))|E(?:11[23]|90[12]|999)))|"
        r"(?P<warning>\w+\d+):?) "
        r"(?P<message>.*)"
    )
    multiline = True

    def on_stderr(self, stderr: bool) -> None:
        """
        @cc 1
        @desc is on stderr
        @arg stderr: if is on stderr
        """
        # if stderr:
        #     self.notify_failure()
        #     logger.error(stderr)

    def parse_output(self, proc, virtual_view) -> List:
        """
        @cc 2
        @desc parse the output of archives
        @ret a list of errors
        """
        errors = super().parse_output(proc, virtual_view)

        filtered_errors = []
        for error in errors:
            # code = error["code"]

            filtered_errors.append(error)

        return filtered_errors

    def reposition_match(self, line, col, m, virtual_view):
        """
        @cc 1
        @desc Reposition white-space errors.
        """
        # code = m.error or m.warning

        return super().reposition_match(line, col, m, virtual_view)
