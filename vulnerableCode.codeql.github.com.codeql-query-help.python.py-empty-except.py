# ...
try:
    security_manager.drop_privileges()
except SecurityError:
    pass
# ...

