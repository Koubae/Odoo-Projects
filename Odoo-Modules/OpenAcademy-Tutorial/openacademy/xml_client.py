import functools
import xmlrpc.client

HOST = 'localhost'
PORT = 8069
DB = 'openacademy'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid:%d)" & (USER, uid))

call = functools.partial(xmlrpc.client.ServerProxy(ROOT + 'object').execute,
                        DB, uid, PASS)

# 2. Read the sessions
sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])

for session in sessions:
    print("Session %s (%s seats)" % (session["name"], session["seats"]))

# 3. Create A new Session
course_id = call('openacademy.course', 'search', [('name', 'ilike', 'Functional')])[0]
session_id = call('openacademy.session', 'create', {
    'name': 'My session', 
    'corse_id': course_id,
})
