# rpilocator api

An Unofficial REST API for [rpilocator.com](https://rpilocator.com/)

Built by [Andre Saddler](https://github.com/axsddlr/)

[![heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Current Endpoints

### `/pi4/<region>`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Region: `US`, `UK`
- Response:


### `/pi4/<region>/<model GiB #>`


- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Region: `1`, `2`, `4`, `8`


## Installation

### Source

```
$ git clone https://github.com/axsddlr/rpilocator_api/
$ cd rpilocator_api
$ pip install -r requirements.txt
```

### Usage

```
python3 main.py
OR 
uvicorn main:app --reload --port 3000
```

## Contributing

Feel free to submit a [pull request](https://github.com/rehkloos/vlrggapi/pull/new/master) or an [issue](https://github.com/rehkloos/vlrggapi/issues/new)!

## License

The MIT License (MIT)