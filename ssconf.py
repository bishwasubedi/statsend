uid = "uid"
key = "key"

remote = ("host", 80)
page = "/command.php"

procs = ["/usr/sbin/sshd"
        ,"/usr/sbin/httpd"
        ,"/usr/sbin/mysqld"
        ]

interfaces = ["venet0"]

pidfile = "statsend.pid"
