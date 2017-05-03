from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime
from .tcode import GetTcode

def index(request):
    return render(request,'index.html')
def sds(request):
    return render(request,'SDS.html')
def sds_result(request):
    x=0
    print(type(request.GET))
    for n in range(1,21):
        name='c'+str(n)
        data=request.GET[name]
        x+=int(data)
    y=int(x*1.25)
    if y<53:
        result='正常'
    elif y>=53 and y<63:
        result='轻度抑郁'
    elif y>=63 and y<73:
        result='中度抑郁'
    else:
        result='重度抑郁'
        
    return HttpResponse(result)

def sas(request):
    return render(request,'SAS.html')
def sas_result(request):
    x=0
    for n in range(1,21):
        name='c'+str(n)
        data=request.GET[name]
        x+=int(data)
    y=int(x*1.25)
    if y<50:
        result='正常'
    elif y>=50 and y<60:
        result='轻度焦虑'
    elif y>=60 and y<70:
        result='中度焦虑'
    else:
        result='重度焦虑'
    return HttpResponse(result)

def mmpi(request):
    return render(request,'MMPI.html')

def scl(request):
    return render(request,'SCL90.html')
def scl_result(request):
    total=tatal_s1=tatal_s2=tatal_s3=tatal_s4=tatal_s5=tatal_s6=tatal_s7=tatal_s8=tatal_s9=0
    positive_num=0
    negative_num=0
    for key in request.GET:
        total+=request.GET[key]
        if request.GET[key]>=2:
            positive_num+=1
        elif request.GET[key]==1:
            negative_num+=1
    total_average=total/90
    positive_average=(total-negative_num)/positive_num
    #躯体化
    s1=['R1','R4','R12','R27','R40','R42','R48','R52','R53','R56','R58']
    for j in s1:
        total_s1+=request.GET[j]
    #强迫症状
    s2=['R3','R9','R10','R28','R38','R45','R46','R51','R55','R65']
    for j in s2:
        total_s2+=request.GET[j]
    #人际关系敏感
    s3=['R6','R21','R34','R36','R37','R41','R61','R69','R73']
    for j in s3:
        total_s3+=request.GET[j]
    #抑郁
    s4=['R5','R14','R15','R20','R22','R26','R29','R30','R31','R32','R54','R71','R79']
    for j in s4:
        total_s4+=request.GET[j]
    #焦虑
    s5=['R2','R17','R23','R33','R39','R57','R72','R78','R80','R86']
    for j in s5:
        total_s5+=request.GET[j]
    #敌对
    s6=['R11','R24','R63','R67','R74','R81']
    for j in s6:
        total_s6+=request.GET[j]
    #恐怖
    s7=['R13','R25','R47','R50','R70','R75','R82']
    for j in s7:
        total_s7+=request.GET[j]
    #偏执
    s8=['R8','R18','R43','R68','R76','R83']
    for j in s8:
        total_s8+=request.GET[j]
    #精神病性
    s9=['R7','R16','R35','R62','R77','R84','R85','R87','R88','R90']
    for j in s9:
        total_s9+=request.GET[j]
        

def les(request):
    return render(request,'LES.html')

def pf(request):
    return render(request,'16PF.html')
