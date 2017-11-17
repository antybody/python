#-*-coding:utf-8-*-
import multiprocessing

def process(num):
    print 'Process:',num

if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()
    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name:' + p.name + "id:"+ str(p.pid))

    print('Process Ended')