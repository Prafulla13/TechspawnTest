$(document).ready(function () {
    $('#create-blog').on("click", function () {
        console.log("aaaaaa")
        var data = {
            blog_name: $("#blog_name").val(),
            blog_content: $("#blog_content").val(),
            blog_tech: $("#blog_tech").val(),
        };
        console.log(data)
        $.ajax({
            type: "POST",
            url: "/create_blog/",
            async: true,
            data: data,
            success: function (data) {
                console.log(data)
            }
        });
    });
});


$(document).ready(function () {
    console.log("Page Load")
    var data = {};
    // console.log(data)
    $.ajax({
        type: "GET",
        url: "/",
        async: true,
        data: data,
        success: function (data) {
            console.log(data)
        }
    });
});