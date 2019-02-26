  

def rename_decorator(old_func):
  	"""Decorator used for generating warnings when deprecated functions
  	are usef """
  	import warnings
  	if old_func.__doc__ == "":
  		warning_msg = '{} is deprecated. There is no replacement function specified'.format(old_func.__name__)
  		warnings.warn(warning_msg, DeprecationWarning)
  	else:
  		warning_msg = '{} is deprecated. Use {} instead'.format(old_func.__name__, old_func.__doc__)
  		warnings.warn(warning_msg, DeprecationWarning)
  	return old_func
