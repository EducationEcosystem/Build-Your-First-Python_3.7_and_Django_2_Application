from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView
from .models import Friend
from .models import Post
from .forms import PostForm


def home(request):
    return render(request, 'accounts/Homepage.html')


class MyFriend(TemplateView):
    template_name = 'accounts/friends.html'

    def get(self,request):
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        return render(request, self.template_name, {'users': users, 'friends': friends})


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('accounts:MyFriends')


class PostView(TemplateView):
    template_name = 'accounts/posts.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        return render(request, self.template_name, {'form': form, 'posts': posts, 'users': users})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            text = form.cleaned_data['post']
            form=PostForm()
            post.save()
            return redirect('accounts:my_posts')

        redirect('accounts:my_posts')


def show_user(request):
    query = request.GET.get("user_name")
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()
    if query:
        users = User.objects.filter(
            Q(username__icontains=query)
        ).distinct()
        return render(request, 'accounts/show_user.html', {'users': users, 'friends': friends})

    return render(request, 'accounts/Homepage.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:home'))
        else:
            return redirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def logout_user(request):
    logout(request)
    return render(request, 'accounts/logout_user.html')


class UserFormView(View):
    form_class_register = UserForm
    form_class_login = LoginForm
    template_name = 'accounts/register.html'
    login_template = 'accounts/Homepage.html'

    def get(self, request):
        form = self.form_class_register(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class_register(None)
        form_register = self.form_class_register(request.POST)
        form_login = self.form_class_login(request.POST)

        # register
        if form_register.is_valid():
            user = form_register.save(commit=False)

            username = form_register.cleaned_data['username']
            password = form_register.cleaned_data['password']
            # password can be saved only with set function
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, self.login_template, {'form': form})

        # login
        if form_login.is_valid():

            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            print('hello')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, self.login_template, {'form': form})

        return render(request, self.template_name, {'form': form})

