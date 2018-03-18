# dataclass
It's sometimes useful to generate an object whose sole responsibility is to house data and be passed around. Python's standard library supplies the `namedtuple`, which usually works well for this. However, the `namedtuple` requires that all attributes have a value assigned to them, which sometimes isn't what we want.

This `dataclass` method is meant to mimic the API of `namedtuple` (which is very concise and clean), but allow for attributes to be initialized as `None`. Another notable difference is that attributes are mutable (though an optional argument could be added to make them immutable when needed).

## Creating a data class and data object
```python
import dataclass

PersonData = dataclass('PersonData', 'name age’)
data_obj = PersonData(name='Bob', age=100)
# => <PersonData name: 'Bob'; age: 100>
```

## Attribute values are mutable
```python
data_obj = PersonData(name='Bob', age=100)
data_obj.age = 101
# => <PersonData name: 'Bob'; age: 101>
```

## Can be initialized with attributes as `None`
```python
data_obj = PersonData()
# => <PersonData name: None; age: None>
data_obj.name = 'Bob'
# => <PersonData name: 'Bob'; age: None>
```

## Prevents new attributes from being added
```python
data_obj = PersonData(name='Bob', age=100)
data_obj.height = 72
# => AttributeError: 'PersonData' object has no attribute 'height'
```