def pf_result(request):
    result_pf=[]
    #乐群性
    a1=['answer3','answer52','answer101','answer126','answer176']
    a2=['answer26','answer27','answer51','answer76','answer151']
    a=0
    for i in a1:
        if request.GET[i]=='0':
            a+=2
        elif request.GET[i]=='1':
            a+=1
    for i in a2:
        if request.GET[i]=='2':
            a+=2
        elif request.GET[i]=='1':
            a+=1
    tcode_a=GetTcode().tcode_pf('a',a)
    result_pf.append(tcode_a)
    
    #聪慧性
    b1=['answer28','answer53','answer54','answer78','answer103','answer128','answer152']
    b2=['answer77','answer102','answer127','answer153']
    b3=['answer177','answer178']
    b=0
    for i in b1:
        if request.GET[i]=='1':
            b+=1
    for i in b2:
        if request.GET[i]=='2':
            b+=1
    for i in b3:
        if request.GET[i]=='0':
            b+=1
    tcode_b=GetTcode().tcode_pf('b',b)
    result_pf.append(tcode_b)    
    #稳定性
    c1=['answer4','answer30','answer55','answer105','answer129','answer130','answer179']
    c2=['answer5','answer29','answer79','answer80','answer104','answer154']
    c=0
    for i in c1:
        if request.GET[i]=='0':
            c+=2
        elif request.GET[i]=='1':
            c+=1
    for i in c2:
        if request.GET[i]=='2':
            c+=2
        elif request.GET[i]=='1':
            c+=1
    tcode_c=GetTcode().tcode_pf('c',c)
    result_pf.append(tcode_c)    
    #持强性
    e1=['answer7','answer56','answer131','answer155','answer156','answer180','answer181']
    e2=['answer6','answer31','answer32','answer57','answer81','answer106']
    e=0
    for i in e1:
        if request.GET[i]=='0':
            e+=2
        elif request.GET[i]=='1':
            e+=1
    for i in e2:
        if request.GET[i]=='2':
            e+=2
        elif request.GET[i]=='1':
            e+=1
    tcode_e=GetTcode().tcode_pf('e',e)
    result_pf.append(tcode_e)    
    #兴奋性
    f1=['answer33','answer58','answer132','answer133','answer182','answer183']
    f2=['answer8','answer82','answer83','answer107','answer157','answer158']
    f=0
    for i in f1:
        if request.GET[i]=='0':
            f+=2
        elif request.GET[i]=='1':
            f+=1
    for i in f2:
        if request.GET[i]=='2':
            f+=2
        elif request.GET[i]=='1':
            f+=1
    tcode_f=GetTcode().tcode_pf('f',f)
    result_pf.append(tcode_f)    
    #有恒性
    g1=['answer59','answer109','answer134','answer160','answer184','answer185']
    g2=['answer9','answer34','answer84','answer159']
    g=0
    for i in g1:
        if request.GET[i]=='0':
            g+=2
        elif request.GET[i]=='1':
            g+=1
    for i in g2:
        if request.GET[i]=='2':
            g+=2
        elif request.GET[i]=='1':
            g+=1
    tcode_g=GetTcode().tcode_pf('g',g)
    result_pf.append(tcode_g)    
    #敢为性
    h1=['answer10','answer36','answer110','answer111','answer136','answer186']
    h2=['answer35','answer60','answer61','answer85','answer86','answer135','answer161']
    h=0
    for i in h1:
        if request.GET[i]=='0':
            h+=2
        elif request.GET[i]=='1':
            h+=1
    for i in h2:
        if request.GET[i]=='2':
            h+=2
        elif request.GET[i]=='1':
            h+=1
    tcode_h=GetTcode().tcode_pf('h',h)
    result_pf.append(tcode_h)    
    #敏感性
    i1=['answer11','answer12','answer37','answer112','answer138','answer163']
    i2=['answer62','answer87','answer137','answer162']
    i=0
    for j in i1:
        if request.GET[j]=='0':
            i+=2
        elif request.GET[j]=='1':
            i+=1
    for j in i2:
        if request.GET[j]=='2':
            i+=2
        elif request.GET[j]=='1':
            i+=1
    tcode_i=GetTcode().tcode_pf('i',i)
    result_pf.append(tcode_i)    
    #怀疑性
    l1=['answer13','answer38','answer88','answer113','answer114','answer164']
    l2=['answer63','answer64','answer89','answer139']
    l=0
    for j in l1:
        if request.GET[j]=='0':
            l+=2
        elif request.GET[j]=='1':
            l+=1
    for j in l2:
        if request.GET[j]=='2':
            l+=2
        elif request.GET[j]=='1':
            l+=1
    tcode_l=GetTcode().tcode_pf('l',l)
    result_pf.append(tcode_l)    
    #幻想性
    m1=['answer39','answer40','answer65','answer91','answer115','answer140']
    m2=['answer14','answer15','answer90','answer116','answer141','answer165','answer166']
    m=0
    for j in m1:
        if request.GET[j]=='0':
            m+=2
        elif request.GET[j]=='1':
            m+=1
    for j in m2:
        if request.GET[j]=='2':
            m+=2
        elif request.GET[j]=='1':
            m+=1
    tcode_m=GetTcode().tcode_pf('m',m)
    result_pf.append(tcode_m)    
    #世故性
    n1=['answer17','answer42','answer117','answer142','answer167']
    n2=['answer16','answer41','answer66','answer67','answer92']
    n=0
    for j in n1:
        if request.GET[j]=='0':
            n+=2
        elif request.GET[j]=='1':
            n+=1
    for j in m2:
        if request.GET[j]=='2':
            n+=2
        elif request.GET[j]=='1':
            n+=1
    tcode_n=GetTcode().tcode_pf('n',n)
    result_pf.append(tcode_n)    
    #忧虑性
    o1=['answer18','answer43','answer69','answer118','answer119','answer143','answer168']
    o2=['answer19','answer44','answer68','answer93','answer94','answer144']
    o=0
    for j in o1:
        if request.GET[j]=='0':
            o+=2
        elif request.GET[j]=='1':
            o+=1
    for j in o2:
        if request.GET[j]=='2':
            o+=2
        elif request.GET[j]=='1':
            o+=1
    tcode_o=GetTcode().tcode_pf('o',o)
    result_pf.append(tcode_o)    
    #实验性
    q11=['answer20','answer21','answer46','answer70','answer145','answer169']
    q12=['answer45','answer95','answer120','answer170']
    q1=0
    for j in q11:
        if request.GET[j]=='0':
            q1+=2
        elif request.GET[j]=='1':
            q1+=1
    for j in q12:
        if request.GET[j]=='2':
            q1+=2
        elif request.GET[j]=='1':
            q1+=1
    tcode_q1=GetTcode().tcode_pf('q1',q1)
    result_pf.append(tcode_q1)    
    #独立性
    q21=['answer47','answer71','answer72','answer146','answer171']
    q22=['answer22','answer96','answer97','answer121','answer122']
    q2=0
    for j in q21:
        if request.GET[j]=='0':
            q2+=2
        elif request.GET[j]=='1':
            q2+=1
    for j in q22:
        if request.GET[j]=='2':
            q2+=2
        elif request.GET[j]=='1':
            q2+=1
    tcode_q2=GetTcode().tcode_pf('q2',q2)
    result_pf.append(tcode_q2)    
    #自律性
    q31=['answer48','answer73','answer98','answer147','answer148','answer173']
    q32=['answer23','answer24','answer123','answer172']
    q3=0
    for j in q31:
        if request.GET[j]=='0':
            q3+=2
        elif request.GET[j]=='1':
            q3+=1
    for j in q32:
        if request.GET[j]=='2':
            q3+=2
        elif request.GET[j]=='1':
            q3+=1
    tcode_q3=GetTcode().tcode_pf('q3',q3)
    result_pf.append(tcode_q3)    
    #紧张性
    q41=['answer25','answer49','answer50','answer74','answer99','answer124','answer149','answer150','answer174']
    q42=['answer75','answer100','answer125','answer175']
    q4=0
    for j in q41:
        if request.GET[j]=='0':
            q4+=2
        elif request.GET[j]=='1':
            q4+=1
    for j in q42:
        if request.GET[j]=='2':
            q4+=2
        elif request.GET[j]=='1':
            q4+=1
    tcode_q4=GetTcode().tcode_pf('q4',q4)
    result_pf.append(tcode_q4)
    
    print(result_pf)
    return HttpResponse(result_pf)
        
        
    
    
    
