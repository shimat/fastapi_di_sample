# fastapi_di_sample
[FastAPI](https://fastapi.tiangolo.com/) + [Dependency Injector](https://python-dependency-injector.ets-labs.org/) code samples

## Installation
```
poetry install
```

## Usage
### Run FastAPI
This sample WebAPI returns whether the input string is included in the predefined string list (`["alice", "bob", "charlie"]`).
```
task fastapi
```

### Query samples
#### curl
```sh
$ curl -s "http://localhost:8000/?word=alice"
{"is_ok":true}

$ curl -s "http://localhost:8000/?word=xxxxx"
{"is_ok":false}
```

#### Windows (PowerShell 3.0 or later)
```ps1
PS> Invoke-RestMethod http://localhost:8000/ -Body @{"word"="alice"}

is_ok
-----
 True

PS> Invoke-RestMethod http://localhost:8000/ -Body @{"word"="xxxxx"}

is_ok
-----
 False
```


### Test
```
task test
```

### Linters
```
task flake8
task mypy
```

## References
- https://python-dependency-injector.ets-labs.org/examples/fastapi.html
