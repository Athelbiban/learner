def is_parent(child, ls=[]):
    ls = ls + [child]
    if child in except_list:
        return ls
    if child in errors and errors[child]:
        for i in errors[child]:
            f = is_parent(i)
            ls.extend(f)
    return ls


errors = {}
for _ in range(int(input())):
    lst = input().split()
    errors[lst[0]] = errors.get(lst[0], lst[2:])
except_list = []
for _ in range(int(input())):
    exception = input()
    if not except_list:
        except_list.append(exception)
    elif except_list:
        res = is_parent(exception)
        for e in except_list:
            if e in res:
                print(exception)
                break
        else:
            except_list.append(exception)
