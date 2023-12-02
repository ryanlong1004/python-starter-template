#!/usr/bin/env python
""" 
Convenience executor
"""

import subprocess
import click
import sys

def run(cmd):
    return subprocess.run(cmd.split(), shell=True, check=True)

@click.command
def test():
    """run testing suites"""
    return run("pytest")

@click.command
@click.option('--port', default=8000, help='specify a port number')
def serve(port=8000):
    """spins up a development server"""
    return run(f"{sys.executable} -m http.server {port}")

@click.command
def publish():
    """publish the project to Pypi"""
    return run(f"{sys.executable} setup.py sdist bdist_wheel upload")

@click.group()
def cli():
    pass

cli.add_command(test)
cli.add_command(serve)
cli.add_command(publish)

if __name__ == "__main__":
    cli()