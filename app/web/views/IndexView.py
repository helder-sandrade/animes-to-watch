from django.shortcuts import render, redirect
from django.views import View

from rpa.SiteScrape import Rpa
from time import sleep
from multiprocessing import Process


class ViewIndex(View):
    def get(self, request):
        data = {'form': 'form'}
        return render(request=request, template_name='web/index.html', context=data)

    def post(self, request):
        data = {'mensagem': 'teste de mensagem'}

        rpa1 = Rpa()
        thread1 = Process(target=rpa1.load_page, args=(1, 20,))
        thread1.start()
        thread1.join()

        rpa2 = Rpa()
        thread2 = Process(target=rpa2.load_page, args=(2, 20,))
        thread2.start()
        thread2.join()

        rpa3 = Rpa()
        thread3 = Process(target=rpa3.load_page, args=(3, 1,))
        thread3.start()
        thread3.join()

        t = [thread1, thread2, thread3]
        print(t)
        for i in range(len(t)-1):
            teste = Process(target=self.killp, args=(t[i],))
            print(f'encerrando {i}')
            teste.start()
            teste.join()

        return render(request=request, template_name='web/index.html', context=data)

    def killp(self, p: Process):
        sleep(5)
        p.terminate()
        print('encerrado')
