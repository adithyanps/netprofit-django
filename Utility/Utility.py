import os
from Credit_Note import models

def test():
    n=60
    return n
# print(test(5))

def autoCreditNoteNumberGenerator():
    queryset = models.CreditNote.objects.all().order_by('-id')[0]
    print(queryset,'xxx')
    print(queryset.Doc_no,'Docno')
