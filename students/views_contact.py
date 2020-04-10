from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all().order_by('id')
    context = {'contacts': contacts, }
    return render(request, 'contact/contact_list.html', context)


def contact_add(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.type = form.cleaned_data['type']
            contact.value = form.cleaned_data['value']
            contact.primary = form.cleaned_data['primary']
            contact.save()
            return redirect('contact-list')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_add.html',
                  {'form': form})


def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.type = form.cleaned_data['type']
            contact.value = form.cleaned_data['value']
            contact.primary = form.cleaned_data['primary']
            contact.save()
            return redirect('contact-list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_edit.html',
                  {'form': form})


def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    try:
        contact.delete()
    except ProtectedError:
        messages.warning(request, 'Contact has related objects and can not be deleted')
    return redirect('contact-list')
