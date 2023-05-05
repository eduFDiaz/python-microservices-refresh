from temporalio import activity, workflow

with workflow.unsafe.imports_passed_through():
    from config import logger as log

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    if n == 1:
        return 2
    count = 1
    num = 3
    while count < n:
        if is_prime(num):
            count += 1
        num += 2
    return num - 2

def find_factorial(n):
    # iterative approach
    log.info(f"Finding factorial of {n}")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@activity.defn
async def find_factorial_activity(n: int) -> int:
    return find_factorial(n)

@activity.defn
async def find_prime(n: int) -> int:
    return find_nth_prime(n)

# @activity.defn
# async def executeNetConfActivity(c: temporal.ctx, ip: InputParams, t: NetConfTask) -> int:
#         return NetConfTask.step_process()
#         log.debug("NetConfStep process")
#         self.payload = self.render_jinja_template()
        
#         config = {
#             "host": self.hostname,
#             "auth_username": self.username,
#             "auth_password": self.password,
#             "auth_strict_key": False,
#             "port": self.port,
#         }

#         client = NetConfClient(config)

#         if self.type == 'FETCH':
#             result = client.get_filter(self.payload)
#             self.extract_variables(result)
#         elif self.type == 'EDIT':
#             result = client.edit_config(self.payload)
#             self.validate_process(result)

#         log.debug(f"NetConfStep process result\n{result}")
