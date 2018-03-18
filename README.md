# dataclass
Method for creating named “data classes” that are able to generate “data objects”.

`namedtuple` provides a concise way to describe data classes, but requires that all attributes have a value, which isn’t always desired.  `dataclass` is intended to provide a similar interface as `namedtuple`, but creates data objects that differ from `namedtuple`s as follows:
- The attributes on `dataclass` objects are initialized to `None` if not specified during initialization.
- The attributes on `dataclass` objects are mutable (though I may add an initialization option to make them immutable).

## How to create a data class and data object
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
