import requests
import re


request = requests.get(input().strip()).text
lst_reg = re.findall(r'<a.*\bhref=["|\']?(?:[htpsf-]*)?(?:://)?(\w[\w.-]*)', request)
lst_sort = sorted(set(lst_reg))
print(*lst_sort, sep='\n')
