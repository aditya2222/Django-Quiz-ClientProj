from django import forms
from django.forms.widgets import RadioSelect
from django.template import Template
from django.utils.safestring import mark_safe
from string import Template
from django.utils.safestring import mark_safe

link = ['']
choice_list_new = ['']


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        global link
        global choice_list_new
        print(link)
        html1 = Template(
            "<input type='radio' name='answers' value='1' required /><img style='height:auto;width:300px' src=$link  /> ")
        html2 = Template(
            "<input type='radio' name='answers' value='1' required /><img style='height:auto;width:300px' src=$link  />")
        html3 = Template("<img src=$link  />")
        html4 = Template("<img src=$link  />")
        return mark_safe(html1.substitute(link=link[1])) + '' + mark_safe(html2.substitute(link=link[2]))


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        global link
        global choice_list_new
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields['answers'] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

        # for i in range(0, len(choice_list)):
        #     word = str(choice_list[i][1])
        #     print(word)
        #     # print(word.find('.jpg'))
        #     if word.find('.jpg') != -1:
        #         link.append(word)
        #         self.fields['images'] = forms.ChoiceField(widget=PictureWidget)
        #
        #     else:
        #         print('entered')
        #         choice_list_new.append(word)
        #         new_choices = [(1, answer) for answer in choice_list_new]
        #         print(new_choices)
        #         self.fields["answers"] = forms.ChoiceField(choices=new_choices, widget=RadioSelect)
        # choice_list_new.clear()
