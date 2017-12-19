# import needed modules
import ldap
import ldap.modlist as modlist

# Open a connection
l = ldap.initialize("ldaps://localhost.localdomain:636/")

# Bind/authenticate with a user with apropriate rights to add objects
l.simple_bind_s("cn=admin,dc=localhost,dc=localdomain","12345")

# The dn of our new entry/object
dn="cn=replica,dc=example,dc=com"

# A dict to help build the "body" of the object
attrs = {}
attrs['objectclass'] = ['top','organizationalRole','simpleSecurityObject']
attrs['cn'] = 'replica'
attrs['userPassword'] = 'aDifferentSecret'
attrs['description'] = 'User object for replication using slurpd'

# Convert our dict to nice syntax for the add-function using modlist-module
ldif = modlist.addModlist(attrs)

# Do the actual synchronous add-operation to the ldapserver
l.add_s(dn,ldif)

# Its nice to the server to disconnect and free resources when done
l.unbind_s()


