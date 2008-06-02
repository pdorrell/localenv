# A test file demonstrating how to access localenv
import localenv.s3

print "My S3 access key = %r" % localenv.s3.accessKey

import localenv.backups

testBackupDetails = localenv.backups.backups["test"]

print "My test backup is %s" % testBackupDetails
