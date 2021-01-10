from django.shortcuts import render
from .forms import CSVModelForm
from .models import CSV
import csv
#from django.http import HttpResponse


def upload_file_view(request):
    form = CSVModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        form = CSVModelForm()
        obj = CSV.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    print(row)
    return render(request, 'csvs/upload.html', {'form': form})

