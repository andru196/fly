    function ajaxxx(adr, fsccss, ffl, data){
    return $.ajax({

        url: adr,

       data: data,

        type: 'get', // This is the default though, you don't actually need to always mention it
        success: fsccss,

        failure: ffl
});}