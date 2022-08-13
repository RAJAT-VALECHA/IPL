from django.shortcuts import render, HttpResponse
from subprocess import run,PIPE
import sys
from Home.models import Btresult
from Home.models import Atresult
import joblib
from Home import Player_Info

# Create your views here.
def index(request):
    return render(request,'mainpage.html')
def analysis(request):
    return render(request,'index.html')
def prediction(request):
    return render(request,'matchprediction.html')
def beforetoss(request):
    return render(request,'beforetoss.html')
def aftertoss(request):
    return render(request,'aftertoss.html')
def mies(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\one.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def mpw(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\two.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def mpwwp(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\three.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def sm(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\four.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def dawt(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\five.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def rdps(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\seven.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')
def hsoi(request):
    out=run([sys.executable,'C:\\Users\\Rajat\\OneDrive\\Desktop\\PROJECT\\Project\\IPL\\Static\\eight.py'],shell=False, stdout=PIPE)
    return render(request,'index.html')

def btresult(request):
    if(request.method == "POST"):
        name1=request.POST.get('Team1_Name',False)
        name2=request.POST.get('Team2_Name',False)
        tw=request.POST.get('Toss_Wining_Team',False)
        td=request.POST.get('Toss_Decision',False)
        v=request.POST.get('Venue',False)
        toss=0
        if(name1 == tw):
            toss=1
        bat1=0
        if(toss==1 and tw==0):
            bat1=1
        elif(toss==0 and tw==1):
            bat1=1
        bat2=0
        if(bat1==0):
            bat2=1
        l=[]
        dt=joblib.load("BTDecisionTree.sav")
        ans1=dt.predict([[14,name1,name2,2,toss,bat1,bat2]])
        l.append(ans1)
        rf=joblib.load("BTRandomForest.sav")
        ans2=rf.predict([[14,name1,name2,2,toss,bat1,bat2,bat2,bat1]])
        l.append(ans2)
        svm=joblib.load("BTSvm.sav")
        ans3=svm.predict([[14,name1,name2,2,toss,bat1,bat2,bat2,bat1]])
        l.append(ans3)
        knn=joblib.load("BTKnn.sav")
        ans4=knn.predict([[14,name1,name2,2,toss,bat1]])
        l.append(ans4)
        ans = mostFrequent(l, 4)
        if(ans not in [name1,name2]):
            ans=int(name1)
        result = Btresult(Team1_Name=name1, Team2_Name=name2, Toss_Wining_Team = tw, Toss_Decision = td, Venue = v, ans=ans)
        result.save()
        if(ans == 0):
            return render(request,"csk.html")
        if(ans == 1):
            return render(request,"delhi.html")
        if(ans == 2):
            return render(request,"kkr.html")
        if(ans == 3):
            return render(request,"punjab.html")
        if(ans == 4):
            return render(request,"mi.html")
        if(ans == 6):
            return render(request,"rajasthan.html")
        if(ans == 7):
            return render(request,"rcb.html")
        if(ans == 8):
            return render(request,"hyderbad.html")
        return HttpResponse(ans)
    return HttpResponse("Error")

def atresult(request):
    if(request.method == "POST"):
        name1=request.POST.get('Team1_Name',False)
        name2=request.POST.get('Team2_Name',False)
        t1p1=request.POST.get('T1P1',False)
        t1p2=request.POST.get('T1P2',False)
        t1p3=request.POST.get('T1P3',False)
        t1p4=request.POST.get('T1P4',False)
        t1p5=request.POST.get('T1P5',False)
        t1p6=request.POST.get('T1P6',False)
        t1p7=request.POST.get('T1P7',False)
        t1p8=request.POST.get('T1P8',False)
        t1p9=request.POST.get('T1P9',False)
        t1p10=request.POST.get('T1P10',False)
        t1p11=request.POST.get('T1P11',False)
        t2p1=request.POST.get('T2P1',False)
        t2p2=request.POST.get('T2P2',False)
        t2p3=request.POST.get('T2P3',False)
        t2p4=request.POST.get('T2P4',False)
        t2p5=request.POST.get('T2P5',False)
        t2p6=request.POST.get('T2P6',False)
        t2p7=request.POST.get('T2P7',False)
        t2p8=request.POST.get('T2P8',False)
        t2p9=request.POST.get('T2P9',False)
        t2p10=request.POST.get('T2P10',False)
        t2p11=request.POST.get('T2P11',False)
        tw=request.POST.get('Toss_Wining_Team',False)
        td=request.POST.get('Toss_Decision',False)
        v=request.POST.get('Venue',False)
        l=[]
        l.append(Player_Info.Score(t1p1))
        l.append(Player_Info.Score(t1p2))
        l.append(Player_Info.Score(t1p3))
        l.append(Player_Info.Score(t1p4))
        l.append(Player_Info.Score(t1p5))
        l.append(Player_Info.Score(t1p6))
        l.append(Player_Info.Score(t1p7))
        l.append(Player_Info.Score(t1p8))
        l.append(Player_Info.Score(t1p9))
        l.append(Player_Info.Score(t1p10))
        l.append(Player_Info.Score(t1p11))
        l.append(Player_Info.Score(t2p1))
        l.append(Player_Info.Score(t2p2))
        l.append(Player_Info.Score(t2p3))
        l.append(Player_Info.Score(t2p4))
        l.append(Player_Info.Score(t2p5))
        l.append(Player_Info.Score(t2p6))
        l.append(Player_Info.Score(t2p7))
        l.append(Player_Info.Score(t2p8))
        l.append(Player_Info.Score(t2p9))
        l.append(Player_Info.Score(t2p10))
        l.append(Player_Info.Score(t2p11))
        a=[]
        a.append(l)
        ll=[]
        dt=joblib.load("ATDecisionTree.sav")
        ans1=dt.predict(a)
        ll.append(ans1[0])
        rf=joblib.load("ATRandomForest.sav")
        ans2=rf.predict(a)
        ll.append(ans2[0])
        svm=joblib.load("ATSvm.sav")
        ans3=svm.predict(a)
        ll.append(ans3[0])
        knn=joblib.load("ATKnn.sav")
        ans4=knn.predict(a)
        ll.append(ans4[0])
        print(l)
        ans = mostFrequent(ll, len(ll))
        p=ans
        if(ans==1):
            ans=name1
        else:
            ans=name2
        result = Atresult(Team1_Name=name1, Team2_Name=name2, Toss_Wining_Team = tw, Toss_Decision = td, Venue = v, ans=ans, T1_P1=t1p1, T1_P2=t1p2, T1_P3=t1p3, T1_P4=t1p4, T1_P5=t1p5, T1_P6=t1p6, T1_P7=t1p7, T1_P8=t1p8, T1_P9=t1p9, T1_P10=t1p10, T1_P11=t1p11, T2_P1=t2p1, T2_P2=t2p2, T2_P3=t2p3, T2_P4=t2p4, T2_P5=t2p5, T2_P6=t2p6, T2_P7=t2p7, T2_P8=t2p8, T2_P9=t2p9, T2_P10=t2p10, T2_P11=t2p11)
        result.save()
        ans=int(ans)
        if(ans == 0):
            return render(request,"csk.html")
        if(ans == 1):
            return render(request,"delhi.html")
        if(ans == 2):
            return render(request,"kkr.html")
        if(ans == 3):
            return render(request,"punjab.html")
        if(ans == 4):
            return render(request,"mi.html")
        if(ans == 5):
            if(p==1):
                return render(request,"one.html")
            elif(p==2):
                return render(request,"two.html")
        if(ans == 6):
            return render(request,"rajasthan.html")
        if(ans == 7):
            return render(request,"rcb.html")
        if(ans == 8):
            return render(request,"hyderbad.html")
    return HttpResponse("Error")
def mostFrequent(arr, n):
    arr.sort()
    max_count = 1
    res = arr[0]
    curr_count = 1
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
        else:
            curr_count = 1
        if (curr_count > max_count):
            max_count = curr_count
            res = arr[i - 1]
    return res
