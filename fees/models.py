
from django.db import models
from students.models import Student

class FeeInvoice(models.Model):
    STATUS_CHOICES = [
        ("paid", "Paid"),
        ("unpaid", "Unpaid"),
        ("partial", "Partial"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='invoices')
    description = models.CharField(max_length=200)   # e.g. "Tuition Fee - Fall 2026"
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="unpaid")
    created_at = models.DateTimeField(auto_now_add=True)

    def balance(self):
        return self.amount_due - self.amount_paid

    def __str__(self):
        return f"{self.student} - {self.description}"


class Payment(models.Model):
    invoice = models.ForeignKey(FeeInvoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=50, blank=True)  # e.g. "Cash", "Bank Transfer"

    def __str__(self):
        return f"{self.invoice.student} - {self.amount}"