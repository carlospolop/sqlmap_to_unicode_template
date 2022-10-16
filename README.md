# sqlmap to unicode template

https://book.hacktricks.xyz/pentesting-web/unicode-injection/unicode-normalization#sql-injection-filter-bypass

```
sqlmap -r req.txt --tamper to_unicode.py --proxy http://127.0.0.1:8080
```