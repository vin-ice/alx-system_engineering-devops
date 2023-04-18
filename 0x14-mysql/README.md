# MySQL
## Resources
- [What is a primary-replica cluster](https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA)
- [MySQL primary replica setup](https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg)
- [Build a robust database backup strategy](https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q)

## Requirements
- MySQL primary must be hosted on `web-01` - do not use the bind-address, just comment out this parameter
- MySQL replica must be hosted on `web-02`
- Setup replication for the MySQL database named `tyrell_corp`
- Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`
- Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`

## Tips:
- Once MySQL replication is setup, add a new record in your table via MySQL on web-01 and check if the record has been replicated in MySQL web-02. If you see it, it means your replication is working!
- Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work.