# properties required for backups

backupBucket = "<your-s3-bucket-name>"
testRestoreDir = "<a sub-directory of your temp directory for restoring files into (when verifying)>"

# record partial backup status after more than restoreTrigger bytes backed up since last record
restoreTrigger = 5000000

# Details of directory to be backed up from your computer to your S3 bucket
class BackupDetails(object):
    def __init__(self, source, prefix):
        self.source = source
        self.prefix = prefix
        
    def __str__(self):
        return "<Backup directory %s into folder %s of the backup bucket>" % (self.source, self.prefix)
        
# details of your projects to be backed up
backups = {"project1": BackupDetails("c:/myprojects/project1", "backups/project1/"), 
           "project2": BackupDetails("c:/myprojects/project2", "backups/project2/"), 
           }

# choose a not too big project for doing test backups with
backups["test"] = backups["project2"]