def epq(request):
    return render(request,'epq.html')

def epq_result(request):
    age=request.GET['age']
    sex=request.GET['sex']
    p1=['answer22','answer26','answer30','answer34','answer46','answer50','answer66','answer68','answer75','answer76','answer81','answer85']
    p2=['answer2','answer6','answer9','answer11','answer18','answer38','answer42','answer56','answer62','answer72','answer88']
    p=0
    for x in p1:
        if request.GET[i]=='1':
            p+=1
    for x in p2:
        if request.GET[i]=='0':
            p+=1
    
    e1=['answer1','answer5','answer10','answer13','answer14','answer17','answer25','answer33','answer37','answer41','answer49','answer53','answer55','answer61','answer65','answer71','answer80','answer84']
    e2=['answer21','answer29','answer45']
    e=0
    for x in e1:
        if request.GET[i]=='1':
            e+=1
    for x in e2:
        if request.GET[i]=='0':
            e+=1
    
    n1=['answer3','answer7','answer12','answer15','answer19','answer23','answer27','answer31','answer35','answer39','answer43','answer47','answer51','answer57','answer59','answer63','answer67','answer69','answer73','answer74','answer78','answer82','answer86']
    n=0
    for x in n1:
        if request.GET[i]=='1':
            n+=1
    
    l1=['answer20','answer32','answer36','answer58','answer87']
    l2=['answer4','answer8','answer16','answer24','answer28','answer40','answer44','answer48','answer52','answer54','answer60','answer64','answer70','answer79','answer83']
    l=0
    for x in l1:
        if request.GET[i]=='1':
            l+=1
    for x in l2:
        if request.GET[i]=='0':
            l+=1
    


