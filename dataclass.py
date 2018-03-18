def dataclass(name, attrs):
    """
    Generate a named "data class" that instantiates "data objects"
    with the specified attributes.

    Args:
        name (str): The desired name of the new data class.
        attrs
            - (str): Names of desired attrs separated by spaces.
            or
            - (list): Names of desired attrs.
    Returns:
        class: "Data class" that instantiates data objects with
            desired attrs.
    """
    data_class_name = name
    allowed_attrs = attrs
    if isinstance(allowed_attrs, str):
        allowed_attrs = allowed_attrs.split()

    class DataClassCreator(type):
        """
        Renames TempDataClass to the desired name of the data class.
        """
        def __new__(cls, name, bases, attributes):
            return type.__new__(cls, data_class_name, bases, attributes)

    class TempDataClass(object):
        __metaclass__ = DataClassCreator
        __slots__ = allowed_attrs

        def __init__(self, **kwargs):
            not_allowed = set(kwargs.keys()).difference(set(allowed_attrs))
            if not_allowed:
                raise AttributeError(
                    'Invalid attrs: ' + str(list(not_allowed))
                )

            # If a value is given for an attr, assign it, otherwise
            # set it to None.
            for attr in allowed_attrs:
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])
                else:
                    setattr(self, attr, None)

        def __eq__(self, other):
            if self.__slots__ != other.__slots__:
                return False
            for attr in self.__slots__:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            return True

        def __ne__(self, other):
            return not self == other

        def __str__(self):
            output_str = '<'
            output_str += self.__class__.__name__ + ' '
            attr_info = [
                '{0}: {1!r}'.format(attr, getattr(self, attr, None))
                for attr in self.__slots__
            ]
            output_str += '; '.join(attr_info)
            output_str += '>'
            return output_str

        def __repr__(self):
            repr_str = ''
            repr_str += self.__class__.__name__ + '('
            attr_info = [
                '{0}={1!r}'.format(attr, getattr(self, attr, None))
                for attr in self.__slots__
            ]
            repr_str += ', '.join(attr_info)
            repr_str += ')'
            return repr_str

    return TempDataClass
