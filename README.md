# `tap-pokemon`

Singer tap for Pokémon.

Built with the [Meltano SDK](https://sdk.meltano.com) for Singer Taps and Targets.

🚧 Under development. Not all endpoints have been implemented. See [API Coverage](#api-coverage). 🚧

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting              | Required | Default            | Description                                                                    |
|:-------------------- |:--------:|:------------------:|:------------------------------------------------------------------------------ |
| base_url             | False    | https://pokeapi.co | The base URL of the Pokémon API.                                               |
| stream_maps          | False    | None               | Config object for stream maps capability.                                      |
| stream_map_config    | False    | None               | User-defined config values to be used within map expressions.                  |
| flattening_enabled   | False    | None               | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth | False    | None               | The max depth to flatten schemas.                                              |

A full list of supported settings and capabilities is available by running: `tap-pokemon --about`

## API Coverage

| Stream            | Endpoint                  |
| ----------------- | ------------------------- |
| `pokemon_species` | `/api/v2/pokemon-species` |

## Usage

You can easily run `tap-pokemon` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pokemon --version
tap-pokemon --help
tap-pokemon --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # or follow https://docs.astral.sh/uv/getting-started/installation/
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
uv run pytest
```

You can also test the `tap-pokemon` CLI interface directly using `uv run`:

```bash
uv run tap-pokemon --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
uv tool install meltano
# Initialize meltano within this directory
cd tap-pokemon
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pokemon --version
# OR run a test EL pipeline:
meltano run tap-pokemon target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
