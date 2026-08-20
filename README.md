# edit-weechat

This simple [weechat](https://weechat.org/) script allows you 
compose messages in your `$EDITOR`.

# Usage

```sh
/edit
# Type some stuff
# Save and quit
```

# Configuration

If you'd like to customize the editor you use outside of the `$EDITOR`
environment variable, you can set it in weechat.

```sh
/set plugins.var.python.edit.editor "vim -f"
```

In case you want to run editor externally without blocking weechat (since
blocking weechat can break things), you can configure the script like this:

```
/set plugins.var.python.edit.editor "gvim -f"
/set plugins.var.python.edit.run_externally "true"
```

You can of course use any editor you want, you can even spawn a terminal and
use terminal vim if you prefer.

# Installation

1. Copy the script to the plugin Python scripts directory located in "data" directory listed in Weechat command `/debug dirs`.
And, since Weechat v3.2, XDG directories are prioritized, it may be: `"${HOME}/.local/share/weechat/python"`.

```bash
pythonScriptsDirpath="${HOME}/.local/share/weechat/python";

mkdir -p -- "$pythonScriptsDirpath" &&
wget 'https://raw.githubusercontent.com/keith/edit-weechat/master/edit.py' "${pythonScriptsDirpath}/edit.py";
```

2. Load the script in Weechat: `/script load edit.py`;
3. Enable autoload in Weechat: `/script autoload edit.py`.
