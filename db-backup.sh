#!/bin/sh
sqlite3 main.db << EOF
.mode insert
.output "backup.sql"
.dump
.exit
EOF

