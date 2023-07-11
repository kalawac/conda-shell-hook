# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from __future__ import annotations

from typing import Iterable
import pluggy

from conda.plugins.hookspec import CondaSpecs

from .shell_types import CondaShellPlugins

spec_name = "shell_plugins"
hookspec = pluggy.HookspecMarker(spec_name)
hookimpl = pluggy.HookimplMarker(spec_name)

class ShellPluginSpecs:
    """"The shell plugin hook specification namespace, to be used by developers."""

    @hookspec
    def shell_hook(self) -> Iterable[CondaShellPlugins]:
        r"""
        Register external shell plugins for use in conda.


        **Example:**

        .. code-block:: python

            import os
            from conda import plugins


            @plugins.hookimpl
            def conda_shell_plugins():
                yield plugins.CondaShellPlugins(
                    name="plugin_name",
                    summary="Conda shell plugin for example shell",
                    osexec=False,
                    script_path=os.path.abspath("./posix_script.sh"),
                    pathsep_join=":".join,
                    sep="/",
                    path_conversion=some_function,
                    script_extension=".sh",
                    tempfile_extension=None,
                    command_join="\n",
                    run_script_tmpl='. "%s"',
                    unset_var_tmpl="unset %s",
                    export_var_tmpl="export %s='%s'",
                    set_var_tmpl="%s='%s'",
                )
        """