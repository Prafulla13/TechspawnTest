
// $(document).ready(function () {
//     console.log('--------')
//     // $('#register-user').on("click", function () {
//     $('#register-user').on("click", function () {
//         console.log("aaaaaa")
//         var data = {
//             name: $("#name").val(),
//             username: $("#username").val(),
//             password: $("#password").val(),
//             password2: $("#password2").val()
//         };
//         console.log(data)
//         $.ajax({
//             type: "POST",
//             url: "/register/",
//             async: true,
//             data: data,
//             success: function (data) {
//                 console.log('Success')
//             }
//         });
//     });
// });

// $(document).ready(function () {
//     $('#loginbtn').on("click", function () {
//         status = 0
//         if (password.length > 7) {
//             status = 1
//         }
//         // console.log(password.length)
//         $.ajax({
//             success: function (status) {
//                 console.log(status)
//             }
//         });
//     });
// });