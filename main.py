import time
import problems.problem_23 as problem


def print_time(runtime):
    if runtime < 0.01:
        print("Runtime: {0}ms".format(str(runtime*1000)[:5]))
    if 0.01 <= runtime <= 60:
        print("Runtime: {0}s".format(str(runtime)[:5]))
    if 60 < runtime <= 3600:
        print("Runtime: {0}m{1:02d}s".format(int(runtime / 60),
                                             int(runtime % 60)))
    if runtime > 3600:
        print("Runtime: {0}h{1:02d}m{2:02d}s".format(int(runtime / 3600),
                                                     int(runtime % 3600 / 60),
                                                     int(runtime % 60)))


start_time = time.time()
problem.main()
timer = time.time()-start_time
print_time(timer)
