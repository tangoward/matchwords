from django.views.generic import TemplateView
from django.shortcuts import render
from collections import Counter
from django.conf import settings

import os

# Create your views here.


class ProfileView(TemplateView):
    template_name = 'words/profile.html'

    def post(self, request, *args, **kwargs):
        found_words = []
        file = open(settings.TEXT_FILE, 'r').read()
        file_data = file.split('\n')

        if request.method == "POST":
            string_word = request.POST['string']

            def isPresent(string_word, file_data):
                char = Counter(string_word)
                for c in file_data.casefold():
                    if char[c] > 0:
                        char[c] -= 1
                    else:
                        return False
                return True

            for i in file_data:
                if len(i) > len(string_word):
                    continue
                x = isPresent(string_word, i)
                if x == True:
                    found_words.append(i)

        return render(request, self.template_name, {'found_words': found_words})
