from django.shortcuts import render, redirect
from .models import Trainee
from course.models import Course
from .forms import TraineeFormModel
from django.views import View, generic
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, "base.html")

# def traineeList(request):
#     context = {"trainees": Trainee.objects.filter(is_active=True)}
#     return render(request, "trainee/trainee.html", context)

class TraineeList(generic.ListView):
    queryset= Trainee.objects.filter(is_active=True)
    template_name = 'trainee/trainee.html'
    context_object_name = "trainees"

def traineeDetails(request, id):
    context = {"trainee": Trainee.objects.get(pk=id)}
    return render(request, "trainee/details.html", context)

# def traineeAdd(request):
#     context = {"trainees": Trainee.objects.all(), 'form':TraineeFormModel()}
#     if request.method == "POST":
#         form = TraineeFormModel(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Trinee_list')
#     return render(request, "trainee/add.html", context=context)

class TraineeAdd(View):
    context = {"trainees": Trainee.objects.all(), 'form':TraineeFormModel()}

    def get(self, request):
        return render(request, "trainee/add.html", TraineeAdd.context)
        
    def post(self, request):
        form= TraineeFormModel(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Trinee_list')
        else:
            TraineeAdd.context['form']=form
            TraineeAdd.context['errors']=form.errors
            return render(request, 'trainee/add.html', TraineeAdd.context)

class TraineeAddGeneric(generic.CreateView):
    model = Trainee
    template_name = 'trainee/add.html'
    context_object_name = 'trainee'
    # form_class = TraineeFormModel
    success_url = reverse_lazy('Trinee_list')
    fields = '__all__'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['trainees'] = Trainee.objects.all()
    #     return context
    
    # def form_invalid(self, form):
    #     context = self.get_context_data()
    #     context['form'] = form
    #     context['errors'] = form.errors
    # return render (self.request, self.template_name, context)


def traineeUpdate(request, id):
    old_trainee = Trainee.objects.get(pk=id)
    form=TraineeFormModel(instance=old_trainee)
    if request.method == "POST":
        form=TraineeFormModel(data=request.POST, files=request.FILES, instance=old_trainee)
        if form.is_valid():
            form.save()
            return redirect('Trinee_list')
        
        else:
            print(form.errors)
            return render(request, 'trainee/update.html', {"form": form})
    
    return render(request, 'trainee/update.html', {"form":TraineeFormModel(instance=old_trainee)})


def traineeDelete(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.delete()
        return redirect('Trinee_list')
    
    return render(request, 'trainee/delete.html')

def traineeSoftDelete(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.is_active = False
        trainee.save()
        return redirect('Trinee_list')
    return render(request, 'trainee/delete.html')
