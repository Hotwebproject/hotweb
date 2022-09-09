

class Footer:
    def __init__(self):
        pass
    
    def footer(self,content="Brought  To You With Love from HotWeb",files=[]):
        open_footer_tag = "\n" + "<footer>" + "\n"
        close_footer_tag = "\n" + "</footer>" + "\n"
        close_body_tag = "\n" + "</body>" + "\n"
        concat = "\n "
        if len(files)>0:
            for file in files:
                concat = concat + "\n" + file
        open_footer_tag = open_footer_tag + content + close_footer_tag + close_body_tag + concat

        return open_footer_tag