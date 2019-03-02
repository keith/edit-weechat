# Open your $EDITOR to compose a message in weechat
#
# Usage:
# /edit
#
# Optional settings:
# /set plugins.var.python.edit.editor "vim -f"
# /set plugins.var.python.edit.terminal "xterm"
# /set plugins.var.python.edit.run_externally "false"
#
# History:
# 10-18-2015
# Version 1.0.2: Add the ability to run the editor in a external terminal
# Version 1.0.1: Add configurable editor key
# Version 1.0.0: initial release

import os
import os.path
import shlex
import subprocess
import weechat


def weechat_config_dir():
    return os.path.expanduser(os.environ.get("WEECHAT_HOME", "~/.weechat/"))


PATH = os.path.join(weechat_config_dir(), "message.txt")


def editor_process_cb(data, command, return_code, out, err):
    buf = data

    if return_code != 0:
        cleanup(PATH, buf)
        weechat.prnt("", "{}: {}".format(
            err.strip(),
            return_code
        ))
        return weechat.WEECHAT_RC_ERROR

    if return_code == 0:
        read_file(PATH, buf)
        cleanup(PATH, buf)

    return weechat.WEECHAT_RC_OK


def cleanup(path, buf):
    try:
        os.remove(path)
    except (OSError, IOError):
        pass

    weechat.command(buf, "/window refresh")


def read_file(path, buf):
    try:
        with open(PATH) as f:
            text = f.read()

        weechat.buffer_set(buf, "input", text)
        weechat.buffer_set(buf, "input_pos", str(len(text)))

    except (OSError, IOError):
        pass

    weechat.command(buf, "/window refresh")


def hook_editor_process(terminal, editor, path, buf):
    term_cmd = "{} -e".format(terminal)
    editor_cmd = "{} {}".format(editor, path)
    weechat.hook_process("{} \"{}\"".format(
        term_cmd,
        editor_cmd
    ), 0, "editor_process_cb", buf)


def run_blocking(editor, path, buf):
    cmd = shlex.split(editor) + [path]
    code = subprocess.Popen(cmd).wait()

    if code != 0:
        cleanup(path,  buf)

    read_file(path, buf)


def edit(data, buf, args):
    editor = (weechat.config_get_plugin("editor")
              or os.environ.get("EDITOR", "vim -f"))

    terminal = (weechat.config_get_plugin("terminal")
                or os.getenv("TERMCMD"))

    terminal = terminal or "xterm"

    run_externally = weechat.config_string_to_boolean(
        weechat.config_get_plugin("run_externally")
    )
    run_externally = bool(run_externally)

    with open(PATH, "w+") as f:
        f.write(weechat.buffer_get_string(buf, "input"))

    if run_externally:
        hook_editor_process(terminal, editor, PATH, buf)
    else:
        run_blocking(editor, PATH, buf)

    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register("edit", "Keith Smiley", "1.0.0", "MIT",
                            "Open your $EDITOR to compose a message", "", ""):
        return weechat.WEECHAT_RC_ERROR

    weechat.hook_command("edit", "Open your $EDITOR to compose a message", "",
                         "", "", "edit", "")


if __name__ == "__main__":
    main()
