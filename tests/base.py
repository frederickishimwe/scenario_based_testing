class ScenarioMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}

        for name, val in filter(lambda n: isinstance(n[1], ScenerioTestMeta), attrs.iteritems()):
            for id, params in enumerate(val.scenarios if not callable(val.scenarios) else val.scenarios()):
                if type(params) in (tuple, list):
                    params, id = params
                # create a unittest discoverable name
                test_name = "test_%s_%s" % (val.__name__, params.get('name'))
                # Wrap the scenario in a closure and assign the discoverable
                # name.
                new_attrs[test_name] = cls._wrap_test(params, val.__test__)
        attrs.update(new_attrs)
        return super(ScenarioMeta, cls).__new__(cls, name, bases, attrs)

    @staticmethod
    def _wrap_test(kwargs, meth):
        def wrapper(self):
            meth(self, **kwargs)

        return wrapper


class ScenerioTestMeta(type):
    def __new__(cls, name, bases, attrs):
        test_meth = attrs.pop("__test__", None)
        if test_meth:
            # Now that the __test__ method is pulled off the base it can be
            # wrapped as static and rebound.  This allows it to be re-composed
            # to the parent test case.
            attrs["__test__"] = staticmethod(test_meth)

        return super(ScenerioTestMeta, cls).__new__(cls, name, bases, attrs)


class ScenerioTest(object):
    __metaclass__ = ScenerioTestMeta
    scenarios = ()


