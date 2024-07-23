# -*- coding=utf-8 -*-

from __future__ import annotations
import pathlib
import json

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True, path_type=pathlib.Path))
def init(path: pathlib.Path) -> None:
    """Initialize a jedi project."""
    path = path.resolve()
    click.echo(f'Initializing project at {path}.')
    json_path = path / ".jedi" / "project.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    settings = [1, {
        "path": str(path),
    }]
    with json_path.open('w') as f:
        json.dump(settings, f)


def main() -> None:
    cli()
