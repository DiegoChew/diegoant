from myanalysis.optimization.opt_angle import angle_opt
from myanalysis.optimization.opt_PID import PID_opt
from myanalysis.optimization.opt_ProbNN import ProbNN_opt

if "--PID" in sys.argv:
    PID_opt()

elif "--angle" in sys.argv:
    angle_opt()

elif "--ProbNN" in sys.argv:
    ProbNN_opt()

else:
    print("ERROR")