Sample Django model

```python
from django.db import models


class ContactSample(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False, )
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    name = models.CharField(max_length=1000)
```
