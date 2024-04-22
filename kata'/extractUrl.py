import re
def domain_name(url):

    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

print(domain_name("x6ghbbnxyi.fr/index.php")) #google
print(domain_name("cbispgatfzt7kvbc33qwmh3t.co.za/warez/"))