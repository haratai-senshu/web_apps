import subprocess
from django.shortcuts import render
import os
from django.http import FileResponse
from .models import Post
from .forms import UploadForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.exceptions import ValidationError
import random
import datetime
import time

dt_now = datetime.datetime.now()


class Create(CreateView):
    template_name = "post_form.html"
    model = Post
    form_class = UploadForm

    def post(self,request):
        if request.method == 'POST' and request.FILES['file_date_file']:
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                form.save()

                file_date = request.FILES['file_date_file']
                file_type = request.POST.get('file_type')

                file_name = file_date.name
                file_name = file_name.replace(" ","_")
                file_name = r"F:\DATE\server_media\media\conversion/" + str(file_name)

                ffmpeg_path = r"C:\x\pj_x\text_edit\ffmpeg.exe"

                file_name_out = str(os.path.splitext(str(file_name))[0]) + str(file_type)

                if os.path.isfile(file_name_out) :
                    file_name_out = str(os.path.splitext(str(file_name))[0]) + str(dt_now.strftime('%Y-%m-%d-%H-%M-%S')) + str(random.random()) + str(file_type)
                else:
                    pass


                command = str(ffmpeg_path) + ' -i ' + str(file_name) + ' ' + str(file_name_out)

                if str(file_name) == str(file_name_out):
                    response = render(request, 'error_message.html')
                else:
                    try:
                        subprocess.call(str(command))
                        response = FileResponse(open(file_name_out, "rb"), as_attachment=True, filename=file_name_out)
                        os.remove(str(file_name))
                    except Exception as e:
                        print(e)
                        response = render(request, 'error_message.html')
                        #raise ValidationError("エラーが発生しました。対応していないパターン、或いはファイルに問題があります。別のファイルを指定してください。")
        try:
            os.remove(str(file_name))
        except:
            pass

        try:
            path = r"C:\x\pj_x\text_edit\dt.txt"
            path_files = r"F:\DATE\server_media\media\conversion"

            dt_time = dt_now.strftime('%Y/%m/%d')
            with open(path) as f:
                dt_txt = f.read()

            if dt_time == dt_txt:
                pass
            else:
                with open(path, mode='w') as f:
                    f.write(str(dt_time))
                files = os.listdir(path_files)
                for i in files:
                    try:
                        i = str(path_files) + '/' + str(i)
                        os.remove(i)
                    except:
                        pass
        except Exception as e:
            print(e)
        #return render(request, 'index.html', context)
        return response
