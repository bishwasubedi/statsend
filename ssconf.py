uid = "uid"
key = "key"

remote = ("cacti-bishwa.rhcloud.com", 80)
page = "/status2stat.php"

procs = ["/usr/sbin/sshd"
        ,"/usr/sbin/httpd"
        ,"/usr/sbin/mysqld"
        ]

interfaces = ["venet0"]

pidfile = "statsend.pid"
