$("#check_name_btn").click(function() {
// for Ajax request
    $.ajax({
        type: "GET",
        url: "check_user_name/",
        data: {
            'user_name': $("#user_name_input").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            console.log(data);
            if (data == 'ok') {
                console.log("OK");
            } else if (data == 'no') {
                console.log("NO");
            }
        }
    });
});