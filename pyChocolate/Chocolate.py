from inspect import stack, getframeinfo,getsource
from colorama import Fore,init
from datetime import datetime

# Before reading code u should now
# -> getframeinfo(stack()[1][0]) function getting data about used code line and
# -> that why we can get debug of a code part from program 

white=Fore.LIGHTWHITE_EX
green=Fore.GREEN
red=Fore.RED
reset=Fore.RESET

init()

class pyChocolate:
      
      def File(self,frame,kwargs):
          return f"{white} file :{frame.filename}" if ifEqual(kwargs,("file",True)) else ""

      def Code(self,frame,color,kwargs):
          return f"{white} code: {color}{frame.code_context[0].strip()}{reset}" if ifEqual(kwargs,("code",True)) else ""

      def Info(self,frame,output,kwargs):
          return f"{white}[Line-{frame.lineno}] ->({green+firstValue(frame.code_context[0].strip())+white}) { green}{output} {self.Code(frame,green,kwargs)} {self.File(frame,kwargs)}"

      def Warn(self,frame,output,kwargs):
          return f"{white}[Line-{frame.lineno}] { red}{output} {self.Code(frame,red,kwargs)} {self.File(frame,kwargs)}"

      def LOG(self,frame,output:"debuging content",kwargs)->"return given output": 
          print(self.Warn(frame,output,kwargs) if ifEqual(kwargs,("mode","warn"))  else self.Info(frame,output,kwargs),reset)
          return output

      def Catch(self,frame,tryFunc,runFunc):
          arg1,arg2=tryFunc[1],runFunc[1]
          name1,name2=str(tryFunc[0]).split(" ")[1],str(runFunc[0]).split(" ")[1]
          string=f"{white}[Line-{frame.lineno}]->(Catch) Func:{ green}{{0}} {white}args:({{1}}{white}){ green} {white} return:{ green}{{2}} {reset}"
          try:
            rv=tryFunc[0](*arg1)
            args=colorfulArgs(arg1)
            print(string.format(name1,args,rv))
          except Exception as func1err:
            try:
              rv=runFunc[0](*arg2)
              args=colorfulArgs(arg2)
              print(string.format(name2,args,rv))
              print(white+f"[Catched]->({green+name1+white})({colorfulArgs(arg1)+white}) "+str(func1err)+reset)
              print(getsource(tryFunc[0]))
            except Exception as func2err:
              print(f"{white}[Line-{frame.lineno}]->({ Fore.LIGHTRED_EX}Catch{white}) { red}'error on both functions' {white}[{ red}{name1}{white},{ red}{name2}{white}]{ reset}")
              print(white+f"[Catched]->({green+name1+white})({colorfulArgs(arg1)+white}) "+str(func1err)+reset)
              print(getsource(tryFunc[0]))
              print(white+f"[Catched]->({green+name2+white})({colorfulArgs(arg2)+white}) "+str(func2err)+reset)
              print(getsource(runFunc[0]))
              return [func1err,func2err]
          return rv

      def put(self,text):
          date=datetime.now().strftime("%H:%M:%S")
          print(white+f"[{date}] "+text+reset)
          
#-----------ChocolateFuncs----------

def ifEqual(kwargs,tuple_):
    return True if tuple_ in list(kwargs.items()) else False

def multiSplit(string,args):
    for arg in args:
        string=string.replace(arg,args[0])
    return string.split(args[0])
    
def getLog(code):    
    x=multiSplit(code,["(",")"])
    try:
      i=x.index("Log")
    except:
      for s in x:
          if "Log" in s:
              i=x.index(s)
    return x[i+1:len(x)-i-1]

def firstValue(code):
    code=getLog(code)
    if len(code)>1:
        return code[0]+white+")("+green+"".join(code[1])
    return " ".join(code).split(",")[0]

def colorfulArgs(arg):
    return ','.join([ green+str(i)+reset if type(i)!=str else green+'"'+str(i)+'"'+reset for i in arg])


#-----------exporting---------------

Chocolate=pyChocolate()

def Log(output:"debuging content",**kwargs)->"return given output":
    return Chocolate.LOG(getframeinfo(stack()[1][0]),output,kwargs)


def Catch(tryFunc:"function",runFunc:"function")->"return given output":
    return Chocolate.Catch(getframeinfo(stack()[1][0]),tryFunc,runFunc)

def put(text):
    Chocolate.put(text)

#-------------Done------------------

