# edit-weechat

This simple [weechat](https://weechat.org/) plugin allows you to
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
blocking weechat can break things), you can configure the plugin like this:

```
/set plugins.var.python.edit.editor "gvim -f"
/set plugins.var.python.edit.run_externally "true"
```

You can of course use any editor you want, you can even spawn a terminal and
use terminal vim if you prefer.

# Installation

Copy the script to `~/.weechat/python/autoload`

```
mkdir -p ~/.weechat/python/autoload
wget https://raw.githubusercontent.com/keith/edit-weechat/master/edit.py ~/.weechat/python/autoload
```
