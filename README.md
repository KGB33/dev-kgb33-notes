# notes.kgb33.dev

A Static site containing various notes I've taken.

# Local Development

### System Requirements

- Python 3.9^
- Poetry (optional)

First, clone the repo.

```
❯ git clone git@github.com:KGB33/dev-kgb33-notes.git
❯ cd dev-kgb33-notes
```

Next, install requirements and activate your virtual environment.

```
❯ poetry install
❯ poetry shell
```

Finally, run the tests.

```
❯ pytest tests/
```

To deploy locally: first ensure that docker is installed and started on your
system, then run `❯ ./prod/start`. You can access the server at `<host-ip>:3333`
from any device on your local network.

# Tools & Resources Used

## Code Highlighting

To convert the `*.md` files to HTML and add code highlighting the tools
[Python-Markdown]() and [Pygments][pygments] are used. An excellent tutorial by
Rudra Narayan can be found [here][code-highlighting]

[py-md]: https://github.com/Python-Markdown/markdown
[pygments]: https://github.com/pygments/pygments
[code-highlighting]: https://rudra.dev/posts/rendering-markdown-from-flask/
