# import needed modules
import ldap
import ldap.modlist as modlist

# Open a connection
l = ldap.initialize("ldaps://localhost.localdomain:636/")

# Bind/authenticate with a user with apropriate rights to add objects
l.simple_bind_s("cn=admin,dc=localhost,dc=localdomain","12345")

# The dn of our existing entry/object
dn="cn=admin,dc=localhost,dc=localdomain"

# Some place-holders for old and new values
old = {'description':'User object for replication using slurpd'}
new = {'description':'Bind object used for replication using slurpd'}

# Convert place-holders for modify-operation using modlist-module
ldif = modlist.modifyModlist(old,new) 

# Do the actual modification 
l.modify_s(dn,ldif)

# Its nice to the server to disconnect and free resources when done
l.unbind_s()
