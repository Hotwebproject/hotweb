$(document).ready(function(){
    // all links should prevent page reloading
    $("a.a__class").click(function(e){
        e.preventDefault()
    })
})//end the document