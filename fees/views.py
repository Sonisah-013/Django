from django.shortcuts import render, redirect
from django.db.models import Sum
from students.models import Student
from .models import FeeInvoice, Payment

def fee_list(request):
    invoices = FeeInvoice.objects.all().order_by('due_date')
    return render(request, 'fees/fee_list.html', {'invoices': invoices})

def invoice_detail(request, invoice_id):
    invoice = FeeInvoice.objects.get(id=invoice_id)
    payments = invoice.payments.all().order_by('-date_paid')

    if request.method == 'POST':
        amount = request.POST.get('amount')
        method = request.POST.get('method')
        if amount:
            Payment.objects.create(invoice=invoice, amount=amount, method=method)
            invoice.amount_paid = invoice.payments.aggregate(total=Sum('amount'))['total'] or 0
            if invoice.amount_paid >= invoice.amount_due:
                invoice.status = 'paid'
            elif invoice.amount_paid > 0:
                invoice.status = 'partial'
            invoice.save()
        return redirect('fees:invoice_detail', invoice_id=invoice.id)

    return render(request, 'fees/invoice_detail.html', {'invoice': invoice, 'payments': payments})

def student_fees(request, student_id):
    student = Student.objects.get(id=student_id)
    invoices = FeeInvoice.objects.filter(student=student).order_by('-due_date')
    total_due = sum(inv.balance() for inv in invoices)
    return render(request, 'fees/student_fees.html', {
        'student': student, 'invoices': invoices, 'total_due': total_due
    })