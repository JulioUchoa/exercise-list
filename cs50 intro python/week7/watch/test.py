import re


### 25-07 tentativa
def parse(s):
    p = r'.*src="(https?://(www\.)?youtube\.com/embed/.*?)".*?'
    r = re.search(p, s)
    if r:
        #-
        first_link = r.group(1)
        f_part, s_part = first_link.split("embed/")
        last_link = 'https://www.youtu.be/'+s_part
        print(last_link)
        #-
        return r.group(1)
    else:
        return None



## tentativa passada ... unknown date
def parse(s):
    regular_exp = r'<iframe .*? src="(https?://(?:www\.)?youtube\.com/embed/.*?)".*?>'
    match = re.search(regular_exp, s)
    if match:
        url = match.group(1)
        y_url = url.replace('youtube.com/embed/', 'youtu.be/')
        return y_url
    return None

########

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<iframe src="http://youtube.com/embed/xvFZjoxxxxxx0"></iframe>

<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>
<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>




# tried patterns log:
# 1 - r"(^src=\".+ (t | >))"
# 2 - r"src=\".+\"
# 3 - r"(src=\".+\" )$"
# 4- r'<iframe .*? scr="(https?://00")'

# r'<iframe .*? src="(https?://(?:www\.)?youtube\.com/embed/.*?)".*?>'

# r'<iframe .*? src="(https?://(?:www\.)?(?:youtube\.com|youtu\.be)/embed/.*?)".*?>'