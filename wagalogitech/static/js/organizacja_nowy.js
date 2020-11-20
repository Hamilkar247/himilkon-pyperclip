console.log("organizacja_nowy.js")


$('.ZapiszOrganizacje').click( function() {
   console.log("console log - organizacja nowy")
   $.ajax({
      url        : "http://127.0.0.1:8000/api/organizacje",
      method     : "POST",
      success : function (data){
               $('#nazwa_organizacji').text(data[0].nazwa);
               $('#opis_organizacji'.text(data[0].opis));
      }
//      data       : {
//          "nazwa"   : "Fundacja gustawa adolfa",
//          "opis"    : "pulawska 3a"
//      }
//   }).done( function (response){
//       alert("Zapisano organizacje")
//   }).fail( function(){
//       alert("Organizacja nie przeszła")
//   })
   });
});