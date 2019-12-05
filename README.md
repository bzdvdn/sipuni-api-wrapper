# Sipuni api client

## Installation

Install using `pip`...

    pip install sipuni-api
    
### Usage
```python
from sipuni_api import Sipuni
client = Sipuni('<user_id>', '<api_key>')
```
#### Make calls
* <a href="https://support.sipuni.com/hc/ru/articles/360016412754-%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%BC%D0%B5%D1%80-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-API">Documentation</a>
```python
# create simple call
client.make_call(phone='79379992', sipnumber='201')

# create call tree
client.make_tree_call(phone='79379992', sipnumber='201', tree='000658610')

# create call external
client.make_external_call(from_phone='79379992', to_phone='79379993', first_sipnumber='201', second_sipnumber='204')
`````
#### Make voice call
* <a href="https://support.sipuni.com/hc/ru/articles/360016537533-%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B3%D0%BE%D0%BB%D0%BE%D1%81%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%B0-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-API">Documentation</a>
```python
client.make_voice_call(phone='79379992', sipnumber='201', message='test 123', voice_type='Vladimir')
```

#### Hangup call
* <a href="https://support.sipuni.com/hc/ru/articles/360016413214-%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%BD%D0%B0-%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%B0">Documentation</a>
```python
client.hangup_call(call_id='123456789.123')
```
#### Statistic
* <a href="https://support.sipuni.com/hc/ru/articles/360016412114-%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BF%D0%BE-%D0%B7%D0%B2%D0%BE%D0%BD%D0%BA%D0%B0%D0%BC-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B5%D0%B9-%D1%80%D0%B0%D0%B7%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D0%B2-%D0%B8-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%BE%D0%B2-%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2">Documentation</a>
```python
# call statistic
from datetime import datetime, timedelta
client.get_call_stats(from_date=(datetime.now() - timedelta(days=1)), to_date=datetime.now())   # return csv data

# get call record
client.get_record('<record_id>')    # return bytes

# get list of managers
client.get_managers()
```

### TODO
* examples
* tests


### License
MIT