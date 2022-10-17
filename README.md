## S3 Bucket Setup Using Pulumi

Sample pulumi python setup to create a new s3 bucket with public-read acl and to attach a public-read bucket policy to it.

---
### Pre-requisite

* Install pulumi
* Setup AWS Credentials
* Signup and create token for Pulumi

---
### [How To] Setup the infrastricture

```shell
pulumi up
```
---
### [How To] destroy the infrastricture

```shell
pulumi destroy
```

---
### [How To] Remove the infrastricture stack

```shell
pulumi stack rm
```