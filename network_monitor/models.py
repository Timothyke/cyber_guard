from django.db import models

# Create your models here.

class ScanLog(models.Model):
    ip_address = models.GenericIPAddressField()
    scanned_at = models.DateTimeField(auto_now_add=True)
    open_ports = models.TextField()

    def __str__(self):
        return f"Scan for {self.ip_address} at {self.scanned_at}"