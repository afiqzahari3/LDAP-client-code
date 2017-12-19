import ldap

try:
	l = ldap.open("fe80::20c:29ff:fef2:71f2%ens33")
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e

baseDN = "ou=Customers, ou=Sales, o=anydomain.com"
searchScope = ldap.SCOPE_SUBTREE

retrieveAttributes = None 
searchFilter = "cn=*jack*"

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	result_set = []
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
		break
	else:
		if result_type == ldap.RES_SEARCH_ENTRY:
		result_set.append(result_data)

	print result_set
except ldap.LDAPError, e:
	print e
	
