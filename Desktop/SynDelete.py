import ldap

try:
	l = ldap.open("fe80::20c:29ff:fef2:71f2%ens33")

	
	l.protocol_version = ldap.VERSION3

	username = "cn=Manager, o=anydomain.com"
	password  = "secret"

	l.simple_bind(username, password)
except ldap.LDAPError, e:
	print e

	deleteDN = "uid=anyuserid, ou=Customers,ou=Sales,o=anydomain.com"
try:
	l.delete_s(deleteDN)
except ldap.LDAPError, e:
	print e
