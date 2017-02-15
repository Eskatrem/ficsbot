# FICS Bot
FICS Bot is a python bot created by [**schachbjm**](https://github.com/schachbjm), 
[**Kevin Schaefer**](http://kevinschaefer.de) and [**Jonas Drotleff**](https://github.com/jonas-drotleff).  
The bot runs as a seperate user on FICS and manages voting and moving.

## Install
FICS Bot is developed in `python`. Make sure you have Python installed. We also recommend to use `pip` 
to get all the dependencies.
#### Mac
Install python with [`brew`](http://brew.sh/):
```commandline
brew install python
```
And install pip:
````commandline
sudo easy_install pip
````

#### Linux

If `python` is not already installed, you might want to use one of the following package managers:

**apt-get**:
```commandline
sudo apt-get install python
```
**yum**:
```commandline
yum install -y python27
```

Get `pip` from [here](https://pip.pypa.io/en/stable/installing/).

#### Windows
Download latest Python 2 release from [python.org](https://www.python.org/downloads/windows/) and install.

Get `pip` from [here](https://pip.pypa.io/en/stable/installing/).

### Install dependecies

Run the following command in the project folder (where this README.md is located):
```commandline
pip install -r requirements.txt
```

### Run
```text
Usage: ./ficsbot [-h] [--quiet | --verbose] [--out=<file>]

-h --help     show this
--out=<file>  specify output file [default: ./ficsbot.log]
-q --quiet    print less text
-v --verbose  print more text
```
#### On Linux/macOS
Make the ficsbot binary in the parent directory executable by the following command:
```commandline
chmod +x ficsbot
```
You can now run ficsbot just by typing
```commandline
./ficsbot [-h] [--quiet | --verbose] [--out=<file>]
```
#### On Windows
To run ficsbot on windows, just run the ficsbot python script in the `src/` directory:
```commandline
python src/ficsbot.py [-h] [--quiet | --verbose] [--out=<file>]
```

## License

Copyright 2017 Jonas Drotleff

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
