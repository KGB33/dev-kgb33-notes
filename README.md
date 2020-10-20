# notes.kgb33.dev

A Static site containing various notes I've taken. 

# Local Development

### System Requirments
- Python 3.9^
- Pandoc
- Poetry (optional)

First, clone the repo.

```
git clone git@github.com:KGB33/dev-kgb33-notes.git
cd dev-kgb33-notes
```

Next, install requirments and activate your virutual environment.

```
poetry install
poetry shell
```

Finally, run the tests.

```
pytest tests/
```

To deploy localy: first ensure that docker is installed and started on your system, then run `./prod/start`.
You can access the server at `<host-ip>:3333` from any device on your local network.
