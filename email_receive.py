#!/usr/bin/python

import os
import poplib

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user(os.environ.get('G_EM'))
pop_conn.pass_(os.environ.get('G_P'))

messages = [pop_conn.retr(i) for i in range(1, 3)]

print (messages)
