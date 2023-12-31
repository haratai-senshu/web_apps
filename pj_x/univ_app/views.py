from django.views.generic.edit import FormView
import pandas as pd

from . import forms

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"

    # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        text = data["text"]
        # 大学リスト
        #universities = ["北海道大学","札幌大学"]
        universities = text.splitlines()
        # 国公立大学リスト
        url = "https://www.mext.go.jp/b_menu/link/daigaku1.htm"
        df_k = pd.read_html(url)
        df = []
        for koku in range(10):
            for i_lis in df_k[int(koku)].values :
                for i_ele in i_lis:
                    df.append(i_ele)


        # 公立大学リスト
        url2 = "https://www.mext.go.jp/a_menu/koutou/kouritsu/04093001/015.htm"
        df2 = pd.read_html(url2)
        df3 = []
        for i in df2[0].values:
            if '  ' in str(i[4]) :
                sp = i[4].split()
                for j in sp :
                    j = j.replace(' ','')
                    df3.append(j)
            else:
                df3.append(i[4])
        # 公立大学との照合
        new_text = []

        koku_list = []
        kou_list = []
        shiri_list = []
        mongai_list = []
        for university in universities:
            if university in df:
                new_text.append(university + "：国立大学")
                koku_list.append(university)
            elif university in df3:
                new_text.append(university + "：公立大学")
                kou_list.append(university)
            elif '公立' + university in df3:
                new_text.append(university + "：公立大学")
                kou_list.append(university)
            elif university == '防衛大学校' or university == '気象大学校' or university == '防衛医科大学校' or university == '海上保安大学校':
                new_text.append(university + "：文部科学省所管外の大学校")
                mongai_list.append(university)
            elif '大学' not in university:
                new_text.append(university + "：大学ではありません。正式名称で入力してください。")
            else:
                new_text.append(university + "：私立大学")
                shiri_list.append(university)

        # テンプレートに渡す
        ctxt = self.get_context_data(koku_list=koku_list,kou_list=kou_list,shiri_list=shiri_list,mongai_list=mongai_list,new_text=new_text, form=form)
        return self.render_to_response(ctxt)
