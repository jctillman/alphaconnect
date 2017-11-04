#
# Some generic functions for checking
# for a particular condition and
# raising an error if that condition
# is not met.
#

#
# Check that an 'instance' has method 'method_name'
#
def check_for_method(method_name, instance):

    def hasmethod(obj, name):
            return hasattr(obj, name) and type(getattr(obj, name)) == types.MethodType
    
    if (not has_method(instance, method_name)):
            msg = "Must have '{0}' method on '{1}' class".format(method_name, instance.__class__.__name)
            raise NotImplementedError()

#
# Check that something is of type string, return if so, otherwise throw
#
def check_is(kind, poss):
    if (poss is kind):
        return poss_str
    raise TypeError("Not class {0}".format(kind.__name__))
