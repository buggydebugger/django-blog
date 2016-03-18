$().ready(function(){ $("#createForm").validate({
                rules: {
                    title: {
                        required: true,
                        minlength: 5,
                        maxlength:100
                    },
                    content: {
                        required: true,
                        minlength: 5
                    },
                },
                messages: {
                    title: {required: "Please enter your title",
                    		minlength: "Title length atleast 5 char",
                    		maxlength: "Title atmost 100 char"
                            },
                    content: {required:"Please enter your content",
                              minlength:"Content must be atleast 5 char"}
                },
               
            });})
            
           
       
    
