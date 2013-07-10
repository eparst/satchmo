+1. rhc app create p27 
+2. git clone 
3. add .openshift, wsgi, data, setup.py, readme.md
4. git add . , commit and push to repo on openshift

old:
-1. instead rhc app create "satchmo" django create from openshift web-site with git https://github.com/eparst/django-example/
-2. go to ssh-openshift and:

$OPENSHIFT_HOMEDIR/python/virtenv/bin/python setup.py install #/var/lib/openshift/51d5b51d4382ecf1c30002a5/python/virtenv/bin/python setup.py install

cd $OPENSHIFT_REPO_DIR/wsgi --?pil--?

$OPENSHIFT_HOMEDIR/python/virtenv/bin/python satchmo/scripts/clonesatchmo.py --?


*changed:
- instal_requers in setup.py
- wsgi / application l. 5 and 6
- added: wsgi / satchmo and wsgi / store - второе, если без clonesatchmo.py
