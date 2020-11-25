console.log("organizacja_nowy.js")


//$('#ZapiszOrganizacje').on("click", function(e) {
//   console.log("console log - organizacja nowy")
//});

//wyswietlanie danych
$("#form_zapisorg").on("submit", function(e) {
   e.preventDefault()
   console.log("form_zapis_org")
   var wyswietl=document.getElementById("opis_organizacji").value
   console.log("wyswietl:" +wyswietl )
   var wyswietl2=$("#opis_organizacji").val()
   console.log("wyswietl2: " +wyswietl2)
})
//   $.ajax({
//      url        : "http://127.0.0.1:8000/api/organizacje",
//      type       : "POST",
//      //beforeSend: function(xhr, settings) {
//      //    xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
//      //},
//      //success: function (arg){
//      //     location.reload()
//      //}
//      //dataType   : "json",
//      //success    : function (data){
//      //         $('#nazwa_organizacji').text(data[0].nazwa);
//      //         $('#opis_organizacji'.text(data[0].opis));
//      //}
//      data: {
//             nazwa: $("#nazwa_organizacji").val(),
//             opis: $("#opis_organizacji").val(),
//      }
//      success: function(){
//         alert("Dodano organizacje successfully!")
//      }
//      error: function(){
//         alert("Nie udalo sie dodac organizacji :'(")
//      }
//   });
