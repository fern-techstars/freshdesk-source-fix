This script goes through all tickets in a freshdesk instance and converts all tickets with `phone` source to `email`. This is helpful if you don't profvide phone support, and find it frustrating that freshdesk statically sets the source to `phone` when you manually create tickets from the UI.

## Requirements

1 Pipenv

## Installation

`pipenv install`

## Running

1. Reanme `.env.sample` to `.env` and replace the values with your freshdesk API key and server portal URL
2. run `pipenv run python3 fresher.py`
