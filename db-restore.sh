#!/bin/sh
sqlite3 main.db << EOF
.read backup.sql
EOF

