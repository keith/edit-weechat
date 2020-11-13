# edit-weechat

This simple [weechat](https://weechat.org/) plugin allows you to
compose messages in your `$EDITOR`, optionally with a file type.

# Usage

- Markdown message (it's the default, same as `/edit md`)
  ```sh
  /edit
  # Type some stuff
  # Save and quit
  ```
- Plain text message
  ```sh
  /edit txt
  # Type some stuff
  # Save and quit
  ```
- Code message with fences added automatically
  ```sh
  /fenced cpp
  # Type some code
  # Save and quit
  ```

# Configuration

If you'd like to customize the editor you use outside of the `$EDITOR`
environment variable, you can set it in weechat.

```sh
/set plugins.var.python.edit.editor "vim -f"
```

# Installation

Copy the script to `~/.weechat/python/autoload`

```
mkdir -p ~/.weechat/python/autoload
wget https://raw.githubusercontent.com/keith/edit-weechat/master/edit.py ~/.weechat/python/autoload
```
