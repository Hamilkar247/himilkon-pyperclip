//wartosci z bazy danych pewnej organizacji
$(document).ready(function(){
   console.log("jestesmy w szczegolach organizacji")
   let searchParams = $(location).attr('href')//w vanilii JS to jestwindow.location.href
   let destinationURL = searchParams.replace("front", "api")
   console.log("current url:" + destinationURL)
   $.ajax({
      url: destinationURL, //do poprawienia !!!
      type: "GET",
   }).done(function(response) {
       console.log("udalo sie pobrac z ajaksa dane !")
       $('#nazwa_organizacji').attr('value', response.nazwa);
       $("#opis_organizacji").attr('value', response.opis);
   }).fail(function() {
     alert("Wystąpił błąd w połączeniu z djangorestapi!");
   })
})