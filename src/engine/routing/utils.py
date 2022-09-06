def redirect(path,res):
        res.text = f"<script>window.location= '{path}'</script>"

def default_response(res):
    res.status_code = 404
    res.text = "Page Not Found"
    return res