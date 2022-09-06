class HeadContent:
    def __init__(self,title="Document",files=[]):
        self.files = files
        self.head(title)
    def head(self,title):
        concat = "\n"
        end_head = "\n" + "</head>"
        if len(self.files) >0:
            for file in self.files:
                concat = concat + "\n" + file
        self.part_one = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>{title}</title> 
                         """
        self.part_one = self.part_one + concat + end_head
        return self.part_one
hd = HeadContent(files=["css","bootstrap"])